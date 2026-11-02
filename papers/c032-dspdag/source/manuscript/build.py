#!/usr/bin/env python3
"""Clean local build; run python3 manuscript/build.py from an extracted project."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess

root = Path(__file__).resolve().parent.parent
source = root / 'manuscript'
work = root / 'tmp/pdfs/clean-build'
logs = root / 'evidence/write'
output = root / 'output/pdf/dspdag-working_paper.pdf'
if work.exists():
    shutil.rmtree(work)
work.mkdir(parents=True)
logs.mkdir(parents=True, exist_ok=True)
output.parent.mkdir(parents=True, exist_ok=True)
for name in ('main.tex', 'references.bib', 'acmart.cls', 'ACM-Reference-Format.bst'):
    shutil.copyfile(source / name, work / name)
build_env = os.environ.copy()
build_env.update(SOURCE_DATE_EPOCH='1793620800', FORCE_SOURCE_DATE='1', TZ='UTC')
commands = [
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex'],
    ['bibtex', 'main'],
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex'],
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'main.tex'],
]
for index, command in enumerate(commands, 1):
    with (logs / f'clean-build-{index}.txt').open('w') as stream:
        subprocess.run(command, cwd=work, env=build_env, stdout=stream,
                       stderr=subprocess.STDOUT, check=True, timeout=90)
shutil.copyfile(work / 'main.pdf', output)
shutil.copyfile(work / 'main.bbl', source / 'main.bbl')
shutil.copyfile(work / 'main.log', logs / 'final-build.log')
shutil.copyfile(work / 'main.blg', logs / 'final-bibtex.log')
record = {'build_command': 'python3 manuscript/build.py',
          'pdf': str(output.relative_to(root)),
          'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
          'source_date_epoch': build_env['SOURCE_DATE_EPOCH'],
          'commands': commands}
(logs / 'clean-build.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record))
