#!/usr/bin/env python3
"""Pass 2: exact new-input sweep checks and portable continuous-cell certificates.

Standard library only. This does not import either supplied candidate checker.
Run from any directory. Finite coverage is not a proof of universal claims.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def cell_minimum_squared(a, b, lo, hi):
    candidates = [(a*v+b)**2/v for v in (lo, hi)]
    if a and b and lo <= b/a <= hi:
        candidates.append(4*a*b)
    return min(candidates)


def all_certificates(p, q, z):
    """A common order, one linear scan per designated coordinate."""
    n = len(p)
    order = sorted(range(n), key=lambda i: q[i]/p[i])
    groups = []
    for i in order:
        v = z*q[i]/p[i]
        if groups and groups[-1][0] == v:
            groups[-1][1].append(i)
        else:
            groups.append((v, [i]))
    result = []
    for j in range(n):
        a, b, lo = 1-p[j], F(0), F(1)
        best = None
        for hi, group in groups:
            value = cell_minimum_squared(a, b, lo, hi)
            best = value if best is None else min(best, value)
            for i in group:
                if i != j:
                    a -= p[i]
                    b += z*q[i]
            lo = hi
        result.append(min(best, cell_minimum_squared(a, b, lo, z*z)))
    return result


def exhaustive_mask_minimum(p, q, z, j):
    """Independent exhaustive branch-cell oracle, no sorted sweep."""
    ids = [i for i in range(len(p)) if i != j]
    values = []
    for mask in range(1 << len(ids)):
        lo, hi = F(1), z*z
        forward, backward = [], []
        for k, i in enumerate(ids):
            if mask & (1 << k):
                backward.append(i)
                lo = max(lo, z*q[i]/p[i])
            else:
                forward.append(i)
                hi = min(hi, z*q[i]/p[i])
        if lo > hi:
            continue
        a = sum((p[i] for i in forward), F(0))
        b = z*sum((q[i] for i in backward), F(0))
        # Independent derivative-clamp evaluation in squared coordinates.
        if not a:
            v = hi
        elif not b:
            v = lo
        else:
            v = max(lo, min(hi, b/a))
        values.append((a*v+b)**2/v)
    return min(values)


def compositions(total, n):
    if n == 1:
        if total > 0:
            yield (total,)
        return
    for head in range(1, total-n+2):
        for tail in compositions(total-head, n-1):
            yield (head,) + tail


def main():
    pairs = []
    for n in range(2, 5):
        vectors = [tuple(F(i, 7) for i in c) for c in compositions(7, n)]
        pairs.extend(product(vectors, repeat=2))
    rng = random.Random(294008)
    for n in (5, 6, 7):
        for _ in range(24):
            pp = [rng.randrange(1, 31) for _ in range(n)]
            qq = [rng.randrange(1, 31) for _ in range(n)]
            pairs.append((tuple(F(i, sum(pp)) for i in pp),
                          tuple(F(i, sum(qq)) for i in qq)))
    comparisons = budgets = 0
    tied = identical = 0
    for p, q in pairs:
        endpoint = max(max(x/y, y/x) for x, y in zip(p, q))
        for z in (endpoint, endpoint*F(9, 8), endpoint*2):
            got = all_certificates(p, q, z)
            for j, value in enumerate(got):
                assert value == exhaustive_mask_minimum(p, q, z, j)
                assert value <= min((1-p[j])**2, (1-q[j])**2)
                comparisons += 1
            budgets += 1
        tied += len(set(y/x for x, y in zip(p, q))) < len(p)
        identical += p == q

    certificates = []
    energies = [F(10001, 10000), F(3, 2), F(2), F(5, 2), F(3),
                F(4), F(5), F(9), F(17), F(100), F(10000)]
    for e in energies:
        xs = {F(1)}
        # Dense rational switches, including irrational-budget families.
        for k in range(1, 33):
            x = 1+(e-1)*F(k, 64)
            if x*x <= e:
                xs.add(x)
        for root in (2, 3, 10, 100):
            if F(root*root) == e:
                xs.add(F(root))
        for x in sorted(xs):
            b = (x+e/x)/2
            z = b*b
            for den in (2, 5, 19):
                a = 1/(den*e)
                c = 1-a*(1+e)
                h = 1-2*a*b
                p = (c, a, a*e)
                q = (c, a*e, a)
                assert all_certificates(p, q, z)[0] == (2*a*b)**2
                certificates.append({
                    'E': str(e), 'a': str(a), 'x': str(x), 'B': str(b),
                    'Z': str(z), 'p': list(map(str, p)), 'q': list(map(str, q)),
                    'peak': str(h),
                    'half_cells': [
                        {'interval': ['1', str(x)], 'coefficients': [
                            [str(-a), str(-a*e), '1'],
                            [str(a), '0', '0'], ['0', str(a*e), '0']]},
                        {'interval': [str(x), str(b)], 'coefficients': [
                            ['0', '0', str(h)],
                            [str(a), '0', '0'], [str(-a), '0', str(2*a*b)]]}]
                })
    (HERE/'research-excursion-path-certificates.json').write_text(
        json.dumps({'basis': 'r_i(u)=A_i*u+B_i/u+C_i; second half reflects and swaps coordinates 1,2',
                    'certificates': certificates}, indent=2)+'\n')
    output = {
        'job_id': 'privacy-interpolation-research-294f008bff48',
        'research_pass': 2, 'status': 'exact finite computations passed; no referee verdict',
        'endpoint_pairs': len(pairs), 'budget_instances': budgets,
        'designated_coordinate_comparisons': comparisons,
        'pairs_with_tied_ratios': tied, 'identical_pairs': identical,
        'domain': 'all denominator-7 positive endpoint pairs in dimensions 2..4, plus 24 seeded pairs each in dimensions 5..7; three exact budgets per pair',
        'family_certificates': len(certificates),
        'coverage_limits': 'New rational inputs relative to the supplied denominator-8 tests. Continuous-cell proofs are separately checked; finite inputs alone prove no universal theorem. Feasibility is not decided by the excursion certificate.'}
    (HERE/'research-excursion-exact-results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
