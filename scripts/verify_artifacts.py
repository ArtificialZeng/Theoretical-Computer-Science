#!/usr/bin/env python3
"""Verify released hashes and every byte of the expanded source archives."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    records = []
    for p in json.loads((ROOT / 'catalog.json').read_text())['papers']:
        for key, digest in [('pdf', 'pdf_sha256'), ('source_archive', 'source_archive_sha256')]:
            assert hashlib.sha256((ROOT / p[key]).read_bytes()).hexdigest() == p[digest], p['id']
        source = ROOT / p['source_directory']
        with zipfile.ZipFile(ROOT / p['source_archive']) as z:
            files = [i for i in z.infolist() if not i.is_dir()]
            prefixes = {PurePosixPath(i.filename).parts[0] for i in files}
            assert len(prefixes) == 1
            expected = set()
            for i in files:
                parts = PurePosixPath(i.filename).parts
                assert '..' not in parts and not i.filename.startswith('/')
                relative = Path(*parts[1:])
                expected.add(relative.as_posix())
                assert (source / relative).read_bytes() == z.read(i), str(relative)
            actual = {f.relative_to(source).as_posix() for f in source.rglob('*') if f.is_file()}
            assert expected == actual, p['id']
        records.append({'id': p['id'], 'files': len(expected), 'hashes_and_expansion_verified': True})
    print(json.dumps({'verified': True, 'papers': records}, indent=2))


if __name__ == '__main__':
    main()
