#!/usr/bin/env python3
"""Bounded research replay. No imports from previous construction/checkers.

Full subset closure, not a word-prefix cutoff. The proof in research-proof.md,
not these finite checks, establishes the infinite parameter theorem.
"""
from collections import deque
from itertools import product
from math import factorial, gcd, lcm
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c015-imagebound-research-337b679e5617'


def transitions(m, lengths):
    states = [('P', j) for j in range(m)]
    states += [(i, j) for i, ell in enumerate(lengths) for j in range(ell)]
    packet = frozenset((i, 0) for i in range(len(lengths)))
    letters = {'a': {}, 'b': {}}
    for q in states:
        i, j = q
        if i == 'P':
            aq = ('P', (j + 1) % m)
            bq = packet if j == 0 else frozenset([('P', 1 + (j - 2) % (m - 1))])
        else:
            aq = (i, (j + 1) % lengths[i])
            bq = frozenset() if j + 1 == lengths[i] else frozenset([('P', 0)])
        letters['a'][q] = frozenset([aq])
        letters['b'][q] = bq
    return states, packet, letters


def image(subset, relation):
    return frozenset(t for q in subset for t in relation[q])


def closure(roots, letters):
    distances = {s: 0 for s in roots}
    parents = {}
    queue = deque(distances)
    while queue:
        current = queue.popleft()
        for name, relation in letters.items():
            nxt = image(current, relation)
            if nxt not in distances:
                distances[nxt] = distances[current] + 1
                parents[nxt] = (current, name)
                queue.append(nxt)
    assert all(image(s, r) in distances for s in distances for r in letters.values())
    return distances, parents


def check(m, lengths, old_certificate=None):
    states, packet, letters = transitions(m, lengths)
    a, b = letters['a'], letters['b']
    k, L = len(lengths), lcm(*lengths)
    row_distances, _ = closure([frozenset([q]) for q in states], letters)
    global_distances, parents = closure([frozenset(states)], letters)
    assert frozenset() in global_distances
    assert max(map(len, row_distances)) == k
    packet_orbit = set()
    current = packet
    for _ in range(L):
        packet_orbit.add(current)
        current = image(current, a)
    assert current == packet and len(packet_orbit) == L
    assert all(len(s) <= 1 or s in packet_orbit for s in row_distances)
    shortest = global_distances[frozenset()]
    assert 1 + (m + 1) * L <= shortest <= 1 + (m + 1) * L + m * m
    word, current = [], frozenset()
    while current in parents:
        current, name = parents[current]
        word.append(name)
    word = ''.join(reversed(word))
    assert len(word) == shortest

    # Replay every row and distance in the supplied complete certificates.
    def mask(s):
        return sum(1 << i for i, q in enumerate(states) if q in s)
    if old_certificate is not None:
        cert = json.loads(old_certificate.read_text())
        assert cert['a'] == [mask(a[q]) for q in states]
        assert cert['b'] == [mask(b[q]) for q in states]
        assert set(cert['singleton_masks']) == {mask(s) for s in row_distances}
        expected = [[mask(s), d, mask(image(s, a)), mask(image(s, b))]
                    for s, d in global_distances.items()]
        assert sorted(expected) == cert['global_bfs']

    # Test the exact potential identity on EVERY quotient configuration, even
    # configurations not reachable from Q, and every a-run residue.
    potential_checks = 0
    for bits in product([False, True], repeat=m + 1):
        T = frozenset(('P', j) for j in range(m) if bits[j])
        present = bits[-1]
        value = len(T) + present
        current = T | (packet if present else frozenset())
        for t in range(lcm(m, L)):
            nxt = image(current, b)
            queue_part = frozenset(q for q in nxt if q[0] == 'P')
            clock_part = nxt - queue_part
            assert clock_part in (frozenset(), packet)
            new_value = len(queue_part) + bool(clock_part)
            assert value - new_value == int(present and (t + 1) % L == 0)
            current = image(current, a)
            potential_checks += 1

    # Execute the claimed mortality strategy and keep an inspectable word.
    current = image(frozenset(states), b)
    assert current == frozenset(('P', j) for j in range(m)) | packet
    constructed = ['b']
    drops = forks = 0
    while current:
        clocks = frozenset(q for q in current if q[0] != 'P')
        assert clocks in (frozenset(), packet)
        if not clocks:
            j = min(q[1] for q in current)
            t = (-j) % m
            for _ in range(t): current = image(current, a)
            current = image(current, b)
            constructed.append('a' * t + 'b')
            forks += 1
            assert packet <= current
        previous = len([q for q in current if q[0] == 'P']) + 1
        for _ in range(L - 1): current = image(current, a)
        current = image(current, b)
        constructed.append('a' * (L - 1) + 'b')
        assert previous - (len([q for q in current if q[0] == 'P']) + bool(current & packet)) == 1
        drops += 1
        assert drops <= m + 1
    constructed = ''.join(constructed)
    assert drops == m + 1 and forks <= m
    assert len(constructed) <= 1 + (m + 1) * L + m * m
    replay = frozenset(states)
    for name in constructed: replay = image(replay, letters[name])
    assert not replay

    for q in states:
        seen, todo = {q}, deque([q])
        while todo:
            v = todo.popleft()
            for u in a[v] | b[v]:
                if u not in seen: seen.add(u); todo.append(u)
        assert len(seen) == len(states)
    return {'m': m, 'lengths': list(lengths), 'n': len(states), 'k': k,
            'L': L, 'row_closure_count': len(row_distances),
            'row_maximum': max(map(len, row_distances)),
            'global_closure_count': len(global_distances),
            'shortest_mortal_length': shortest, 'shortest_word': word,
            'constructive_word': constructed, 'constructive_length': len(constructed),
            'potential_checks_all_configurations': potential_checks,
            'strongly_connected': True,
            'complete_global_bfs': sorted([[mask(s), d, mask(image(s, a)), mask(image(s, b))]
                                          for s, d in global_distances.items()]),
            'complete_row_closure_masks': sorted(mask(s) for s in row_distances)}


