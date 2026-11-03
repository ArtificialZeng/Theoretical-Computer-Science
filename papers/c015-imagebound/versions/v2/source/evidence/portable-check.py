#!/usr/bin/env python3
"""Portable finite reproduction for the mortality construction.

Run with Python3 (standard library only) from any directory. No downloaded
source papers, private paths, audit snapshots, or generated files are inputs.
The program checks complete finite reachable closures and stated arithmetic
examples; the infinite theorem is proved analytically in the paper.
Derived from the supervisor's independent set-based checker; this does not
claim another fresh mathematical referee or external human verification.
"""
from collections import deque
from itertools import product
from math import factorial, gcd, lcm
import json


def model(m, lengths):
    states = [('p', j) for j in range(m)]
    states += [(i, j) for i, length in enumerate(lengths) for j in range(length)]
    packet = frozenset(((i, 0) for i in range(len(lengths))))
    a, b = ({}, {})
    for state in states:
        i, j = state
        if i == 'p':
            a[state] = frozenset([('p', (j + 1) % m)])
            if j == 0:
                b[state] = packet
            else:
                b[state] = frozenset([('p', m - 1 if j == 1 else j - 1)])
        else:
            a[state] = frozenset([(i, (j + 1) % lengths[i])])
            b[state] = frozenset() if j == lengths[i] - 1 else frozenset([('p', 0)])
    return (states, packet, a, b)


def move(subset, letter):
    return frozenset((v for u in subset for v in letter[u]))


def graph(roots, letters):
    distance = {r: 0 for r in roots}
    queue = deque(roots)
    while queue:
        s = queue.popleft()
        for letter in letters:
            t = move(s, letter)
            if t not in distance:
                distance[t] = distance[s] + 1
                queue.append(t)
    return distance


def verify(m, lengths, certificate=None):
    states, packet, a, b = model(m, lengths)
    k = len(lengths)
    letters = [a, b]
    rows = graph([frozenset([s]) for s in states], letters)
    assert max(map(len, rows)) <= k
    distances = graph([frozenset(states)], letters)
    threshold = distances[frozenset()]
    L = lcm(*lengths)
    assert 1 + (m + 1) * L <= threshold <= 1 + (m + 1) * L + m * m
    if certificate is not None:

        def convert(mask):
            return frozenset((states[i] for i in range(len(states)) if mask >> i & 1))
        assert {convert(s) for s in certificate['singleton_masks']} == set(rows)
        encoded = {convert(s): d for s, d, _, _ in certificate['global_bfs']}
        assert encoded == distances
        for s, d, to_a, to_b in certificate['global_bfs']:
            assert move(convert(s), a) == convert(to_a)
            assert move(convert(s), b) == convert(to_b)
        for i, s in enumerate(states):
            assert a[s] == convert(certificate['a'][i])
            assert b[s] == convert(certificate['b'][i])
        current = frozenset(states)
        for c in certificate['shortest_word']:
            current = move(current, a if c == 'a' else b)
        assert not current and len(certificate['shortest_word']) == threshold
    potential_checks = 0
    for indicators in product([False, True], repeat=m + 1):
        queue = frozenset((('p', j) for j in range(m) if indicators[j]))
        present = indicators[m]
        current = queue | (packet if present else frozenset())
        value = len(queue) + present
        for t in range(lcm(m, *lengths)):
            nxt = move(current, b)
            new_queue = {s for s in nxt if s[0] == 'p'}
            new_packet = nxt - frozenset(new_queue)
            assert new_packet in (frozenset(), packet)
            drop = value - (len(new_queue) + bool(new_packet))
            assert drop == int(present and all(((t + 1) % ell == 0 for ell in lengths)))
            potential_checks += 1
            current = move(current, a)
    for source in states:
        seen = {source}
        queue = deque([source])
        while queue:
            s = queue.popleft()
            for v in a[s] | b[s]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        assert len(seen) == len(states)
    return {'m': m, 'lengths': lengths, 'states': len(states), 'shortest': threshold, 'reachable_global_sets': len(distances), 'singleton_images': len(rows), 'all_quotient_potential_checks': potential_checks, 'strongly_connected': True}


def parameters():
    checked = 0
    for k in range(1, 13):
        K = factorial(k)
        A = 1 + k * (k + 1) // 2
        for n in range(2 * k + 2 * A * K, 2 * k + 2 * A * K + 101):
            M = K * ((n - k) // (A * K))
            lengths = [1 + i * M for i in range(1, k + 1)]
            m = n - sum(lengths)
            assert M >= 2 and m >= M and (2 * A * M >= n)
            assert all((gcd(x, y) == 1 for j, x in enumerate(lengths) for y in lengths[j + 1:]))
            lower = m + 1
            for ell in lengths:
                lower *= ell
            assert lower * (2 * A) ** (k + 1) >= factorial(k) * n ** (k + 1)
            checked += 1
    return checked

def main():
    fixed=[(m,lengths) for m in (2,3,4)
           for lengths in ((3,5),(2,3,5),(3,4,5))]
    boundary=[(2,(2,)),(3,(4,)),(5,(3,)),(2,(2,2)),(3,(2,4)),
              (5,(2,4,6)),(2,(2,3,4)),(5,(2,2,3,3)),(3,(2,3,5,7))]
    # Four further controls chosen by the separate referee context.
    controls=[(2,(2,3)),(4,(2,2)),(3,(3,6)),(4,(2,))]
    cases=[verify(m,list(lengths)) for m,lengths in fixed+boundary+controls]
    expected=[48, 91, 181, 63, 123, 243, 78, 155, 301, 7, 21, 21, 7, 21, 80, 37, 45, 843, 19, 13, 27, 13]
    assert [r['shortest'] for r in cases]==expected
    result={'finite_automata':len(cases),
            'shortest_mortal_lengths':expected,
            'all_quotient_potential_checks':sum(r['all_quotient_potential_checks'] for r in cases),
            'parameter_arithmetic_cases':parameters(),
            'full_singleton_closure_checked':True,
            'full_global_subset_bfs_checked':True,
            'strong_connectivity_checked':True,
            'scope':'Finite reproduction only; the all-parameter theorem is justified by the written proof.',
            'cases':cases}
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
