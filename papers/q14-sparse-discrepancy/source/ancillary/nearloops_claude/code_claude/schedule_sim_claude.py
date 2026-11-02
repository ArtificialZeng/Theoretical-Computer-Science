#!/usr/bin/env python3
"""Simulation of the schedule lemma (dense2_claude): ordering + marks absorbed/paid with
p_v + max(2,a_v) <= l_v.  We delete v_1, v_2, ... applying Lemma cheap (J = absorbed later
neighbours, the others pay) and assert its hypotheses at every step.  Orientations of min
max in-degree come from a max-flow (Hakimi); we check the resulting bound k+2."""
import random, itertools, sys

def min_indeg_orientation(n, E):
    """Orientation (owner = head = charged endpoint) minimizing max in-degree, by max-flow."""
    from collections import deque
    m = len(E)
    for k in range(0, n + 1):
        # nodes: 0 source, 1..m edges, m+1..m+n vertices, m+n+1 sink
        N = m + n + 2; s = 0; t = N - 1
        cap = {}
        adj = [[] for _ in range(N)]
        def add(u, v, c):
            if (u, v) not in cap:
                adj[u].append(v); adj[v].append(u); cap[(u, v)] = 0; cap.setdefault((v, u), 0)
            cap[(u, v)] += c
        for i, (a, b) in enumerate(E):
            add(s, 1 + i, 1); add(1 + i, m + 1 + a, 1); add(1 + i, m + 1 + b, 1)
        for v in range(n):
            add(m + 1 + v, t, k)
        flow = 0
        while True:
            par = {s: None}; dq = deque([s])
            while dq and t not in par:
                u = dq.popleft()
                for v in adj[u]:
                    if v not in par and cap[(u, v)] > 0:
                        par[v] = u; dq.append(v)
            if t not in par: break
            v = t
            while par[v] is not None:
                u = par[v]; cap[(u, v)] -= 1; cap[(v, u)] += 1; v = u
            flow += 1
        if flow == m:
            owner = []
            for i, (a, b) in enumerate(E):
                owner.append(a if cap[(1 + i, m + 1 + a)] == 0 else b)
            return k, owner
    raise RuntimeError

def simulate(n, E, order, owner, levels):
    pos = {v: i for i, v in enumerate(order)}
    lev = dict(levels)
    alive = set(range(n))
    nb = {v: set() for v in range(n)}
    for (a, b) in E: nb[a].add(b); nb[b].add(a)
    own = {frozenset(e): owner[i] for i, e in enumerate(E)}
    for h in order:
        rem = [r for r in nb[h] if r in alive and r != h]
        J = [r for r in rem if own[frozenset((h, r))] == h]
        pay = [r for r in rem if own[frozenset((h, r))] == r]
        assert all(lev[r] >= 2 for r in rem), "neighbour below 2"
        assert len(J) <= lev[h], "too many cheap"
        if J: assert lev[h] >= 2
        assert lev[h] >= 1
        for r in pay: lev[r] -= 1
        alive.remove(h)
    return True

rng = random.Random(1)
cnt = 0
for trial in range(400):
    n = rng.randint(4, 14)
    p = rng.random()
    E = [(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p]
    if not E: continue
    k, owner = min_indeg_orientation(n, E)
    # check owner loads
    load = [0] * n
    for o in owner: load[o] += 1
    assert max(load) <= k
    # Hakimi bound check: k == max over subsets ceil(e/v) for small n
    if n <= 10:
        best = 0
        for mask in range(1, 1 << n):
            vs = [v for v in range(n) if mask >> v & 1]
            e = sum(1 for (a, b) in E if mask >> a & 1 and mask >> b & 1)
            best = max(best, -(-e // len(vs)))
        assert best == k, (best, k)
    for t in range(5):
        order = list(range(n)); rng.shuffle(order)
        simulate(n, E, order, owner, {v: k + 2 for v in range(n)})
        cnt += 1
print("schedule lemma: %d simulated schedules (random graphs n<=14, min in-degree orientations, level k+2, random orders): all hypotheses of Lemma cheap hold" % cnt)
