"""Independent finite audit of the frozen DFS extraction lemma.

Exhausts all two-intermediate-level nested partitions on five labels,
all allowed hidden cores for two (b,B) choices, and every compatible
leaf permutation. It imports no proposer checker and changes no frozen file.
The all-n mathematical proof is reviewed separately.
"""
from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import time


def partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for old in partitions(rest):
        yield (frozenset((first,)),) + old
        for j in range(len(old)):
            yield old[:j] + (old[j] | {first},) + old[j + 1:]


def possible_cores(cluster, b, cap):
    if len(cluster) <= cap:
        yield frozenset()
    for k in range(b + 1, len(cluster) + 1):
        if len(cluster) - k <= b:
            for s in combinations(sorted(cluster), k):
                yield frozenset(s)


def main():
    start = time.monotonic()
    n = 5
    universe = frozenset(range(n))
    bottom = tuple(frozenset((x,)) for x in range(n))
    parts = list(partitions(tuple(range(n))))
    assert len(parts) == 52 and len(set(parts)) == 52
    counts = Counter()
    changing = repeated = empty = 0
    max_ratio = [0, 1]
    for p1 in parts:
        for p2 in parts:
            if not all(any(a <= b for b in p2) for a in p1):
                continue
            levels = (bottom, p1, p2, (universe,))
            nodes = [(i, c) for i in (1, 2) for c in levels[i]]
            containing = {(i, x): c for i, cs in enumerate(levels)
                          for c in cs for x in c}
            orders = []
            for order in permutations(range(n)):
                position = {x: j for j, x in enumerate(order)}
                if all(max(position[x] for x in c) - min(position[x] for x in c)
                       + 1 == len(c) for _, c in nodes):
                    orders.append(order)
            assert orders
            counts['nested_partition_chains'] += 1
            for b, cap in ((1, 2), (2, 3)):
                options = [tuple(possible_cores(c, b, cap)) for _, c in nodes]
                for chosen in product(*options):
                    cores = dict(zip(nodes, chosen))
                    cores.update({(0, c): frozenset() for c in bottom})
                    cores[3, universe] = universe
                    counts['core_assignments'] += 1
                    empty += sum(not g for g in cores.values())
                    for i, c in nodes:
                        if (i - 1, c) in cores:
                            repeated += 1
                            changing += cores[i - 1, c] != cores[i, c]
                    # Shortest-path closure is the entrywise largest metric
                    # satisfying all pairwise core diameter upper bounds.
                    d = [[0 if x == y else 8 for y in range(n)]
                         for x in range(n)]
                    for (i, c), g in cores.items():
                        for x in g:
                            for y in g:
                                if x != y:
                                    d[x][y] = min(d[x][y], 1 << i)
                    for z in range(n):
                        for x in range(n):
                            for y in range(n):
                                d[x][y] = min(d[x][y], d[x][z] + d[z][y])
                    h = sum((1 << i) * len(cs) for i, cs in enumerate(levels))
                    omega = sum((1 << i) * len(c - cores[i, c])
                                for i, cs in enumerate(levels) for c in cs)
                    for order in orders:
                        direct, late = Counter(), Counter()
                        cost = immediate_cost = late_cost = 0
                        for u, v in zip(order, order[1:]):
                            j = next(i for i in range(1, 4)
                                     if containing[i, u] == containing[i, v])
                            promo = {x: next(i for i in range(j, 4)
                                             if x in cores[i, containing[i, x]])
                                     for x in (u, v)}
                            k = max(promo.values())
                            g = cores[k, containing[k, u]]
                            for x in (u, v):
                                assert cores[promo[x], containing[promo[x], x]] & g
                            assert d[u][v] <= 3 * (1 << k)
                            cost += d[u][v]
                            counts['path_edges'] += 1
                            if k == j:
                                key = j - 1, containing[j - 1, u]
                                direct[key] += 1
                                assert d[u][v] <= 2 * (1 << key[0])
                                immediate_cost += d[u][v]
                                counts['immediate_edges'] += 1
                            else:
                                x = u if promo[u] == k else v
                                key = k - 1, containing[k - 1, x]
                                assert x not in cores[key]
                                late[key] += 1
                                assert d[u][v] <= 6 * (1 << key[0])
                                late_cost += d[u][v]
                                counts['late_edges'] += 1
                        assert all(v <= 1 for v in direct.values())
                        assert all(v <= 2 * len(c - cores[i, c])
                                   for (i, c), v in late.items())
                        assert immediate_cost <= 2 * h
                        assert late_cost <= 12 * omega
                        bound = 2 * h + 12 * omega
                        assert cost <= bound
                        if cost * max_ratio[1] > max_ratio[0] * bound:
                            max_ratio = [cost, bound]
                        counts['ordered_cases'] += 1
    result = {
        'job_id': 'c040-mstdecfull-referee-8513177dc0bb',
        'snapshot_digest': '3a7133dbcc463bfba827578e6a5a4028802dc5a73d23c647e733201b0be99d76',
        'passed': True,
        'n': n,
        'levels': [0, 1, 2, 3],
        'b_B_choices': [[1, 2], [2, 3]],
        'counts': dict(counts),
        'empty_core_occurrences': empty,
        'repeated_cluster_occurrences': repeated,
        'changed_repeated_core_occurrences': changing,
        'maximum_cost_to_bound_numerator_denominator': max_ratio,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic() - start,
        'scope': 'All nested partitions at two intermediate levels on five labels, all admissible core subsets for the two stated budgets, all compatible leaf permutations; beta=1 maximal exact integer constraint metrics.',
        'limitations': [
            'Finite extraction-lemma audit only, not an all-n proof.',
            'Does not execute the all-p carving algorithm or its very large constants.',
            'The proposer checker was inspected but was not imported or rerun.'
        ]
    }
    path = Path(__file__).with_name('referee-8513177dc0bb-exact-check.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
