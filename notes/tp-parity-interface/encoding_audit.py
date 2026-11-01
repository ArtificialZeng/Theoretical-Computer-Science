"""Independent reconstruction of the finite binary-interface CNF semantics.

No imports from the encoding producer, enumeration code or solver. Original
packet inputs, all vertex orders and tube adjacency are checked independently.
"""
import collections
import gzip
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE
PROJECT = HERE
OLD = HERE / "packets"


def components(vertices, graph):
    left = set(vertices); answer = []
    while left:
        first = min(left); found = {first}; stack = [first]
        while stack:
            v = stack.pop()
            for w in graph[v] & left - found:
                found.add(w); stack.append(w)
        left -= found; answer.append(found)
    return sorted(answer, key=min)


def independent_edges(packet):
    adjacency = packet["graph"]["adjacency_bits"]
    n = len(adjacency)
    graph = {u: {v for v in range(n) if adjacency[u] & (1 << v)} for u in range(n)}
    assert graph[0] == set(range(1, n))
    assert all(u in graph[v] for u in graph for v in graph[u])
    parents = [tuple(p) for p in packet["trees"]]
    assert len(parents) == len(set(parents))
    # Independent complete enumeration by every order.
    from_orders = set()
    for order in itertools.permutations(range(n)):
        rank = {v: i for i, v in enumerate(order)}; parent = [-2] * n

        def build(vertices, up):
            root = min(vertices, key=rank.get); parent[root] = up
            for part in components(set(vertices) - {root}, graph):
                build(part, root)

        build(set(range(n)), -1); from_orders.add(tuple(parent))
    assert set(parents) == from_orders
    faces = {}
    for i, p in enumerate(parents):
        children = {v: [] for v in range(n)}
        for v, up in enumerate(p):
            if up >= 0:
                children[up].append(v)

        def descendants(v):
            vertices = {v}
            for w in children[v]:
                vertices |= descendants(w)
            return vertices

        tubes = sorted(sum(1 << v for v in descendants(w)) for w in range(n) if p[w] >= 0)
        for j in range(n - 1):
            face = tuple(tubes[:j] + tubes[j + 1:]); faces.setdefault(face, []).append(i)
    edges = set()
    for pair in faces.values():
        assert len(pair) == 2; edges.add(tuple(sorted(pair)))
    assert edges == {tuple(sorted(e)) for e in packet["rotation_edges"]}
    return graph, edges


def main():
    summary = json.loads((OLD / "enumeration-summary.json").read_text())
    packets, hashes = {}, {}
    for row in summary["cases"]:
        if row.get("status") != "SAT_CHECKED" or row["n"] > 6:
            continue
        path = PROJECT / row["packet"]
        packets[tuple(row["adjacency_bits"])] = json.loads(gzip.decompress(path.read_bytes()))
        if row["n"] <= 6:
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    edge_cache = {}

    def edges(a):
        if a not in edge_cache:
            edge_cache[a] = independent_edges(packets[a])
        return edge_cache[a][1]

    cases = []
    for a, packet in packets.items():
        n = len(a)
        if n > 6:
            continue
        graph = {u: {v for v in range(n) if a[u] & (1 << v)} for u in range(n)}
        parts = components(range(1, n), graph)
        if len(parts) != 2:
            continue
        factors = []
        for part in parts:
            vertices = [0] + sorted(part); renaming = {v: i for i, v in enumerate(vertices)}
            factor = tuple(sum(1 << renaming[v] for v in graph[u] if v in renaming) for u in vertices)
            assert factor in packets
            factors.append((factor, vertices, renaming,
                            {tuple(p): i for i, p in enumerate(packets[factor]["trees"])}))
        features = []
        for parent in packet["trees"]:
            local_indices = []
            for factor, vertices, renaming, index in factors:
                restricted = []
                for v in vertices:
                    up = parent[v]
                    while up >= 0 and up not in renaming:
                        up = parent[up]
                    restricted.append(-1 if up < 0 else renaming[up])
                local_indices.append(index[tuple(restricted)])
            chain = []; up = parent[0]
            while up >= 0:
                chain.append(up); up = parent[up]
            chain.reverse()
            owners = [0 if v in parts[0] else 1 for v in chain]
            lengths = (sum(c == 0 for c in owners) % 2, sum(c == 1 for c in owners) % 2)
            inversion = sum(owners[i] > owners[j] for i in range(len(owners))
                            for j in range(i + 1, len(owners))) % 2
            features.append((*local_indices, (*lengths, inversion)))
        cases.append((packet["graph"]["id"], a, [f[0] for f in factors], features))
    meta = json.loads((HERE / "training.encoding.json").read_text())
    assert [c[0] for c in cases] == meta["cases"]
    clauses = []; variables = 0

    def one_color():
        nonlocal variables
        x = (variables + 1, variables + 2, variables + 3); variables += 3
        clauses.append(x)
        for u, v in itertools.combinations(x, 2):
            clauses.append((-u, -v))
        return x

    fs = {}
    for a in sorted({factor for _, _, factors, _ in cases for factor in factors}):
        fs[a] = [one_color() for _ in packets[a]["trees"]]
        for u, v in sorted(edges(a)):
            for c in range(3):
                clauses.append((-fs[a][u][c], -fs[a][v][c]))
    table = {key: one_color() for key in itertools.product(range(3), range(3), range(2), range(2), range(2))}
    for name, a, (first, second), features in cases:
        global_colors = [one_color() for _ in features]
        for i, (u, v, bits) in enumerate(features):
            # If factor inputs and the table output have their chosen colors,
            # force that same global color. One-hot constraints give equivalence.
            for ca, cb, out in itertools.product(range(3), repeat=3):
                clauses.append((-fs[first][u][ca], -fs[second][v][cb],
                                -table[(ca, cb) + bits][out], global_colors[i][out]))
        for u, v in sorted(edges(a)):
            for c in range(3):
                clauses.append((-global_colors[u][c], -global_colors[v][c]))
    actual = []; header = None; pending = []
    for line in (HERE / "training.cnf").read_text().splitlines():
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            _, kind, var, count = line.split(); assert kind == "cnf"; header = int(var), int(count); continue
        for value in map(int, line.split()):
            if value:
                pending.append(value)
            else:
                actual.append(tuple(pending)); pending = []
    assert not pending and header == (variables, len(actual))
    assert len(clauses) == len(actual) == meta["clauses"]
    # Clause ordering and literal repetition are semantically irrelevant. Keep
    # multiplicities of whole clauses while normalizing each clause to its set.
    canonical = lambda c: tuple(sorted(set(c)))
    assert collections.Counter(map(canonical, clauses)) == collections.Counter(map(canonical, actual))
    result = {"verified": True, "variables": variables, "clauses": len(clauses),
              "graph_cases": len(cases), "global_states": sum(len(c[3]) for c in cases),
              "factor_types": len(fs), "factor_states": sum(map(len, fs.values())),
              "table_entries": len(table), "original_clause_duplicate_literal_count": sum(len(c) - len(set(c)) for c in actual),
              "cnf_sha256": hashlib.sha256((HERE / "training.cnf").read_bytes()).hexdigest(),
              "packet_hashes": hashes,
              "scope": "Exact equivalence of copied CNF to the specified finite shared binary parity-interface hypothesis; no universal TP coloring disproof",
              "fresh_model_review": False, "original_resolved": False}
    (HERE / "encoding-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "packet_hashes"}, indent=2))


if __name__ == "__main__":
    main()
