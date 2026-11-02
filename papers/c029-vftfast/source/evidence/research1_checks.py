#!/usr/bin/env python3
"""Exact bounded checks for research1-separator.md; no external packages."""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def bfs(adj, x, y, deleted=0):
    if (deleted >> x) & 1 or (deleted >> y) & 1:
        return None
    prev = {x: None}
    queue = deque([x])
    while queue:
        v = queue.popleft()
        if v == y:
            path = []
            while v is not None:
                path.append(v)
                v = prev[v]
            return path[::-1]
        for w in adj[v]:
            if w not in prev and not ((deleted >> w) & 1):
                prev[w] = v
                queue.append(w)
    return None


def distance(adj, x, y, deleted=0):
    path = bfs(adj, x, y, deleted)
    return len(path) - 1 if path is not None else 10**9


def protected_gap(adj, x, y, protected, radius, budget):
    deleted = 0
    for j in range(budget + 1):
        path = bfs(adj, x, y, deleted)
        if path is None or len(path) - 1 > radius:
            return deleted, "cut"
        block = sum(1 << v for v in path if not ((protected >> v) & 1))
        if not block:
            return None, "protected_path"
        if j == budget:
            return None, "packing"
        deleted |= block
    raise AssertionError("unreachable")


def check_protected_gap():
    counts = Counter()
    per_n = {}
    for n in range(2, 6):
        pairs = list(combinations(range(n), 2))
        local = Counter()
        for graph_mask in range(1 << len(pairs)):
            adj = [[] for _ in range(n)]
            for i, (u, v) in enumerate(pairs):
                if (graph_mask >> i) & 1:
                    adj[u].append(v)
                    adj[v].append(u)
            for x, y in pairs:
                distances = [distance(adj, x, y, c) for c in range(1 << n)]
                for protected in range(1 << n):
                    if (protected & ((1 << x) | (1 << y))) != ((1 << x) | (1 << y)):
                        continue
                    allowed = [c for c in range(1 << n) if not (c & protected)]
                    for radius in range(1, 5):
                        for budget in range(3):
                            witness_exists = any(c.bit_count() <= budget and distances[c] > radius
                                                 for c in allowed)
                            cut, mode = protected_gap(adj, x, y, protected, radius, budget)
                            if cut is None:
                                assert not witness_exists, (n, graph_mask, x, y, protected, radius, budget)
                            else:
                                assert not (cut & protected)
                                assert cut.bit_count() <= (radius - 1) * budget
                                assert distances[cut] > radius
                            local[mode] += 1
                            local["cases"] += 1
            local["graphs"] += 1
        per_n[str(n)] = dict(local)
        counts.update(local)
    return {"domain": "all labeled simple H, n=2..5; every distinct unordered terminal pair; every protected superset; r=1..4; f=0..2",
            "totals": dict(counts), "per_n": per_n, "failures": 0}


def check_obstruction():
    counts = Counter()
    for p in range(1, 5):
        for f in range(1, 5):
            n = p + f + 2
            universe = set(range(2, n))
            supports = [set(a) for a in combinations(sorted(universe), p)]
            for a in supports:
                faults = universe - a
                adj = [[] for _ in range(n)]
                for z in sorted(faults):
                    for u, v in [(0, z), (z, 1)]:
                        adj[u].append(v)
                        adj[v].append(u)
                assert len(faults) == f
                assert distance(adj, 0, 1, sum(1 << v for v in faults)) > n
                for t in supports:
                    max_allowed_cut = sum(1 << v for v in universe - t)
                    protected_distance = distance(adj, 0, 1, max_allowed_cut)
                    assert (protected_distance == 2) == (t != a)
                    if t != a:
                        z = min(t - a)
                        assert z in adj[0] and 1 in adj[z] and z in t
                    counts["support_pairs"] += 1
                counts["H_A_graphs"] += 1
            counts["parameter_pairs"] += 1
    fixture = {"p": 2, "f": 2, "d": 3, "r": 12,
               "G_vertices": list(range(6)),
               "G_edges": [list(e) for e in combinations(range(6), 2) if e != (0, 1)],
               "H_edges": [[0, 4], [4, 1], [0, 5], [5, 1]],
               "faults": [4, 5], "witness_path": [0, 2, 3, 1],
               "surviving_G_distance": 2,
               "required_supports_for_all_H_A": [list(t) for t in combinations(range(2, 6), 2)],
               "scope": "fixed-endpoint, H-oblivious exact-length path-list obstruction; not shortest-distance-d or original construction hardness"}
    (HERE / "research1-obstruction-witness.json").write_text(json.dumps(fixture, indent=2) + "\n")
    return {"domain": "p,f=1..4, every A and T support", "totals": dict(counts), "failures": 0}


def main():
    start = time.monotonic()
    result = {"job_id": "c029-vftfast-research-6281f7685c7a", "arithmetic": "exact integer graph and subset operations"}
    result["protected_gap"] = check_protected_gap()
    result["path_list_obstruction"] = check_obstruction()
    result["source_sha256"] = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
    result["source_matches_preserved_triage_digest"] = result["source_sha256"] == "45828a099cc88bde52aee6450b298c8b73397e4367d3911585521595f94657b8"
    assert result["source_matches_preserved_triage_digest"]
    result["elapsed_seconds"] = round(time.monotonic() - start, 3)
    result["limitations"] = ["finite checks supplement, not replace, the written arguments",
                             "no joint separator implemented or proved",
                             "no computational verification of the source packing proof",
                             "no full original-scope resolution"]
    (HERE / "research1-checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