def main():
    started = time.monotonic()
    cases = []
    for m, lengths in product([2, 3, 4], [(3, 5), (2, 3, 5), (3, 4, 5)]):
        filename = f'queue-clock-m{m}-' + '-'.join(map(str, lengths)) + '.json'
        old = ROOT / 'intake/root-queue-clock/queue-clock-certificates' / filename
        cases.append(check(m, lengths, old))
    # Fixed boundary cases inherited from the supervisor packet: k=1,
    # repeated/noncoprime clocks, and k=4. No search-driven parameter growth.
    boundary = [(2, [2]), (3, [4]), (5, [3]), (2, [2, 2]), (3, [2, 4]),
                (5, [2, 4, 6]), (2, [2, 3, 4]), (5, [2, 2, 3, 3]), (3, [2, 3, 5, 7])]
    controls = [check(m, lengths) for m, lengths in boundary]
    arithmetic = 0
    for k in range(1, 13):
        K, A = factorial(k), 1 + k * (k + 1) // 2
        N = 2 * k + 2 * A * K
        for n in [N + j for j in range(101)] + [10 * N - 1, 10 * N, 10 * N + 1]:
            M = K * ((n - k) // (A * K))
            lengths = [1 + i * M for i in range(1, k + 1)]
            m = n - sum(lengths)
            assert M >= 2 and m >= M and 2 * A * M >= n
            assert all(gcd(x, y) == 1 for j, x in enumerate(lengths) for y in lengths[j + 1:])
            assert (m + 1) * lcm(*lengths) * (2 * A) ** (k + 1) >= K * n ** (k + 1)
            arithmetic += 1
    report = {'job_id': JOB, 'source_sha256': hashlib.sha256((ROOT / 'source.md').read_bytes()).hexdigest(),
              'scope': '18 fixed automata, full row/global closures; all quotient configurations and a-run residues; arithmetic samples are not an infinite proof',
              'frozen_cases': cases, 'boundary_cases': controls,
              'arithmetic_cases': arithmetic, 'elapsed_seconds': time.monotonic() - started}
    (ROOT / 'evidence/research-check-results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'frozen_shortest': [r['shortest_mortal_length'] for r in cases],
                      'boundary_shortest': [r['shortest_mortal_length'] for r in controls],
                      'potential_checks': sum(r['potential_checks_all_configurations'] for r in cases + controls),
                      'arithmetic_cases': arithmetic, 'elapsed_seconds': report['elapsed_seconds']}))


if __name__ == '__main__': main()
