"""Fresh finite stress test; no imports from the proposer's verifier.

Binary laminar trees with independently chosen cores at each scale, including
repeated clusters.  Exact shortest-path metrics are maximal under all core
diameter constraints.  Every binary child orientation is enumerated.  This
tests selected fixtures, not every hierarchy or the complete MST algorithm.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import random

JOB = "c040-mstdecfull-referee-c896e1b53be0"
SEED = 402896153


def tree(rng, n):
    nodes = [(frozenset([x]), 0, None) for x in range(n)]
    while len(nodes) > 1:
        a = nodes.pop(rng.randrange(len(nodes)))
        b = nodes.pop(rng.randrange(len(nodes)))
        level = max(a[1], b[1]) + rng.randint(1, 3)
        nodes.append((a[0] | b[0], level, (a, b)))
    return nodes[0]


def partitions(root):
    def at(node, level):
        if node[1] <= level:
            return [node[0]]
        return at(node[2][0], level) + at(node[2][1], level)
    return [at(root, level) for level in range(root[1] + 1)]


def leaf_orders(node):
    if node[2] is None:
        return [(next(iter(node[0])),)]
    a, b = map(leaf_orders, node[2])
    return [order for u, v in product(a, b) for order in (u + v, v + u)]


def one(rng, n, b, B, serial):
    root = tree(rng, n)
    levels = partitions(root)
    L = len(levels) - 1
    cores = {}
    for i, parts in enumerate(levels):
        for c in parts:
            if i == L:
                g = c
            elif len(c) <= B and (len(c) <= b or rng.randrange(2) == 0):
                g = frozenset()
            else:
                max_out = min(b, len(c) - b - 1)
                if max_out < 0:
                    g = frozenset()
                else:
                    # Frequently use the maximal allowed number of outliers.
                    k = max_out if serial % 2 == 0 else rng.randint(0, max_out)
                    g = c - frozenset(rng.sample(sorted(c), k))
            assert (not g and len(c) <= B) or i == L or (len(g) > b and len(c-g) <= b)
            cores[i, c] = g
    d = [[0 if x == y else 1 << L for y in range(n)] for x in range(n)]
    for (i, c), g in cores.items():
        for x in g:
            for y in g:
                if x != y:
                    d[x][y] = min(d[x][y], 1 << i)
    for z in range(n):
        for x in range(n):
            for y in range(n):
                d[x][y] = min(d[x][y], d[x][z] + d[z][y])
    container = {(i, x): c for i, parts in enumerate(levels) for c in parts for x in c}
    H = sum((1 << i) * len(parts) for i, parts in enumerate(levels))
    orders = leaf_orders(root)
    worst = 0
    late_edges = 0
    for order in orders:
        total = 0
        immediate, late = Counter(), Counter()
        for u, v in zip(order, order[1:]):
            total += d[u][v]
            j = min(i for i in range(1, L+1) if container[i,u] == container[i,v])
            ku = min(i for i in range(j,L+1) if u in cores[i,container[i,u]])
            kv = min(i for i in range(j,L+1) if v in cores[i,container[i,v]])
            k = max(ku, kv)
            common = container[k,u]
            assert cores[ku,container[ku,u]] & cores[k,common]
            assert cores[kv,container[kv,v]] & cores[k,common]
            if k == j:
                key = (j-1,container[j-1,u])
                immediate[key] += 1
                assert d[u][v] <= 2 * (1 << key[0])
            else:
                x = u if ku == k else v
                key = (k-1,container[k-1,x])
                assert x not in cores[key]
                late[key] += 1
                late_edges += 1
                assert d[u][v] <= 6 * (1 << key[0])
        assert all(v <= 1 for v in immediate.values())
        assert all(v <= 2*len(c-cores[i,c]) for (i,c),v in late.items())
        assert total <= (2+12*B)*H
        worst = max(worst,total)
    record = {'n':n,'b':b,'B':B,'levels':L+1,'orders':len(orders),
              'edges':len(orders)*(n-1),'late_edges':late_edges,
              'worst_cost':worst,'hierarchy_cost':H,
              'fixture_sha256':hashlib.sha256(json.dumps({
                  'levels':[[sorted(c) for c in cs] for cs in levels],
                  'cores':[[i,sorted(c),sorted(g)] for (i,c),g in cores.items()]
              },sort_keys=True).encode()).hexdigest()}
    return record


def main():
    rng = random.Random(SEED)
    records = [one(rng,n,b,B,serial)
               for n in (6,8,10,12) for b in (1,2,3)
               for B in (b,2*b) for serial in range(4)]
    result = {'job_id':JOB,'seed':SEED,'passed':True,
              'scope':'96 selected binary laminar hierarchies on 6,8,10,12 points; b=1,2,3, B=b or 2b; independent per-level cores; every child orientation; maximal exact constraint metrics.',
              'fixtures':len(records),'orders':sum(r['orders'] for r in records),
              'edges':sum(r['edges'] for r in records),
              'late_edges':sum(r['late_edges'] for r in records),
              'max_cost_over_H':str(max(Fraction(r['worst_cost'],r['hierarchy_cost']) for r in records)),
              'limitations':['Selected fixtures only, not exhaustive over all hierarchies or core assignments.','Does not execute the high-quantile clustering algorithm.','The infinite theorem is assessed through its mathematical proof, not these tests.'],
              'records':records}
    output=Path(__file__).with_name('extraction-check.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))


if __name__ == '__main__':
    main()
