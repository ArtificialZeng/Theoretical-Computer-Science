#!/usr/bin/env python3
"""Computational sanity check of the congestion-one rounding (Section 3 of main.tex).

For random instances (dense core + pendant terminals, or sparser cores), the script
  1. computes alpha (max uniform product demand alpha/q routable with congestion 1) by LP,
  2. applies the degree reduction of Lemma 3.3,
  3. runs the selection of Section 3.5 (clusters, bad bridges, tags, Steps 1-5),
  4. builds the spreading flows by max-flow (Lemma 3.8) and checks the spreading-system
     conditions (Claim 7 edge-disjointness, receivers <= rho, loads <= 1/2 / 1),
  5. independently checks by LP that the selected pairs are routable with congestion one,
     and that the number selected is >= max(1, alpha|M|/2^15).
This is a diagnostic, not a proof.  Usage: python3 -I verify_rounding.py [seed_start] [num]
"""
import sys, random, itertools, json, math
import networkx as nx
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix

EPS = 1e-7

# ---------------------------------------------------------------- graphs with multiplicities
class MG:
    """Undirected multigraph stored as simple graph with integer 'mult' on edges."""
    def __init__(self):
        self.G = nx.Graph()
    def add_edge(self, u, v, m=1):
        if self.G.has_edge(u, v):
            self.G[u][v]['mult'] += m
        else:
            self.G.add_edge(u, v, mult=m)
    def mult(self, u, v):
        return self.G[u][v]['mult']
    def degree(self, v):
        return sum(d['mult'] for _, _, d in self.G.edges(v, data=True))
    def edges(self):
        return [tuple(sorted((u, v), key=str)) for u, v in self.G.edges()]

def key(u, v):
    return tuple(sorted((u, v), key=str))

def bridges_of(H):
    """Bridges of a multigraph given as nx.Graph with 'mult' (mult>=2 never a bridge)."""
    res = set()
    for u, v in nx.bridges(H):
        if H[u][v].get('mult', 1) == 1:
            res.add(key(u, v))
    return res

# ---------------------------------------------------------------- LP helpers
def max_uniform_product(mg, X):
    """Largest alpha<=1 s.t. demand alpha/q on all pairs of X is routable (source-aggregated)."""
    G = mg.G
    q = len(X)
    nodes = list(G.nodes())
    nid = {v: i for i, v in enumerate(nodes)}
    arcs = []
    for u, v in G.edges():
        arcs.append((u, v)); arcs.append((v, u))
    A = len(arcs)
    nv = q * A + 1  # last var = alpha
    # equality: conservation per source per node
    rows_eq = q * len(nodes)
    Aeq = lil_matrix((rows_eq, nv))
    beq = np.zeros(rows_eq)
    for si, s in enumerate(X):
        base = si * A
        for ai, (u, v) in enumerate(arcs):
            Aeq[si * len(nodes) + nid[u], base + ai] += 1.0   # outflow
            Aeq[si * len(nodes) + nid[v], base + ai] -= 1.0   # inflow
        for w in nodes:
            r = si * len(nodes) + nid[w]
            if w == s:
                Aeq[r, nv - 1] = -(q - 1) / (2.0 * q)
            elif w in Xset_cache(X):
                Aeq[r, nv - 1] = 1.0 / (2.0 * q)
    # capacity
    edges = list(G.edges())
    Aub = lil_matrix((len(edges), nv))
    bub = np.zeros(len(edges))
    eidx = {key(u, v): i for i, (u, v) in enumerate(edges)}
    for si in range(q):
        for ai, (u, v) in enumerate(arcs):
            Aub[eidx[key(u, v)], si * A + ai] = 1.0
    for i, (u, v) in enumerate(edges):
        bub[i] = G[u][v]['mult']
    c = np.zeros(nv); c[-1] = -1.0
    bounds = [(0, None)] * (nv - 1) + [(0, 1.0)]
    res = linprog(c, A_ub=csr_matrix(Aub), b_ub=bub, A_eq=csr_matrix(Aeq), b_eq=beq,
                  bounds=bounds, method='highs')
    assert res.status == 0, res.message
    return res.x[-1]

