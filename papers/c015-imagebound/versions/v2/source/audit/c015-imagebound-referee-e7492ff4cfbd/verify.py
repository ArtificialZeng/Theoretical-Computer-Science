#!/usr/bin/env python3
"""Fresh referee checks; no imports from any frozen checker.

The infinite theorem is reviewed in audit/math.md. These finite exact checks
are supplementary and do not certify untested parameters or novelty.
"""
from collections import deque
from datetime import datetime, timezone
from hashlib import sha256
from math import factorial, gcd, lcm
from pathlib import Path
import json
import shutil
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
JOB = 'c015-imagebound-referee-e7492ff4cfbd'


def step(mask, relation):
    answer = 0
    while mask:
        bit = mask & -mask
        answer |= relation[bit.bit_length() - 1]
        mask ^= bit
    return answer


def build(m, lengths):
    n = m + sum(lengths)
    a, b = [0] * n, [0] * n
    starts, offset = [], m
    for ell in lengths:
        starts.append(offset)
        offset += ell
    packet = sum(1 << start for start in starts)
    for j in range(m):
        a[j] = 1 << ((j + 1) % m)
    b[0] = packet
    b[1] = 1 << (m - 1)
    for j in range(2, m):
        b[j] = 1 << (j - 1)
    for start, ell in zip(starts, lengths):
        for j in range(ell):
            a[start + j] = 1 << (start + (j + 1) % ell)
            b[start + j] = 0 if j == ell - 1 else 1
    return a, b, packet


def closure(seeds, relations):
    d = dict.fromkeys(seeds, 0)
    todo = deque(d)
    while todo:
        x = todo.popleft()
        for r in relations:
            y = step(x, r)
            if y not in d:
                d[y] = d[x] + 1
                todo.append(y)
    return d


def check_case(m, lengths, record=None, certificate=None):
    a, b, packet = build(m, lengths)
    n, k, L = len(a), len(lengths), lcm(*lengths)
    queue_mask = (1 << m) - 1
    full = (1 << n) - 1
    rows = closure([1 << j for j in range(n)], [a, b])
    distances = closure([full], [a, b])
    assert max(x.bit_count() for x in rows) == k
    assert 0 in distances
    assert 1 + (m + 1) * L <= distances[0] <= 1 + (m + 1) * L + m*m
    assert step(full, b) == queue_mask | packet
    orbit = set()
    x = packet
    for _ in range(L):
        orbit.add(x)
        x = step(x, a)
    assert x == packet and len(orbit) == L
    assert all(x.bit_count() <= 1 or x in orbit for x in rows)

    # Every abstract b-boundary, reachable or not, and every phase of a.
    potential_checks = 0
    simultaneous_replacements = 0
    for T in range(1 << m):
        for c in [0, 1]:
            x = T | (packet if c else 0)
            old = T.bit_count() + c
            for t in range(lcm(m, L)):
                y = step(x, b)
                clocks = y & ~queue_mask
                assert clocks in (0, packet)
                drop = old - ((y & queue_mask).bit_count() + int(bool(clocks)))
                assert drop == int(c == 1 and (t + 1) % L == 0)
                if drop and clocks:
                    simultaneous_replacements += 1
                x = step(x, a)
                potential_checks += 1

    # Constructive mortality, including gcd(m,L)>1.
    x, length, drops, forks = step(full, b), 1, 0, 0
    while x:
        if not (x & ~queue_mask):
            j = (x & -x).bit_length() - 1
            t = (-j) % m
            for _ in range(t):
                x = step(x, a)
            x = step(x, b)
            assert (x & ~queue_mask) == packet
            forks += 1
            length += t + 1
        for _ in range(L - 1):
            x = step(x, a)
        x = step(x, b)
        length += L
        drops += 1
        assert drops <= m + 1
    assert drops == m + 1 and forks <= m
    assert length <= 1 + (m + 1)*L + m*m

    # Reachability in the underlying graph, ignoring labels.
    for j in range(n):
        seen, old_seen = 1 << j, -1
        while seen != old_seen:
            old_seen = seen
            seen |= step(seen, a) | step(seen, b)
        assert seen == full

    def verify_saved_graph(saved):
        assert len(saved) == len(distances)
        mapping = {row[0]: row[1:] for row in saved}
        assert len(mapping) == len(saved) and set(mapping) == set(distances)
        # A local distance certificate: edge inequalities and a predecessor
        # one level lower for each non-root give exact shortest distances.
        predecessors = set()
        assert mapping[full][0] == 0
        for x, (d, ya, yb) in mapping.items():
            assert [ya, yb] == [step(x, a), step(x, b)]
            assert d == distances[x]
            for y in [ya, yb]:
                assert mapping[y][0] <= d + 1
                if mapping[y][0] == d + 1:
                    predecessors.add(y)
        assert predecessors == set(mapping) - {full}

    if record is not None:
        assert record['shortest_mortal_length'] == distances[0]
        assert set(record['complete_row_closure_masks']) == set(rows)
        verify_saved_graph(record['complete_global_bfs'])
        for word_key in ['shortest_word', 'constructive_word']:
            x = full
            for letter in record[word_key]:
                assert letter in 'ab'
                x = step(x, a if letter == 'a' else b)
            assert x == 0
        assert len(record['shortest_word']) == distances[0]
    if certificate is not None:
        assert certificate['a'] == a and certificate['b'] == b
        assert certificate['packet'] == packet
        assert set(certificate['singleton_masks']) == set(rows)
        verify_saved_graph(certificate['global_bfs'])
    return {'m': m, 'lengths': list(lengths), 'n': n, 'k': k,
            'L': L, 'shortest_mortal_length': distances[0],
            'constructed_length': length, 'row_closure_count': len(rows),
            'global_closure_count': len(distances),
            'potential_checks': potential_checks,
            'simultaneous_replacement_checks': simultaneous_replacements}


