#!/usr/bin/env python3
"""Run the released finite checks in disposable copies; standard library only."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]


def select(parser):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true')
    group.add_argument('--paper')
    parser.add_argument('--jobs', type=int, default=3)
    parser.add_argument('--timeout', type=int, default=600)
    args = parser.parse_args()
    papers = json.loads((ROOT / 'catalog.json').read_text())['papers']
    chosen = [p for p in papers if args.all or p['id'] == args.paper]
    if not chosen:
        parser.error('Unknown paper ID')
    if args.jobs < 1 or args.timeout < 1:
        parser.error('jobs and timeout must be positive')
    return args, chosen


def check(p, timeout, destination):
    records = []
    with tempfile.TemporaryDirectory(prefix='tcs-check-') as temporary:
        source = Path(temporary) / 'source'
        shutil.copytree(ROOT / p['source_directory'], source)
        for i, command in enumerate(p['reproduction_commands'], 1):
            started = time.monotonic()
            try:
                r = subprocess.run([sys.executable, '-B', *command], cwd=source,
                                   capture_output=True, timeout=timeout)
                output, code = r.stdout + r.stderr, r.returncode
            except subprocess.TimeoutExpired as e:
                output, code = (e.stdout or b'') + (e.stderr or b'') + b'\nTIMEOUT\n', 124
            output = output.replace(str(Path(temporary)).encode(), b'<temporary>')
            log = destination / f"{p['id']}-{i}.log"
            log.write_bytes(output)
            records.append({'command': ['python3', '-B', *command], 'exit_code': code,
                            'seconds': round(time.monotonic() - started, 3),
                            'log': log.relative_to(ROOT).as_posix()})
            if code:
                break
    passed = all(r['exit_code'] == 0 for r in records)
    print(f"{p['id']}: {'PASS' if passed else 'FAIL'}", flush=True)
    return {'id': p['id'], 'passed': passed, 'checks': records}


def main():
    if sys.version_info < (3, 10):
        raise SystemExit('Python 3.10+ is required (some exact checks use int.bit_count).')
    args, papers = select(argparse.ArgumentParser(description=__doc__))
    destination = ROOT / 'validation/reproduction'
    destination.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        records = list(executor.map(lambda p: check(p, args.timeout, destination), papers))
    passed = all(p['passed'] for p in records)
    (destination / 'summary.json').write_text(json.dumps({
        'utc': datetime.now(timezone.utc).isoformat(), 'passed': passed,
        'python': sys.version, 'python_executable': Path(sys.executable).name,
        'scope': 'Finite checks accompanying the manuscripts; not an independent proof of all general theorems',
        'papers': records}, indent=2) + '\n')
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
