"""Fresh finite checks, independent of the frozen proposer implementation.

Uses set/bit-mask contractions, scalar topological recurrence, and direct path
enumeration. This checks semantics and batching only, not fast MM complexity.
"""
from itertools import product, permutations, combinations
from collections import Counter
from pathlib import Path
import hashlib
import json
import random
import time

JOB = "c032-dspdag-referee-56b0105494de"
COUNTS = Counter()


def scalar_reach(adj, seed):
    n, k = len(adj[0]), len(adj)
    reached = {seed}
    # Independent ascending-minimum scalar dynamic program.
    for v in range(n):
        for q in tuple(reached):
            if min(q) != v:
                continue
            label = q.index(v)
            for x in adj[label][v]:
                if x not in q:
                    reached.add(q[:label] + (x,) + q[label + 1:])
    return reached


def batched_reach(adj, seed):
    n, k = len(adj[0]), len(adj)
    size = 1 << (n - 1).bit_length()
    reached = {seed}

    def visit(lo, hi):
        if hi - lo == 1:
            return
        mid = (lo + hi) // 2
        width = mid - lo
        visit(lo, mid)
        # These immutable source masks prevent intra-cross-step feedback.
        sources = tuple(q for q in reached if lo <= min(q) < mid)
        calls = 0
        for label in range(k):
            context_domains = [(range(mid, size),) * (k - 1)]
            target_domains = [range(mid, hi)]
            for first in range(k - 1):
                context_domains.append((range(hi, size),) * first
                    + (range(mid, hi),)
                    + (range(mid, size),) * (k - 2 - first))
                target_domains.append(range(hi, size))
            for domains, xs in zip(context_domains, target_domains):
                contexts = list(product(*domains))
                targets = list(xs)
                for ci in range(0, len(contexts), width ** (k - 1)):
                    batch = contexts[ci:ci + width ** (k - 1)]
                    masks = []
                    for c in batch:
                        mask = 0
                        for q in sources:
                            if q.index(min(q)) == label and q[:label] + q[label + 1:] == c:
                                mask |= 1 << (q[label] - lo)
                        masks.append(mask)
                    for xi in range(0, len(targets), width):
                        calls += 1
                        for x in targets[xi:xi + width]:
                            edge_mask = sum(1 << (u - lo) for u in range(lo, mid)
                                            if u < n and x in adj[label][u])
                            for c, mask in zip(batch, masks):
                                q = c[:label] + (x,) + c[label:]
                                if mask & edge_mask and len(set(q)) == k:
                                    assert mid <= min(q) < hi
                                    reached.add(q)
        assert calls <= k * k * (size // width) ** (k - 1)
        COUNTS["cross_nodes"] += 1
        COUNTS["product_batches"] += calls
        visit(mid, hi)

    visit(0, size)
    return reached


def matrix(n, edge_set):
    a = [set() for _ in range(n)]
    for u, v in edge_set:
        a[u].add(v)
    return a


def compare(adj, seed):
    assert batched_reach(adj, seed) == scalar_reach(adj, seed)
    COUNTS["complete_state_set_comparisons"] += 1


def shortest_paths(n, edges, s, t):
    candidates = []
    def walk(v, path, weight):
        if v == t:
            candidates.append((weight, path))
            return
        for a, b, w in edges:
            if a == v:
                walk(b, path + (b,), weight + w)
    walk(s, (s,), 0)
    if not candidates:
        return []
    least = min(w for w, _ in candidates)
    return [p for w, p in candidates if w == least]


def normalized_answer(n, edges, pairs, mode):
    k = len(pairs)
    if mode == "strict" and any(set(a) & set(b) for a, b in combinations(pairs, 2)):
        return False
    terminals = set(sum((list(p) for p in pairs), []))
    copies = []
    for v in range(n):
        if v not in terminals or mode in ("strict", "internal_only"):
            copies.append((v, -1))
        if mode != "strict":
            copies.extend((v, i) for i, pair in enumerate(pairs) if v in pair)
    rank = {v: i for i, v in enumerate(copies)}
    def mapped(v, i):
        if mode != "strict" and v in pairs[i]:
            return rank[v, i]
        return rank.get((v, -1))
    total = len(copies) + k
    adj = []
    for i, (s, t) in enumerate(pairs):
        dist = [None] * n
        dist[s] = 0
        for u in range(n):
            for a, b, w in edges:
                if a == u and dist[a] is not None:
                    nd = dist[a] + w
                    if dist[b] is None or nd < dist[b]:
                        dist[b] = nd
        if dist[t] is None:
            return False
        allowed = []
        for u, v, w in edges:
            a, b = mapped(u, i), mapped(v, i)
            if a is not None and b is not None and v != s and u != t:
                if dist[u] is not None and dist[u] + w == dist[v]:
                    allowed.append((a, b))
        allowed.append((mapped(t, i), len(copies) + i))
        adj.append(matrix(total, allowed))
    reached = batched_reach(adj, tuple(mapped(s, i) for i, (s, t) in enumerate(pairs)))
    return tuple(range(len(copies), total)) in reached


def direct_answer(n, edges, pairs, mode):
    for paths in product(*(shortest_paths(n, edges, s, t) for s, t in pairs)):
        valid = True
        for i, j in combinations(range(len(pairs)), 2):
            if mode == "strict":
                conflict = set(paths[i]) & set(paths[j])
            elif mode == "endpoints_only":
                conflict = (set(paths[i]) & set(paths[j])) - (set(pairs[i]) & set(pairs[j]))
            else:
                conflict = set(paths[i][1:-1]) & set(paths[j][1:-1])
            if conflict:
                valid = False
                break
        if valid:
            return True
    return False


def main():
    start = time.monotonic()
    # Exhaust every triple of distinct labelled DAGs on three ordered vertices.
    edges3 = list(combinations(range(3), 2))
    dags = [matrix(3, [e for i, e in enumerate(edges3) if mask >> i & 1])
            for mask in range(1 << len(edges3))]
    for adj in product(dags, repeat=3):
        for seed in permutations(range(3)):
            compare(adj, seed)
    COUNTS["exhaustive_labelled_n3_k3"] = 8 ** 3 * 6
    # Exhaust all common-edge DAGs on four vertices and every ordered 3-seed.
    edges4 = list(combinations(range(4), 2))
    for mask in range(1 << len(edges4)):
        a = matrix(4, [e for i, e in enumerate(edges4) if mask >> i & 1])
        for seed in permutations(range(4), 3):
            compare([a, a, a], seed)
    COUNTS["exhaustive_common_n4_k3"] = 64 * 24
    rng = random.Random(5610494)
    for k, n, trials in [(2, 7, 30), (3, 7, 50), (4, 6, 20), (5, 6, 10)]:
        for _ in range(trials):
            adj = [matrix(n, [e for e in combinations(range(n), 2) if rng.random() < .55])
                   for _ in range(k)]
            compare(adj, tuple(rng.sample(range(n), k)))
        COUNTS[f"random_labelled_k{k}"] = trials
    modes = ("strict", "endpoints_only", "internal_only")
    outcomes = {mode: Counter() for mode in modes}
    for trial in range(120):
        n = 6
        edges = [(u, v, (1 << 180) + rng.randrange(1, 8) if trial % 5 == 0
                          else v - u if trial % 3 == 0 else rng.randrange(1, 9))
                 for u, v in combinations(range(n), 2) if rng.random() < .65]
        pairs = [tuple(rng.choices(range(n), k=2)) for _ in range(3)]
        if trial % 4 == 0:
            pairs = [(0, 3), (1, 4), (2, 5)]
        for mode in modes:
            observed = normalized_answer(n, edges, pairs, mode)
            expected = direct_answer(n, edges, pairs, mode)
            assert observed == expected, (trial, mode, pairs, edges)
            outcomes[mode]["yes" if observed else "no"] += 1
            COUNTS["weighted_direct_enumeration_comparisons"] += 1
    result = {"job_id": JOB, "status": "passed", "counts": dict(COUNTS),
              "weighted_outcomes": {m: dict(c) for m, c in outcomes.items()},
              "seed": 5610494, "elapsed_seconds": time.monotonic() - start,
              "scope": "Independent bit-mask batching versus scalar recurrence; direct original weighted shortest-path enumeration and three endpoint conventions. Finite bug checks, not an asymptotic or novelty certificate.",
              "fast_rectangular_algorithm_implemented": False,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name("verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
