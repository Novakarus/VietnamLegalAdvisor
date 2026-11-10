# SPDX-License-Identifier: Apache-2.0
"""Static repository checks only. No network, deployment or model execution. Standard library only.

Skill frontmatter and agent YAML in this project use the JSON subset of YAML.
Run from any directory: python path/to/scripts/validate.py
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'instructions', 'vietnam-legal-research', 'legal-validity-verification',
    'vietnam-contract-review', 'legal-due-diligence', 'legal-document-drafting',
    'legal-reasoning', 'opposing-counsel-review', 'corporate-governance',
    'investment-and-ma', 'regulatory-compliance', 'legal-source-verification',
    'legal-quality-audit'}

def valid_png(path):
    """Complete square PNG, 256-4096 px, at most 5 MiB (header and end marker only; pixels are not decoded)."""
    try:
        data = path.read_bytes()
    except OSError:
        return False
    if len(data) > 5*1024*1024 or data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
        return False
    width, height = int.from_bytes(data[16:20], 'big'), int.from_bytes(data[20:24], 'big')
    return 256 <= width == height <= 4096 and data[-12:-4] == b'\x00\x00\x00\x00IEND'

ZIP_NOT_CHECKED = []

def valid_pass(case, results, root, version):
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
        # dist/ is a locally built product and is not in Git (see .gitignore): the CI environment has no ZIP.
        # Skip the hash check but emit a warning.
        if archive.name not in ZIP_NOT_CHECKED:
            ZIP_NOT_CHECKED.append(archive.name)
        return True
    if hashlib.sha256(archive.read_bytes()).hexdigest() != digest:
        return False
    return True

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def validate(root=ROOT):
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
                check(key + ' complete square PNG', valid_png(pkg / rel))
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
                check(case['case_id'] + ' pass evidence', valid_pass(case, results, root, version))
        if any(c['status'] != 'PASS' for c in results['cases']):
            warnings.append('Behavioral acceptance is incomplete; static PASS does not certify legal/model behavior.')
        else:
            warnings.append('Behavioral PASS is AI-graded, not an independent legal review; acceptance is recorded in STATUS.md.')
        if ZIP_NOT_CHECKED:
            warnings.append('The tested ZIP ' + ZIP_NOT_CHECKED[0] + ' is missing, so its SHA-256 was not compared with the test record.')
        check('fixtures exist', (root/'tests/fixtures.md').is_file())
        status = re.search(r'^Current version:\s*(\S+)', (root/'STATUS.md').read_text(encoding='utf-8'), re.M)
        check('STATUS.md version matches manifest', status and status.group(1) == version)
        check('README title has current version', version in (root/'README.md').read_text(encoding='utf-8').splitlines()[0])
        for name in ['LICENSE.md','LICENSE-Apache-2.0.txt','LICENSE-CC-BY-4.0.txt','NOTICE','THIRD_PARTY_NOTICES.md']:
            check('license file '+name, (root/name).is_file())
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
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        check('validation completed: '+str(exc), False)
    return {'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL',
        'scope':'Static structure and consistency only; no legal/model execution or deployment',
        'candidate':version,'checks':checks,'warnings':warnings}

if __name__ == '__main__':
    report = validate()
    print(json.dumps({k:report[k] for k in ['status','scope','candidate','warnings']},ensure_ascii=False,indent=2))
    print(str(sum(c['passed'] for c in report['checks']))+'/'+str(len(report['checks']))+' checks passed')
    for item in report['checks']:
        if not item['passed']: print('FAIL: '+item['check'])
    raise SystemExit(0 if report['status']=='PASS' else 1)
