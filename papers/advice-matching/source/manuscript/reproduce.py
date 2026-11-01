#!/usr/bin/env python3
"""Finite exact checks for the matching-advice manuscript; standard library only.

Prints JSON to stdout and never changes any file. These finite checks do not
establish the unbounded theorems, whose proofs are in the manuscript.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json


def events(rows, order):
    seen = set()
    out = []
    for v in order:
        old = seen.intersection(rows[v])
        root = len(rows[v]) == 2 and not old
        out.append((v, tuple(rows[v]), old, root))
        seen.update(rows[v])
    return out


def run(schedule, advice=None, bits=()):
    occupied = set()
    ri = 0
    for v, neighbors, old, root in schedule:
        free = sorted(set(neighbors) - occupied)
        exhausted = sorted(set(free) & old)
        chosen = None
        if exhausted:
            chosen = exhausted[0]
        elif free:
            if advice is not None and advice[v] in free:
                chosen = advice[v]
            elif advice is None and root:
                chosen = free[bits[ri]]
            else:
                chosen = free[0]
        ri += int(root)
        if chosen is not None:
            occupied.add(chosen)
    return len(occupied)


def fair(schedule):
    a = sum(e[3] for e in schedule)
    values = [run(schedule, bits=bits) for bits in product((0, 1), repeat=a)]
    return Fraction(sum(values), len(values)), values


def tables(m, q):
    def visit(prefix, used):
        if len(prefix) == m:
            yield tuple(prefix)
            return
        for u in (-1, *range(q)):
            if u == -1 or u not in used:
                yield from visit(prefix + [u], used | ({u} if u >= 0 else set()))
    return list(visit([], set()))


def optimum_tables(rows, all_tables):
    feasible = [t for t in all_tables
                if all(u == -1 or u in rows[v] for v, u in enumerate(t))]
    opt = max(sum(u >= 0 for u in t) for t in feasible)
    return opt, [t for t in feasible if sum(u >= 0 for u in t) == opt]


def continuation(rows, used):
    if not rows:
        return 0
    return max([continuation(rows[1:], used)] +
               [1 + continuation(rows[1:], used | {u})
                for u in rows[0] if u not in used])


def main():
    counts = Counter()
    min_e = Fraction(1)
    n = 3
    all_tables = tables(n, n)
    assert len(all_tables) == 34
    possible = [()] + [(u,) for u in range(n)] + list(combinations(range(n), 2))
    for rows in product(possible, repeat=n):
        degrees = [sum(u in ns for ns in rows) for u in range(n)]
        if max(degrees) > 2:
            continue
        counts['labelled_n3_graphs'] += 1
        regular = all(d == 2 for d in degrees) and all(len(ns) == 2 for ns in rows)
        opt, good = optimum_tables(rows, all_tables)
        for order in permutations(range(n)):
            counts['n3_graph_orders'] += 1
            schedule = events(rows, order)
            mean, values = fair(schedule)
            assert 4 * mean >= 3 * opt, (rows, order, mean, opt)
            if opt:
                min_e = min(min_e, mean / opt)
            if regular:
                assert 8 * mean >= 7 * opt
            for advice in good:
                assert run(schedule, advice=advice) == opt
                counts['n3_maximum_advice_cases'] += 1
            for advice in all_tables:
                val = run(schedule, advice=advice)
                assert 2 * val >= opt
                counts['n3_arbitrary_advice_cases'] += 1
                if regular:
                    assert 4 * val >= 3 * opt
                    counts['n3_regular_arbitrary_advice_cases'] += 1

    # Each connected path type, up to reversal of its bipartition endpoints.
    for m in range(1, 7):
        components = [
            ('offline-ended', [(i, i + 1) for i in range(m)], m + 1, 0),
            ('balanced', [(i, i + 1) for i in range(m - 1)] + [(m - 1,)], m, 1),
        ]
        if m >= 2:
            components += [
                ('online-ended', [(0,)] + [(i - 1, i) for i in range(1, m - 1)]
                 + [(m - 2,)], m - 1, 2),
                ('cycle', [(i, (i + 1) % m) for i in range(m)], m, None),
            ]
        for kind, rows, q, ell in components:
            for order in permutations(range(m)):
                schedule = events(rows, order)
                a = sum(e[3] for e in schedule)
                mean, values = fair(schedule)
                opt = min(m, q)
                if ell is None:
                    formula = Fraction(m) if a == 1 else Fraction(m) - Fraction(a, 4)
                    assert all(4 * val >= 3 * opt for val in values)
                    assert 8 * mean >= 7 * opt
                    counts['cycle_root_orientations'] += len(values)
                else:
                    formula = (Fraction(opt) if a == 0 else
                               Fraction(m) - Fraction(a - 1, 4) - Fraction(ell, 2))
                assert mean == formula, (kind, m, order, mean, formula)
                assert 4 * mean >= 3 * opt
                counts['component_orders_through_6'] += 1

    # Best possible late continuation for every common early action.
    for first in (-1, 0, 1):
        used = set() if first == -1 else {first}
        early = int(first >= 0)
        summed = sum(early + continuation([late], used)
                     for late in ((0,), (1,)))
        assert summed <= 3
        counts['Z_prefixes'] += 1
    late_worlds = [((0, 2), (1, 3)), ((0, 3), (1, 2))]
    advice = (0, 2, 3, 1)
    early_rows = ((0, 1), (2, 3))
    for late in late_worlds:
        rows = early_rows + late
        assert all(sum(u in ns for ns in rows) == 2 for u in range(4))
        assert all(len(ns) == 2 for ns in rows)
        assert continuation(rows, set()) == 4
    assert all(advice[v] in ns for v, ns in enumerate(early_rows + late_worlds[1]))
    missing = [(v, u) for v, u in enumerate(advice)
               if u not in (early_rows + late_worlds[0])[v]]
    assert missing == [(2, 3)]
    for x1, x2 in product((-1, 0, 1), (-1, 2, 3)):
        used = {u for u in (x1, x2) if u >= 0}
        early = len(used)
        summed = sum(early + continuation(late, used) for late in late_worlds)
        assert summed <= 7
        counts['cycle_prefixes'] += 1
    assert counts['labelled_n3_graphs'] == 265
    print(json.dumps({'ok': True, 'scope': 'finite exact checks only',
                      'counts': dict(counts), 'minimum_E_ratio_n3': str(min_e),
                      'component_max_online': 6, 'dependencies': 'Python standard library'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
