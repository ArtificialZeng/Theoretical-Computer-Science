#!/usr/bin/env python3
"""Verify every indexed PDF, ZIP and expanded source byte, including versions."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def verify(p):
    keys=[('source_archive','source_archive_sha256')]
    if 'pdf' in p:
        keys.append(('pdf','pdf_sha256'))
    else:
        assert p.get('kind')=='unresolved-research-record' and p.get('has_pdf') is False
    for key, digest in keys:
        assert hashlib.sha256((ROOT / p[key]).read_bytes()).hexdigest() == p[digest], p[key]
    source = ROOT / p['source_directory']
    prefix = p['archive_prefix']
    expected = set()
    with zipfile.ZipFile(ROOT / p['source_archive']) as archive:
        for item in archive.infolist():
            if item.is_dir():
                continue
            assert item.filename.startswith(prefix)
            relative = PurePosixPath(item.filename[len(prefix):])
            assert str(relative) and not relative.is_absolute() and '..' not in relative.parts
            assert str(relative) not in expected
            expected.add(str(relative))
            assert (source / str(relative)).read_bytes() == archive.read(item), str(relative)
    actual = {f.relative_to(source).as_posix() for f in source.rglob('*') if f.is_file()}
    assert expected == actual, p['id'] if 'id' in p else p['pdf']
    return len(expected)


def main():
    records=[]
    for p in json.loads((ROOT/'catalog.json').read_text())['papers']:
        count=verify(p)
        versions=[{'pdf':v['pdf'],'files':verify(v)} for v in p.get('additional_versions',[])]
        records.append({'id':p['id'],'files':count,'additional_versions':versions,'verified':True})
    research=[]
    index=ROOT/'research-records.json'
    if index.is_file():
        for p in json.loads(index.read_text())['records']:
            research.append({'id':p['id'],'original_status':p['original_status'],
                             'files':verify(p),'verified':True,'has_pdf':False})
    print(json.dumps({'verified':True,'topics':len(records),'papers':records,'research_records':research},indent=2))


if __name__ == '__main__':
    main()
