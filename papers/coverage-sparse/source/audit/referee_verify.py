#!/usr/bin/env python3
"""Fresh exact finite attacks; does not import or run the research verifier.

Run from any directory. Writes only audit/referee-checks.json. These finite
checks supplement the analytic proof; they do not prove an infinite theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'coverage-sparse-referee-ec417dd22ce0'


def integrity():
    snap = json.loads((ROOT/'audit/snapshot.json').read_text())
    actual = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
              for p in snap['files']}
    assert actual == snap['files']
    digest = hashlib.sha256(json.dumps(actual, sort_keys=True,
        separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    assert digest == snap['digest']
    return {'snapshot_digest': digest, 'all_frozen_files_match': True,
            'source_sha256': actual['source.md']}


def direct_subsets():
    cases = []
    for k, max_m in [(2, 6), (3, 4), (4, 3), (5, 2)]:
        for m in range(1, max_m+1):
            n = k*m
            features = [sum(1 << (r*k+j) for r, j in enumerate(u))
                        for u in product(range(k), repeat=m)]
            edge_masks = [(1 << (r*k+i)) | (1 << (r*k+j))
                          for r in range(m) for i, j in combinations(range(k), 2)]
            q = F(k-1, k)
            alpha, beta = 1-q**k, q**k/k
            for mask in range(1 << n):
                # Evaluate the serialized definition, not the occupancy formula.
                f = F(sum(bool(mask & h) for h in features), len(features))
                t = mask.bit_count()
                collisions = sum((mask & e) == e for e in edge_masks)
                occupancy = [(mask >> (r*k) & ((1 << k)-1)).bit_count()
                             for r in range(m)]
                assert f == 1-prod(F(k-a, k) for a in occupancy)
                assert f <= 1-q**t+F(collisions, k*k)
                assert f <= alpha+beta*(t-k)+F(collisions, k*k)
            cases.append({'k': k, 'm': m, 'all_subsets': 1 << n,
                          'explicit_features': len(features),
                          'tested_edges': len(edge_masks)})
    return cases


def color_laws():
    n = 4
    inputs = [{0: F(1)}, {15: F(1)}, {1: F(1, 3), 14: F(2, 3)}]
    weights = [((7*s+3) % 11)+1 for s in range(16)]
    inputs.append({s: F(w, sum(weights)) for s, w in enumerate(weights)})
    law_count = feature_count = edge_count = 0
    for k in range(1, 5):
        alpha = 1-F(k-1, k)**k
        # Includes every labeled coloring, empty classes, and repeated colors.
        for colors in product(range(k), repeat=n):
            masks = [sum(1 << i for i in range(n) if colors[i] == c)
                     for c in range(k)]
            for law in inputs:
                # Independent implementation: form each projected law first,
                # then convolve those disjoint-coordinate distributions.
                out = {0: F(1)}
                for cmask in masks:
                    projected = defaultdict(F)
                    for s, mass in law.items():
                        projected[s & cmask] += mass
                    nxt = defaultdict(F)
                    for a, pa in out.items():
                        for b, pb in projected.items():
                            nxt[a | b] += pa*pb
                    out = nxt
                assert sum(out.values()) == 1
                x = [sum(p for s, p in law.items() if s & (1 << i))
                     for i in range(n)]
                for i in range(n):
                    assert sum(p for s, p in out.items() if s & (1 << i)) == x[i]
                for i, j in combinations(range(n), 2):
                    if colors[i] != colors[j]:
                        e = (1 << i) | (1 << j)
                        assert sum(p for s, p in out.items() if s & e == e) == x[i]*x[j]
                        edge_count += 1
                for h in range(1 << n):
                    old = sum(p for s, p in law.items() if s & h)
                    new = sum(p for s, p in out.items() if s & h)
                    assert new >= alpha*old
                    feature_count += 1
                law_count += 1
    return {'n': n, 'k_range': [1, 4], 'all_labeled_colorings': 354,
            'laws_per_coloring': len(inputs), 'law_cases': law_count,
            'feature_cases': feature_count, 'tested_edge_equalities': edge_count,
            'serialized_laws': [{str(s): str(p) for s, p in law.items()}
                                for law in inputs]}


def occupancy_extreme_points():
    """Exact optimization after within-block and block-permutation averaging.

    This averaging preserves objective, every marginal, and every tested
    edge constraint. A uniform orbit of an occupancy profile has marginal
    T/(mk) and tested moment C/(m*choose(k,2)). The reduced LP therefore has
    E T=k and E C=k(k-1)/(2m), or the corresponding upper-error inequality.
    A vertex has at most three support profiles, or two with slack moment.
    All such supports are enumerated with rational arithmetic.
    """
    results = []
    for k, max_m in [(2, 6), (3, 3), (4, 2)]:
        for m in range(1, max_m+1):
            states = []
            for a in combinations_with_replacement(range(k+1), m):
                states.append((sum(a), sum(comb(v, 2) for v in a),
                    1-prod(F(k-v, k) for v in a), a))
            for delta in [None, F(0), F(1, 3), F(2), F(100)]:
                cap = F(k*(k-1), 2*m)*(1 if delta is None else 1+delta)
                best = None
                witness = None
                feasible_vertices = 0

                def consider(indices, ps):
                    nonlocal best, witness, feasible_vertices
                    if any(p < 0 for p in ps) or sum(ps) != 1:
                        return
                    et = sum(p*states[i][0] for i, p in zip(indices, ps))
                    ec = sum(p*states[i][1] for i, p in zip(indices, ps))
                    if et != k or (ec != cap if delta is None else ec > cap):
                        return
                    value = sum(p*states[i][2] for i, p in zip(indices, ps))
                    feasible_vertices += 1
                    if best is None or value > best:
                        best = value
                        witness = [{'profile': states[i][3], 'mass': str(p)}
                                   for i, p in zip(indices, ps) if p]

                for i, state in enumerate(states):
                    consider((i,), (F(1),))
                for i, j in combinations(range(len(states)), 2):
                    ti, tj = states[i][0], states[j][0]
                    if ti != tj:
                        p = F(k-tj, ti-tj)
                        consider((i, j), (p, 1-p))
                    # If ti=tj=k, moment-active endpoints can use two states.
                    elif ti == k and states[i][1] != states[j][1]:
                        p = (cap-states[j][1])/(states[i][1]-states[j][1])
                        consider((i, j), (p, 1-p))
                for i, j, l in combinations(range(len(states)), 3):
                    ti, ci = states[i][:2]
                    tj, cj = states[j][:2]
                    tl, cl = states[l][:2]
                    det = (ti-tl)*(cj-cl)-(tj-tl)*(ci-cl)
                    if det:
                        pi = ((k-tl)*(cj-cl)-(tj-tl)*(cap-cl))/det
                        pj = ((ti-tl)*(cap-cl)-(k-tl)*(ci-cl))/det
                        consider((i, j, l), (pi, pj, 1-pi-pj))
                assert best is not None
                alpha = 1-F(k-1, k)**k
                bound = min(F(1), alpha+(1 if delta is None else 1+delta)*F(k-1, 2*k*m))
                assert alpha <= best <= bound
                if k == 2:
                    assert best == bound
                results.append({'k': k, 'm': m,
                    'model': 'equality' if delta is None else 'upper-error',
                    'delta': None if delta is None else str(delta),
                    'exact_optimum': str(best), 'claimed_upper_bound': str(bound),
                    'orbit_witness': witness, 'feasible_vertices': feasible_vertices})
    return results


def main():
    before = integrity()
    result = {'job_id': JOB, 'arithmetic': 'fractions.Fraction; exact',
              'integrity': before, 'direct_subset_attacks': direct_subsets(),
              'independent_projected_law_checks': color_laws(),
              'exact_symmetrized_LP_attacks': occupancy_extreme_points(),
              'limitations': 'Finite checks only; all-parameter conclusions use the analytic proof in audit/math.md. No owner script was executed.'}
    assert integrity() == before
    (ROOT/'audit/referee-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'integrity': before,
        'all_subsets_checked': sum(r['all_subsets'] for r in result['direct_subset_attacks']),
        'resampling_law_cases': result['independent_projected_law_checks']['law_cases'],
        'resampling_feature_cases': result['independent_projected_law_checks']['feature_cases'],
        'exact_LP_instances': len(result['exact_symmetrized_LP_attacks']),
        'all_checks_passed': True}, sort_keys=True))


if __name__ == '__main__':
    main()
