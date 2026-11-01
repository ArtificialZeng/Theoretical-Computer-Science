#!/usr/bin/env python3
"""Fresh, bounded referee verification; no imports of discovery/research code.

The infinite theorem is checked in math.md.  These are complete finite closures,
not word-length cutoffs.  Only files listed in the frozen snapshot are inputs.
"""
from collections import deque
from hashlib import sha256
from itertools import combinations
from math import factorial, gcd, lcm
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c015-imagebound-referee-c91c0d194005'


def step(mask, letter):
    answer = 0
    while mask:
        bit = mask & -mask
        answer |= letter[bit.bit_length() - 1]
        mask ^= bit
    return answer


def make(m, lengths):
    starts = []
    offset = m
    for ell in lengths:
        starts.append(offset)
        offset += ell
    packet = sum(1 << s for s in starts)
    a = [1 << ((j + 1) % m) for j in range(m)]
    b = [packet] + [1 << (m - 1)] + [1 << (j - 1) for j in range(2, m)]
    for start, ell in zip(starts, lengths):
        a += [1 << (start + (j + 1) % ell) for j in range(ell)]
        b += [1] * (ell - 1) + [0]
    return a, b, packet


def closure(seeds, a, b):
    distances = dict.fromkeys(seeds, 0)
    parents = {}
    todo = deque(distances)
    while todo:
        x = todo.popleft()
        for symbol, letter in [('a', a), ('b', b)]:
            y = step(x, letter)
            if y not in distances:
                distances[y] = distances[x] + 1
                parents[y] = (x, symbol)
                todo.append(y)
    # Exhaustion plus this closure check certifies the entire reachable domain.
    assert all(step(x, letter) in distances for x in distances for letter in (a, b))
    return distances, parents


def check(m, lengths, reference=None, certificate=None):
    a, b, packet = make(m, lengths)
    n, k, period = len(a), len(lengths), lcm(*lengths)
    full = (1 << n) - 1
    queue_mask = (1 << m) - 1
    rows, _ = closure([1 << q for q in range(n)], a, b)
    glob, parents = closure([full], a, b)
    assert 0 in glob and max(x.bit_count() for x in rows) == k
    assert step(full, b) == queue_mask | packet
    threshold = glob[0]
    assert 1 + (m + 1) * period <= threshold <= 1 + (m + 1) * period + m * m
    orbit, s = set(), packet
    while s not in orbit:
        orbit.add(s)
        s = step(s, a)
    assert s == packet and len(orbit) == period
    assert all(x.bit_count() <= 1 or x in orbit for x in rows)
    bfs_table = sorted([x, d, step(x, a), step(x, b)] for x, d in glob.items())
    if reference is not None:
        assert bfs_table == reference['complete_global_bfs']
        assert sorted(rows) == reference['complete_row_closure_masks']
        assert threshold == reference['shortest_mortal_length']
        s = full
        for symbol in reference['constructive_word']:
            s = step(s, a if symbol == 'a' else b)
        assert s == 0
    if certificate is not None:
        assert certificate['a'] == a and certificate['b'] == b
        assert certificate['packet'] == packet
        assert certificate['global_bfs'] == bfs_table
        assert certificate['singleton_masks'] == sorted(rows)
        assert len(certificate['shortest_word']) == threshold
        s = full
        for symbol in certificate['shortest_word']:
            s = step(s, a if symbol == 'a' else b)
        assert s == 0
    word, s = [], 0
    while s != full:
        s, symbol = parents[s]
        word.append(symbol)
    word = ''.join(reversed(word))
    assert len(word) == threshold
    potential_checks = 0
    for tset in range(1 << m):
        for present in (0, 1):
            old = tset.bit_count() + present
            current = tset | (packet if present else 0)
            for t in range(lcm(m, period)):
                nxt = step(current, b)
                clocks = nxt & ~queue_mask
                assert clocks == 0 or clocks == packet
                new = (nxt & queue_mask).bit_count() + int(bool(clocks))
                assert old - new == int(present and (t + 1) % period == 0)
                current = step(current, a)
                potential_checks += 1
    # Independent choice in the mortality controller: use highest queue index.
    current = step(full, b)
    length, drops, forks = 1, 0, 0
    while current:
        if not (current & ~queue_mask):
            j = current.bit_length() - 1
            t = (-j) % m
            for _ in range(t):
                current = step(current, a)
            current = step(current, b)
            length += t + 1
            forks += 1
        assert current & ~queue_mask == packet
        old = (current & queue_mask).bit_count() + 1
        for _ in range(period - 1):
            current = step(current, a)
        current = step(current, b)
        new = (current & queue_mask).bit_count() + int(bool(current & ~queue_mask))
        assert new == old - 1
        drops += 1
        length += period
        assert drops <= m + 1
    assert drops == m + 1 and forks <= m
    assert length <= 1 + (m + 1) * period + m * m
    # Reachability in the unlabelled graph, not the powerset automaton.
    for q in range(n):
        seen = 1 << q
        while True:
            expanded = seen | step(seen, a) | step(seen, b)
            if seen == expanded:
                break
            seen = expanded
        assert seen == full
    return dict(m=m, lengths=lengths, n=n, k=k, L=period,
                row_closure_count=len(rows), global_closure_count=len(glob),
                shortest_mortal_length=threshold, shortest_word=word,
                lower_bound=1 + (m + 1) * period,
                upper_bound=1 + (m + 1) * period + m * m,
                potential_configurations_and_residues=potential_checks,
                strong_connectivity=True,
                complete_bfs_sha256=sha256(json.dumps(bfs_table).encode()).hexdigest(),
                complete_row_closure_sha256=sha256(json.dumps(sorted(rows)).encode()).hexdigest())


