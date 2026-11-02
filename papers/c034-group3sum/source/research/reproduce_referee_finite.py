#!/usr/bin/env python3
"""Portable execution of the exact finite part of the original fresh verifier.

The original audit/referee-verifier.py is preserved byte-for-byte. Its last
internal whole-packet integrity check needs third-party literature caches,
which are deliberately not redistributed. This adapter executes every finite
check before that integrity-only suffix, verifies the original code hash,
and compares the full finite counts with the original recorded result.
No fast matrix algorithm or infinite theorem is validated by this script.
"""
import ast
import hashlib
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
ORIGINAL = PROJECT / 'audit/referee-verifier.py'
EXPECTED_ORIGINAL_SHA256 = '3f35af1acdcc3169499b0d8faee516255a1e6ba16c80be2743079701b4394df2'
SNAPSHOT_DIGEST = '15a73043f23436b1592a376f95f678e39919b724da29d1fc7773757f6a82f52a'
source = ORIGINAL.read_bytes()
assert hashlib.sha256(source).hexdigest() == EXPECTED_ORIGINAL_SHA256
module = ast.parse(source, filename=str(ORIGINAL))
markers = [i for i, statement in enumerate(module.body)
           if isinstance(statement, ast.Assign)
           and any(isinstance(t, ast.Name) and t.id == 'snapshot'
                   for t in statement.targets)]
assert len(markers) == 1, 'Original integrity suffix must be located unambiguously'
cut = markers[0]
assert cut > 0
finite = ast.Module(body=module.body[:cut], type_ignores=[])
namespace = {'__name__': '__main__', '__file__': str(ORIGINAL)}
exec(compile(ast.fix_missing_locations(finite), str(ORIGINAL), 'exec'), namespace)
counts = dict(namespace['stats'])
recorded = json.loads((PROJECT / 'audit/referee-verifier-results.json').read_text())
assert recorded['snapshot_digest'] == SNAPSHOT_DIGEST
assert counts == recorded['counts'], 'Finite coverage changed'
result = {
    'job_id': recorded['job_id'],
    'snapshot_digest': SNAPSHOT_DIGEST,
    'status': 'all_exact_assertions_passed',
    'counts': counts,
    'mode': 'root portable finite-only adapter; not a new fresh review',
    'original_verifier_sha256': EXPECTED_ORIGINAL_SHA256,
    'all_finite_checks_executed': True,
    'internal_literature_cache_hash_loop_executed': False,
    'limitations': [
        'Third-party paper full texts are not in the delivered archive; the original internal whole-packet integrity loop is intentionally omitted here.',
        'The unchanged original verifier and its recorded results are included. Every finite check before its integrity-only suffix executes unchanged.',
        'These are finite algebra/interface checks, not a fast-backend benchmark, formal proof, or a new mathematical/novelty acceptance.'
    ]
}
(PROJECT / 'evidence/portable-referee-results.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
