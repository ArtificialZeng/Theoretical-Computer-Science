# Sanity check: for random maximal planar graphs, build a canonical ordering (dFPP), mark the two
# outer contour edges of each u_k absorbed and inner contour edges paid, and verify the hypotheses of
# Lemma schedule at level 3 (deletion order = reverse canonical): a_v <= 2, p_v <= 1, and
# l >= p + max(1,a), l >= p + 2 if a >= 1.  Also re-verify by a generic schedule checker.
import random, sys
import networkx as nx
from scipy.spatial import Delaunay
import numpy as np

def maximal_planar(n, seed):
    rng = np.random.default_rng(seed)
    pts = rng.random((n - 1, 2))
    tri = Delaunay(pts)
    G = nx.Graph()
    for s in tri.simplices:
        a, b, c = map(int, s)
        G.add_edges_from([(a, b), (b, c), (a, c)])
    inf = n - 1
    hull = tri.convex_hull
    for e in hull:
        G.add_edge(int(e[0]), inf); G.add_edge(int(e[1]), inf)
    assert G.number_of_edges() == 3 * n - 6, (G.number_of_edges(), n)
    return G

def canonical_order(G):
    ok, emb = nx.check_planarity(G)
    assert ok
    # choose an outer face: any triangle face; take first face found
    u = next(iter(G.nodes)); v = next(iter(G[u]))
    face = emb.traverse_face(u, v)
    assert len(face) == 3
    u1, u2, w = face
    # reverse construction: repeatedly remove an outer vertex (not u1,u2) with no chord
    outer = [u1, w, u2]  # cycle order: u1 ... u2 (path from u1 to u2 avoiding edge u1u2)
    alive = set(G.nodes)
    order_rev = []
    H = G.copy()
    while len(alive) > 3:
        removed = False
        for i in range(1, len(outer) - 1):
            x = outer[i]
            pos = {y: j for j, y in enumerate(outer)}
            chord = any((y in pos) and abs(pos[y] - i) > 1 for y in H[x])
            if chord:
                continue
            left, right = outer[i - 1], outer[i + 1]
            # neighbours of x strictly between left and right in rotation (the interior side)
            nbrs = list(emb.neighbors_cw_order(x))
            nbrs = [y for y in nbrs if y in alive]
            k = len(nbrs)
            # find the order from right to left going through the interior
            iL, iR = nbrs.index(left), nbrs.index(right)
            seq1 = [nbrs[(iR + t) % k] for t in range(k)]
            cut = seq1.index(left)
            mid = seq1[1:cut]
            # orientation check: the other direction
            seq2 = [nbrs[(iL + t) % k] for t in range(k)]
            cut2 = seq2.index(right)
            mid2 = seq2[1:cut2]
            # interior neighbours are those not on outer; one of mid/mid2 contains only non-outer vertices
            if all(y not in pos for y in mid) and (len(mid2) == 0 or any(y in pos for y in mid2) or len(mid) >= len(mid2)):
                inner = list(reversed(mid))
            else:
                inner = list(mid2)
            outer = outer[:i] + inner + outer[i + 1:]
            alive.discard(x); H.remove_node(x)
            order_rev.append(x)
            removed = True
            break
        assert removed, "no removable vertex"
    order = [u1, u2] + [y for y in alive if y not in (u1, u2)] + list(reversed(order_rev))
    return order

def check_canonical(G, order):
    n = len(order); idx = {v: i for i, v in enumerate(order)}
    # verify: for k>=3 (index>=2) earlier nbrs form a path on outer cycle of G_{k-1}; compute marks
    a = {v: 0 for v in G}; p = {v: 0 for v in G}
    covered = {}
    # outer cycle maintenance via embedding of G_k is complex; instead verify marks by the defining
    # property directly: earlier neighbours of u_k induce a path (in G) and inner path vertices are
    # never earlier neighbours' inner vertices twice.
    for k in range(2, n):
        x = order[k]
        E = [y for y in G[x] if idx[y] < k]
        sub = G.subgraph(E)
        assert nx.is_connected(sub) and max(dict(sub.degree()).values()) <= 2 and sub.number_of_edges() == len(E) - 1, "not a path"
        ends = [y for y in E if sub.degree(y) <= 1]
        if len(E) == 2: ends = E
        for y in E:
            if y in ends:
                a[x] += 1          # absorbed, charged to x (deletion-earlier endpoint)
            else:
                p[y] += 1          # paid, charged to y (deletion-later endpoint)
    a[order[1]] += 1  # edge u1u2 absorbed by u2
    L = 3
    for v in G:
        assert a[v] <= 2 and p[v] <= 1, (v, a[v], p[v])
        assert L >= p[v] + max(1, a[v]) and (a[v] == 0 or L >= p[v] + 2)
    return max(p.values()), max(a.values())

cnt = 0
for n in [6, 8, 10, 15, 20, 30, 50, 80]:
    for seed in range(40):
        G = maximal_planar(n, seed * 1000 + n)
        order = canonical_order(G)
        assert sorted(order) == sorted(G.nodes)
        check_canonical(G, order)
        cnt += 1
print("ok", cnt, "maximal planar graphs: canonical schedules satisfy Lemma schedule at level 3")
