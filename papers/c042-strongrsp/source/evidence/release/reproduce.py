"""Rebuild the complete declared publication source package in an isolated subdirectory."""
from pathlib import Path
import hashlib, json, shutil, subprocess, zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'evidence/release'
pub = json.loads((ROOT / 'publication.json').read_text())
files = sorted(set(pub['source_files'] + ['publication.json']))
archive = OUT / 'source-package-working_paper.zip'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for name in files:
        z.write(ROOT / name, name)
dest = OUT / 'reproduced'
dest.mkdir(exist_ok=False)
with zipfile.ZipFile(archive) as z:
    z.extractall(dest)
for name in files:
    assert sha(ROOT / name) == sha(dest / name), name
with (OUT / 'reproduction-build.log').open('w') as log:
    build = subprocess.run(['sh', 'manuscript/build.sh'], cwd=dest, stdout=log, stderr=subprocess.STDOUT)
assert build.returncode == 0, 'See reproduction-build.log'
pdf = dest / pub['pdf']
text = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-'])
original = subprocess.check_output(['pdftotext', '-layout', str(ROOT / pub['pdf']), '-'])
assert text == original, 'Extracted text mismatch'
info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
assert any(s.split()[1] == str(pub['pages']) for s in info.splitlines() if s.startswith('Pages:'))
pages = OUT / 'reproduction-pages'
pages.mkdir()
subprocess.run(['pdftoppm', '-r', '115', '-png', str(pdf), str(pages / 'page')], check=True)
for image in list(pages.glob('page-*.png')):
    number = int(image.stem.rsplit('-', 1)[1])
    target = pages / f'page-{number:02d}.png'
    if image != target:
        image.rename(target)
image_checks = []
for i in range(1, pub['pages'] + 1):
    name = f'page-{i:02d}.png'
    same = sha(pages / name) == sha(OUT / 'pages' / name)
    image_checks.append({'page': i, 'pixels_identical': same})
    assert same, name
result = {'job_id': 'c042-strongrsp-release-8a7cb8c2de68', 'archive': str(archive.relative_to(ROOT)),
          'archive_digest': sha(archive), 'files': {n: sha(ROOT / n) for n in files},
          'clean_source_rebuild': True, 'text_identical': True, 'pages': pub['pages'],
          'page_comparisons': image_checks, 'pdf_bytes_identical': sha(pdf) == sha(ROOT / pub['pdf']),
          'note': 'PDF creation dates and object identifiers may differ; every rendered page and extracted text must match.'}
(OUT / 'reproduction.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'clean_source_rebuild': True, 'text_identical': True, 'all_page_pixels_identical': True, 'pages': pub['pages']}))
