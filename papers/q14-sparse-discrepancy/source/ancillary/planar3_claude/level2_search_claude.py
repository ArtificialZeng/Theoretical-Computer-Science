# Search for cheap-deletion schedules (Lemma cheap only) at uniform level 2 on small graphs.
# State: remaining vertex set + current levels (1 or 2). Delete v with level l_v and J subset of its
# remaining neighbours, |J| <= l_v, J nonempty only if l_v >= 2; the other neighbours must have level 2
# and drop to 1.
import itertools, functools, sys
import networkx as nx

def good(G, L0=2):
    nodes = sorted(G.nodes); idx = {v: i for i, v in enumerate(nodes)}
    nb = [frozenset(idx[u] for u in G[v]) for v in nodes]
    n = len(nodes)
    @functools.lru_cache(maxsize=None)
    def solve(rem, lev1):   # rem: bitmask of remaining; lev1: bitmask of remaining vertices at level 1
        if rem == 0: return True
        for v in range(n):
            if not rem >> v & 1: continue
            N = [u for u in nb[v] if rem >> u & 1]
            lv = 1 if lev1 >> v & 1 else 2
            maxJ = lv if lv >= 2 else 0
            for js in range(min(maxJ, len(N)), -1, -1):
                for J in itertools.combinations(N, js):
                    pay = [u for u in N if u not in J]
                    if any(lev1 >> u & 1 for u in pay): continue
                    nl = lev1
                    for u in pay: nl |= 1 << u
                    nr = rem & ~(1 << v)
                    if solve(nr, nl & nr): return True
        return False
    return solve((1 << n) - 1, 0 if L0 >= 2 else (1 << n) - 1)

tests = {
  'Q3 cube': nx.hypercube_graph(3),
  'grid 3x3': nx.grid_2d_graph(3, 3),
  'grid 3x4': nx.grid_2d_graph(3, 4),
  'C4': nx.cycle_graph(4),
  'K_{2,3}': nx.complete_bipartite_graph(2, 3),
  'K_{3,3} (nonplanar)': nx.complete_bipartite_graph(3, 3),
  'octahedron (E=12,n=6)': nx.octahedral_graph(),
  'K4': nx.complete_graph(4),
  'K5 (E=10=2n)': nx.complete_graph(5),
  'Petersen (nonplanar)': nx.petersen_graph(),
}
for name, G in tests.items():
    print(f"{name:28s} n={G.number_of_nodes():2d} m={G.number_of_edges():2d}  level-2 schedule: {good(G)}", flush=True)
