"""Independent exact finite checks of the categorical block identities.

Written in native agent /root/coverage_route_challenge; no imports from intake.
This does not certify the theorem or novelty. Run with Python 3.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json
from pathlib import Path
import random

rng = random.Random(118037)
stats = dict(families=0, large_occurrences=0, hall_subfamilies=0,
             feature_class_color_identities=0, coefficient_columns=0,
             repeated_occurrence_families=0, multiple_same_block_tests=0)


def check(n, k, t, edges):
    # Each list entry is one tagged occurrence; equal sets are never deduplicated.
    q = k*t
    assert all(sum(j in S for _, S in edges) <= t for j in range(n))
    large = [S for _, S in edges if len(S) >= q]
    small = [(i, S) for i, S in edges if len(S) < q]
    for z in range(1, len(large)+1):
        for Q in combinations(large, z):
            assert len(set().union(*Q)) >= k*z
            stats['hall_subfamilies'] += 1
    # Standard augmenting paths, independently implemented for copied Hall slots.
    slots = [S for S in large for _ in range(k)]
    owner = {}
    def augment(a, seen):
        for j in sorted(slots[a]):
            if j in seen:
                continue
            seen.add(j)
            if j not in owner or augment(owner[j], seen):
                owner[j] = a
                return True
        return False
    for a in range(len(slots)):
        assert augment(a, set())
    reps = {a: j for j, a in owner.items()}
    blocks = [tuple(reps[a] for a in range(h*k, (h+1)*k))
              for h in range(len(large))]
    blocks += [(j,) for j in range(n) if j not in owner]
    assert all(set(blocks[h]) <= large[h] for h in range(len(large)))
    where = {j: (b, x) for b, B in enumerate(blocks) for x, j in enumerate(B)}
    touches = lambda S: sorted({where[j][0] for j in S})
    adj = [set() for _ in blocks]
    for _, S in small:
        for b, d in combinations(touches(S), 2):
            adj[b].add(d)
            adj[d].add(b)
    colors = []
    for b, neighbors in enumerate(adj):
        assert len(neighbors) <= q*(q-2)
        used = {colors[d] for d in neighbors if d < b}
        colors.append(next(c for c in range(q*(q-2)+1) if c not in used))
    assert max(colors, default=0)+1 <= (q-1)**2
    # Nonuniform laws deliberately test more than the source's uniform/integral case.
    laws = []
    for _ in blocks:
        a = [rng.randrange(1, 5) for _ in range(k)]
        laws.append([F(x, sum(a)) for x in a])
    uniform = [[F(1, k)]*k for _ in blocks]

    def direct(S, c, distributions, restricted=None, miss=False):
        relevant = touches(S) if restricted is None else restricted
        ans = F(0)
        for shifts in product(range(k), repeat=len(relevant)):
            mass = F(1)
            assignment = dict(zip(relevant, shifts))
            for b, r in assignment.items():
                mass *= distributions[b][r]
            hit = any(b in assignment and (x+assignment[b]) % k == c
                      for j in S for b, x in [where[j]])
            if hit != miss:
                ans += mass
        return ans

    for _, S in edges:
        assert len({direct(S, c, uniform) for c in range(k)}) == 1
    m = max((i for i, S in edges), default=0)+1
    for cls in set(colors):
        active = [b for b in range(len(blocks)) if colors[b] == cls]
        A = {(b, r): [F(0)]*(m*k) for b in active for r in range(k)}
        for i, S in small:
            here = [b for b in touches(S) if b in active]
            assert len(here) <= 1
            if not here:
                continue
            b = here[0]
            inside = [where[j][1] for j in S if where[j][0] == b]
            stats['multiple_same_block_tests'] += len(inside) > 1
            for c in range(k):
                outside = [d for d in touches(S) if d != b]
                # Outside miss probability by joint enumeration, not product formula.
                v = direct(S, c, laws, outside, miss=True)
                z = [int(any((x+r) % k == c for x in inside)) for r in range(k)]
                affine = 1-v + v*sum(laws[b][r]*z[r] for r in range(k))
                assert affine == direct(S, c, laws)
                for r in range(k):
                    A[b, r][i*k+c] += v*z[r]
                stats['feature_class_color_identities'] += 1
        for (b, r), col in A.items():
            assert sum(abs(x) for x in col) <= t*len(blocks[b]) <= q
            stats['coefficient_columns'] += 1
    stats['families'] += 1
    stats['large_occurrences'] += len(large)
    stats['repeated_occurrence_families'] += len({tuple(sorted(S)) for _, S in edges}) < len(edges)


check(5, 2, 1, [(0, {0,1}), (1, {2,3}), (0, {4})])
check(8, 2, 3, [(0, set(range(6))), (1, set(range(6))),
                 (0, {0,1,6}), (1, {2,3,7}), (0, {4,5})])
check(12, 3, 3, [(0, set(range(9))), (1, set(range(9))),
                  (0, {0,1,9}), (1, {2,3,10}), (2, {4,5,11})])
for _ in range(40):
    n = rng.randrange(3, 9)
    k = rng.choice([2, 3, 4])
    t = rng.randrange(1, 5)
    remaining = [t]*n
    edges = []
    for _ in range(2*n):
        available = [j for j in range(n) if remaining[j]]
        if not available:
            break
        S = set(rng.sample(available, rng.randrange(1, len(available)+1)))
        edges.append((rng.randrange(3), S))
        for j in S:
            remaining[j] -= 1
    check(n, k, t, edges)
result = dict(kind='independent finite evidence; not proof or acceptance',
              native_agent='/root/coverage_route_challenge', seed=118037,
              all_assertions_passed=True, counts=stats)
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