def main():
    started = time.monotonic()
    snapshot = json.loads((ROOT/'audit/snapshot.json').read_text())
    actual = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in snapshot['files']}
    assert actual == snapshot['files']
    digest = sha256(json.dumps(actual, sort_keys=True, separators=(',', ':'),
                               ensure_ascii=False).encode()).hexdigest()
    assert digest == snapshot['digest']
    # Preserve previous active review bytes without consulting their verdicts.
    prior_dir = OUT/'prior-active-audits'
    prior_dir.mkdir(exist_ok=True)
    archived = {}
    for name in ['math.md', 'math.json', 'innovation.json']:
        source, dest = ROOT/'audit'/name, prior_dir/name
        if source.exists() and not dest.exists():
            shutil.copyfile(source, dest)
        if dest.exists():
            archived[str(dest.relative_to(ROOT))] = sha256(dest.read_bytes()).hexdigest()
    (OUT/'progress.json').write_text(json.dumps({
        'job_id': JOB, 'snapshot_digest': digest, 'frozen_integrity': 'pass',
        'status': 'independent finite verification in progress',
        'prior_reviews_preserved_without_using_their_contents': archived}, indent=2)+'\n')

    records = json.loads((ROOT/'evidence/research-check-results.json').read_text())
    replay = []
    for section in ['frozen_cases', 'boundary_cases']:
        for r in records[section]:
            cert = None
            if section == 'frozen_cases':
                name = 'queue-clock-m'+str(r['m'])+'-'+'-'.join(map(str,r['lengths']))+'.json'
                cert = json.loads((ROOT/'intake/root-queue-clock/queue-clock-certificates'/name).read_text())
            replay.append(check_case(r['m'], r['lengths'], record=r, certificate=cert))

    held_out = []
    old_parameters = {(r['m'], tuple(r['lengths'])) for r in replay}
    for m in range(2, 8):
        for lengths in [(2,), (2, 2), (3, 6), (2, 3), (2, 2, 4),
                        (2, 3, 5), (2, 3, 4, 5), (2, 2, 3, 3, 4)]:
            if (m, lengths) not in old_parameters:
                held_out.append(check_case(m, lengths))
    arithmetic = 0
    for k in range(2, 21):
        K, A = factorial(k), 1 + k*(k+1)//2
        N = 2*k + 2*A*K
        for n in [N + j for j in range(2*A*K if k < 5 else 31)] + [7*N-1, 7*N, 7*N+1]:
            M = K*((n-k)//(A*K))
            lengths = [1+i*M for i in range(1, k+1)]
            m = n-sum(lengths)
            assert m >= M >= 2 and 2*A*M >= n
            assert all(gcd(x,y) == 1 for i,x in enumerate(lengths) for y in lengths[i+1:])
            assert (m+1)*lcm(*lengths)*(2*A)**(k+1) >= K*n**(k+1)
            arithmetic += 1
    output = {'job_id': JOB, 'snapshot_digest': digest,
              'completed_at': datetime.now(timezone.utc).isoformat(),
              'implementation': 'new integer-bitmask verifier; no frozen checker imports',
              'scope_limit': 'finite exact support only; infinite proof separately reconstructed',
              'frozen_replays': replay, 'held_out_cases': held_out,
              'arithmetic_samples': arithmetic,
              'total_potential_checks': sum(r['potential_checks'] for r in replay+held_out),
              'total_simultaneous_replacement_checks': sum(r['simultaneous_replacement_checks'] for r in replay+held_out),
              'preserved_previous_audits': archived,
              'elapsed_seconds': time.monotonic()-started}
    (OUT/'verification.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: output[k] for k in ['job_id','snapshot_digest','arithmetic_samples',
        'total_potential_checks','total_simultaneous_replacement_checks','elapsed_seconds']} |
        {'frozen_replays':len(replay), 'held_out_cases':len(held_out)}))


if __name__ == '__main__':
    main()
