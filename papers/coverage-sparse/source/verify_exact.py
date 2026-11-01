#!/usr/bin/env python3
"""Exact finite checks, using only Python's standard library.

Not a proof of the asymptotic theorem. Enumerates ALL occupancy profiles for
the stated (k,m), then solves the symmetrized moment LP by enumerating bases.
The symmetry reduction is valid because blocks and vertices within blocks can
be permuted; marginal and edge constraints and the objective are invariant.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json
from pathlib import Path


def solve(a, b):
    """Square rational Gaussian elimination, returns None if singular."""
    n = len(b)
    t = [[F(v) for v in row] + [F(y)] for row, y in zip(a, b)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if t[i][j]), None)
        if pivot is None:
            return None
        t[j], t[pivot] = t[pivot], t[j]
        d = t[j][j]
        t[j] = [v / d for v in t[j]]
        for i in range(n):
            if i != j:
                d = t[i][j]
                t[i] = [v - d * w for v, w in zip(t[i], t[j])]
    return [row[-1] for row in t]


def profiles(total, width):
    if width == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for rest in profiles(total - x, width - 1):
                yield (x,) + rest


def value(k, profile):
    uncovered = F(1)
    for a, count in enumerate(profile):
        uncovered *= F(k - a, k) ** count
    return 1 - uncovered


def exact_lp(k, m):
    pp = list(profiles(m, k + 1))
    cols = [(1, sum(a * c for a, c in enumerate(p)),
             sum(comb(a, 2) * c for a, c in enumerate(p))) for p in pp]
    values = [value(k, p) for p in pp]
    rhs = [F(1), F(k), F(comb(k, 2), m)]
    best = None
    certificate = None
    bases = 0
    for ids in combinations(range(len(pp)), 3):
        bases += 1
        basis = [[cols[j][i] for j in ids] for i in range(3)]
        weights = solve(basis, rhs)
        if weights is None or min(weights) < 0:
            continue
        objective = sum(w * values[j] for w, j in zip(weights, ids))
        if best is None or objective > best:
            best = objective
            certificate = None
        if objective == best:
            y = solve([list(cols[j]) for j in ids], [values[j] for j in ids])
            if y is not None and all(sum(a * b for a, b in zip(y, col)) >= v
                                     for col, v in zip(cols, values)):
                certificate = (ids, weights)
    assert best is not None
    assert certificate is not None, 'No exact matching dual certificate found'
    ids, weights = certificate
    dual = solve([list(cols[j]) for j in ids], [values[j] for j in ids])
    assert dual is not None
    assert all(sum(a * b for a, b in zip(dual, col)) >= v
               for col, v in zip(cols, values)), "dual infeasible"
    assert sum(a * b for a, b in zip(dual, rhs)) == best
    assert sum(weights) == 1 and min(weights) >= 0
    for i in range(3):
        assert sum(w * cols[j][i] for w, j in zip(weights, ids)) == rhs[i]
    alpha = 1 - F(k - 1, k) ** k
    bound = alpha + F(k - 1, 2 * k * m)
    assert alpha <= best <= min(F(1), bound)
    return {
        'k': k, 'm': m, 'occupancy_profiles': len(pp), 'bases_enumerated': bases,
        'alpha': str(alpha), 'exact_optimum': str(best), 'analytic_upper': str(bound),
        'ratio': str(1 / best), 'dual': list(map(str, dual)),
        'primal': [{'profile': pp[j], 'weight': str(w)}
                   for j, w in zip(ids, weights) if w],
        'all_dual_constraints_checked_exactly': True,
    }


def main():
    local_cases = 0
    for k in range(1, 81):
        q = F(k - 1, k)
        for a in range(k + 1):
            difference = q ** a - (1 - F(a, k))
            assert 0 <= difference <= F(comb(a, 2), k * k)
            local_cases += 1
    product_cases = 0
    for k in range(1, 7):
        for m in range(1, 6):
            q = F(k - 1, k)
            for occupancies in product(range(k + 1), repeat=m):
                uncovered = F(1)
                for a in occupancies:
                    uncovered *= 1 - F(a, k)
                f = 1 - uncovered
                upper = 1 - q ** sum(occupancies) + sum(
                    F(comb(a, 2), k * k) for a in occupancies)
                assert f <= upper
                product_cases += 1
    results = [exact_lp(k, m) for k, m in
               [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 3)]]
    output = {'arithmetic': 'fractions.Fraction (exact rational)',
              'local_inequality_cases': local_cases,
              'product_inequality_cases': product_cases,
              'finite_lp_cases': results,
              'scope': 'Only the enumerated finite ranges; analytic proof required for all k,m.'}
    target = Path(__file__).with_name('evidence')
    target.mkdir(exist_ok=True)
    (target / 'exact-checks.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
