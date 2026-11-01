#!/usr/bin/env python3
"""Clean-build manuscript PDFs in disposable copies, preserving released files."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

from reproduce import ROOT, select


def pdf_text(path):
    if not shutil.which('pdftotext'):
        return None
    result = subprocess.run(['pdftotext', str(path), '-'], capture_output=True, check=True)
    return re.sub(rb'\s+', b' ', result.stdout).strip()


def build(p, timeout, destination):
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix='tcs-build-') as temporary:
        source = Path(temporary) / 'source'
        shutil.copytree(ROOT / p['source_directory'], source)
        for suffix in ('.aux', '.bbl', '.blg', '.fdb_latexmk', '.fls', '.out', '.toc'):
            for f in source.rglob('*' + suffix):
                f.unlink()
        for f in source.rglob('*.pdf'):
            f.unlink()
        environment = os.environ.copy()
        environment['TEXINPUTS'] = './/:'
        environment['BSTINPUTS'] = './/:'
        command = ['latexmk', '-gg', '-pdf', '-interaction=nonstopmode', '-halt-on-error',
                   '-outdir=../output/pdf', 'main.tex']
        try:
            result = subprocess.run(command, cwd=source / 'manuscript', env=environment,
                                    capture_output=True, timeout=timeout)
            output, code = result.stdout + result.stderr, result.returncode
        except subprocess.TimeoutExpired as e:
            output, code = (e.stdout or b'') + (e.stderr or b'') + b'\nTIMEOUT\n', 124
        built = source / 'output/pdf/main.pdf'
        text_equal = pdf_text(built) == pdf_text(ROOT / p['pdf']) if code == 0 and built.exists() else False
        log = destination / (p['id'] + '.log')
        log.write_bytes(output.replace(str(Path(temporary)).encode(), b'<temporary>'))
        passed = code == 0 and built.is_file() and text_equal
        record = {'id': p['id'], 'passed': passed, 'exit_code': code,
                  'normalized_pdf_text_matches_release': text_equal,
                  'seconds': round(time.monotonic() - started, 3),
                  'log': log.relative_to(ROOT).as_posix()}
    print(f"{p['id']}: {'PASS' if passed else 'FAIL'}", flush=True)
    return record


def main():
    args, papers = select(argparse.ArgumentParser(description=__doc__))
    for tool in ('latexmk', 'pdftotext'):
        if not shutil.which(tool):
            raise SystemExit('Required build verification tool not installed: ' + tool)
    destination = ROOT / 'validation/builds'
    destination.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        records = list(executor.map(lambda p: build(p, args.timeout, destination), papers))
    passed = all(p['passed'] for p in records)
    (destination / 'summary.json').write_text(json.dumps({
        'utc': datetime.now(timezone.utc).isoformat(), 'passed': passed,
        'comparison': 'Whitespace-normalized pdftotext output; PDF timestamps may differ',
        'papers': records}, indent=2) + '\n')
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
