# Level-3 schedules for maximal planar graphs from canonical orderings (reverse removal process).
import networkx as nx, numpy as np
from scipy.spatial import Delaunay

def maximal_planar(n, seed):
    rng = np.random.default_rng(seed)
    pts = rng.random((n - 1, 2)); tri = Delaunay(pts); G = nx.Graph()
    for s in tri.simplices:
        a, b, c = map(int, s); G.add_edges_from([(a, b), (b, c), (a, c)])
    for e in tri.convex_hull:
        G.add_edge(int(e[0]), n - 1); G.add_edge(int(e[1]), n - 1)
    assert G.number_of_edges() == 3 * n - 6
    return G

def schedule_by_removal(G):
    ok, emb = nx.check_planarity(G); assert ok
    u = next(iter(G.nodes)); v = next(iter(G[u]))
    face = emb.traverse_face(u, v); assert len(face) == 3
    u1, u2, w = face
    outer = [u1, w, u2]; alive = set(G.nodes)
    a = {x: 0 for x in G}; p = {x: 0 for x in G}; exposed = set()
    while len(alive) > 3:
        pos = {y: j for j, y in enumerate(outer)}
        for i in range(1, len(outer) - 1):
            x = outer[i]
            if any((y in pos) and abs(pos[y] - i) > 1 for y in G[x] if y in alive):
                continue
            left, right = outer[i-1], outer[i+1]
            nb = [y for y in emb.neighbors_cw_order(x) if y in alive]
            k = len(nb); others = set(nb) - {left, right}
            s0 = nb.index(left); seq = [nb[(s0 + t) % k] for t in range(k)]
            arc1 = seq[1:seq.index(right)]            # from left towards right
            arc2 = seq[seq.index(right) + 1:]         # from right back to left
            if set(arc1) == others:
                inner = arc1
            else:
                assert set(arc2) == others and not arc1, "neighbours not a contour path"
                inner = list(reversed(arc2))
            assert all(y not in pos for y in inner)
            a[x] += 2
            for y in inner:
                assert y not in exposed
                exposed.add(y); p[y] += 1
            outer = outer[:i] + inner + outer[i+1:]
            assert len(set(outer)) == len(outer)
            alive.discard(x)
            break
        else:
            raise AssertionError("no removable vertex")
    rest = [y for y in alive if y not in (u1, u2)]; assert len(rest) == 1
    a[rest[0]] += 2; a[u2] += 1
    for x in G:
        assert a[x] <= 2 and p[x] <= 1
        assert 3 >= p[x] + max(1, a[x]) and (a[x] == 0 or 3 >= p[x] + 2)
    assert sum(a.values()) + sum(p.values()) == G.number_of_edges()

cnt = 0
for n in [5, 6, 8, 10, 15, 20, 30, 50, 80, 120]:
    for seed in range(40):
        schedule_by_removal(maximal_planar(n, seed * 1000 + n)); cnt += 1
# icosahedron and octahedron explicitly
for G in (nx.icosahedral_graph(), nx.octahedral_graph()):
    schedule_by_removal(G); cnt += 1
print("ok", cnt, "maximal planar graphs: every edge marked once, a<=2, p<=1; level-3 schedule valid")
