"""Checks for Theorem thm:mad (insert v3).
For a graph H and integer k >= 1 with |E(H')| < k|V(H')| for all nonempty subgraphs:
  * find an orientation with all in-degrees <= k (max-flow; exists by Hakimi),
  * build the ordering from the end as in the proof (choose u in R with in-degree < k or an
    in-neighbour outside R); assert it never gets stuck,
  * mark edges (absorbed iff oriented towards the earlier endpoint), check
    p_v + a_v = indeg(v), the hypotheses of lem:schedule (v3) with l = k+1, and simulate the
    proof of lem:schedule (all hypotheses of lem:cheap along the run).
Graphs: random graphs (n <= 11, k = least admissible integer, computed exactly), random planar
triangulations (stacked + random flips, n <= 60, k = 3), the icosahedron (5-regular, k = 3),
random graphs of max degree Delta (k = floor(Delta/2)+1).
Sanity: K_7 with k = 3 (|E| = 3|V|): the greedy must get stuck.
Run: python3 -I mad_ref.py
"""
import sys, os, random, time
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_mad.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def orient(n, edges, k):
    """max-flow: source->edge (1), edge->endpoint (1), vertex->sink (k). Returns heads or None."""
    m = len(edges)
    S, T = 0, 1
    E0 = 2
    V0 = 2 + m
    N = 2 + m + n
    graph = [[] for _ in range(N)]

    def add(u, v, c):
        graph[u].append([v, c, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])
    for i in range(m):
        add(S, E0 + i, 1)
        add(E0 + i, V0 + edges[i][0], 1)
        add(E0 + i, V0 + edges[i][1], 1)
    for v in range(n):
        add(V0 + v, T, k)
    flow = 0
    while True:
        prev = [None] * N
        prev[S] = (S, -1)
        dq = deque([S])
        while dq and prev[T] is None:
            u = dq.popleft()
            for idx, (v, c, r) in enumerate(graph[u]):
                if c > 0 and prev[v] is None:
                    prev[v] = (u, idx)
                    dq.append(v)
        if prev[T] is None:
            break
        v = T
        while v != S:
            u, idx = prev[v]
            graph[u][idx][1] -= 1
            rv = graph[u][idx][2]
            graph[v][rv][1] += 1
            v = u
        flow += 1
    if flow < m:
        return None
    heads = []
    for i in range(m):
        h = None
        for v, c, r in graph[E0 + i]:
            if V0 <= v < V0 + n and c == 0:
                h = v - V0
        heads.append(h)
    return heads


def greedy_order(n, edges, heads, k):
    indeg = [0] * n
    inn = [[] for _ in range(n)]
    for (a, b), h in zip(edges, heads):
        t = a if h == b else b
        indeg[h] += 1
        inn[h].append(t)
    R = set(range(n))
    rev = []
    while R:
        cand = [u for u in R if indeg[u] < k or any(w not in R for w in inn[u])]
        if not cand:
            return None, indeg
        u = random.choice(cand)
        rev.append(u)
        R.remove(u)
    return rev[::-1], indeg


def check_schedule(n, edges, heads, order, k):
    pos = {v: i for i, v in enumerate(order)}
    a = [0] * n
    p = [0] * n
    indeg = [0] * n
    mark = []
    incA = [False] * n
    for (u, v), h in zip(edges, heads):
        t = u if h == v else v
        indeg[h] += 1
        e, l = (u, v) if pos[u] < pos[v] else (v, u)
        if h == e:          # oriented towards earlier endpoint
            mark.append("A")
            a[e] += 1
            incA[u] = incA[v] = True
        else:
            mark.append("P")
            p[l] += 1
    L = k + 1
    ok_sum = all(p[v] + a[v] == indeg[v] for v in range(n))
    ok_hyp = all(L >= p[v] + max(1, a[v]) and (not incA[v] or L >= p[v] + 2) for v in range(n))
    # simulate
    lev = [L] * n
    alive = set(range(n))
    Emap = {frozenset(e): m for e, m in zip(edges, mark)}
    ok_sim = True
    for h in order:
        nb = [u for u in alive if u != h and frozenset((h, u)) in Emap]
        J = [u for u in nb if Emap[frozenset((h, u))] == "A"]
        if any(lev[u] < 2 for u in nb) or len(J) > lev[h] or (J and lev[h] < 2) or lev[h] < 1:
            ok_sim = False
            break
        for u in nb:
            if u not in J:
                lev[u] -= 1
        alive.remove(h)
    return ok_sum, ok_hyp, ok_sim


def least_k(n, edges):
    k = 1
    while True:
        ok = True
        for X in range(1, 1 << n):
            sz = bin(X).count("1")
            e = sum(1 for (u, v) in edges if X >> u & 1 and X >> v & 1)
            if e >= k * sz:
                ok = False
                break
        if ok:
            return k
        k += 1


