#!/usr/bin/env python3
"""Exact finite checks of the promise-reset SPE construction.

No third-party packages. All histories are explored through the common
VERTEX-update memory machine; deviation reachability holds opponents fixed.
The finite checks supplement, and do not prove, the arbitrary-arena theorem.
"""
from collections import deque
from itertools import product
from pathlib import Path
import argparse
import json
import random
import time


def augmented(adj, targets, start=0):
    x0 = (start, targets[start])
    succ, queue = {}, deque([x0])
    while queue:
        x = queue.popleft()
        if x in succ:
            continue
        v, W = x
        succ[x] = tuple((w, W | targets[w]) for w in adj[v])
        queue.extend(y for y in succ[x] if y not in succ)
    return x0, succ


def path_filter(succ, P, n):
    """Keep labels with an infinite labelled path completing their targets.

    First remove nodes with no infinite continuation in the induced labelled
    subgraph; on a finite graph this is sink pruning. Then reverse reach from
    nodes whose visited bitset already equals the payoff label.
    """
    out = {x: set() for x in succ}
    for p in range(1 << n):
        live = {x for x in succ if p in P[x]}
        while True:
            new = {x for x in live if any(y in live for y in succ[x])}
            if new == live:
                break
            live = new
        good = {x for x in live if x[1] == p}
        while True:
            new = good | {x for x in live if any(y in good for y in succ[x])}
            if new == good:
                break
            good = new
        for x in good:
            out[x].add(p)
    return out


def label_fixed_point(adj, owners, targets, n):
    x0, succ = augmented(adj, targets)
    P = {x: {p for p in range(1 << n) if x[1] & ~p == 0} for x in succ}
    P = path_filter(succ, P, n)
    iterations = 0
    while True:
        iterations += 1
        Q = {}
        for x in succ:
            i = owners[x[0]]
            Q[x] = {p for p in P[x]
                    if p & (1 << i) or all(any(not(q & (1 << i)) for q in P[y])
                                          for y in succ[x])}
        Q = path_filter(succ, Q, n)
        if Q == P:
            break
        P = Q
    assert all(P[x] for x in succ), ('empty labels', adj, owners, targets)
    return x0, succ, P, iterations


def selectors(succ, P, n, use_rank=True):
    f, distances = {}, {}
    for p in range(1 << n):
        live = {x for x in succ if p in P[x]}
        if not live:
            continue
        d = {x: 0 for x in live if x[1] == p}
        while len(d) < len(live):
            new = {x: 1 + min(d[y] for y in succ[x] if y in d)
                   for x in live if x not in d and any(y in d for y in succ[x])}
            assert new, ('missing finite progress witness', p, live, d)
            d.update(new)
        for x in live:
            if use_rank and d[x] > 0:
                ys = [y for y in succ[x] if y in d and d[y] == d[x] - 1]
            else:
                ys = [y for y in succ[x] if y in live]
            assert ys
            f[x, p] = min(ys)[0]
            distances[x, p] = d[x]
    return f, distances


def construct(adj, owners, targets, n, P, succ, initial_p,
              remember_owner=True, use_rank=True):
    f, distances = selectors(succ, P, n, use_rank=use_rank)
    m0 = (0, initial_p, 0)

    def normalize(m, v):
        W, p, j = m
        x = (v, W | targets[v])
        assert x in P and P[x]
        r = p if p in P[x] else min(P[x], key=lambda q: (bool(q & (1 << j)), q))
        assert x[1] & ~r == 0
        return x, r

    def update(m, v):
        x, r = normalize(m, v)
        return (x[1], r, owners[v] if remember_owner else 0)

    def move(m, v):
        x, r = normalize(m, v)
        return f[x, r]

    return m0, update, move, normalize, distances