_xs = {}
def Xset_cache(X):
    k = id(X)
    if k not in _xs:
        _xs[k] = set(X)
    return _xs[k]

def min_congestion_pairs(mg, pairs):
    """Minimum congestion for routing one unit for each pair (LP)."""
    G = mg.G
    nodes = list(G.nodes()); nid = {v: i for i, v in enumerate(nodes)}
    arcs = []
    for u, v in G.edges():
        arcs.append((u, v)); arcs.append((v, u))
    A = len(arcs); P = len(pairs)
    nv = P * A + 1
    Aeq = lil_matrix((P * len(nodes), nv)); beq = np.zeros(P * len(nodes))
    for pi, (s, t) in enumerate(pairs):
        for ai, (u, v) in enumerate(arcs):
            Aeq[pi * len(nodes) + nid[u], pi * A + ai] += 1.0
            Aeq[pi * len(nodes) + nid[v], pi * A + ai] -= 1.0
        beq[pi * len(nodes) + nid[s]] = 1.0
        beq[pi * len(nodes) + nid[t]] = -1.0
    edges = list(G.edges()); eidx = {key(u, v): i for i, (u, v) in enumerate(edges)}
    Aub = lil_matrix((len(edges), nv)); bub = np.zeros(len(edges))
    for pi in range(P):
        for ai, (u, v) in enumerate(arcs):
            Aub[eidx[key(u, v)], pi * A + ai] = 1.0
    for i, (u, v) in enumerate(edges):
        Aub[i, nv - 1] = -G[u][v]['mult']
    c = np.zeros(nv); c[-1] = 1.0
    res = linprog(c, A_ub=csr_matrix(Aub), b_ub=bub, A_eq=csr_matrix(Aeq), b_eq=beq,
                  bounds=[(0, None)] * nv, method='highs')
    assert res.status == 0, res.message
    return res.x[-1]

# ---------------------------------------------------------------- Lemma 3.3 degree reduction
def degree_reduce(mg, X):
    Xs = set(X)
    out = MG()
    # assign each incident edge-copy of a split vertex to a path vertex
    attach = {}  # (v, (u,v) copy index) -> path vertex
    port = {}
    for v in mg.G.nodes():
        if v in Xs or mg.degree(v) <= 3:
            continue
        d = mg.degree(v)
        port[v] = [('split', v, i) for i in range(d)]
        for i in range(d - 1):
            out.add_edge(port[v][i], port[v][i + 1], d)
    used = {v: 0 for v in port}
    def endpoint(v):
        if v in port:
            p = port[v][used[v]]; used[v] += 1; return p
        return v
    for u, v in mg.G.edges():
        for _ in range(mg.mult(u, v)):
            out.add_edge(endpoint(u), endpoint(v), 1)
    for v in mg.G.nodes():
        if v not in port and v not in out.G:
            out.G.add_node(v)
    return out

# ---------------------------------------------------------------- Section 3 selection
def clusters(H, X, rho, W=2.0):
    """Lemma 3.9 on simple underlying graph H (max degree 3), terminals X are leaves."""
    Xs = set(X)
    root = next(v for v in H.nodes() if v not in Xs)
    T = nx.bfs_tree(H, root)
    parent = {v: p for p, v in T.edges()}
    alive = set(H.nodes())
    out = []
    def subtree(x):
        res = []; stack = [x]
        while stack:
            y = stack.pop(); res.append(y)
            stack.extend(c for c in T.successors(y) if c in alive)
        return res
    def wt(S):
        return rho * sum(1 for y in S if y in Xs)
    while wt(alive) >= W - EPS:
        x = root
        while True:
            heavy = [c for c in T.successors(x) if c in alive and wt(subtree(c)) >= W - EPS]
            if heavy:
                x = heavy[0]
            else:
                break
        S = subtree(x)
        assert x not in Xs
        assert wt(S) < 3 * W + EPS
        out.append(set(S))
        alive -= set(S)
        if x == root:
            break
    if alive:
        out[-1] |= alive
    for S in out:
        assert W - EPS <= wt(S) < 4 * W + EPS, wt(S)
        assert nx.is_connected(H.subgraph(S))
    return out

