"""Exact finite discriminator for the proposed route; no theorem certificate.

Run: python3 evidence/triage_first_test.py
Enumerates unlabeled multisets of <=3 nonempty feature subsets for n<=4,
t in {1,2}, k in {2,3}, plus explicit mixed/block fixtures. Occurrences retain
their positions even when subsets coincide. Function rows alternate 0,1.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import hashlib
import json

counts = dict(families=0, hall_subfamilies=0, affine_identities=0,
              coefficient_columns=0, repeated_families=0,
              same_block_intersections=0, large_occurrences=0)


def check(n, t, k, edges):
    assert all(sum(j in S for S in edges) <= t for j in range(n))
    q = t*k
    large = [S for S in edges if len(S) >= q]
    small = [(h % 2, S) for h, S in enumerate(edges) if len(S) < q]
    for mask in range(1, 1 << len(large)):
        chosen = [S for h, S in enumerate(large) if mask >> h & 1]
        assert len(set().union(*chosen)) >= k*len(chosen)
        counts['hall_subfamilies'] += 1

    def assign(h, used):
        if h == len(large):
            return []
        for b in combinations(sorted(large[h]-used), k):
            rest = assign(h+1, used | set(b))
            if rest is not None:
                return [b] + rest
        return None

    blocks = assign(0, set())
    assert blocks is not None
    used = set().union(*(set(B) for B in blocks)) if blocks else set()
    blocks += [(j,) for j in range(n) if j not in used]
    owner = {j: b for b, B in enumerate(blocks) for j in B}
    base = {j: a for B in blocks for a, j in enumerate(B)}
    graph = [set() for B in blocks]
    for _, S in small:
        touching = {owner[j] for j in S}
        for b in touching:
            graph[b].update(touching - {b})
            if len(S.intersection(blocks[b])) > 1:
                counts['same_block_intersections'] += 1
    assert all(len(g) <= q*(q-2) for g in graph)
    classes = []
    for b, neighbors in enumerate(graph):
        c = 0
        while c in {classes[a] for a in neighbors if a < b}:
            c += 1
        classes.append(c)
    assert max(classes, default=-1)+1 <= (q-1)**2
    laws = [[F(r+1, k*(k+1)//2) for r in range(k)] for _ in blocks]

    def hits(S, c, b, r):
        return any((base[j]+r) % k == c for j in S if owner[j] == b)

    def miss(S, c, b):
        return sum(laws[b][r] for r in range(k) if not hits(S,c,b,r))

    for cl in set(classes):
        active = {b for b in range(len(blocks)) if classes[b] == cl}
        for _, S in small:
            touching = sorted({owner[j] for j in S})
            inside = active.intersection(touching)
            assert len(inside) <= 1
            for c in range(k):
                direct = F(0)
                for shifts in product(range(k), repeat=len(touching)):
                    probability = F(1)
                    for b,r in zip(touching,shifts):
                        probability *= laws[b][r]
                    if any(hits(S,c,b,r) for b,r in zip(touching,shifts)):
                        direct += probability
                outside_miss = F(1)
                for b in set(touching)-active:
                    outside_miss *= miss(S,c,b)
                if inside:
                    b = next(iter(inside))
                    predicted = 1-outside_miss + outside_miss*sum(
                        laws[b][r]*hits(S,c,b,r) for r in range(k))
                else:
                    predicted = 1-outside_miss
                assert direct == predicted
                counts['affine_identities'] += 1
        for b in active:
            for r in range(k):
                column_mass = F(0)
                for _, S in small:
                    if not S.intersection(blocks[b]):
                        continue
                    for c in range(k):
                        v = F(1)
                        for a in {owner[j] for j in S}-{b}:
                            v *= miss(S,c,a)
                        column_mass += v*hits(S,c,b,r)
                assert column_mass <= q
                counts['coefficient_columns'] += 1
    counts['families'] += 1
    counts['large_occurrences'] += len(large)
    counts['repeated_families'] += len(set(map(frozenset, edges))) < len(edges)


for n in range(1,5):
    subsets = [{j for j in range(n) if mask >> j & 1}
               for mask in range(1,1 << n)]
    for size in range(4):
        for indexes in combinations_with_replacement(range(len(subsets)), size):
            edges = [subsets[h] for h in indexes]
            for t in (1,2):
                if any(sum(j in S for S in edges) > t for j in range(n)):
                    continue
                for k in (2,3):
                    check(n,t,k,edges)

fixtures = [
    (4,2,2,[set(range(4)),{0,1}]),
    (6,2,3,[set(range(6)),{0,1}]),
    (6,2,2,[{0,1,2,3},{2,3,4,5},{0,1}]),
    (8,2,2,[set(range(8)),set(range(8))]),
    (6,3,2,[set(range(6)),{0,1},{0,1}]),
    (8,2,4,[set(range(8)),{0,1,2}]),
]
for fixture in fixtures:
    check(*fixture)

result = {
    'job_id': 'c002-coverage-triage-beb2748f534b',
    'all_assertions_passed': True, 'arithmetic': 'fractions.Fraction',
    'counts': counts, 'extra_fixtures': len(fixtures),
    'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
    'coverage': 'All multisets of <=3 nonempty incidence subsets on [n], n=1..4, satisfying t=1 or 2; k=2 or 3; plus six listed fixtures. Alternating two function tags; nonuniform block laws.',
    'limitations': 'Checks Hall feasibility, interaction degree/classes, class-affine identities and column l1 bounds on finite cases only. Does not test the complete rounding algorithm, prove an all-parameter bound, or establish novelty/acceptance.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
