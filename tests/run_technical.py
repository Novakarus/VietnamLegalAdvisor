# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import shutil, subprocess, json, hashlib, sys, zipfile
import argparse
src=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Technical tests on disposable copies; never executes legal/model cases.')
parser.add_argument('--work-dir', required=True, help='New directory outside this repository for synthetic test copies')
args=parser.parse_args()
out=Path(args.work_dir).resolve()
if out == src or out.is_relative_to(src) or out.exists():
    parser.error('Choose a new directory outside the repository')
out.mkdir(parents=True)
rows=[]
def case(name, mutate=None, expected=0, package=False):
    root=out/name
    shutil.copytree(src,root,ignore=shutil.ignore_patterns('dist','__pycache__'))
    if mutate: mutate(root)
    script=root/'scripts'/('package.py' if package else 'validate.py')
    cmd=[sys.executable,'-X','utf8',str(script)]
    if not package: cmd.append('--no-write')
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
    row={'test':name,'expected':'accept' if expected==0 else 'reject','exit_code':p.returncode,'passed':(p.returncode==0)==(expected==0),'output':p.stdout+p.stderr}
    rows.append(row)
    return root
def edit(root,rel,fn):
    p=root/rel; obj=json.loads(p.read_text(encoding='utf-8-sig')); fn(obj); p.write_text(json.dumps(obj),encoding='utf-8')
case('baseline')
case('missing_icon',lambda r:(r/'plugin/assets/vietnam-legal-advisor-icon-v4.png').unlink(),1)
case('manifest_mismatch',lambda r:edit(r,'plugin/plugin.json',lambda o:o.update(version='0.69.2')),1)
case('missing_skill',lambda r:(r/'plugin/skills/legal-reasoning/SKILL.md').unlink(),1)
case('invalid_json',lambda r:(r/'plugin/plugin.json').write_text('{'),1)
case('missing_webpage',lambda r:(r/'docs/privacy/index.html').unlink(),1)
def false_pass(r):
    def change(o):
        c=o['cases'][0]; c.update(status='PASS',scores=[4]*6,reviewer='test',evidence_locations=['does-not-exist.txt'],defects=['critical: fabricated authority'])
    edit(r,'tests/results.json',change)
case('false_pass_evidence',false_pass,1)
def fake_png(r):
    (r/'plugin/assets/vietnam-legal-advisor-icon-v4.png').write_bytes(b'\x89PNG\r\n\x1a\n'+b'\0'*8+(512).to_bytes(4,'big')*2)
case('truncated_png',fake_png,1)
case('unexpected_root_file',lambda r:(r/'plugin/unexpected.txt').write_text('fixture'),1,True)
case('env_exact',lambda r:(r/'plugin/assets/.env').write_text('SYNTHETIC_TEST=1'),1,True)
case('env_local',lambda r:(r/'plugin/assets/.env.local').write_text('SYNTHETIC_TEST=1'),1,True)
root=case('package_baseline',package=True)
z=next((root/'dist').glob('*.zip')); first=hashlib.sha256(z.read_bytes()).hexdigest()
p=subprocess.run([sys.executable,str(root/'scripts/package.py')],capture_output=True)
rows.append({'test':'reproducible_zip','passed':p.returncode==0 and first==hashlib.sha256(z.read_bytes()).hexdigest()})
with zipfile.ZipFile(z) as f:
    rows.append({'test':'archive_integrity','passed':f.testzip() is None and 'plugin.json' in f.namelist() and all(not n.startswith(('docs/','tests/','scripts/')) for n in f.namelist()),'file_count':len(f.namelist())})
(out/'technical-results.json').write_text(json.dumps({'source':str(src),'tests':rows,'behavioral_suite':'NOT_RUN: no isolated candidate-loaded model executor used'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{'test':r['test'],'passed':r['passed']} for r in rows],indent=2))

raise SystemExit(0 if all(row["passed"] for row in rows) else 1)
