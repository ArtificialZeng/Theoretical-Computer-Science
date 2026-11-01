#!/usr/bin/env python3
"""Read-only exact checks of the accompanying finite certificates; no optimizer."""
from pathlib import Path
import json, runpy
ROOT=Path(__file__).resolve().parents[1]
def main():
    f=runpy.run_path(str(ROOT/'evidence/revision-research/verify_revision.py'),run_name='readonly_source_check')
    results={name:f[name]() for name in ('finite_certificates','matching_tests','core_dual_tests','product_tests','heterogeneous_tests')}
    print(json.dumps({'arithmetic':'exact fractions; Python standard library',
                     'scope':'finite verification; infinite statements have analytic proofs in the article',
                     'results':results},indent=2))
if __name__=='__main__': main()
