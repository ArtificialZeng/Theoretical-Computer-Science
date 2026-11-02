"""Run the packaged finite diagnostics without overwriting frozen results.

Use an unpacked source package. A temporary tree under manuscript/ is removed
after execution; only scientific counts are compared, never timestamps or
workflow identities. These checks do not prove the universal theorem.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    'evidence/research-bf90b0105355-check.py',
    'intake/root-diagnostics/check_fenwick_trace_oracle.py',
    'intake/root-diagnostics/check_localized_net.py',
    'manuscript/repro/independent_check.py',
]

def main():
    expected_research = json.loads((ROOT / 'evidence/research-bf90b0105355-checks.json').read_text())
    expected_independent = json.loads((ROOT / 'manuscript/repro/independent_reference.json').read_text())
    with tempfile.TemporaryDirectory(prefix='diagnostic-', dir=ROOT / 'manuscript') as tmp:
        clean = Path(tmp)
        for rel in FILES:
            target = clean / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        for script in [FILES[0], FILES[-1]]:
            subprocess.run([sys.executable, str(clean / script)], cwd=clean, check=True)
        actual_research = json.loads((clean / 'evidence/research-bf90b0105355-checks.json').read_text())
        actual_independent = json.loads((clean / 'manuscript/repro/independent_check.json').read_text())
        for actual, expected in [(actual_research, expected_research),
                                 (actual_independent, expected_independent)]:
            if actual['status'] != 'passed' or actual['counts'] != expected['counts']:
                raise RuntimeError('Finite scientific counts differ from the packaged reference.')
    print('Both diagnostic suites reproduced their packaged scientific counts.')

if __name__ == '__main__':
    main()