def run_instance(mg, X, M, verbose=False):
    q = len(X)
    alpha = max_uniform_product(mg, X)
    res = {'q': q, 'M': len(M), 'alpha': alpha}
    Xs = set(X)
    rho = alpha / 4.0
    G = mg.G
    Gbr = bridges_of(G)
    if rho * q < 2:
        res['branch'] = 'base'
        sel = [M[0]]
        cong = min_congestion_pairs(mg, sel)
        res.update(selected=1, congestion=cong)
        assert cong <= 1 + 1e-6
        return res
    Cl = clusters(G, X, rho)
    j = {}
    for idx, S in enumerate(Cl):
        for v in S:
            j[v] = idx
    S_ = [set(v for v in S if v in Xs) for S in Cl]
    Gj = [G.subgraph(S).copy() for S in Cl]
    # Step 1
    marked = set(); Z = []
    for (s, t) in M:
        if j[s] not in marked and j[t] not in marked:
            Z.append((s, t)); marked |= {j[s], j[t]}
    assert len(Z) >= rho * len(M) / 16 - EPS
    Z1 = [p for p in Z if j[p[0]] == j[p[1]]]
    def check_walks_and_route(pairs, walks, label):
        used = set()
        for w in walks:
            for a, b in zip(w, w[1:]):
                e = key(a, b)
                assert e not in used or G[a][b]['mult'] > 1, ('edge reuse', label)
                used.add(e)
        cong = min_congestion_pairs(mg, pairs)
        assert cong <= 1 + 1e-6, (label, cong)
        return cong
    if 2 * len(Z1) >= len(Z):
        walks = [nx.shortest_path(Gj[j[s]], s, t) for s, t in Z1]
        cong = check_walks_and_route(Z1, walks, 'Z1')
        res.update(branch='Z1', selected=len(Z1), congestion=cong)
        return res
    Zp = [p for p in Z if j[p[0]] != j[p[1]]]
    # bad bridges / tags
    info = {}
    for (s, t) in Zp:
        for x in (s, t):
            H = Gj[j[x]]
            Sj = S_[j[x]]
            bad = []
            for e in bridges_of(H):
                if e in Gbr:
                    continue
                H2 = H.copy(); H2.remove_edge(*e)
                comp = nx.node_connected_component(H2, x)
                if rho * len(comp & Sj) < 1 - EPS:
                    bad.append((e, comp))
            if not bad:
                info[x] = None
                continue
            bad.sort(key=lambda bc: len(bc[1]))
            for (e1, c1), (e2, c2) in zip(bad, bad[1:]):
                assert c1 <= c2, 'nesting violated'
            e_s, Zs = bad[0]
            f = None
            for z in Zs:
                for y in G.neighbors(z):
                    if y not in Zs and key(z, y) != e_s:
                        f = (z, y); break
                if f: break
            assert f is not None and f[1] not in Cl[j[x]]
            info[x] = {'e': e_s, 'Z': Zs, 'f': f, 'tau': j[f[1]]}
    # Step 2: digraph and independent set
    pidx = {p: i for i, p in enumerate(Zp)}
    owner = {}
    for p in Zp:
        for x in p:
            owner[j[x]] = p
    nbr = {p: set() for p in Zp}
    for p in Zp:
        for x in p:
            if info[x] is not None and info[x]['tau'] in owner:
                p2 = owner[info[x]['tau']]
                if p2 != p:
                    nbr[p].add(p2); nbr[p2].add(p)
    I = []; rem = set(Zp)
    while rem:
        p = min(rem, key=lambda r: len(nbr[r] & rem))
        assert len(nbr[p] & rem) <= 4
        I.append(p); rem -= ({p} | nbr[p])
    assert 5 * len(I) >= len(Zp)
    I2 = [(s, t) for (s, t) in I if (info[s] and info[s]['tau'] == j[t]) or (info[t] and info[t]['tau'] == j[s])]
    I3 = [p for p in I if p not in I2]
    if 2 * len(I2) >= len(I):
        walks = []
        for (s, t) in I2:
            if info[s] and info[s]['tau'] == j[t]:
                x, y = info[s]['f']
                w = nx.shortest_path(Gj[j[s]], s, x) + nx.shortest_path(Gj[j[t]], y, t)
            else:
                x, y = info[t]['f']
                w = nx.shortest_path(Gj[j[t]], t, x) + nx.shortest_path(Gj[j[s]], y, s)
            walks.append(w)
        cong = check_walks_and_route(I2, walks, 'I2')
        res.update(branch='I2', selected=len(I2), congestion=cong)
        return res
    Iterm = set(x for p in I for x in p)
    T_ = {}
    for (s, t) in I3:
        for x in (s, t):
            if info[x] is not None:
                C = info[x]['tau']
                assert not (Cl[C] & Iterm), 'transit cluster contains I terminal'
                T_.setdefault(C, []).append(x)
    partner = {}; ppath = {}; isolated = set()
    for C, Ts in T_.items():
        if len(Ts) < 2:
            continue
        HC = nx.bfs_tree(Gj[C], next(iter(Cl[C]))).to_undirected()
        Ts = list(Ts)
        if len(Ts) % 2 == 1:
            isolated.add(Ts.pop())
        # pairing in tree via leaf-peeling (Lemma 3.13)
        paths = tree_pairing(HC, [(info[x]['f'][1], x) for x in Ts])
        for (x1, x2, path) in paths:
            partner[x1] = x2; partner[x2] = x1; ppath[(x1, x2)] = path; ppath[(x2, x1)] = path[::-1]
        used = set()
        for (_, _, path) in paths:
            for a, b in zip(path, path[1:]):
                assert key(a, b) not in used; used.add(key(a, b))
    Y = [(s, t) for (s, t) in I3 if s not in isolated and t not in isolated]
    assert 3 * len(Y) >= len(I3)
    Yp = []; taken = set()
    for (s, t) in Y:
        if any((partner.get(x) in taken) for x in (s, t)):
            continue
        Yp.append((s, t)); taken |= {s, t}
    # conflict-free check
    Ypt = set(x for p in Yp for x in p)
    Ya = [(s, t) for (s, t) in Yp if partner.get(s) == t]
    Yb = [p for p in Yp if p not in Ya]
    if 2 * len(Ya) >= len(Yp):
        walks = []
        for (s, t) in Ya:
            xs, ys = info[s]['f']; xt, yt = info[t]['f']
            w = nx.shortest_path(Gj[j[s]], s, xs) + ppath[(s, t)] + nx.shortest_path(Gj[j[t]], xt, t)
            walks.append(w)
        cong = check_walks_and_route(Ya, walks, 'Ya') if Ya else None
        if not Ya:
            cong = min_congestion_pairs(mg, [M[0]]); res.update(branch='Ya-empty->1', selected=1, congestion=cong); return res
        res.update(branch='Ya', selected=len(Ya), congestion=cong)
        return res
    # Step 5: spreading for Yb
    flows = []; recv_total = {}; edge_owner = {}
    cases = {'alpha': 0, 'beta': 0, 'gamma': 0}
    for (s, t) in Yb:
        for x in (s, t):
            if info[x] is None:
                Q = Gj[j[x]].copy(); R = set(S_[j[x]]); cases['alpha'] += 1
            else:
                C = info[x]['tau']
                if len(T_[C]) == 1:
                    Q = nx.compose(Gj[j[x]], Gj[C]); Q.add_edge(*info[x]['f'], mult=G[info[x]['f'][0]][info[x]['f'][1]]['mult'])
                    R = S_[j[x]] | S_[C]; cases['beta'] += 1
                else:
                    x2 = partner[x]
                    assert x2 not in Ypt
                    Q = nx.compose(Gj[j[x]], Gj[j[x2]])
                    path = ppath[(x, x2)]
                    for a, b in zip(path, path[1:]):
                        Q.add_edge(a, b, mult=G[a][b]['mult'])
                    for (a, b) in (info[x]['f'], info[x2]['f']):
                        Q.add_edge(a, b, mult=G[a][b]['mult'])
                    R = S_[j[x]] | S_[j[x2]]; cases['gamma'] += 1
            # Claim 7: edge-disjointness
            for a, b in Q.edges():
                e = key(a, b)
                assert e not in edge_owner, 'Q(s) not edge-disjoint'
                edge_owner[e] = x
            for v in R:
                assert v not in recv_total, 'receivers not disjoint'
                recv_total[v] = 0.0
            flows.append(spread_flow(Q, x, R, rho, Gbr, G))
    # spreading-system check
    load = {}
    for fl, gam in flows:
        for e, val in fl.items():
            load[e] = load.get(e, 0) + val
        for v, val in gam.items():
            recv_total[v] = recv_total.get(v, 0) + val
            assert val <= rho + 1e-6
    for e, val in load.items():
        cap = 1.0 if e in Gbr else 0.5 * G[e[0]][e[1]]['mult']
        assert val <= cap + 1e-6, ('spreading load', e, val, cap)
    cong = min_congestion_pairs(mg, Yb) if Yb else min_congestion_pairs(mg, [M[0]])
    assert cong <= 1 + 1e-6, cong
    res.update(branch='Yb', selected=max(1, len(Yb)), congestion=cong, cases=cases)
    return res