def main():
    started = time.monotonic()
    snap = json.loads((ROOT / 'audit/snapshot.json').read_text())
    actual = {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in snap['files']}
    assert actual == snap['files']
    digest = sha256(json.dumps(actual, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    assert digest == snap['digest']
    existing = json.loads((ROOT / 'evidence/research-check-results.json').read_text())
    checked = []
    for group in ('frozen_cases', 'boundary_cases'):
        for row in existing[group]:
            m, lengths = row['m'], row['lengths']
            cert = None
            if group == 'frozen_cases':
                name = f'intake/root-queue-clock/queue-clock-certificates/queue-clock-m{m}-' + '-'.join(map(str, lengths)) + '.json'
                assert name in snap['files']
                cert = json.loads((ROOT / name).read_text())
            checked.append(check(m, lengths, row, cert))
    # Fixed adversarial controls chosen before running: repeated lengths,
    # L sharing factors with m, and a one-clock calibration.
    controls = [check(m, lengths) for m, lengths in
                [(2, [2, 3]), (4, [2, 2]), (3, [3, 6]), (4, [2])]]
    arithmetic = 0
    for k in range(2, 21):
        K, A = factorial(k), 1 + k * (k + 1) // 2
        N = 2 * k + 2 * A * K
        for n in [N + j for j in range(41)] + [3 * N - 1, 3 * N, 10 * N + 1]:
            M = K * ((n - k) // (A * K))
            ell = [1 + i * M for i in range(1, k + 1)]
            m = n - sum(ell)
            assert M >= 2 and m >= M and 2 * A * M >= n
            assert all(gcd(x, y) == 1 for x, y in combinations(ell, 2))
            assert lcm(*ell) >= K * M ** k
            assert (m + 1) * lcm(*ell) * (2 * A) ** (k + 1) >= K * n ** (k + 1)
            arithmetic += 1
    result = dict(job_id=JOB, snapshot_digest=digest, frozen_integrity_verified=True,
                  finite_scope='22 fixed automata: complete singleton/global closures, every boundary subset and phase residue; 836 arithmetic samples. These finite checks do not prove the infinite theorem.',
                  replayed_cases=checked, fresh_controls=controls, arithmetic_samples=arithmetic,
                  elapsed_seconds=time.monotonic() - started)
    (ROOT / 'audit/referee-verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(verified_automata=len(checked) + len(controls),
                          replayed_thresholds=[x['shortest_mortal_length'] for x in checked],
                          new_control_thresholds=[x['shortest_mortal_length'] for x in controls],
                          potential_checks=sum(x['potential_configurations_and_residues'] for x in checked + controls),
                          arithmetic_samples=arithmetic, elapsed_seconds=result['elapsed_seconds'])))


if __name__ == '__main__':
    main()