def verify(adj, owners, targets, n, machine, expected_p):
    """Independent product reachability and best-response checks.

    next/update are called using the same incoming memory, then every legal
    successor is explored. This includes histories inconsistent with profile.
    For each i, reverse reachability with all i-edges and only the prescribed
    opponent edge computes exactly where any unilateral deviation can reach Ti.
    """
    m0, update, move, normalize, _ = machine
    start = (0, m0)
    nodes, queue, edges, prescribed = set(), deque([start]), {}, {}
    while queue:
        z = queue.popleft()
        if z in nodes:
            continue
        nodes.add(z)
        v, m = z
        m1 = update(m, v)
        edges[z] = tuple((w, m1) for w in adj[v])
        prescribed[z] = (move(m, v), m1)
        assert prescribed[z] in edges[z]
        queue.extend(y for y in edges[z] if y not in nodes)
    actual = {}
    for z in nodes:
        seen, y, bits = set(), z, z[1][0]
        while y not in seen:
            seen.add(y)
            v, m = y
            bits |= targets[v]
            y = prescribed[y]
        actual[z] = bits
        _, promised = normalize(z[1], z[0])
        assert bits == promised, ('promise not realized', z, bits, promised)
    assert actual[start] == expected_p
    for i in range(n):
        reverse = {z: [] for z in nodes}
        for z in nodes:
            successors = edges[z] if owners[z[0]] == i else (prescribed[z],)
            for y in successors:
                reverse[y].append(z)
        winning = {z for z in nodes if (z[1][0] | targets[z[0]]) & (1 << i)}
        queue = deque(winning)
        while queue:
            y = queue.popleft()
            for z in reverse[y]:
                if z not in winning:
                    winning.add(z)
                    queue.append(z)
        for z in nodes:
            assert actual[z] & (1 << i) or z not in winning, (
                'profitable deviation after legal history', i, z, actual[z])
    return len(nodes)


def check_game(adj, owners, targets, n):
    x0, succ, P, iterations = label_fixed_point(adj, owners, targets, n)
    # Verify the exact structural hypotheses separately from machine checking.
    for x in succ:
        i = owners[x[0]]
        for p in P[x]:
            assert x[1] & ~p == 0
            for y in succ[x]:
                assert any(bool(q & (1 << i)) <= bool(p & (1 << i)) for q in P[y])
    profiles = product_nodes = max_nodes = max_rank = 0
    for p in sorted(P[x0]):
        machine = construct(adj, owners, targets, n, P, succ, p)
        count = verify(adj, owners, targets, n, machine, p)
        profiles += 1
        product_nodes += count
        max_nodes = max(max_nodes, count)
        max_rank = max(max_rank, max(machine[-1].values(), default=0))
    return dict(profiles=profiles, product_nodes=product_nodes,
                max_product_nodes=max_nodes, max_rank=max_rank,
                max_fixed_point_iterations=iterations)


def expect_rejection(call, phrase):
    try:
        call()
    except AssertionError as exc:
        assert phrase in str(exc), str(exc)
        return str(exc)
    raise AssertionError('negative control unexpectedly passed')


