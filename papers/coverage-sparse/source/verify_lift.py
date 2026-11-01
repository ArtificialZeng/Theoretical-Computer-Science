#!/usr/bin/env python3
"""Independently lift rational occupancy certificates to every individual set.

Reads the six finite certificates; uses explicit bitsets, rather than the LP's
occupancy variables, to verify normalization, every vertex and edge moment,
coverage value and every dual inequality. Standard library only.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json

root = Path(__file__).resolve().parent
data = json.loads((root / 'evidence/exact-checks.json').read_text())
reports = []
for case in data['finite_lp_cases']:
    k, m = case['k'], case['m']
    n = k * m
    atoms = {}
    for atom in case['primal']:
        profile = tuple(atom['profile'])
        # The multinomial integer must be computed with a single denominator.
        denom = 1
        for count in profile:
            denom *= factorial(count)
        orbit = factorial(m) // denom
        for a, count in enumerate(profile):
            orbit *= comb(k, a) ** count
        atoms[profile] = F(atom['weight']) / orbit
    mass = F(0)
    marginals = [F(0)] * n
    edges = {(r*k+i, r*k+j): F(0)
             for r in range(m) for i in range(k) for j in range(i+1, k)}
    expected = F(0)
    dual = list(map(F, case['dual']))
    for bits in range(1 << n):
        counts = [((bits >> (r*k)) & ((1 << k)-1)).bit_count()
                  for r in range(m)]
        profile = tuple(counts.count(a) for a in range(k+1))
        weight = atoms.get(profile, F(0))
        uncovered = F(1)
        for a in counts:
            uncovered *= F(k-a, k)
        f = 1 - uncovered
        t = bits.bit_count()
        pairs = sum(a*(a-1)//2 for a in counts)
        assert dual[0] + dual[1]*t + dual[2]*pairs >= f
        mass += weight
        expected += weight*f
        for i in range(n):
            if bits & (1 << i):
                marginals[i] += weight
        for i, j in edges:
            if bits & (1 << i) and bits & (1 << j):
                edges[i, j] += weight
    assert mass == 1
    assert all(x == F(1, m) for x in marginals)
    assert all(x == F(1, m*m) for x in edges.values())
    assert expected == F(case['exact_optimum'])
    assert sum(a*b for a, b in zip(dual, [1, k, F(comb(k,2),m)])) == expected
    reports.append({'k': k, 'm': m, 'sets_enumerated': 1 << n,
                    'vertices_checked': n, 'edges_checked': len(edges),
                    'verified_optimum': str(expected)})
result = {'arithmetic': 'exact rational', 'full_set_lifts': reports,
          'status': 'all finite primal/dual certificates verified'}
(root/'evidence/lift-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
