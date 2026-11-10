# SPDX-License-Identifier: Apache-2.0
"""Validate, then package only plugin/ into dist/. Never upload or deploy."""
from pathlib import Path
import hashlib
import json
import zipfile
from validate import ROOT, validate

def package():
    report = validate()
    if report['status'] != 'PASS':
        for c in report['checks']:
            if not c['passed']: print('FAIL: '+c['check'])
        raise SystemExit('Packaging stopped: static validation failed.')
    pkg = ROOT/'plugin'
    files = sorted(p for p in pkg.rglob('*') if p.is_file())
    allowed = {'plugin.json','.codex-plugin/plugin.json','LICENSE.md'}
    for p in files:
        rel = p.relative_to(pkg).as_posix()
        if p.is_symlink() or not p.resolve().is_relative_to(pkg.resolve()):
            raise SystemExit('Unsafe package path: '+rel)
        if rel not in allowed and not rel.startswith(('skills/','assets/')):
            raise SystemExit('Unexpected package file; review before inclusion: '+rel)
        if rel.startswith('assets/') and p.suffix.lower() != '.png':
            raise SystemExit('Asset type not approved: '+rel)
        if rel.startswith('skills/') and p.suffix.lower() not in {'.md','.json','.yaml'}:
            raise SystemExit('Skill file type not approved: '+rel)
    dest = ROOT/'dist'; dest.mkdir(exist_ok=True)
    archive = dest/('Vietnam-Legal-Advisor-'+report['candidate']+'.zip')
    temporary = archive.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temporary,'w',zipfile.ZIP_DEFLATED) as z:
        for p in files:
            entry = zipfile.ZipInfo(p.relative_to(pkg).as_posix(),date_time=(1980,1,1,0,0,0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry,p.read_bytes())
    with zipfile.ZipFile(temporary) as z:
        assert z.testzip() is None
        assert 'plugin.json' in z.namelist()
        assert set(z.namelist()) == {p.relative_to(pkg).as_posix() for p in files}
        assert all(z.read(p.relative_to(pkg).as_posix()) == p.read_bytes() for p in files)
    temporary.replace(archive)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix('.zip.sha256').write_text(digest+'  '+archive.name+'\n',encoding='utf-8')
    print(json.dumps({'archive':str(archive),'files':len(files),'sha256':digest,'behavioral_acceptance':'Not certified by this script','deployed':False},indent=2))

if __name__ == '__main__':
    package()
