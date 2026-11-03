"""Changed finite test of actual-outlier DFS charging; standard library only.

Selected coalescent partitions on 6..16 points, varying b,B, with repeated
clusters, empty cores and independently changing nonnested cores. No imports
from previous checkers. Exact maximal constraint metrics use integer shortest
paths. This is not exhaustive over hierarchies and does not execute carving.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import random
import time

JOB = "c040-mstdecfull-research-e695ca56645f"
SEED = 69556645


def make_levels(rng, n, fixture):
    current = [frozenset([x]) for x in range(n)]
    levels = [tuple(current)]
    while len(current) > 1:
        if (len(levels) + fixture) % 3 == 0:
            levels.append(tuple(current))
        rng.shuffle(current)
        width = rng.randint(2, min(4, len(current)))
        current = [frozenset().union(*current[:width])] + current[width:]
        levels.append(tuple(current))
    # Repeated full sets below the root also receive independently chosen cores.
    if fixture % 2 == 0:
        levels.append(tuple(current))
    return levels


def choose_cores(rng, levels, b, big_b, mode):
    last = len(levels) - 1
    cores = {}
    for i, clusters in enumerate(levels):
        for c in clusters:
            if i == last:
                g = c
            elif i == 0 or len(c) <= b:
                g = frozenset()
            elif len(c) <= big_b and (mode == 0 or rng.randrange(3) == 0):
                g = frozenset()
            else:
                max_out = min(b, len(c) - b - 1)
                count = max_out if mode == 1 else rng.randint(0, max_out)
                order = sorted(c, reverse=bool((i + mode) % 2))
                if mode == 2:
                    rng.shuffle(order)
                g = c - frozenset(order[:count])
            assert g <= c
            assert (i == last or not g or (len(g) > b and len(c - g) <= b))
            assert g or len(c) <= big_b
            cores[i, c] = g
    return cores


def leaf_order(rng, levels, mode):
    def visit(i, c):
        if i == 0:
            return list(c)
        children = [a for a in levels[i - 1] if a <= c]
        children.sort(key=lambda a: min(a), reverse=mode == 1)
        if mode >= 2:
            rng.shuffle(children)
        return [x for a in children for x in visit(i - 1, a)]
    return visit(len(levels) - 1, levels[-1][0])


def verify_case(levels, cores, order, dist, counts):
    last = len(levels) - 1
    contain = {(i, x): c for i, cs in enumerate(levels) for c in cs for x in c}
    direct, late = Counter(), Counter()
    h = sum((1 << i) * len(cs) for i, cs in enumerate(levels))
    omega = sum((1 << i) * len(c - cores[i, c])
                for i, cs in enumerate(levels) for c in cs)
    cost = direct_cost = late_cost = 0
    for u, v in zip(order, order[1:]):
        counts['edges'] += 1
        cost += dist[u][v]
        j = next(i for i in range(1, last + 1) if contain[i, u] == contain[i, v])
        ku = next(i for i in range(j, last + 1) if u in cores[i, contain[i, u]])
        kv = next(i for i in range(j, last + 1) if v in cores[i, contain[i, v]])
        k = max(ku, kv)
        dcore = cores[k, contain[k, u]]
        assert dcore
        assert cores[ku, contain[ku, u]] & dcore
        assert cores[kv, contain[kv, v]] & dcore
        assert dist[u][v] <= 3 * (1 << k)
        if k == j:
            key = (j - 1, contain[j - 1, u])
            direct[key] += 1
            direct_cost += dist[u][v]
            counts['immediate_edges'] += 1
            assert dist[u][v] <= 2 * (1 << key[0])
        else:
            x = u if ku == k else v
            key = (k - 1, contain[k - 1, x])
            late[key] += 1
            late_cost += dist[u][v]
            counts['late_edges'] += 1
            assert x not in cores[key]
            assert dist[u][v] <= 6 * (1 << key[0])
    assert all(v <= 1 for v in direct.values())
    assert all(v <= 2 * len(c - cores[i, c]) for (i, c), v in late.items())
    assert direct_cost <= 2 * h
    assert late_cost <= 12 * omega
    assert cost <= 2 * h + 12 * omega
    return Fraction(cost, 2 * h + 12 * omega), h, omega


def main():
    start = time.monotonic()
    rng = random.Random(SEED)
    counts = Counter()
    max_ratio, worst = Fraction(0), None
    heights, bs, big_bs = set(), set(), set()
    for n in (6, 7, 8, 9, 10, 12, 16):
        for fixture in range(12):
            levels = make_levels(rng, n, fixture)
            last = len(levels) - 1
            counts['hierarchies'] += 1
            counts['repeated_cluster_occurrences'] += sum(
                c in levels[i - 1] for i in range(1, last + 1) for c in levels[i])
            heights.add(last)
            for b in (1, 2, 3, 5):
                for big_b in (b, b + 3):
                    bs.add(b)
                    big_bs.add(big_b)
                    for mode in range(3):
                        cores = choose_cores(rng, levels, b, big_b, mode)
                        counts['core_assignments'] += 1
                        counts['empty_core_occurrences'] += sum(not g for g in cores.values())
                        counts['changing_repeated_cores'] += sum(
                            (i - 1, c) in cores and cores[i - 1, c] != g
                            for (i, c), g in cores.items())
                        dist = [[0 if x == y else 1 << last for y in range(n)] for x in range(n)]
                        for (i, c), g in cores.items():
                            for x in g:
                                for y in g:
                                    if x != y:
                                        dist[x][y] = min(dist[x][y], 1 << i)
                        for z in range(n):
                            for x in range(n):
                                for y in range(n):
                                    dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])
                        for order_mode in range(6):
                            order = leaf_order(rng, levels, order_mode)
                            assert sorted(order) == list(range(n))
                            ratio, h, omega = verify_case(levels, cores, order, dist, counts)
                            counts['ordered_cases'] += 1
                            if ratio > max_ratio:
                                max_ratio = ratio
                                worst = dict(n=n, fixture=fixture, b=b, B=big_b,
                                             core_mode=mode, order_mode=order_mode,
                                             H=h, Omega=omega, order=order)
    result = dict(job_id=JOB, passed=True, seed=SEED, counts=dict(counts),
                  n_values=[6, 7, 8, 9, 10, 12, 16], heights=sorted(heights),
                  b_values=sorted(bs), B_values=sorted(big_bs),
                  maximum_cost_over_retained_bound=str(max_ratio), witness=worst,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  elapsed_seconds=time.monotonic() - start,
                  scope='Selected deep coalescent nested partitions; 3 core patterns per b,B and 6 compatible DFS orders per assignment; exact integer maximal constraint metric.',
                  limitations=['Not exhaustive over hierarchies, core assignments or orders.',
                               'Not an all-n proof or a full seed-carving algorithm execution.',
                               'Same proposer context, not a fresh referee.'])
    path = Path(__file__).resolve().parents[1] / 'evidence/outlier-charges-pass2.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
