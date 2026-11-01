#!/usr/bin/env python3
"""Exact, foreground, standard-library check independent of candidate_check.py.

No script import from the parent seed.  Forward integer path weights check E;
complete root orientations check all deterministic priority algorithms on cycles.
Finite tests supplement the analytic proof, never certify its infinite scope.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SHA = '3ec230456a31ba9b004000be9e79c74a77636a28a31e9b4eec31918f5ab305ed'


def schedule(adj, order, q):
    seen = [0] * q
    events = []
    for v in order:
        ns = adj[v]
        old = tuple(u for u in ns if seen[u])
        root = len(ns) == 2 and not old
        events.append((v, ns, old, root))
        for u in ns:
            seen[u] += 1
    assert max(seen, default=0) <= 2
    return events


def exact_fair(events):
    states = {0: 1}
    roots = 0
    for _, ns, old, root in events:
        next_states = Counter()
        for mask, weight in states.items():
            free = [u for u in ns if not (mask >> u) & 1]
            exhausted = [u for u in free if u in old]
            if root:
                assert len(free) == 2
                for u in free:
                    next_states[mask | (1 << u)] += weight
            elif free:
                u = min(exhausted or free)
                next_states[mask | (1 << u)] += weight
            else:
                next_states[mask] += weight
        roots += root
        states = dict(next_states)
        assert sum(states.values()) == 2 ** roots
    return Fraction(sum(mask.bit_count() * w for mask, w in states.items()), 2 ** roots)


def priority(events, advice=None, bits=()):
    mask = 0
    ri = 0
    for v, ns, old, root in events:
        free = [u for u in ns if not (mask >> u) & 1]
        exhausted = [u for u in free if u in old]
        if exhausted:
            u = min(exhausted)
        elif not free:
            continue
        elif advice is not None and advice[v] in free:
            u = advice[v]
        elif root and bits:
            u = free[bits[ri]]
        else:
            u = min(free)
        ri += root
        mask |= 1 << u
    return mask.bit_count()


def advice_tables(m, q):
    def visit(v, used, prefix):
        if v == m:
            yield prefix
            return
        yield from visit(v + 1, used, prefix + (-1,))
        for u in range(q):
            if u not in used:
                yield from visit(v + 1, used | {u}, prefix + (u,))
    return visit(0, set(), ())


def matching_tables(adj, q):
    def visit(v, used, prefix):
        if v == len(adj):
            yield prefix
            return
        yield from visit(v + 1, used, prefix + (-1,))
        for u in adj[v]:
            if u not in used:
                yield from visit(v + 1, used | {u}, prefix + (u,))
    return list(visit(0, set(), ()))


def component(typ, m):
    if typ == 'offline_ends':
        return [(i, i + 1) for i in range(m)], m + 1, 0
    if typ == 'balanced':
        return [(i, i + 1) for i in range(m - 1)] + [(m - 1,)], m, 1
    if typ == 'online_ends':
        return [(0,)] + [(i - 1, i) for i in range(1, m - 1)] + [(m - 2,)], m - 1, 2
    return [(i, (i + 1) % m) for i in range(m)], m, None


def best_future(rows, mask):
    vals = {mask: 0}
    for ns in rows:
        nxt = dict(vals)
        for used, val in vals.items():
            for u in ns:
                if not (used >> u) & 1:
                    z = used | (1 << u)
                    nxt[z] = max(nxt.get(z, -1), val + 1)
        vals = nxt
    return max(vals.values())


def gadget_hypotheses():
    out = []
    for kind, worlds, advice in (
        ('path', (((0, 1), (0,)), ((0, 1), (1,))), (0, 1)),
        ('cycle', (((0, 1), (2, 3), (0, 2), (1, 3)),
                   ((0, 1), (2, 3), (0, 3), (1, 2))), (0, 2, 3, 1))):
        q = len(advice)
        assert len(set(advice)) == q
        record = dict(kind=kind, advice=advice, worlds=[])
        for adj in worlds:
            degrees = [sum(u in ns for ns in adj) for u in range(q)]
            assert max(degrees) <= 2 and max(map(len, adj)) <= 2
            opt = best_future(adj, 0)
            assert opt == q
            if kind == 'cycle':
                assert set(degrees) == {2} and set(map(len, adj)) == {2}
                # Connectivity of the full bipartite graph.
                reached = {('u', 0)}
                while True:
                    nxt = set(reached)
                    for v, ns in enumerate(adj):
                        for u in ns:
                            if ('u', u) in reached or ('v', v) in reached:
                                nxt.update((('u', u), ('v', v)))
                    if nxt == reached:
                        break
                    reached = nxt
                assert len(reached) == 2*q
            record['worlds'].append(dict(adjacencies=adj, offline_degrees=degrees,
                                         opt=opt, advice_realized=all(advice[v] in ns for v, ns in enumerate(adj))))
        assert not record['worlds'][0]['advice_realized']
        assert record['worlds'][1]['advice_realized']
        out.append(record)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-online', type=int, default=8)
    args = parser.parse_args()
    assert hashlib.sha256((ROOT / 'source.md').read_bytes()).hexdigest() == SOURCE_SHA
    totals = Counter()
    summaries = []
    for typ in ('offline_ends', 'balanced', 'online_ends', 'cycle'):
        rows = 0
        worst = None
        for m in range(1 if typ in ('offline_ends', 'balanced') else 2, args.max_online + 1):
            adj, q, ell = component(typ, m)
            opt = min(m, q)
            valid = matching_tables(adj, q)
            good = [a for a in valid if sum(u >= 0 for u in a) == opt]
            for order in permutations(range(m)):
                events = schedule(adj, order, q)
                a = sum(e[3] for e in events)
                measured = exact_fair(events)
                predicted = Fraction(m) if typ == 'cycle' and a == 1 else (
                    Fraction(m) - Fraction(a, 4) if typ == 'cycle' else (
                    Fraction(opt) if a == 0 else Fraction(m) - Fraction(a - 1, 4) - Fraction(ell, 2)))
                assert measured == predicted, (typ, m, order, measured, predicted)
                assert measured >= Fraction(3, 4) * opt
                if ell in (0, 2) or typ == 'cycle':
                    assert measured >= Fraction(7, 8) * opt
                for advice in good:
                    assert priority(events, advice=advice) == opt, (typ, m, order, advice)
                    totals['perfect_advice_cases'] += 1
                if typ == 'cycle':
                    for bits in product((0, 1), repeat=a):
                        value = priority(events, bits=bits)
                        assert value >= m - a // 2
                        totals['cycle_orientation_cases'] += 1
                ratio = measured / opt
                if worst is None or ratio < Fraction(worst['ratio']):
                    worst = dict(m=m, offline=q, order=order, roots=a,
                                 expected=str(measured), opt=opt, ratio=str(ratio))
                rows += 1
        summaries.append(dict(type=typ, arrival_orders=rows, worst=worst))
        totals['component_arrival_orders'] += rows
        print(json.dumps(dict(type=typ, completed_orders=rows)), flush=True)

    # Exhaustive labelled inputs n=3 include disconnected graphs, isolates,
    # absent advised edges, and every partial injective table (34 tables).
    n = 3
    all_advice = list(advice_tables(n, n))
    for edge_bits in range(1 << (n*n)):
        adj = [tuple(u for u in range(n) if edge_bits >> (v*n+u) & 1) for v in range(n)]
        if max(map(len, adj)) > 2 or any(sum(u in ns for ns in adj) > 2 for u in range(n)):
            continue
        valid = matching_tables(adj, n)
        opt = max(sum(u >= 0 for u in t) for t in valid)
        good = set(t for t in valid if sum(u >= 0 for u in t) == opt)
        for order in permutations(range(n)):
            events = schedule(adj, order, n)
            assert exact_fair(events) >= Fraction(3, 4)*opt
            for advice in all_advice:
                value = priority(events, advice=advice)
                assert value * 2 >= opt
                if advice in good:
                    assert value == opt
                totals['labelled_graph_order_advice_cases'] += 1
        totals['labelled_graphs_n3'] += 1

    # All deterministic prefixes, then optimal continuations on both worlds.
    gadget = []
    for x in (-1, 0, 1):
        mask = 0 if x == -1 else 1 << x
        z = int(x != -1)
        score = 2*z + best_future(((0,),), mask) + best_future(((1,),), mask)
        assert score <= 3
        gadget.append(dict(kind='path', first=[x], sum_bound=score))
    for x, y in product((-1, 0, 1), (-1, 2, 3)):
        mask = (0 if x == -1 else 1 << x) | (0 if y == -1 else 1 << y)
        z = int(x != -1) + int(y != -1)
        score = 2*z + best_future(((0, 2), (1, 3)), mask) + best_future(((0, 3), (1, 2)), mask)
        assert score <= 7
        gadget.append(dict(kind='cycle', first=[x, y], sum_bound=score))
    output = dict(job_id='advice-matching-research-eee7dbe89d57',
                  status='exact finite checks passed; researcher evidence only',
                  source_sha256=SOURCE_SHA, max_component_online=args.max_online,
                  method='forward integer distribution, independently implemented',
                  summaries=summaries, totals=dict(totals), gadget=gadget,
                  gadget_hypotheses=gadget_hypotheses(),
                  completeness='Every connected degree-two component type and every arrival permutation through the stated online size, up to graph isomorphism; every labelled bounded-degree n=3 graph/order/advice table.',
                  limitations='Finite checks do not prove unbounded theorems, novelty, or independent referee acceptance.')
    out = ROOT / 'evidence' / 'frontier-checks.json'
    out.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(dict(output=str(out.relative_to(ROOT)), totals=dict(totals))))


if __name__ == '__main__':
    main()