def controls():
    # Merging histories: root->a or b; a is P1, b P2; both can loop or
    # enter common w. P3 at w chooses terminal target of P1 or P2.
    # P3's objective is empty. Promise 000 at both a,b needs DIFFERENT
    # reset payoffs at w. Every legal history, including root->b, is checked.
    adj = ((1, 2), (1, 3), (2, 3), (4, 5), (4,), (5,))
    owners = (2, 0, 1, 2, 2, 2)
    targets = (0, 0, 0, 0, 1, 2)
    n = 3
    x0, succ, P, _ = label_fixed_point(adj, owners, targets, n)
    assert 0 in P[x0] and 0 not in P[3, 0]
    correct = construct(adj, owners, targets, n, P, succ, 0)
    count = verify(adj, owners, targets, n, correct, 0)
    bad = construct(adj, owners, targets, n, P, succ, 0, remember_owner=False)
    owner_rejection = expect_rejection(
        lambda: verify(adj, owners, targets, n, bad, 0), 'profitable deviation')
    # Rank-free local feasibility can postpone a promised Reach target forever.
    a2, o2, t2 = ((0, 1), (1,)), (0, 0), (0, 1)
    x2, s2, p2, _ = label_fixed_point(a2, o2, t2, 1)
    correct2 = construct(a2, o2, t2, 1, p2, s2, 1)
    verify(a2, o2, t2, 1, correct2, 1)
    bad2 = construct(a2, o2, t2, 1, p2, s2, 1, use_rank=False)
    rank_rejection = expect_rejection(
        lambda: verify(a2, o2, t2, 1, bad2, 1), 'promise not realized')
    # A Nash threat is not automatically credible: at off-path b, P2
    # prescribes its losing sink even though it can take its own target.
    # This independent control checks that verifier visits off-profile b.
    a3, o3, t3 = ((1, 2), (1,), (3, 4), (3,), (4,)), (0, 0, 1, 0, 0), (0, 1, 0, 0, 2)
    m0 = (0, 0, 0)
    def upd(m, v): return (m[0] | t3[v], 0, 0)
    def mov(m, v): return (1, 1, 3, 3, 4)[v]
    def norm(m, v):
        W = m[0] | t3[v]
        return (v, W), W | (1 if v in (0, 1) else 0)
    threat = (m0, upd, mov, norm, {})
    threat_rejection = expect_rejection(
        lambda: verify(a3, o3, t3, 2, threat, 1), 'profitable deviation')
    return {'merging_history_correct_product_nodes': count,
            'owner_omission_rejected': owner_rejection,
            'rank_omission_rejected': rank_rejection,
            'off_profile_noncredible_threat_rejected': threat_rejection,
            'merging_game': {'adj': adj, 'owners_zero_based': owners,
                             'target_masks': targets, 'players': n,
                             'initial_payoff_mask': 0}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--random-games', type=int, default=1000)
    parser.add_argument('--output', default='evidence/promise-reset-finite-checks.json')
    args = parser.parse_args()
    started = time.monotonic()
    totals = dict(games=0, profiles=0, product_nodes=0, max_product_nodes=0,
                  max_rank=0, max_fixed_point_iterations=0)
    def add(r):
        totals['games'] += 1
        for k, value in r.items():
            totals[k] = max(totals[k], value) if k.startswith('max_') else totals[k] + value
    negative = controls()
    # Complete labelled two-vertex/two-player game domain, initial vertex 0:
    # every nonempty successor subset, each owner and each target membership.
    successor_sets = ((0,), (1,), (0, 1))
    for adj in product(successor_sets, repeat=2):
        for owners in product(range(2), repeat=2):
            for targets in product(range(4), repeat=2):
                add(check_game(adj, owners, targets, 2))
    exhaustive = dict(totals)
    rng = random.Random(20261102)
    random_domain = set()
    for index in range(args.random_games):
        n = 1 + index % 4
        N = 3 + (index // 4) % 6
        adj = tuple(tuple(w for w in range(N) if rng.randrange(3) == 0) for _ in range(N))
        adj = tuple(row if row else (rng.randrange(N),) for row in adj)
        owners = tuple(rng.randrange(n) for _ in range(N))
        targets = tuple(rng.randrange(1 << n) if rng.randrange(3) == 0 else 0 for _ in range(N))
        add(check_game(adj, owners, targets, n))
        random_domain.add((n, N))
    result = {'job_id': 'c022-spe-memory-research-5979be48ad66',
              'arithmetic': 'exact finite sets and integer bitmasks',
              'exhaustive': {'description': 'all labelled 2-vertex 2-player no-dead-end directed arenas, all ownership and target memberships, initial vertex 0',
                             'expected_games': 3**2 * 2**2 * 4**2, **exhaustive},
              'random': {'seed': 20261102, 'games': args.random_games,
                         'players_vertices': sorted(random_domain)},
              'total': totals, 'negative_controls': negative,
              'all_checks_passed': True,
              'elapsed_seconds': round(time.monotonic()-started, 3),
              'scope_limit': 'Finite structural-label/machine checks only; arbitrary infinite arenas are covered only by the separate mathematical proof.'}
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
