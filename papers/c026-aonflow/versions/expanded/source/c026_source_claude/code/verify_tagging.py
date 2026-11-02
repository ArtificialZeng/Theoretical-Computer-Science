#!/usr/bin/env python3
"""Randomized check of Lemmas 3.8 (criterion), 3.11 (nesting of bad bridges, tag edge) and
3.12 (tagging) of main.tex, on random multigraphs with degree-one terminals.
Diagnostic only.  Usage: python3 -I verify_tagging.py [trials]
"""
import sys, random
import networkx as nx

EPS = 1e-9

def key(u, v):
    return tuple(sorted((u, v), key=str))

def bridges_of(H):
    return {key(u, v) for u, v in nx.bridges(H) if H[u][v].get('mult', 1) == 1}

def spreads(Q, s, R, rho, Gbr):
    D = nx.DiGraph()
    for a, b, d in Q.edges(data=True):
        cap = 1.0 if key(a, b) in Gbr else 0.5 * d.get('mult', 1)
        D.add_edge(a, b, capacity=cap); D.add_edge(b, a, capacity=cap)
    for v in R:
        D.add_edge(v, '__z__', capacity=rho)
    if s not in D:
        return 0.0
    return nx.maximum_flow_value(D, s, '__z__')

def random_instance(rng):
    n = rng.randint(8, 30)
    G = nx.Graph()
    T = nx.random_labeled_tree(n, seed=rng.randrange(10**9)) if hasattr(nx, 'random_labeled_tree') else nx.random_tree(n, seed=rng.randrange(10**9))
    for u, v in T.edges():
        G.add_edge(u, v, mult=rng.choice([1, 1, 1, 2]))
    for _ in range(rng.choice([rng.randint(0, 3), rng.randint(0, n)])):
        u, v = rng.sample(range(n), 2)
        if G.has_edge(u, v):
            G[u][v]['mult'] += 1
        else:
            G.add_edge(u, v, mult=1)
    q = rng.randint(6, 40)
    X = []
    for i in range(q):
        t = ('t', i); G.add_edge(t, rng.randrange(n), mult=1); X.append(t)
    return G, X

def connected_set(G, rng, start, size, forbid):
    S = {start}; frontier = [start]
    while frontier and len(S) < size:
        x = frontier.pop(rng.randrange(len(frontier)))
        for y in G.neighbors(x):
            if y not in S and y not in forbid and len(S) < size:
                S.add(y); frontier.append(y)
    return S

def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    rng = random.Random(12345)
    stats = dict(criterion=0, nested=0, tags=0, tagging=0)
    for _ in range(trials):
        G, X = random_instance(rng)
        Xs = set(X)
        Gbr = bridges_of(G)
        rho = rng.choice([0.05, 0.1, 0.15, 0.25])
        # --- Lemma 3.8 on a random connected Q with random R
        core = [v for v in G.nodes() if v not in Xs]
        Qv = connected_set(G, rng, rng.choice(core), rng.randint(3, len(G)), set())
        Q = G.subgraph(Qv).copy()
        if rng.random() < 0.5 and Q.number_of_edges() > 1:  # drop random edges, keep connected
            for e in list(Q.edges()):
                Q2 = Q.copy(); Q2.remove_edge(*e)
                if nx.is_connected(Q2) and rng.random() < 0.3:
                    Q = Q2
        R = [v for v in Qv if v in Xs]
        if R and rho * len(R) >= 1:
            s = rng.choice(list(Qv))
            ok = True
            for e in bridges_of(Q):
                if e in Gbr:
                    continue
                Q2 = Q.copy(); Q2.remove_edge(*e)
                comp = nx.node_connected_component(Q2, s)
                if rho * len(comp & set(R)) < 1 - EPS:
                    ok = False; break
            if ok:
                assert spreads(Q, s, R, rho, Gbr) >= 1 - 1e-7, 'Lemma 3.8 violated'
                stats['criterion'] += 1
        # --- Lemmas 3.11 / 3.12
        Vj = connected_set(G, rng, rng.choice(core), rng.randint(3, len(G)), set())
        Sj = {v for v in Vj if v in Xs}
        if rho * len(Sj) < 2 or not Sj:
            continue
        Gj = G.subgraph(Vj).copy()
        s = rng.choice(sorted(Sj, key=str))
        bad = []
        for e in bridges_of(Gj):
            if e in Gbr:
                continue
            H = Gj.copy(); H.remove_edge(*e)
            comp = nx.node_connected_component(H, s)
            if rho * len(comp & Sj) < 1 - EPS:
                bad.append((e, comp))
        if not bad:
            assert spreads(Gj, s, Sj, rho, Gbr) >= 1 - 1e-7, 'Lemma 3.11(i) violated'
            continue
        bad.sort(key=lambda t: len(t[1]))
        for (e1, c1), (e2, c2) in zip(bad, bad[1:]):
            assert c1 < c2, 'Lemma 3.11(ii) nesting violated'
        stats['nested'] += 1
        e_s, Zs = bad[0]
        f = None
        for z in Zs:
            for y in G.neighbors(z):
                if y not in Zs and key(z, y) != e_s:
                    f = (z, y); break
            if f: break
        assert f is not None and f[1] not in Vj, 'Lemma 3.11(ii) tag edge missing'
        stats['tags'] += 1
        # second cluster disjoint from Vj, reachable from y_s without edges of G_j
        rest = [v for v in G.nodes() if v not in Vj and v not in Xs]
        if not rest:
            continue
        Vj2 = connected_set(G, rng, rng.choice(rest), rng.randint(2, len(G)), Vj)
        Sj2 = {v for v in Vj2 if v in Xs}
        if rho * len(Sj2) < 1:
            continue
        Gminus = G.copy()
        Gminus.remove_edges_from(list(Gj.edges()))
        try:
            path = nx.shortest_path(Gminus, f[1], next(iter(Vj2)))
        except nx.NetworkXNoPath:
            continue
        A = G.subgraph(Vj2).copy()
        A.add_edge(*f, mult=G[f[0]][f[1]]['mult'])
        for a, b in zip(path, path[1:]):
            A.add_edge(a, b, mult=G[a][b]['mult'])
        assert not (set(map(lambda e: key(*e), A.edges())) & set(map(lambda e: key(*e), Gj.edges())))
        Q = nx.compose(Gj, A)
        assert spreads(Q, s, Sj | Sj2, rho, Gbr) >= 1 - 1e-7, 'Lemma 3.12 violated'
        stats['tagging'] += 1
    print('ALL CHECKS PASSED', stats)

if __name__ == '__main__':
    main()
