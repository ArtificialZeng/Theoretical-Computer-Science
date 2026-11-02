import sys, networkx as nx
src = open("arboricity_search_claude.py").read(); src = src[:src.index("def union_of_trees")]
ns = {}; exec(src, ns); schedule_exists = ns['schedule_exists']
def cn2(n):
    G = nx.Graph()
    for i in range(n): G.add_edge(i, (i+1) % n); G.add_edge(i, (i+2) % n)
    return G
def nash_williams_ok(G, a):
    # exact check of arboricity <= a by brute force over vertex subsets (small n only)
    import itertools
    nodes = list(G.nodes)
    for r in range(2, len(nodes)+1):
        for S in itertools.combinations(nodes, r):
            if G.subgraph(S).number_of_edges() > a*(r-1): return False
    return True
for n in [8, 9, 10, 11, 12]:
    G = cn2(n); G.remove_edge(0, 1); G.remove_edge(n//2, n//2+1)
    arb2 = nash_williams_ok(G, 2) if n <= 12 else None
    print(f"C_{n}^2 minus 2 far edges: m={G.number_of_edges()} (2n-2={2*n-2}), arboricity<=2: {arb2}, level-2 schedule: {schedule_exists(G, 2)}", flush=True)
# 3-regular planar triangle-free / girth 5: dodecahedron (n=20) and generalized Petersen GP(7,2)
for name, G in [("GP(7,2)", nx.generalized_petersen_graph(7,2) if hasattr(nx,'generalized_petersen_graph') else None)]:
    if G is not None:
        print(name, schedule_exists(G, 2), flush=True)