def degeneracy(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    alive = set(range(n))
    d = 0
    while alive:
        v = min(alive, key=lambda x: len(adj[x] & alive))
        d = max(d, len(adj[v] & alive))
        alive.remove(v)
    return d


def random_triangulation(n, rng, flips):
    faces = [(0, 1, 2), (0, 2, 1)]   # two faces of a triangle on the sphere
    for v in range(3, n):
        i = rng.randrange(len(faces))
        a, b, c = faces.pop(i)
        faces += [(a, b, v), (b, c, v), (c, a, v)]
    def edges_of(fs):
        E = set()
        for a, b, c in fs:
            for x, y in ((a, b), (b, c), (c, a)):
                E.add(frozenset((x, y)))
        return E
    for _ in range(flips):
        E = edges_of(faces)
        e = rng.choice(list(E))
        x, y = tuple(e)
        inc = [i for i, f in enumerate(faces) if x in f and y in f]
        if len(inc) != 2:
            continue
        f1, f2 = faces[inc[0]], faces[inc[1]]
        c = [z for z in f1 if z not in (x, y)][0]
        d = [z for z in f2 if z not in (x, y)][0]
        if c == d or frozenset((c, d)) in E:
            continue
        for i in sorted(inc, reverse=True):
            faces.pop(i)
        faces += [(c, d, x), (d, c, y)]
    E = edges_of(faces)
    return [tuple(sorted(e)) for e in E]


def icosahedron():
    # vertices 0 (top), 1..5 upper ring, 6..10 lower ring, 11 bottom
    E = set()
    for i in range(5):
        u = 1 + i
        u2 = 1 + (i + 1) % 5
        l = 6 + i
        l2 = 6 + (i + 1) % 5
        E |= {(0, u), (u, u2), (u, l), (u, l2), (l, l2), (l, 11)}
    return [tuple(sorted(e)) for e in E]


def run_case(n, edges, k, stats, key):
    heads = orient(n, edges, k)
    st = stats.setdefault(key, [0, 0, 0, 0, 0])
    st[0] += 1
    if heads is None:
        st[1] += 1
        return
    order, indeg = greedy_order(n, edges, heads, k)
    if order is None:
        st[2] += 1
        return
    ok_sum, ok_hyp, ok_sim = check_schedule(n, edges, heads, order, k)
    if not (ok_sum and ok_hyp):
        st[3] += 1
    if not ok_sim:
        st[4] += 1


def main():
    rng = random.Random(23)
    random.seed(29)
    stats = {}
    t0 = time.time()
    for _ in range(3000):
        n = rng.randint(1, 11)
        edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < rng.uniform(0.1, 0.95)]
        k = least_k(n, edges)
        run_case(n, edges, k, stats, "random n<=11, least k")
    tri_degs = {}
    for _ in range(400):
        n = rng.randint(4, 60)
        edges = random_triangulation(n, rng, rng.randint(0, 6 * n))
        assert len(edges) == 3 * n - 6
        d = degeneracy(n, edges)
        tri_degs[d] = tri_degs.get(d, 0) + 1
        run_case(n, edges, 3, stats, "planar triangulations, k=3")
    ico = icosahedron()
    assert len(ico) == 30
    for _ in range(50):
        run_case(12, ico, 3, stats, "icosahedron (dgn 5), k=3")
    for _ in range(1000):
        n = rng.randint(2, 30)
        Delta = rng.randint(2, 9)
        deg = [0] * n
        edges = []
        pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
        rng.shuffle(pairs)
        for u, v in pairs:
            if deg[u] < Delta and deg[v] < Delta and rng.random() < 0.7:
                edges.append((u, v))
                deg[u] += 1
                deg[v] += 1
        run_case(n, edges, Delta // 2 + 1, stats, "max degree Delta, k=floor(Delta/2)+1")
    log("case: [instances, no orientation, greedy stuck, p+a!=indeg or schedule hypothesis fails, "
        "proof simulation fails]  (all but the first must be 0)")
    for k_, v in stats.items():
        log(f"  {k_}: {v}")
    log(f"  degeneracies of the random triangulations: {dict(sorted(tri_degs.items()))}")
    # sanity: K_7, k = 3 -> |E| = 21 = 3*7, the greedy gets stuck
    n = 7
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    heads = orient(n, edges, 3)
    order, indeg = greedy_order(n, edges, heads, 3)
    log(f"sanity K_7 with k=3: orientation found: {heads is not None}, in-degrees {sorted(indeg)}, "
        f"greedy stuck: {order is None} (expected True)")
    log(f"time {time.time()-t0:.1f}s")


main()
out.close()
