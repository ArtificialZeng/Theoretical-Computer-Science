#!/usr/bin/env python3
"""Replay the actual 61-case reassessment without private literature caches.

Uses the included fixed referee implementation and serialized case results.
This is reproducibility of finite checks, not another mathematical referee,
an infinite proof, or a claim to rerun private snapshot/priority checks.
"""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'audit/c015-imagebound-referee-e7492ff4cfbd'
spec = importlib.util.spec_from_file_location('included_referee_verifier', AUDIT / 'verify.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)
saved = json.loads((AUDIT / 'verification.json').read_text())
original = json.loads((ROOT / 'evidence/research-check-results.json').read_text())
records = {(r['m'], tuple(r['lengths'])): r
           for key in ['frozen_cases', 'boundary_cases'] for r in original[key]}
results = []
serialized_checks = 0
for expected in saved['frozen_replays'] + saved['held_out_cases']:
    record = records.get((expected['m'], tuple(expected['lengths'])))
    actual = verifier.check_case(expected['m'], expected['lengths'], record=record)
    assert actual == expected
    results.append(actual)
    serialized_checks += int(record is not None)
potential = sum(r['potential_checks'] for r in results)
replacements = sum(r['simultaneous_replacement_checks'] for r in results)
assert potential == saved['total_potential_checks']
assert replacements == saved['total_simultaneous_replacement_checks']
print(json.dumps({
    'finite_cases_recomputed': len(results),
    'serialized_original_records_checked': serialized_checks,
    'potential_checks': potential,
    'simultaneous_replacement_checks': replacements,
    'all_saved_case_results_match': True,
    'scope': '61 finite case replays and included original-record comparisons; '
             'does not rerun nine extra intake certificates, private full-snapshot '
             'integrity, infinite proof, literature or novelty review'
}))