def tree_pairing(HC, items):
    """items: list of (vertex, label); returns (label1,label2,path) with edge-disjoint paths."""
    T = HC.copy()
    at = {}
    for v, lab in items:
        at.setdefault(v, []).append((lab, [v]))
    out = []
    def flush(v):
        L = at.get(v, [])
        while len(L) >= 2:
            (l1, p1), (l2, p2) = L.pop(), L.pop()
            assert p1[-1] == v and p2[-1] == v
            out.append((l1, l2, p1 + p2[::-1][1:]))
    # paths are stored from original vertex to current position
    for v in list(at):
        flush(v)
    while T.number_of_nodes() > 1:
        leaf = next(v for v in T.nodes() if T.degree(v) == 1)
        u = next(iter(T.neighbors(leaf)))
        L = at.pop(leaf, [])
        assert len(L) <= 1
        for lab, p in L:
            at.setdefault(u, []).append((lab, p + [u]))
        T.remove_node(leaf)
        flush(u)
    assert all(len(L) == 0 for L in at.values())
    return out

def spread_flow(Q, s, R, rho, Gbr, G):
    D = nx.DiGraph()
    for a, b, d in Q.edges(data=True):
        e = key(a, b)
        cap = 1.0 if e in Gbr else 0.5 * G[a][b]['mult']
        for (u, v) in ((a, b), (b, a)):
            D.add_edge(u, v, capacity=cap)
    for v in R:
        D.add_edge(v, '__sink__', capacity=rho)
    val, fd = nx.maximum_flow(D, s, '__sink__')
    assert val >= 1 - 1e-6, ('criterion failed', val)
    sc = 1.0 / val
    fl = {}
    for a, b in Q.edges():
        net = abs(fd[a].get(b, 0) - fd[b].get(a, 0)) * sc
        if net > 1e-12:
            fl[key(a, b)] = net
    gam = {v: fd[v]['__sink__'] * sc for v in R if fd[v]['__sink__'] > 1e-12}
    return fl, gam

