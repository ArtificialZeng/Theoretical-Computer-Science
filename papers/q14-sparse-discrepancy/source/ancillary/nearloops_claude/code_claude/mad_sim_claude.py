#!/usr/bin/env python3
"""Check of the mad-schedule (dense2_claude): if |E(H')| < k|V(H')| for all nonempty H' (k>=2),
take an orientation with in-degree <= k (max-flow), build the ordering greedily from the end
(place a vertex that has in-degree < k or an in-neighbour already placed), and simulate the
deletions with all levels k+1, asserting the hypotheses of Lemma cheap at every step
(cheap neighbours level >= 2, payers level >= 2, |J| <= l_h, l_h >= 2 if J nonempty)."""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schedule_sim_claude import min_indeg_orientation, simulate
from fractions import Fraction

def max_density(n, E):
    best = Fraction(0)
    for mask in range(1, 1 << n):
        vs = bin(mask).count("1")
        e = sum(1 for (a, b) in E if mask >> a & 1 and mask >> b & 1)
        best = max(best, Fraction(e, vs))
    return best

def orient_k(n, E, k):
    k0, owner = min_indeg_orientation(n, E)
    assert k0 <= k
    return owner

def greedy_order(n, E, owner, k):
    indeg = [0] * n
    inn = {v: [] for v in range(n)}
    for i, (a, b) in enumerate(E):
        h = owner[i]; t = a if h == b else b
        indeg[h] += 1; inn[h].append(t)
    R = set(range(n)); placed = set(); rev = []
    while R:
        cand = [u for u in R if indeg[u] < k or any(w in placed for w in inn[u])]
        assert cand, "greedy stuck"
        u = random.choice(cand)
        R.remove(u); placed.add(u); rev.append(u)
    return rev[::-1]

rng = random.Random(3); random.seed(3)
cnt = 0
for trial in range(600):
    n = rng.randint(3, 13)
    p = rng.random()
    E = [(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p]
    if not E: continue
    dens = max_density(n, E)
    k = max(2, int(dens) + 1)           # smallest k >= 2 with density < k
    owner = orient_k(n, E, k)
    for t in range(4):
        order = greedy_order(n, E, owner, k)
        simulate(n, E, order, owner, {v: k + 1 for v in range(n)})
        cnt += 1
print("mad schedule: %d simulated schedules on random graphs (n<=13), level k+1 with k = smallest integer >= 2 exceeding max |E'|/|V'|: all hypotheses of Lemma cheap hold" % cnt)
