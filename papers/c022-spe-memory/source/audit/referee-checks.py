"""Fresh finite falsification checks; no imports of the researcher's code.

All mathematical infinite-arena and all-k conclusions rest on the proofs.
The verifier searches each player's deviation graph forward from every
legal-history product state, including states off the prescribed outcome.
"""
from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import json
import random

JOB = "c022-spe-memory-referee-af2ba8807d2f"


def inspect_game(edges, owner, target, players, start, init, update, move):
    # Product stores actual prefix target bits independently of machine memory.
    initial = (start, init, 0)
    todo, reached = deque([initial]), set()
    legal, chosen = {}, {}
    while todo:
        z = todo.popleft()
        if z in reached:
            continue
        reached.add(z)
        v, m, past = z
        after = update(m, v)
        bits = past | target[v]
        legal[z] = tuple((w, after, bits) for w in edges[v])
        chosen[z] = (move(m, v), after, bits)
        assert chosen[z] in legal[z]
        todo.extend(legal[z])
    payoffs = {}
    for z in reached:
        x, seen, bits = z, set(), z[2]
        while x not in seen:
            seen.add(x)
            bits |= target[x[0]]
            x = chosen[x]
        payoffs[z] = bits
    violations = []
    for z in reached:
        for i in range(players):
            if payoffs[z] & (1 << i):
                continue
            todo, seen = [z], set()
            while todo:
                x = todo.pop()
                if x in seen:
                    continue
                seen.add(x)
                if (x[2] | target[x[0]]) & (1 << i):
                    violations.append((z, i))
                    break
                todo.extend(legal[x] if owner[x[0]] == i else (chosen[x],))
    return initial, reached, legal, payoffs, violations


def recompress(edges, owner, target, players, start, original,
               remember_owner=True, use_rank=True, expect_valid=True):
    initial, states, legal, payoff, failures = original
    assert not failures
    labels = {}
    augedges = {}
    for v, memory, past in states:
        x = (v, past | target[v])
        labels.setdefault(x, set()).add(payoff[v, memory, past])
        augedges[x] = tuple((w, x[1] | target[w]) for w in edges[v])
    selected, maximum_rank = {}, 0
    for p in set.union(*labels.values()):
        live = {x for x in labels if p in labels[x]}
        dist = {x: 0 for x in live if x[1] == p}
        frontier = list(dist)
        reverse = {x: [] for x in live}
        for x in live:
            for y in augedges[x]:
                if y in live:
                    reverse[y].append(x)
        queue = deque(frontier)
        while queue:
            y = queue.popleft()
            for x in reverse[y]:
                if x not in dist:
                    dist[x] = dist[y] + 1
                    queue.append(x)
        assert set(dist) == live
        maximum_rank = max(maximum_rank, max(dist.values()))
        for x in live:
            candidates = [y for y in augedges[x] if y in live and
                          (not use_rank or dist[x] == 0 or dist[y] == dist[x]-1)]
            assert candidates
            selected[x, p] = candidates[0][0]
    for x, ps in labels.items():
        i = owner[x[0]]
        for p in ps:
            assert x[1] & ~p == 0
            for y in augedges[x]:
                assert any((q >> i & 1) <= (p >> i & 1) for q in labels[y])
    initial_p = payoff[initial]
    def normalize(m, v):
        past, incoming, previous_owner = m
        x = (v, past | target[v])
        if incoming in labels[x]:
            p = incoming
        else:
            p = min(labels[x], key=lambda q: (q >> previous_owner & 1, q))
        return x, p
    def update(m, v):
        x, p = normalize(m, v)
        return (x[1], p, owner[v] if remember_owner else 0)
    def move(m, v):
        x, p = normalize(m, v)
        return selected[x, p]
    compressed = inspect_game(edges, owner, target, players, start,
                              (0, initial_p, 0), update, move)
    if not expect_valid:
        broken_promises = sum(p != normalize(z[1], z[0])[1]
                              for z, p in compressed[3].items())
        assert compressed[-1] or broken_promises
        return {'profitable_deviation_positions':len(compressed[-1]),
                'unfulfilled_promise_positions':broken_promises}
    assert not compressed[-1]
    assert compressed[3][compressed[0]] == initial_p
    for z, p in compressed[3].items():
        assert p == normalize(z[1], z[0])[1]
    return len(states), len(compressed[1]), maximum_rank, any(
        len(ps) > 1 for ps in labels.values())


def negative_controls():
    edges = {0:(1,2),1:(1,3),2:(2,3),3:(4,5),4:(4,),5:(5,)}
    owner = dict(enumerate((2,0,1,2,2,2)))
    target = dict(enumerate((0,0,0,0,1,2)))
    def update(m,v):
        return owner[v]
    def move(m,v):
        if v == 3:
            return 5 if m == 0 else 4
        return edges[v][0]
    original = inspect_game(edges,owner,target,3,0,2,update,move)
    assert not original[-1] and original[3][original[0]] == 0
    recompress(edges,owner,target,3,0,original)
    owner_free = recompress(edges,owner,target,3,0,original,
                            remember_owner=False,expect_valid=False)
    edges,owner,target = {0:(0,1),1:(1,)},{0:0,1:0},{0:0,1:1}
    original = inspect_game(edges,owner,target,1,0,0,
                            lambda m,v:0,lambda m,v:1)
    assert not original[-1]
    rank_free = recompress(edges,owner,target,1,0,original,
                           use_rank=False,expect_valid=False)
    return {'previous_owner_omission_rejected':owner_free,
            'progress_omission_rejected':rank_free}


