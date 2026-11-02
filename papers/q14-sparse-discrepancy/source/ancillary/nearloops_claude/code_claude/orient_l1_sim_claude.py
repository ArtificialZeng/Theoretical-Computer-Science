#!/usr/bin/env python3
"""Orientation schedules with level-1 cheap neighbours allowed (dense2_claude): any ordering, levels
k+1 (k = max in-degree); assert: cheap neighbours level >= 1, payers level >= 2, |J| <= l_h,
l_h >= 2 if J nonempty, l_h >= 1.  Also wheels at level 2 with the explicit schedule."""
import random, sys, os, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    from schedule_sim_claude import min_indeg_orientation
def simulate_l1(n, E, order, owner, levels):
    lev = dict(levels); alive = set(range(n)); nb = {v: set() for v in range(n)}
    for (a, b) in E: nb[a].add(b); nb[b].add(a)
    own = {frozenset(e): owner[i] for i, e in enumerate(E)}
    for h in order:
        rem = [r for r in nb[h] if r in alive]
        J = [r for r in rem if own[frozenset((h, r))] == h]
        pay = [r for r in rem if own[frozenset((h, r))] == r]
        assert all(lev[r] >= 1 for r in J) and all(lev[r] >= 2 for r in pay)
        assert len(J) <= lev[h] and lev[h] >= 1 and (not J or lev[h] >= 2)
        for r in pay: lev[r] -= 1
        alive.remove(h)
rng = random.Random(5); cnt = 0
for trial in range(800):
    n = rng.randint(3, 16); p = rng.random()
    E = [(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p]
    if not E: continue
    k, owner = min_indeg_orientation(n, E)
    for t in range(4):
        order = list(range(n)); rng.shuffle(order)
        simulate_l1(n, E, order, owner, {v: k + 1 for v in range(n)}); cnt += 1
# wheels: hub = n, rim 0..n-1; order r1..r_{n-1}, r0, hub
wcnt = 0
for n in range(3, 40):
    E = [(i, (i + 1) % n) for i in range(n)] + [(i, n) for i in range(n)]
    E = [tuple(sorted(e)) for e in E]
    order = list(range(1, n)) + [0, n]
    pos = {v: i for i, v in enumerate(order)}
    owner = []
    for (a, b) in E:
        if {a, b} == {0, 1}: owner.append(0)          # paid by r0
        elif {a, b} == {0, n}: owner.append(n)        # paid by hub
        else: owner.append(a if pos[a] < pos[b] else b)   # absorbed by earlier endpoint
    simulate_l1(n + 1, E, order, owner, {v: 2 for v in range(n + 1)}); wcnt += 1
print("level-1-cheap schedules: %d random (levels k+1, any order) and %d wheels W_3..W_39 at level 2: all hypotheses hold" % (cnt, wcnt))