# ---------------------------------------------------------------- instances
FORCED = sys.argv[3] if len(sys.argv) > 3 else None

def instance(seed):
    rng = random.Random(seed)
    kind = rng.choice(['dense', 'dense', 'ring', 'expander', 'necklace', 'necklace'])
    if FORCED:
        kind = FORCED
    mg = MG()
    if kind == 'k_simple':
        m = rng.randint(10, 13)
        for u, v in itertools.combinations(range(m), 2):
            if rng.random() < 0.85:
                mg.add_edge(('c', u), ('c', v), 1)
        q = 2 * rng.randint(18, 24)
    elif kind == 'k_big':
        m = rng.randint(14, 18)
        for u, v in itertools.combinations(range(m), 2):
            if rng.random() < 0.6:
                mg.add_edge(('c', u), ('c', v), 1)
        q = 2 * rng.randint(28, 34)
    elif kind == 'dense':
        m = rng.randint(6, 10)
        core = nx.complete_graph(m)
        p_drop = rng.choice([0.0, 0.2, 0.4])
        for u, v in core.edges():
            if rng.random() >= p_drop:
                mg.add_edge(('c', u), ('c', v), rng.choice([1, 1, 2]))
        q = 2 * rng.randint(10, 18)
    elif kind == 'ring':
        m = rng.randint(8, 14)
        for i in range(m):
            mg.add_edge(('c', i), ('c', (i + 1) % m), rng.choice([2, 3, 4]))
            if rng.random() < 0.3:
                mg.add_edge(('c', i), ('c', (i + 2) % m), 1)
        q = 2 * rng.randint(6, 12)
    elif kind == 'necklace':
        r = rng.randint(3, 6); c = rng.randint(3, 5)
        for b_ in range(r):
            for u, v in itertools.combinations(range(c), 2):
                mg.add_edge(('c', b_, u), ('c', b_, v), rng.choice([1, 2]))
            mg.add_edge(('c', b_, 0), ('c', (b_ + 1) % r, 1), rng.choice([1, 2, 3]))
            other = rng.randrange(r)
            if rng.random() < 0.5 and other != b_:
                mg.add_edge(('c', b_, 2), ('c', other, 2), 1)
        q = 2 * rng.randint(6, 14)
    else:
        m = 2 * rng.randint(5, 8)
        core = nx.random_regular_graph(3, m, seed=seed)
        for u, v in core.edges():
            mg.add_edge(('c', u), ('c', v), rng.choice([2, 3]))
        q = 2 * rng.randint(6, 12)
    cores = [v for v in mg.G.nodes()]
    if not nx.is_connected(mg.G):
        return None
    X = []
    for i in range(q):
        c = rng.choice(cores)
        mg.add_edge(('t', i), c, 1)
        X.append(('t', i))
    perm = X[:]; rng.shuffle(perm)
    M = [(perm[2 * i], perm[2 * i + 1]) for i in range(q // 2)]
    return kind, mg, X, M

def main():
    s0 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    num = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    results = []
    for seed in range(s0, s0 + num):
        inst = instance(seed)
        if inst is None:
            continue
        kind, mg, X, M = inst
        mgr = degree_reduce(mg, X)
        assert max(len(list(mgr.G.neighbors(v))) for v in mgr.G.nodes()) <= 3
        r = run_instance(mgr, X, M)
        r['seed'] = seed; r['kind'] = kind
        r['bound'] = max(1.0, r['alpha'] * len(M) / 2 ** 15)
        assert r['selected'] >= r['bound'] - 1e-9
        results.append(r)
        print(json.dumps(r), flush=True)
    print('ALL CHECKS PASSED on', len(results), 'instances')

if __name__ == '__main__':
    main()
