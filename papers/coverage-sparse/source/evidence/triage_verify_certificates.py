#!/usr/bin/env python3
"""Check supplied rational LP certificates on original subsets, not LP bases.

This finite check does not certify the proposed infinite graph-class theorem.
Run from PROJECT_DIR: python3 evidence/triage_verify_certificates.py
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'evidence/exact-checks.json').read_text())
results = []
for case in data['finite_lp_cases']:
    k, m = case['k'], case['m']
    n = k * m
    edge_list = [(r*k+i, r*k+j) for r in range(m)
                 for i, j in combinations(range(k), 2)]
    law = {}
    for atom in case['primal']:
        profile = tuple(atom['profile'])
        multiplicity = factorial(m) // prod(factorial(c) for c in profile)
        multiplicity *= prod(comb(k, a)**c for a, c in enumerate(profile))
        assert profile not in law
        law[profile] = Q(atom['weight']) / multiplicity
    mass = Q(0)
    marginals = [Q(0) for _ in range(n)]
    moments = [Q(0) for _ in edge_list]
    objective = Q(0)
    dual = list(map(Q, case['dual']))
    for mask in range(1 << n):
        occupancy = [sum((mask >> (r*k+i)) & 1 for i in range(k))
                     for r in range(m)]
        profile = tuple(occupancy.count(a) for a in range(k+1))
        value = 1 - prod(Q(k-a, k) for a in occupancy)
        pair_count = sum(comb(a, 2) for a in occupancy)
        assert dual[0] + dual[1]*sum(occupancy) + dual[2]*pair_count >= value
        probability = law.get(profile, Q(0))
        mass += probability
        objective += probability * value
        for i in range(n):
            if (mask >> i) & 1:
                marginals[i] += probability
        for j, (u, v) in enumerate(edge_list):
            if ((mask >> u) & 1) and ((mask >> v) & 1):
                moments[j] += probability
    assert mass == 1
    assert all(x == Q(1, m) for x in marginals)
    assert all(x == Q(1, m*m) for x in moments)
    dual_objective = dual[0] + dual[1]*k + dual[2]*Q(comb(k, 2), m)
    assert objective == dual_objective == Q(case['exact_optimum'])
    results.append({'k': k, 'm': m, 'original_subsets_checked': 1 << n,
                    'tested_edges': len(edge_list), 'optimum': str(objective),
                    'primal_marginals_and_each_edge_checked': True,
                    'dual_checked_on_each_subset': True})
output = {'job_id': 'coverage-sparse-triage-8c18589f991c',
          'arithmetic': 'exact fractions.Fraction', 'cases': results,
          'source_sha256': hashlib.sha256((ROOT / 'source.md').read_bytes()).hexdigest(),
          'scope': 'Six finite witness instances only; no infinite theorem or novelty certification.'}
target = ROOT / 'evidence/triage-certificate-checks.json'
target.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
