"""Clean, deterministic local build. Run with Python 3; requires TeX Live.

No network access or package installation is performed. Process environments
are never printed. The fixed timestamp is public build metadata.
"""
from pathlib import Path
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def main():
    # Remove only this manuscript's known generated build outputs.
    for suffix in ['aux', 'bbl', 'blg', 'fdb_latexmk', 'fls', 'log', 'out', 'pdf']:
        (HERE / ('main.' + suffix)).unlink(missing_ok=True)
    build_env = os.environ.copy()
    build_env['SOURCE_DATE_EPOCH'] = '1793613600'  # 2026-11-02 10:00:00 UTC
    build_env['FORCE_SOURCE_DATE'] = '1'
    with (HERE / 'build-console.log').open('w') as log:
        run = subprocess.run(
            ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
            cwd=HERE, env=build_env, stdout=log, stderr=subprocess.STDOUT)
    if run.returncode:
        print('Build failed; inspect manuscript/build-console.log.')
        return run.returncode
    text = (HERE / 'main.log').read_text(errors='replace')
    failures = [s for s in ['undefined references', 'undefined citations',
                           'Citation `', 'Overfull \\hbox', 'Overfull \\vbox',
                           '! LaTeX Error', '! Class acmart Error'] if s in text]
    if failures:
        print('Build-quality check failed:', ', '.join(failures))
        return 1
    print('Clean build passed: manuscript/main.pdf; full log in manuscript/main.log.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
