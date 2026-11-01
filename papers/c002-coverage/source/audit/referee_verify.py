"""Fresh finite diagnostics; does not import or rerun the submitted search.

Run: python3 audit/referee_verify.py
These exact finite checks supplement the written all-parameter proof review.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c002-coverage-referee-3e90f78a9294'
rng = random.Random(391057)
counts = dict(serialized_certificates=0, hall_subfamilies=0,
              affine_laws=0, class_matrices=0, direct_states=0,
              column_checks=0, generic_exhaustive_rounding_cases=0,
              multi_item_block_features=0, repeated_tagged_cases=0)


def certificate_check(f):
    n, t, k, m = (f[a] for a in ('n', 't', 'k', 'm'))
    es = [(e['function'], set(e['items'])) for e in f['features']]
    bs, cls, col = f['blocks'], f['classes'], f['colors']
    assert sorted(j for b in bs for j in b) == list(range(n))
    assert all(len(b) in (1, k) for b in bs)
    deg = [sum(j in s for _, s in es) for j in range(n)]
    assert max(deg, default=0) <= t
    assert len(cls) == len(bs) and len(col) == n
    for b in bs:
        assert len({(col[j]-a) % k for a, j in enumerate(b)}) == 1
    q = k*t
    large = [s for _, s in es if len(s) >= q]
    assert len(bs) >= len(large)
    # The serialized witness order is the input large-occurrence order.
    for a, s in enumerate(large):
        assert len(bs[a]) == k and set(bs[a]) <= s
        assert {col[j] for j in s} == set(range(k))
    for mask in range(1 << len(large)):
        sub = [large[a] for a in range(len(large)) if mask >> a & 1]
        union = set().union(*sub)
        assert len(union) >= k*len(sub)
        counts['hall_subfamilies'] += 1
    owner = {j: a for a, b in enumerate(bs) for j in b}
    adj = [set() for _ in bs]
    for _, s in es:
        if len(s) >= q:
            continue
        touching = {owner[j] for j in s}
        assert len({cls[a] for a in touching}) == len(touching)
        for a in touching:
            adj[a] |= touching-{a}
            if sum(j in s for j in bs[a]) > 1:
                counts['multi_item_block_features'] += 1
    assert all(len(v) <= q*(q-2) for v in adj)
    assert len(set(cls)) <= (q-1)**2
    values = [[0]*k for _ in range(m)]
    for i, s in es:
        for c in {col[j] for j in s}:
            values[i][c] += 1
    gap = max(max(v)-min(v) for v in values)
    assert values == f['coverage'] and gap == f['discrepancy']
    assert gap <= f['asserted_bound'] == 4*q*(q-1)**2
    counts['serialized_certificates'] += 1
    counts['repeated_tagged_cases'] += len({tuple(sorted(s)) for _, s in es}) < len(es)
    return es, bs, cls


def affine_check(es, bs, cls, k, m, t, laws):
    """Compare literal enumeration with nonnegative class matrices.

    Outside miss coefficients are computed by enumerating outside states,
    rather than the submitted code's product-of-miss-factors formula.
    """
    q = k*t
    base = {j: a for b in bs for a, j in enumerate(b)}
    owner = {j: a for a, b in enumerate(bs) for j in b}
    small = [(i, s) for i, s in es if len(s) < q]
    large = [(i, s) for i, s in es if len(s) >= q]
    assert all(any(len(b) == k and set(b) <= s for b in bs) for _, s in large)
    direct = [F(0)]*(m*k)
    for states in product(range(k), repeat=len(bs)):
        weight = F(1)
        for b, r in enumerate(states):
            weight *= laws[b][r]
        if weight:
            for i, s in es:
                colors = {(base[j]+states[owner[j]]) % k for j in s}
                for c in colors:
                    direct[i*k+c] += weight
        counts['direct_states'] += 1
    for cl in sorted(set(cls)):
        inside = [a for a, c in enumerate(cls) if c == cl]
        outside = [a for a in range(len(bs)) if a not in inside]
        coords = [(a, r) for a in inside for r in range(k)]
        idx = {v: b for b, v in enumerate(coords)}
        A = [[F(0)]*len(coords) for _ in range(m*k)]
        const = [F(0)]*(m*k)
        for i, _ in large:
            for c in range(k):
                const[i*k+c] += 1
        for state_tuple in product(range(k), repeat=len(outside)):
            states = dict(zip(outside, state_tuple))
            weight = F(1)
            for a, r in states.items():
                weight *= laws[a][r]
            if not weight:
                continue
            for i, s in small:
                touched_inside = {owner[j] for j in s} & set(inside)
                assert len(touched_inside) <= 1
                outside_colors = {(base[j]+states[owner[j]]) % k for j in s
                                  if owner[j] in states}
                for c in outside_colors:
                    const[i*k+c] += weight
                if touched_inside:
                    a = next(iter(touched_inside))
                    for r in range(k):
                        block_colors = {(base[j]+r) % k for j in s if owner[j] == a}
                        for c in block_colors-outside_colors:
                            A[i*k+c][idx[a, r]] += weight
        for h, (a, r) in enumerate(coords):
            mass = sum(row[h] for row in A)
            incident = sum(len(set(bs[a]) & s) for _, s in small)
            assert 0 <= mass <= incident <= len(bs[a])*t <= q
            counts['column_checks'] += 1
        got = [const[h]+sum(A[h][j]*laws[a][r]
                           for j, (a, r) in enumerate(coords)) for h in range(m*k)]
        assert got == direct
        counts['class_matrices'] += 1
    counts['affine_laws'] += 1


def random_laws(bs, k, mode):
    laws = []
    for a in range(len(bs)):
        if mode == 0:
            laws.append([F(1, k)]*k)
        elif mode == 1 and a % 2:
            r = rng.randrange(k)
            laws.append([F(c == r) for c in range(k)])
        else:
            weights = [rng.randrange(5) for _ in range(k)]
            weights[rng.randrange(k)] += 1
            laws.append([F(v, sum(weights)) for v in weights])
    return laws


def generic_rounding_check():
    # Existential check uses complete integral choice enumeration, no floating
    # routine or nullspace code. Include zero D and initially fixed groups.
    for case in range(160):
        g, k, rows = rng.randrange(1, 7), rng.randrange(2, 4), rng.randrange(1, 5)
        width = g*k
        A = [[F(rng.randrange(-2, 3), rng.randrange(1, 4)) for _ in range(width)]
             for _ in range(rows)]
        if case == 0:
            A = [[F(0)]*width for _ in range(rows)]
        p = []
        for group in range(g):
            w = [rng.randrange(4) for _ in range(k)]
            w[rng.randrange(k)] += 1
            p.extend(F(v, sum(w)) for v in w)
        D = max(sum(abs(row[a]) for row in A) for a in range(width))
        target = [sum(a*x for a, x in zip(row, p)) for row in A]
        best = None
        for states in product(range(k), repeat=g):
            err = max(abs(sum(row[h*k+states[h]] for h in range(g))-v)
                      for row, v in zip(A, target))
            best = err if best is None else min(best, err)
        assert best <= 2*D
        counts['generic_exhaustive_rounding_cases'] += 1


def main():
    packet = json.loads((ROOT/'evidence/research_rounding_check.json').read_text())
    for f in packet['fixture_certificates']:
        es, bs, cls = certificate_check(f)
        if f['k']**len(bs) <= 4096:
            for mode in range(3):
                affine_check(es, bs, cls, f['k'], f['m'], f['t'],
                             random_laws(bs, f['k'], mode))
    # Additional held-out block partitions: every nonempty subset, with
    # repeated subsets assigned to distinct function tags. Large t ensures
    # these are small; classes are computed directly from intersections.
    for k in (2, 3, 4):
        bs = [list(range(k)), [k], [k+1]]
        n, m = k+2, 3
        es = [(mask % m, {j for j in range(n) if mask >> j & 1})
              for mask in range(1, 1 << n)]
        es += [(1, set(range(k))), (2, set(range(k)))]
        t = max(sum(j in s for _, s in es) for j in range(n))
        for mode in range(3):
            affine_check(es, bs, list(range(len(bs))), k, m, t,
                         random_laws(bs, k, mode))
    generic_rounding_check()
    out = dict(job_id=JOB, all_assertions_passed=True,
               method='Fresh exact Fraction enumeration; no submitted code imported or executed.',
               seed=391057, counts=counts,
               source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
               limitations='Finite diagnostics only; the all-parameter conclusion rests on the written proof audit. No exhaustive full-product enumeration for the two largest serialized fixtures.')
    (ROOT/'audit/referee-verification.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
