#!/usr/bin/env python3
"""Exact finite checks for the subset-memory SPE lower-bound family.

The proof for all k is in evidence/research-pass2/exponential-lower-bound.md.
This program checks explicit finite profiles after ALL legal histories; it
does not exhaust all machines or replace the unbounded lower-bound proof.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import json


def family(k):
    r = k // 2
    adj, owner, targets = {}, {}, {}
    first_e, first_c = ('E', 0, 0), ('C', 0)
    for phase, budget, player in [('A', r, 0), ('E', k-r, 1)]:
        for i in range(k):
            for c in range(i+1):
                if not c <= budget <= c+k-i:
                    continue
                q = (phase, i, c)
                choices = []
                for d in (0, 1):
                    if not c+d <= budget <= c+d+k-i-1:
                        continue
                    z = (phase+'mark', i, c, d)
                    choices.append(z)
                    nxt = ((phase, i+1, c+d) if i+1 < k else
                           (first_e if phase == 'A' else first_c))
                    adj[z], owner[z] = (nxt,), player
                    targets[z] = (1 << (i+2)) if d else 0
                adj[q], owner[q], targets[q] = tuple(choices), player, 0
    for i in range(k):
        q = ('C', i)
        adj[q] = ((('C', i+1) if i+1 < k else ('winE',)), ('winA',))
        owner[q], targets[q] = i+2, 0
    for q, bits in [(('winA',), 1 | (((1 << k)-1) << 2)),
                    (('winE',), 2)]:
        adj[q], owner[q], targets[q] = (q,), 0, bits
    assert all(adj[v] and all(w in adj for w in adj[v]) for v in adj)
    assert max(map(len, adj.values())) <= 2
    return adj, owner, targets


def profile(k, forget=False):
    adj, owner, targets = family(k)

    def update(v, a, seen):
        if v[0] == 'Amark':
            _, i, _, d = v
            a = (a | (1 << i)) if d else (a & ~(1 << i))
        return a, seen | targets[v]

    def move(v, a, seen):
        if v[0] == 'A':
            return adj[v][0]
        if v[0] == 'E':
            wanted = int(not ((0 if forget else a) & (1 << v[1])))
            return next((w for w in adj[v] if w[3] == wanted), adj[v][0])
        if v[0] == 'C':
            return adj[v][0 if seen & (1 << owner[v]) else 1]
        return adj[v][0]

    return adj, owner, targets, update, move


def verify(k, forget=False):
    adj, owner, targets, update, move = profile(k, forget)
    start = (('A', 0, 0), 0, 0)
    edges, prescribed, nodes = {}, {}, set()
    queue = deque([start])
    while queue:
        z = queue.popleft()
        if z in nodes:
            continue
        nodes.add(z)
        v, a, seen = z
        a1, seen1 = update(v, a, seen)
        edges[z] = tuple((w, a1, seen1) for w in adj[v])
        prescribed[z] = (move(v, a, seen), a1, seen1)
        assert prescribed[z] in edges[z]
        queue.extend(w for w in edges[z] if w not in nodes)
    payoff = {}
    for z in nodes:
        current, path, bits = z, set(), z[2]
        while current not in path:
            path.add(current)
            bits |= targets[current[0]]
            current = prescribed[current]
        payoff[z] = bits
    violations, initial_a_deviation = 0, None
    for player in range(k+2):
        reverse = {z: [] for z in nodes}
        for z in nodes:
            choices = edges[z] if owner[z[0]] == player else (prescribed[z],)
            for w in choices:
                reverse[w].append(z)
        distance = {z: 0 for z in nodes if (z[2] | targets[z[0]]) & (1 << player)}
        queue = deque(distance)
        while queue:
            w = queue.popleft()
            for z in reverse[w]:
                if z not in distance:
                    distance[z] = distance[w]+1
                    queue.append(z)
        for z in nodes:
            if z in distance and not payoff[z] & (1 << player):
                violations += 1
        if player == 0 and start in distance and not payoff[start] & 1:
            current, path = start, [start[0]]
            while distance[current]:
                choices = edges[current] if owner[current[0]] == player else (prescribed[current],)
                current = next(w for w in choices if distance.get(w) == distance[current]-1)
                path.append(current[0])
            initial_a_deviation = path
    expected = 2 | (((1 << k)-1) << 2)
    if not forget:
        assert payoff[start] == expected and violations == 0
    return {'k': k, 'players': k+2, 'arena_vertices': len(adj),
            'all_legal_history_product_positions': len(nodes),
            'profitable_deviation_positions': violations,
            'initial_payoff_mask': payoff[start],
            'initial_A_profitable_deviation': initial_a_deviation}


def subset_checks(k):
    subsets = [sum(1 << i for i in W) for W in combinations(range(k), k//2)]
    responses = [sum(1 << i for i in U) for U in combinations(range(k), k-k//2)]
    full = (1 << k)-1
    for W in subsets:
        successful = [U for U in responses if W | U == full]
        assert successful == [full ^ W]
    return {'k': k, 'A_subsets': len(subsets), 'E_response_subsets': len(responses),
            'pairs_exhaustively_checked': len(subsets)*len(responses),
            'distinct_required_memory_states': len(subsets),
            'unique_successful_response_is_complement': True}


def main():
    checks = [verify(k) for k in range(1, 8)]
    control = verify(2, forget=True)
    assert control['profitable_deviation_positions'] > 0
    assert control['initial_A_profitable_deviation'] is not None
    result = {'job_id': 'c022-spe-memory-research-776ae007899c',
              'arithmetic': 'exact integer masks and graph reachability',
              'coverage': 'Explicit canonical SPE profiles for k=1..7, every legal history; no exhaustive enumeration of arbitrary machines.',
              'profile_checks': checks,
              'subset_complement_checks': [subset_checks(k) for k in range(1, 13)],
              'forgetful_E_control': control,
              'unbounded_lower_bound_basis': 'The mathematical injectivity argument, not these finite tests.'}
    out = Path(__file__).resolve().parent.parent/'evidence/research-pass2/subset-memory-checks.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'verified_profiles': len(checks),
                      'all_history_positions': sum(c['all_legal_history_product_positions'] for c in checks),
                      'forgetful_control_rejected': True}))


if __name__ == '__main__':
    main()