def upper_checks():
    counts = dict(original_profiles=0, original_SPEs=0, compressed_profiles=0,
                  original_positions=0, compressed_positions=0,
                  max_rank=0, cases_with_multiple_labels=0)
    def test(edges, owner, target, n, memory, update, move):
        counts['original_profiles'] += 1
        result = inspect_game(edges, owner, target, n, 0, memory, update, move)
        if result[-1]:
            return
        counts['original_SPEs'] += 1
        before, after, rank, multi = recompress(edges, owner, target, n, 0, result)
        counts['compressed_profiles'] += 1
        counts['original_positions'] += before
        counts['compressed_positions'] += after
        counts['max_rank'] = max(counts['max_rank'], rank)
        counts['cases_with_multiple_labels'] += multi
    choices = ((0,), (1,), (0,1))
    for adjacency in product(choices, repeat=2):
        edges = dict(enumerate(adjacency))
        for owners in product(range(2), repeat=2):
            owner = dict(enumerate(owners))
            for targets in product(range(4), repeat=2):
                target = dict(enumerate(targets))
                for policy in product(*adjacency):
                    test(edges, owner, target, 2, 0, lambda m,v: 0,
                         lambda m,v: policy[v])
    exhaustive = dict(counts)
    rng = random.Random(22112026)
    # Actual history-dependent original machines; labels are extracted from
    # their verified continuations, rather than produced by label elimination.
    for _ in range(2000):
        n, size, qsize = rng.randint(1,3), rng.randint(2,5), rng.randint(1,3)
        edges = {v: tuple(w for w in range(size) if rng.randrange(3) == 0)
                 for v in range(size)}
        edges = {v: ws or (rng.randrange(size),) for v,ws in edges.items()}
        owner = {v: rng.randrange(n) for v in edges}
        target = {v: rng.randrange(1 << n) if rng.randrange(3) == 0 else 0
                  for v in edges}
        upd = {(m,v): rng.randrange(qsize) for m in range(qsize) for v in edges}
        policy = {(m,v): rng.choice(edges[v]) for m in range(qsize) for v in edges}
        test(edges, owner, target, n, 0, lambda m,v: upd[m,v],
             lambda m,v: policy[m,v])
    return {'exhaustive_two_vertex_positional_inputs': exhaustive,
            'additional_seeded_arbitrary_machine_inputs': 2000,
            'seed': 22112026, 'total': counts}


def lower_family(k):
    edges, owner, target = {}, {}, {}
    for p, quota, player in [('a', k//2, 0), ('e', k-k//2, 1)]:
        for index in range(k):
            for count in range(index+1):
                if not count <= quota <= count+k-index:
                    continue
                v = (p,index,count)
                legal = []
                for take in range(2):
                    if not count+take <= quota <= count+take+k-index-1:
                        continue
                    marker = ('mark',p,index,count,take)
                    legal.append(marker)
                    endpoint = (p,index+1,count+take) if index+1 < k else (
                        ('e',0,0) if p == 'a' else ('check',0))
                    edges[marker] = (endpoint,)
                    owner[marker] = player
                    target[marker] = (1 << (index+2)) if take else 0
                edges[v], owner[v], target[v] = tuple(legal), player, 0
    for index in range(k):
        v = ('check',index)
        edges[v] = ((('check',index+1) if index+1 < k else ('end','e')),
                    ('end','a'))
        owner[v], target[v] = index+2, 0
    edges[('end','a')] = (('end','a'),)
    edges[('end','e')] = (('end','e'),)
    owner[('end','a')] = owner[('end','e')] = 0
    target[('end','a')] = 1 | (((1 << k)-1) << 2)
    target[('end','e')] = 2
    return edges,owner,target


def lower_checks():
    results = []
    for k in range(1,7):
        edges,owner,target = lower_family(k)
        def update(m,v):
            selected,past = m
            if v[0] == 'mark' and v[1] == 'a' and v[4]:
                selected |= 1 << v[2]
            return selected,past | target[v]
        def move(m,v):
            selected,past = m
            if v[0] == 'e':
                intended = int(not(selected >> v[1] & 1))
                return next((w for w in edges[v] if w[4] == intended),edges[v][0])
            if v[0] == 'check':
                return edges[v][0 if past >> owner[v] & 1 else 1]
            return edges[v][0]
        res = inspect_game(edges,owner,target,k+2,('a',0,0),(0,0),update,move)
        assert not res[-1] and res[3][res[0]] == (1 << (k+2))-2
        assert max(map(len,edges.values())) <= 2
        # Fresh direct enumeration of subset/complement necessity.
        selections = [s for s in range(1 << k) if s.bit_count() == k//2]
        full = (1 << k)-1
        replies = [s for s in range(1 << k) if s.bit_count() == k-k//2]
        for s in selections:
            assert [u for u in replies if s | u == full] == [full ^ s]
        results.append({'k':k,'vertices':len(edges),'all_history_positions':len(res[1]),
                        'canonical_profile_is_SPE':True,
                        'distinct_required_responses':len(selections)})
    return results


if __name__ == '__main__':
    result = {'job_id':JOB,'arithmetic':'exact finite integer/graph operations',
              'method':'fresh implementation; independent forward deviation searches; no imports of proposer code',
              'upper':upper_checks(),'lower':lower_checks(),
              'negative_controls':negative_controls(),
              'limitations':'Finite falsification checks only; infinite-arena upper bound and all-k lower bound are verified by the separate mathematical argument.'}
    result['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
