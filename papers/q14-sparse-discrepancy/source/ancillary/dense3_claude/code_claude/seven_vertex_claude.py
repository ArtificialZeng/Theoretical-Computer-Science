#!/usr/bin/env python3
"""Which graphs on 7 vertices are 2-good by cheap deletions (Lemma lem:cheap of the paper) ending in the
proved bases?  Bases (all levels >= 1, level-1 vertices independent):
  - at most 5 vertices (Theorem thm:leveled5, plus Thm H(b) of the paper for all levels >= 2);
  - 6 vertices with at most two level-1 vertices (Theorem thm:leveled5 / thm:six).
Moves: delete h with J subset of N(h), |J| <= l_h, l_h >= 2 if J nonempty; every vertex of N(h)\\J needs
level >= 2 and drops by one.  (Raising levels and passing to subgraphs preserve goodness, so it is
enough to try, for each h, all J.)  Output: the edge-maximal 7-vertex graphs NOT resolved.
usage: python3 -I seven_vertex_claude.py"""
import itertools
from functools import lru_cache

def canon(n, edges, levels):
    best = None
    for p in itertools.permutations(range(n)):
        e = tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in edges))
        l = tuple(levels[p.index(i)] for i in range(n))
        key = (l, e)
        if best is None or key < best: best = key
    return best

def base_ok(n, edges, levels):
    if min(levels, default=2) < 1: return False
    ones = [v for v in range(n) if levels[v] == 1]
    E = set(edges)
    if any((a, b) in E or (b, a) in E for a, b in itertools.combinations(ones, 2)): return False
    if n <= 5: return True
    if n == 6 and len(ones) <= 2: return True
    return False

def good(key):
    levels, edges = key
    n = len(levels)
    if base_ok(n, edges, levels): return True
    if n <= 6 and min(levels) < 1: return False
    adj = {v: set() for v in range(n)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    for h in range(n):
        lh = levels[h]
        if lh < 1: continue
        N = sorted(adj[h])
        maxJ = min(lh, len(N)) if lh >= 2 else 0
        for r in range(maxJ, -1, -1):
            for J in itertools.combinations(N, r):
                rest = [u for u in N if u not in J]
                if any(levels[u] < 2 for u in rest): continue
                newlev = list(levels)
                for u in rest: newlev[u] -= 1
                keep = [v for v in range(n) if v != h]
                idx = {v: i for i, v in enumerate(keep)}
                ne = [(idx[a], idx[b]) for a, b in edges if a != h and b != h]
                nl = [newlev[v] for v in keep]
                if good((tuple(nl), tuple(ne))): return True
    return False

import numpy as np
n = 7
allpairs = list(itertools.combinations(range(n), 2))
pidx = {p: i for i, p in enumerate(allpairs)}
perms = list(itertools.permutations(range(n)))
Mp = np.zeros((len(allpairs), len(perms)))
for j_, p in enumerate(perms):
    for i, (a, b) in enumerate(allpairs):
        Mp[i, j_] = 2.0 ** pidx[tuple(sorted((p[a], p[b])))]
def canon_fast(nonedge_lists):
    B = np.zeros((len(nonedge_lists), len(allpairs)))
    for t, ne in enumerate(nonedge_lists):
        for e in ne: B[t, pidx[e]] = 1
    return (B @ Mp).min(axis=1).astype(np.int64).tolist()
# enumerate graphs by complement edge sets (non-edges), small complements first; a graph is resolved if good
unresolved = []
seen = set()
for k in range(0, 8):
    combos = list(itertools.combinations(allpairs, k))
    reps = {}
    for s0 in range(0, len(combos), 2000):
        chunk = combos[s0:s0 + 2000]
        for code, ne in zip(canon_fast(chunk), chunk):
            if code not in reps: reps[code] = ne
    for code, ne in reps.items():
        seen.add(code)
        E = [e for e in allpairs if e not in ne]
        if not good((tuple([2] * n), tuple(E))): unresolved.append((k, ne))
print("7-vertex graphs (up to iso) with <= 7 non-edges examined:", len(seen))
# report unresolved graphs that are maximal (no supergraph among the unresolved list is needed: list all)
for k, ne in unresolved:
    print("NOT resolved: K_7 minus", ne)
print("number unresolved:", len(unresolved))
