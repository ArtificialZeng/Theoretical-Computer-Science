"""Exact diagnostics for the all-parameter proof; not an infinite certificate.

Run from project root: python3 evidence/research_rounding_check.py
Only the standard library is used. Seeds, ranges, and fixtures are below.
No theorem or asymptotic runtime claim is inferred from these finite tests.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import random
import time

JOB = 'c002-coverage-research-8e44b8ae65fb'
COUNTS = dict(generic_cases=0, coverage_cases=0, rounding_calls=0,
              floating_moves=0, row_drops=0, constrained_moves=0,
              class_stages=0, affine_row_checks=0, large_occurrences=0,
              same_block_intersections=0, repeated_occurrence_cases=0,
              exhaustive_product_expectations=0)
MAXIMA = dict(classes=0, discrepancy=0, floating_coordinates=0,
              rounding_error=F(0))


def dot(a, x):
    return sum((v*w for v, w in zip(a, x)), F(0))


def kernel_vector(rows, width):
    """Exact homogeneous RREF; returns one nonzero kernel vector."""
    mat = [list(map(F, row)) for row in rows]
    pivots = []
    rank = 0
    for col in range(width):
        pivot = next((r for r in range(rank, len(mat)) if mat[r][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        scale = mat[rank][col]
        mat[rank] = [v/scale for v in mat[rank]]
        for r in range(len(mat)):
            if r != rank and mat[r][col]:
                scale = mat[r][col]
                mat[r] = [a-scale*b for a, b in zip(mat[r], mat[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(mat):
            break
    assert rank < width
    free = next(c for c in range(width) if c not in pivots)
    direction = [F(0)]*width
    direction[free] = F(1)
    for r, col in enumerate(pivots):
        direction[col] = -mat[r][free]
    assert any(direction) and all(dot(row, direction) == 0 for row in rows)
    return direction


def round_choices(A, groups, p, D):
    """Independent exact implementation of the floating-coordinate proof."""
    COUNTS['rounding_calls'] += 1
    p = list(map(F, p))
    A = [list(map(F, row)) for row in A]
    D = F(D)
    size = len(p)
    assert sorted(a for g in groups for a in g) == list(range(size))
    assert all(sum(p[a] for a in g) == 1 for g in groups)
    assert all(0 <= v <= 1 for v in p)
    assert all(sum(abs(row[a]) for row in A) <= D for a in range(size))
    x = p.copy()
    target = [dot(row, p) for row in A]
    active = set(range(len(A)))
    dropped = {}
    while True:
        W = [a for a in range(size) if 0 < x[a] < 1]
        assert all(dot(A[r], x) == target[r] for r in active)
        if not W:
            break
        MAXIMA['floating_coordinates'] = max(MAXIMA['floating_coordinates'], len(W))
        Wset = set(W)
        fractional_groups = [g for g in groups if any(a in Wset for a in g)]
        assert all(sum(a in Wset for a in g) >= 2 for g in fractional_groups)
        for r in sorted(active):
            mass = sum(abs(A[r][a]) for a in W)
            if mass <= 2*D:
                dropped[r] = (W.copy(), x.copy(), mass)
        newly_dropped = active.intersection(dropped)
        active.difference_update(newly_dropped)
        COUNTS['row_drops'] += len(newly_dropped)
        assert len(active)+len(fractional_groups) < len(W)
        equations = [[A[r][a] for a in W] for r in sorted(active)]
        equations += [[F(a in g) for a in W] for g in fractional_groups]
        d = kernel_vector(equations, len(W))
        steps = [(1-x[a])/v if v > 0 else -x[a]/v
                 for a, v in zip(W, d) if v]
        step = min(steps)
        assert step > 0
        for a, v in zip(W, d):
            x[a] += step*v
        assert all(0 <= v <= 1 for v in x)
        assert all(sum(x[a] for a in g) == 1 for g in groups)
        assert sum(0 < v < 1 for v in x) < len(W)
        assert all(dot(A[r], x) == target[r] for r in active)
        COUNTS['floating_moves'] += 1
        COUNTS['constrained_moves'] += bool(active)
    assert all(v in (0, 1) for v in x)
    for r, row in enumerate(A):
        error = abs(dot(row, x)-target[r])
        assert error <= 2*D
        MAXIMA['rounding_error'] = max(MAXIMA['rounding_error'], error)
        if r in dropped:
            W, at_drop, mass = dropped[r]
            assert dot(row, at_drop) == target[r]
            assert all(x[a] == at_drop[a] for a in range(size) if a not in W)
            assert error <= sum(abs(row[a])*abs(x[a]-at_drop[a]) for a in W) <= mass
        else:
            assert error == 0
    return x


def solve_coverage(n, t, k, features, m=2, save=False):
    """Each (function, item set) list entry is a distinct feature occurrence."""
    features = [(i, frozenset(S)) for i, S in features]
    assert all(0 <= i < m and S and all(0 <= j < n for j in S) for i, S in features)
    assert all(sum(j in S for _, S in features) <= t for j in range(n))
    q = t*k
    large = [(i, S) for i, S in features if len(S) >= q]
    small = [(i, S) for i, S in features if len(S) < q]
    slots = [(e, r) for e in range(len(large)) for r in range(k)]
    # Augmenting-path matching differs from the triage subset-choice recursion.
    matched_item = {}

    def augment(slot, seen):
        e, _ = slot
        for j in sorted(large[e][1]):
            if j in seen:
                continue
            seen.add(j)
            if j not in matched_item or augment(matched_item[j], seen):
                matched_item[j] = slot
                return True
        return False

    for slot in slots:
        assert augment(slot, set())
    blocks = [tuple(sorted(j for j, slot in matched_item.items() if slot[0] == e))
              for e in range(len(large))]
    assert all(len(B) == k and set(B) <= large[e][1] for e, B in enumerate(blocks))
    blocks += [(j,) for j in range(n) if j not in matched_item]
    assert sorted(j for B in blocks for j in B) == list(range(n))
    owner = {j: b for b, B in enumerate(blocks) for j in B}
    base = {j: a for B in blocks for a, j in enumerate(B)}

    def hit(S, c, b, r):
        return any((base[j]+r) % k == c for j in S if owner[j] == b)

    graph = [set() for _ in blocks]
    for _, S in small:
        touch = {owner[j] for j in S}
        for b in touch:
            graph[b].update(touch-{b})
            COUNTS['same_block_intersections'] += sum(owner[j] == b for j in S) > 1
    assert all(len(adj) <= q*(q-2) for adj in graph)
    classes = []
    for b, adj in enumerate(graph):
        used = {classes[a] for a in adj if a < b}
        cl = next(c for c in range(len(blocks)) if c not in used)
        classes.append(cl)
    H = max(classes)+1
    assert H <= (q-1)**2
    p = [[F(1, k)]*k for B in blocks]

    def expectation():
        values = [[F(0)]*k for _ in range(m)]
        for i, S in features:
            touch = {owner[j] for j in S}
            for c in range(k):
                miss = F(1)
                for b in touch:
                    miss *= sum(p[b][r] for r in range(k) if not hit(S, c, b, r))
                values[i][c] += 1-miss
        return [v for row in values for v in row]

    initial = expectation()
    assert all(len(set(initial[i*k:(i+1)*k])) == 1 for i in range(m))
    if len(blocks) <= 5 and k**len(blocks) <= 1024:
        direct = [F(0)]*(m*k)
        for shifts in product(range(k), repeat=len(blocks)):
            probability = F(1, k**len(blocks))
            colors = [(base[j]+shifts[owner[j]]) % k for j in range(n)]
            for i, S in features:
                for c in {colors[j] for j in S}:
                    direct[i*k+c] += probability
        assert direct == initial
        COUNTS['exhaustive_product_expectations'] += 1
    trace = []
    for cl in range(H):
        active = [b for b, c in enumerate(classes) if c == cl]
        aset = set(active)
        before = expectation()
        pos = {(b, r): k*h+r for h, b in enumerate(active) for r in range(k)}
        A = [[F(0)]*(k*len(active)) for _ in range(m*k)]
        constant = [F(0)]*(m*k)
        for i, S in large:
            for c in range(k):
                constant[i*k+c] += 1
        for i, S in small:
            touch = {owner[j] for j in S}
            inside = touch & aset
            assert len(inside) <= 1
            for c in range(k):
                v = F(1)
                for b in touch-aset:
                    v *= sum(p[b][r] for r in range(k) if not hit(S, c, b, r))
                constant[i*k+c] += 1-v
                if inside:
                    b = next(iter(inside))
                    assert all(sum(hit(S, cc, b, r) for cc in range(k)) == len(S.intersection(blocks[b]))
                               for r in range(k))
                    for r in range(k):
                        A[i*k+c][pos[b, r]] += v*hit(S, c, b, r)
        flat = [p[b][r] for b in active for r in range(k)]
        assert all(constant[a]+dot(row, flat) == before[a] for a, row in enumerate(A))
        assert all(sum(row[a] for row in A) <= q for a in range(len(flat)))
        groups = [list(range(h*k, (h+1)*k)) for h in range(len(active))]
        y = round_choices(A, groups, flat, q)
        for b in active:
            p[b] = [y[pos[b, r]] for r in range(k)]
        after = expectation()
        assert all(constant[a]+dot(row, y) == after[a] for a, row in enumerate(A))
        drift = [abs(a-b) for a, b in zip(after, before)]
        assert max(drift, default=F(0)) <= 2*q
        assert max(abs(a-b) for a, b in zip(after, initial)) <= 2*q*(cl+1)
        trace.append({'class': cl, 'blocks': len(active), 'max_drift': str(max(drift)),
                      'max_column_mass': str(max((sum(row[a] for row in A) for a in range(len(flat))), default=F(0)))})
        COUNTS['class_stages'] += 1
        COUNTS['affine_row_checks'] += 2*len(A)
    shifts = [law.index(F(1)) for law in p]
    colors = [(base[j]+shifts[owner[j]]) % k for j in range(n)]
    literal = [[0]*k for _ in range(m)]
    for i, S in features:
        hit_colors = {colors[j] for j in S}
        for c in hit_colors:
            literal[i][c] += 1
        if len(S) >= q:
            assert hit_colors == set(range(k))
    assert [F(v) for row in literal for v in row] == expectation()
    gap = max(max(row)-min(row) for row in literal)
    assert gap <= 4*q*H <= 4*q*(q-1)**2
    MAXIMA['classes'] = max(MAXIMA['classes'], H)
    MAXIMA['discrepancy'] = max(MAXIMA['discrepancy'], gap)
    COUNTS['coverage_cases'] += 1
    COUNTS['large_occurrences'] += len(large)
    COUNTS['repeated_occurrence_cases'] += len(set(S for _, S in features)) < len(features)
    if save:
        return dict(n=n, t=t, k=k, m=m, features=[dict(function=i, items=sorted(S)) for i, S in features],
                    blocks=blocks, classes=classes, colors=colors, coverage=literal,
                    discrepancy=gap, asserted_bound=4*q*(q-1)**2, trace=trace)


def generic_tests():
    # Complete 3^4 signed matrix row range, two fractional laws per matrix.
    for row in product((-1, 0, 1), repeat=4):
        A = [row]
        D = max(map(abs, row))
        for p in ([F(1, 2)]*4, [F(1, 3), F(2, 3), F(3, 4), F(1, 4)]):
            round_choices(A, [[0, 1], [2, 3]], p, D)
            COUNTS['generic_cases'] += 1
    # Threshold equality, zero columns/matrix, fixed groups, zeros, odd V.
    fixtures = [([[1, 1]], [[0, 1]], [F(1, 2)]*2, 1),
                ([[0, 0, 0]], [[0, 1, 2]], [0, F(1, 3), F(2, 3)], 0),
                ([[1, -1, 0, 0, 0]], [[0, 1], [2, 3, 4]], [1, 0, F(1, 3), F(1, 3), F(1, 3)], 1)]
    for A, groups, p, D in fixtures:
        round_choices(A, groups, p, D)
        COUNTS['generic_cases'] += 1
    rng = random.Random(734901)
    for case in range(220):
        sizes = [rng.randint(1, 5) for _ in range(rng.randint(2, 14))]
        groups, p = [], []
        for size in sizes:
            group = list(range(len(p), len(p)+size))
            weights = [rng.randint(0, 7) for _ in group]
            if not any(weights):
                weights[0] = 1
            p.extend(F(w, sum(weights)) for w in weights)
            groups.append(group)
        rows = rng.randint(1, 5)
        A = [[F(rng.randint(-3, 3), rng.randint(1, 4)) for _ in p] for _ in range(rows)]
        D = max(sum(abs(row[a]) for row in A) for a in range(len(p)))
        round_choices(A, groups, p, D)
        COUNTS['generic_cases'] += 1


def coverage_tests():
    # Complete multisets of <=3 nonempty subsets, all two-function taggings.
    for n in range(1, 5):
        subsets = [frozenset(j for j in range(n) if mask >> j & 1) for mask in range(1, 1 << n)]
        for size in range(4):
            for indexes in combinations_with_replacement(range(len(subsets)), size):
                edges = [subsets[h] for h in indexes]
                degree = max((sum(j in S for S in edges) for j in range(n)), default=0)
                for t in (1, 2):
                    if degree > t:
                        continue
                    for k in (2, 3):
                        for tags in product(range(2), repeat=size):
                            solve_coverage(n, t, k, list(zip(tags, edges)))
    # Hold-out structured families added after the proof was written.
    fixtures = [
        (4, 2, 2, [(0, {0, 1, 2, 3}), (1, {0, 1})]),
        (6, 2, 3, [(0, set(range(6))), (1, {0, 1})]),
        (8, 2, 2, [(0, set(range(8))), (1, set(range(8)))]),
        (8, 2, 4, [(0, set(range(8))), (1, {0, 1, 2})]),
        (12, 3, 2, [(0, set(range(8))), (1, set(range(4, 12))),
                    (0, {0, 1}), (1, {0, 1}), (0, {8, 9})]),
        (48, 2, 2, [(0, set(range(j, j+4))) for j in range(0, 48, 4)]
                    + [(j % 2, {j}) for j in range(48)]),
        (30, 2, 3, [(0, {j}) for j in range(30)] + [(1, {j, j+1}) for j in range(0, 30, 2)]),
    ]
    certificates = [solve_coverage(*case, save=True) for case in fixtures]
    rng = random.Random(184631)
    for n in (6, 8, 12, 18, 24):
        for t in (1, 2, 3, 4):
            for k in (2, 3, 4):
                for repeat in range(3):
                    degrees = [0]*n
                    features = []
                    for attempt in range(2*n):
                        available = [j for j in range(n) if degrees[j] < t]
                        if not available:
                            break
                        size = rng.randint(1, len(available))
                        if attempt % 3 == 0 and len(available) >= t*k:
                            size = t*k
                        S = frozenset(rng.sample(available, size))
                        features.append((rng.randrange(3), S))
                        for j in S:
                            degrees[j] += 1
                    solve_coverage(n, t, k, features, m=3)
    return certificates


def main():
    start = time.monotonic()
    generic_tests()
    certificates = coverage_tests()
    result = dict(job_id=JOB, all_assertions_passed=True,
                  arithmetic='exact fractions.Fraction; homogeneous rational RREF',
                  source_sha256=hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
                  counts=COUNTS, maxima={k: str(v) if isinstance(v, F) else v for k, v in MAXIMA.items()},
                  coverage=[
                      'All 3^4 single-row matrices over {-1,0,1}, two nonuniform/uniform two-choice group laws each.',
                      'Three equality/zero/fixed-coordinate fixtures and 220 seeded signed-rational generic matrices, groups of size 1..5.',
                      'All multisets of <=3 nonempty subsets on n=1..4, t=1,2, k=2,3, all two-function assignments to the occurrences.',
                      'Seven explicitly serialized hold-out coverage fixtures.',
                      '180 seeded degree-capped families: n=6,8,12,18,24; t=1..4; k=2..4; three repetitions, three functions.'
                  ],
                  seeds=[734901, 184631],
                  limitations='Finite diagnostic checks only. Infinite theorem rests on research/proof.md. No priority, audit acceptance, or Python polynomial-runtime certification.',
                  elapsed_seconds=round(time.monotonic()-start, 3),
                  fixture_certificates=certificates)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'fixture_certificates'}, indent=2))


if __name__ == '__main__':
    main()
