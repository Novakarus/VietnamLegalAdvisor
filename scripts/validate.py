# SPDX-License-Identifier: Apache-2.0
"""Static repository checks only. No network, deployment or model execution.

Skill frontmatter and agent YAML in this project use the JSON subset of YAML.
Run from any directory: python path/to/scripts/validate.py
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import argparse
import hashlib
import json
import re
import warnings
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'instructions', 'vietnam-legal-research', 'legal-validity-verification',
    'vietnam-contract-review', 'legal-due-diligence', 'legal-document-drafting',
    'legal-reasoning', 'opposing-counsel-review', 'corporate-governance',
    'investment-and-ma', 'regulatory-compliance', 'legal-source-verification',
    'legal-quality-audit'}

def valid_png(path):
    try:
        from PIL import Image
        with warnings.catch_warnings():
            warnings.simplefilter('error', Image.DecompressionBombWarning)
            with Image.open(path) as img:
                if img.format != 'PNG' or not (256 <= img.width == img.height <= 4096):
                    return False
                img.verify()
            with Image.open(path) as img:
                img.load()
        return path.stat().st_size <= 5*1024*1024
    except (ImportError, OSError, ValueError, SyntaxError, Warning):
        return False

ZIP_NOT_CHECKED = []

def valid_pass(case, results, root, pkg, version):
    fields = {'evidence_fidelity','temporal_applicability','legal_reasoning',
              'task_coverage','risk_actionability','disclosure'}
    scores = case.get('scores')
    if not isinstance(scores, dict) or set(scores) != fields:
        return False
    if not all(type(v) is int and 3 <= v <= 4 for v in scores.values()) or sum(scores.values()) < 20:
        return False
    for key in ['reviewer','model','tool_mode','date']:
        if not isinstance(case.get(key), str) or not case[key].strip():
            return False
    try:
        datetime.fromisoformat(case['date'].replace('Z', '+00:00'))
    except ValueError:
        return False
    evidence = case.get('evidence_locations')
    if not isinstance(evidence, list) or not evidence:
        return False
    for rel in evidence:
        if not isinstance(rel, str) or not rel.strip() or Path(rel).is_absolute():
            return False
        target = (root/rel).resolve()
        if not target.is_relative_to(root) or not target.is_file() or target.stat().st_size == 0:
            return False
    defects = case.get('defects')
    if not isinstance(defects, list) or not all(isinstance(d, dict) and d.get('severity') == 'minor' and isinstance(d.get('description'), str) and d['description'].strip() for d in defects):
        return False
    route = case.get('observed_route')
    if not isinstance(route, list) or not route or not all(isinstance(x, str) and x in EXPECTED for x in route):
        return False
    digest = results.get('candidate_zip_sha256')
    tested = results.get('tested_archive')
    archive = (root/tested) if tested else root/'dist'/('Vietnam-Legal-Advisor-'+version+'.zip')
    if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-f]{64}', digest):
        return False
    if not archive.is_file():
        # dist/ là sản phẩm dựng cục bộ, không nằm trong Git (xem .gitignore): môi trường CI không có ZIP.
        # Bỏ qua phép so ZIP, nhưng báo cảnh báo; kiểm tra đầy đủ chạy được khi có ZIP.
        if archive.name not in ZIP_NOT_CHECKED:
            ZIP_NOT_CHECKED.append(archive.name)
        return True
    if hashlib.sha256(archive.read_bytes()).hexdigest() != digest:
        return False
    import zipfile
    post = results.get('post_test_changes') or {}
    changed = set(post.get('files', []))
    try:
        with zipfile.ZipFile(archive) as z:
            current = {p.relative_to(pkg).as_posix(): p for p in pkg.rglob('*') if p.is_file()}
            if len(z.namelist()) != len(current) or set(z.namelist()) != set(current):
                return False
            # Mọi file phải trùng ZIP đã kiểm thử, trừ các file đã ghi trong post_test_changes.
            if not all(z.read(n) == p.read_bytes() for n, p in current.items() if n not in changed):
                return False
        if changed:
            cur = root/'dist'/('Vietnam-Legal-Advisor-'+version+'.zip')
            want = post.get('current_zip_sha256')
            if not (isinstance(want, str) and re.fullmatch(r'[0-9a-f]{64}', want)):
                return False
            if cur.is_file() and hashlib.sha256(cur.read_bytes()).hexdigest() != want:
                return False
        return True
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError):
        return False

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def validate(root=ROOT, write_report=True):
    root = Path(root).resolve()
    pkg = root / 'plugin'
    checks, warnings = [], []
    ZIP_NOT_CHECKED.clear()
    version = None
    def check(label, value):
        checks.append({'check': label, 'passed': bool(value)})
    def contained_file(base, relative):
        target = (base / relative).resolve()
        return target.is_relative_to(base.resolve()) and target.is_file()
    try:
        check('plugin directory exists', pkg.is_dir())
        check('no symlinks in plugin', not any(p.is_symlink() for p in pkg.rglob('*')))
        m = read_json(pkg / 'plugin.json')
        legacy = read_json(pkg / '.codex-plugin/plugin.json')
        i = m['extensions']['com.openai']['interface']
        version = m['version']
        check('semantic version', re.fullmatch(r'\d+\.\d+\.\d+', version))
        check('manifest fields synchronized', all(m[k] == legacy[k] for k in ['name','version','description','author']))
        check('interface synchronized', i == legacy['interface'])
        check('skills discovery path', legacy.get('skills') == './skills')
        check('plugin identity', m['name'] == 'gpt-20c5e24b4c10dd0e31dd8b7cb4f7bfe6')
        check('display name', i['displayName'] == 'Vietnam Legal Advisor')
        check('subtitle length', 0 < len(i['shortDescription']) <= 30)
        for key in ['logo','composerIcon']:
            rel = i[key]
            valid = contained_file(pkg, rel)
            check(key + ' path exists inside plugin', valid)
            check(key + ' canonical filename', Path(rel).name == 'vietnam-legal-advisor-icon-v4.png')
            if valid:
                check(key + ' fully decoded square PNG (requires Pillow)', valid_png(pkg / rel))
        skills = list((pkg/'skills').glob('*/SKILL.md'))
        check('13 required skills', {p.parent.name for p in skills} == EXPECTED)
        for p in skills:
            body = p.read_text(encoding='utf-8-sig')
            fm = json.loads(body.split('---', 2)[1])
            check(p.parent.name + ' metadata', body.startswith('---\n') and fm['name'] == p.parent.name and bool(fm['description'].strip()))
            for link in re.findall(r'\]\(([^)]+)\)', body):
                if urlsplit(link).scheme or link.startswith('#'):
                    continue
                target = (p.parent / unquote(urlsplit(link).path)).resolve()
                check(p.parent.name + ' reference ' + link, target.is_relative_to(pkg) and target.is_file())
        router = (pkg/'skills/instructions/SKILL.md').read_text(encoding='utf-8')
        check('router covers all specialists', all('| '+name+' |' in router for name in EXPECTED-{'instructions'}))
        for p in pkg.rglob('*.json'):
            read_json(p)
        for p in pkg.rglob('*.yaml'):
            a = read_json(p)['interface']
            check('agent metadata '+str(p.relative_to(pkg)), all(isinstance(a.get(k),str) and a[k].strip() for k in ['display_name','short_description','default_prompt']))
        cases = read_json(root/'tests/cases.json')
        ids = [c['id'] for c in cases]
        check('22 unique cases', len(ids) == len(set(ids)) == 22)
        check('core test categories', {'research','contract','diligence','transaction','validity'} <= {c['category'] for c in cases})
        check('case expectations and routes', all(c['prompt'] and c['must_include'] and c['must_not'] and set(c['expected_skills']) <= EXPECTED for c in cases))
        results = read_json(root/'tests/results.json')
        check('results candidate version matches', results['candidate'] == version)
        check('result IDs match cases', len(results['cases']) == len(ids) and {c['case_id'] for c in results['cases']} == set(ids))
        check('result statuses', all(c['status'] in ['NOT_RUN','PASS','FAIL','BLOCKED'] for c in results['cases']))
        for case in results['cases']:
            if case['status'] == 'PASS':
                check(case['case_id'] + ' pass evidence', valid_pass(case, results, root, pkg, version))
        if any(c['status'] != 'PASS' for c in results['cases']):
            warnings.append('Behavioral acceptance is incomplete; static PASS does not certify legal/model behavior.')
        elif str(results.get('formal_acceptance','')).startswith('BLOCKED'):
            warnings.append('Behavioral PASS is provisional AI-graded; formal acceptance is blocked by Protocol v2 gates (see tests/run_integrity.py).')
        if ZIP_NOT_CHECKED:
            warnings.append('Chưa đối chiếu SHA-256/nội dung ZIP với bản ghi kiểm thử vì thiếu dist/' + ZIP_NOT_CHECKED[0] + ' (dist/ không nằm trong Git). Chạy lại cục bộ sau khi dựng ZIP để kiểm tra đầy đủ.')
        check('fixtures exist', (root/'tests/fixtures.md').is_file())
        docs = root/'docs'
        class Links(HTMLParser):
            def handle_starttag(self, tag, attrs):
                for key, value in attrs:
                    if key not in ['src','href'] or not value:
                        continue
                    url = urlsplit(value)
                    if url.scheme or url.netloc or not url.path:
                        continue
                    target = (self.path.parent / unquote(url.path)).resolve()
                    if target.is_dir(): target = target/'index.html'
                    check(str(self.path.relative_to(root))+' -> '+value, target.is_relative_to(docs) and target.is_file())
        for rel in ['index.html','support/index.html','privacy/index.html','terms/index.html','.nojekyll']:
            check('website file '+rel, (docs/rel).is_file())
        for p in docs.rglob('*.html'):
            parser = Links(); parser.path = p
            parser.feed(p.read_text(encoding='utf-8'))
        if 'publication-status" content="draft' in (docs/'terms/index.html').read_text(encoding='utf-8'):
            warnings.append('Terms remain a draft; package checks do not establish public-submission readiness.')
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        check('validation completed: '+str(exc), False)
    files = []
    if pkg.exists():
        files = [{'path':p.relative_to(pkg).as_posix(), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(pkg.rglob('*')) if p.is_file() and not p.is_symlink()]
    report = {'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL',
        'scope':'Static structure and consistency only; no legal/model execution or deployment',
        'candidate':version,'generated_at':datetime.now(timezone.utc).isoformat(),
        'checks':checks,'warnings':warnings,'plugin_files':files}
    if write_report:
        (root/'tests/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-write', action='store_true', help='Do not write tests/validation.json')
    args = parser.parse_args()
    report = validate(write_report=not args.no_write)
    print(json.dumps({k:report[k] for k in ['status','scope','candidate','warnings']},ensure_ascii=False,indent=2))
    for item in report['checks']:
        if not item['passed']: print('FAIL: '+item['check'])
    raise SystemExit(0 if report['status']=='PASS' else 1)
