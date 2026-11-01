#!/usr/bin/env python3
"""Fresh referee's exact finite checks; never writes frozen evidence.

Objectives in the five certificates are recomputed by explicitly listing
transversal features, rather than using the submitted occupancy objective.
No submitted Python module or optimizer is imported or executed.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'coverage-sparse-referee-20ee9a6fefc3'


def check_inputs():
    snap = json.loads((ROOT / 'audit/snapshot.json').read_text())
    for name, digest in snap['files'].items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    digest = sha256(json.dumps(snap['files'], sort_keys=True,
                              separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    assert digest == snap['digest']
    return snap


def alpha(k):
    return 1 - F(k - 1, k) ** k


def check_certificates():
    rows = json.loads((ROOT / 'evidence/revision-research/finite-certificates.json').read_text())
    results = []
    for row in rows:
        k, m = row['k'], row['m']
        n = k * m
        vertices = range(n)
        blocks = [set(range(r*k, (r+1)*k)) for r in range(m)]
        edges = [frozenset(e) for b in blocks for e in combinations(sorted(b), 2)]
        features = [frozenset(h) for h in product(*(sorted(b) for b in blocks))]
        subsets = [frozenset(vertices[i] for i in range(n) if mask & (1 << i))
                   for mask in range(1 << n)]
        values = {s: F(sum(bool(s & h) for h in features), len(features)) for s in subsets}
        orbits = defaultdict(list)
        y0, yt, yc = map(F, row['dual_y0_yT_yC'])
        slacks = []
        for s in subsets:
            occupancy = tuple(sorted(len(s & b) for b in blocks))
            orbits[occupancy].append(s)
            collisions = sum(e <= s for e in edges)
            rhs = y0 + yt * len(s) + yc * collisions
            assert rhs >= values[s], (row, s)
            # This separately verifies the submitted product-count identity.
            assert values[s] == 1 - prod(F(k-len(s & b), k) for b in blocks)
            slacks.append(rhs - values[s])
        assert len(orbits) == comb(m+k, k) == row['profiles']
        law = defaultdict(F)
        for profile, mass in row['primal']:
            orbit = orbits[tuple(profile)]
            for s in orbit:
                law[s] += F(mass) / len(orbit)
        assert sum(law.values()) == 1 and all(p >= 0 for p in law.values())
        for i in vertices:
            assert sum(p for s, p in law.items() if i in s) == F(1, m)
        cap = F(1, m*m)
        if row['model'] == 'upper':
            cap *= 1 + F(row['delta'])
            assert yc >= 0
        for e in edges:
            moment = sum(p for s, p in law.items() if e <= s)
            assert moment == cap
        expected = sum(p * values[s] for s, p in law.items())
        dual = y0 + yt * k + yc * len(edges) * cap
        assert expected == dual == F(row['optimum'])
        # Independent numerator certificate: a uniform whole block hits every feature.
        assert all(values[frozenset(b)] == 1 for b in blocks)
        results.append({'k': k, 'm': m, 'model': row['model'],
                        'exact_optimum': str(expected), 'all_subsets': len(subsets),
                        'explicit_features': len(features), 'individual_marginals': n,
                        'individual_tested_pairs': len(edges), 'support_size': len(law),
                        'minimum_dual_slack': str(min(slacks))})
    return results


def check_integer_duals():
    local = lines = profiles = 0
    for k in range(2, 33):
        q = F(k-1, k)
        for a in range(k+1):
            d = q**a - 1 + F(a, k)
            assert 0 <= d <= F(a*(a-1), 2*k*k)
            local += 1
        for t in range(0, 6*k+1):
            assert 1-q**t <= alpha(k)+F(q**k, k)*(t-k)
            lines += 1
        if k <= 7:
            for m in range(1, 8):
                for a in combinations_with_replacement(range(k+1), m):
                    value = 1-prod(F(k-v, k) for v in a)
                    c = sum(v*(v-1)//2 for v in a)
                    bound = alpha(k)+F(q**k, k)*(sum(a)-k)+F(c, k*k)
                    assert value <= bound
                    profiles += 1
    return {'local_cases': local, 'local_k_range': [2, 32],
            'integer_line_cases': lines, 'integer_t_range': '0..6k',
            'occupancy_profiles': profiles, 'occupancy_k_range': [2, 7],
            'occupancy_m_range': [1, 7]}


def check_matching():
    count = 0
    for m in range(1, 21):
        for mode in ['equality', 'multiplicative', 'additive']:
            errors = [F(0)] if mode == 'equality' else sorted({
                F(0), F(1, 7*m*m), F(1, m), F(m-1, m), F(m-1), F(m), F(2*m)})
            for error in errors:
                cap = F(1, m*m)+(error if mode == 'additive' else error/(m*m))
                t = min(F(1), m*cap)
                law = defaultdict(F)
                if m == 1:
                    law[frozenset([0, 1])] = F(1)
                else:
                    for r in range(m):
                        law[frozenset([2*r, 2*r+1])] += t/m
                    for r, s in combinations(range(m), 2):
                        for i, j in product(range(2), repeat=2):
                            law[frozenset([2*r+i, 2*s+j])] += (1-t)/(4*comb(m, 2))
                assert sum(law.values()) == 1 and all(p >= 0 for p in law.values())
                for i in range(2*m):
                    assert sum(p for s, p in law.items() if i in s) == F(1, m)
                for r in range(m):
                    moment = sum(p for s, p in law.items() if {2*r, 2*r+1} <= s)
                    assert moment <= cap
                    if mode == 'equality':
                        assert moment == cap
                value = sum(p*(1-prod(F(2-len(s & {2*r, 2*r+1}), 2) for r in range(m)))
                            for s, p in law.items())
                assert value == F(3, 4)+t/4
                count += 1
    return {'m_range': [1, 20], 'exact_coupling_cases': count,
            'modes': ['equality', 'multiplicative', 'additive']}


def check_resampling():
    cases = features_checked = 0
    n = 5
    original_laws = [
        {0: F(1)}, {31: F(1)},
        {0: F(1, 2), 31: F(1, 2)},
        {1: F(1, 6), 6: F(1, 3), 25: F(1, 2)},
        {3: F(2, 7), 12: F(3, 7), 17: F(2, 7)},
    ]
    for k in range(1, 6):
        classes = [sum(1 << i for i in range(n) if i % k == c) for c in range(k)]
        for d in original_laws:
            converted = {0: F(1)}
            for b in classes:
                nxt = defaultdict(F)
                for r, p in converted.items():
                    for s, z in d.items():
                        nxt[r | (s & b)] += p*z
                converted = dict(nxt)
            assert sum(converted.values()) == 1
            margins = [sum(p for s, p in d.items() if s & (1 << i)) for i in range(n)]
            for i in range(n):
                assert sum(p for s, p in converted.items() if s & (1 << i)) == margins[i]
            for i, j in combinations(range(n), 2):
                if i % k != j % k:
                    both = (1 << i) | (1 << j)
                    assert sum(p for s, p in converted.items() if s & both == both) == margins[i]*margins[j]
            for h in range(1 << n):
                before = sum(p for s, p in d.items() if s & h)
                after = sum(p for s, p in converted.items() if s & h)
                assert after >= alpha(k)*before
                features_checked += 1
            cases += 1
    return {'ground_set_size': n, 'color_counts': [1, 2, 3, 4, 5],
            'exact_law_conversions': cases, 'features_checked': features_checked,
            'boundaries': 'zero and one marginals; empty feature; deterministic laws'}


def check_products_and_table():
    cases = []
    for k, m in [(2, 1), (2, 3), (3, 2), (3, 3), (4, 2)]:
        n = k*m
        features = [frozenset(h) for h in product(*(range(r*k, (r+1)*k) for r in range(m)))]
        expected = F(0)
        for mask in range(1 << n):
            s = frozenset(i for i in range(n) if mask & (1 << i))
            weight = F(1, m)**len(s)*F(m-1, m)**(n-len(s))
            expected += weight*F(sum(bool(s & h) for h in features), len(features))
        assert expected == alpha(m)
        assert expected <= min(F(1), alpha(k)+F(k-1, 2*k*m))
        cases.append({'k': k, 'm': m, 'product_expectation': str(expected)})
    assert alpha(3) == F(19, 27) < alpha(2)
    table = [{'k': k, 'alpha': str(alpha(k)), 'inverse': str(1/alpha(k)),
              'finite_coefficient': str(F(k-1, 2*k))} for k in range(2, 7)]
    return {'exact_product_cases': cases, 'constant_table': table,
            'alpha_k_lower_bound_for_full_hierarchy': 'false; k=2,m=3,t=6 gives 19/27 < 3/4'}


def main():
    snap = check_inputs()
    result = {'job_id': JOB, 'snapshot_digest': snap['digest'],
              'arithmetic': 'exact rational; Python standard library only',
              'certificates': check_certificates(), 'integer_duals': check_integer_duals(),
              'matching': check_matching(), 'resampling': check_resampling(),
              'product_and_table': check_products_and_table(),
              'limits': 'Finite checks supplement the all-parameter analytic audit; no formalization or optimizer.'}
    assert check_inputs()['digest'] == snap['digest']
    out = ROOT / 'audit/referee-20ee9a6fefc3-verification.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
