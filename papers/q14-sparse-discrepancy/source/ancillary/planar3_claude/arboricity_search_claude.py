# Test: does every graph of arboricity <= L admit a cheap-deletion schedule at uniform level L?
import itertools, functools, random, sys
import networkx as nx

def schedule_exists(G, L):
    nodes = sorted(G.nodes); idx = {v: i for i, v in enumerate(nodes)}
    nb = [tuple(idx[u] for u in G[v]) for v in nodes]; n = len(nodes)
    sys.setrecursionlimit(10000)
    @functools.lru_cache(maxsize=None)
    def solve(rem, levs):        # levs: tuple of current levels (only meaningful on rem)
        if rem == 0: return True
        # heuristic order: try vertices with few remaining neighbours first
        cand = sorted((v for v in range(n) if rem >> v & 1), key=lambda v: sum(1 for u in nb[v] if rem >> u & 1))
        for v in cand:
            N = [u for u in nb[v] if rem >> u & 1]
            lv = levs[v]
            maxJ = lv if lv >= 2 else 0
            for js in range(min(maxJ, len(N)), -1, -1):
                for J in itertools.combinations(N, js):
                    pay = [u for u in N if u not in J]
                    if any(levs[u] < 2 for u in pay): continue
                    nl = list(levs)
                    for u in pay: nl[u] -= 1
                    nl[v] = 0
                    if solve(rem & ~(1 << v), tuple(nl)): return True
        return False
    return solve((1 << n) - 1, tuple([L] * n))

def union_of_trees(n, k, rng):
    G = nx.Graph(); G.add_nodes_from(range(n))
    for _ in range(k):
        T = nx.random_labeled_tree(n, seed=rng.randrange(10**9)) if hasattr(nx, 'random_labeled_tree') else nx.random_tree(n, seed=rng.randrange(10**9))
        G.add_edges_from(T.edges())
    return G

rng = random.Random(2027)
for L, ns, trials in [(2, [6, 7, 8, 9, 10, 11], 40), (3, [6, 7, 8, 9], 25)]:
    for n in ns:
        bad = 0
        for t in range(trials):
            G = union_of_trees(n, L, rng)
            if not schedule_exists(G, L):
                bad += 1
                print(f"  COUNTEREXAMPLE L={L} n={n} edges={sorted(G.edges())}", flush=True)
        print(f"L={L} n={n}: {trials-bad}/{trials} unions of {L} random spanning trees have level-{L} schedules", flush=True)
