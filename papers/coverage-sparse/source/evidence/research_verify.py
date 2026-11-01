#!/usr/bin/env python3
"""New exact checks of the research proof. Run from any directory.

Checks only the stated finite domains. The all-parameter proof is in
research-proof.md. No optimizer or floating-point computation is used.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod
from pathlib import Path
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parents[1]
JOB = 'coverage-sparse-research-6239617d8b3f'
SOURCE_HASH = 'eb7061a17cead0bc8cc0e4426f3f8260ac3137dd23b6f4813d8f4952b00ec731'


def coverage(k, a):
    return 1-prod(Q(k-v, k) for v in a)


def local_and_integer_line():
    local_count = line_count = 0
    for k in range(2, 121):
        q = Q(k-1, k)
        alpha, beta = 1-q**k, q**k/k
        for a in range(k+1):
            gap = q**a-Q(k-a, k)
            assert 0 <= gap <= Q(comb(a, 2), k*k)
            local_count += 1
        for t in range(12*k+1):
            assert 1-q**t <= alpha+beta*(t-k)
            line_count += 1
    return {'local_k_range': [2, 120], 'local_a_range': '0..k',
            'local_cases': local_count, 'supporting_line_t_range': '0..12k',
            'supporting_line_cases': line_count}


def occupancy_dual():
    count = original_vectors = 0
    for k in range(2, 11):
        q = Q(k-1, k)
        alpha, beta = 1-q**k, q**k/k
        for m in range(1, 7):
            # Every ordered vector is a permutation of one sorted vector;
            # all expressions checked here are invariant under permutations.
            for a in combinations_with_replacement(range(k+1), m):
                t, c = sum(a), sum(comb(v, 2) for v in a)
                val = coverage(k, a)
                assert val <= 1-q**t+Q(c, k*k)
                assert val <= alpha+beta*(t-k)+Q(c, k*k)
                count += 1
            original_vectors += (k+1)**m
    return {'k_range': [2, 10], 'm_range': [1, 6],
            'sorted_occupancy_profiles_checked': count,
            'ordered_vectors_covered_by_permutation_symmetry': original_vectors,
            'symmetry_reason': 'objective, T, C, and dual are block-permutation invariant'}


def resampling_laws():
    rng = random.Random(6239617)
    cases = features = edges = 0
    for k in range(1, 5):
        n = k+2
        colors = [i % k for i in range(n)]
        cmasks = [sum(1 << i for i in range(n) if colors[i] == c)
                  for c in range(k)]
        # Laws include degenerate marginals zero and one, plus fixed-seed
        # irregular rational laws. This is a finite sample, not exhaustion.
        laws = [{0: Q(1)}, {(1 << n)-1: Q(1)},
                {1: Q(1, 3), (1 << n)-2: Q(2, 3)}]
        for _ in range(7):
            masks = rng.sample(range(1 << n), min(5, 1 << n))
            weights = [rng.randrange(1, 12) for _ in masks]
            laws.append(dict(zip(masks, [Q(w, sum(weights)) for w in weights])))
        alpha = 1-Q(k-1, k)**k
        for law in laws:
            rlaw = defaultdict(Q)
            for samples in product(list(law), repeat=k):
                r = 0
                for s, cmask in zip(samples, cmasks):
                    r |= s & cmask
                rlaw[r] += prod(law[s] for s in samples)
            assert sum(rlaw.values()) == 1
            x = [sum(p for s, p in law.items() if s & (1 << i))
                 for i in range(n)]
            for i in range(n):
                assert sum(p for r, p in rlaw.items() if r & (1 << i)) == x[i]
            for i, j in combinations(range(n), 2):
                if colors[i] != colors[j]:
                    moment = sum(p for r, p in rlaw.items()
                                 if r & (1 << i) and r & (1 << j))
                    assert moment == x[i]*x[j]
                    edges += 1
            # Check every possible feature of this finite ground set.
            for h in range(1 << n):
                oldhit = sum(p for s, p in law.items() if s & h)
                newhit = sum(p for r, p in rlaw.items() if r & h)
                assert newhit >= alpha*oldhit
                features += 1
            cases += 1
    return {'seed': 6239617, 'k_range': [1, 4], 'n': 'k+2',
            'laws_checked': cases, 'feature_inequalities_checked': features,
            'individual_edge_equalities_checked': edges,
            'law_coverage': '3 boundary/structured and 7 fixed-seed rational laws for each k'}


def matching_error_laws():
    cases = []
    for m in range(1, 8):
        deltas = sorted(set([Q(0), Q(1, 3), Q(1), Q(2),
                             Q(m-1), Q(m), Q(m+1)]))
        for delta in deltas:
            law = defaultdict(Q)
            if m == 1:
                law[3] = Q(1)
            else:
                t = min(Q(1), (1+delta)/m)
                for r in range(m):
                    law[3 << (2*r)] += t/m
                for r, s in combinations(range(m), 2):
                    for i, j in product(range(2), repeat=2):
                        law[(1 << (2*r+i)) | (1 << (2*s+j))] += (1-t)/(4*comb(m, 2))
            assert sum(law.values()) == 1
            for i in range(2*m):
                assert sum(p for s, p in law.items() if s & (1 << i)) == Q(1, m)
            for r in range(m):
                edge = 3 << (2*r)
                moment = sum(p for s, p in law.items() if s & edge == edge)
                assert moment <= (1+delta)/m**2
                if delta == 0:
                    assert moment == Q(1, m*m)
            expected = sum(p*coverage(2, [((s >> (2*r)) & 3).bit_count()
                                         for r in range(m)]) for s, p in law.items())
            upper = min(Q(1), Q(3, 4)+(1+delta)/(4*m))
            assert expected == upper
            cases.append({'m': m, 'delta': str(delta),
                          'explicit_feasible_value': str(expected)})
    return {'scope': 'finite explicit matching laws, not a new general optimization claim',
            'm_range': [1, 7], 'cases': cases}


def main():
    before = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert before == SOURCE_HASH
    result = {'job_id': JOB, 'arithmetic': 'fractions.Fraction (exact)',
              'local_and_line': local_and_integer_line(),
              'occupancy_dual': occupancy_dual(),
              'resampling': resampling_laws(),
              'one_sided_error_attacks': matching_error_laws(),
              'source_sha256': before,
              'scope': 'Only finite checks as specified; infinite theorem relies on analytic proof.'}
    assert hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest() == before
    (ROOT/'evidence/research-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
