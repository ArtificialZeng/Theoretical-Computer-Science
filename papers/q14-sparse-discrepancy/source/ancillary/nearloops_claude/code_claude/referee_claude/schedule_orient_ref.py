"""Checks for version-2 items lem:schedule and prop:orient.

(1) lem:schedule bookkeeping.  Random graphs G (n <= 12), random orderings, random
    absorbed/paid marks, levels l_v = p_v + max(2,a_v) + slack.  Simulate the proof:
    repeatedly delete the first remaining vertex h with J = neighbours joined by absorbed
    edges, and check the hypotheses of lem:cheap at every step (all neighbours of h have
    current level >= 2, |J| <= l_h, l_h >= 2 if J nonempty), then lower the paid neighbours.
    Also check that the hypothesis p_v+max(2,a_v)<=l_v is re-established for G - v_1.
    Sanity: with levels one below the bound somewhere, a hypothesis check must fail.
(2) prop:orient.  For random graphs (n <= 9) compute exactly
      * the least k such that some orientation has all in-degrees <= k (brute force),
      * p(H) = max over nonempty vertex subsets of ceil(|E(H[X])|/|X|) (Hakimi),
      * the degeneracy dgn(H) and max degree Delta,
    and check k == p(H), dgn/2 <= p <= dgn, and that the Euler-tour orientation (new vertex
    joined to odd-degree vertices) has in-degrees <= ceil(Delta/2).  Also check the
    conversion: for an optimal orientation and a random ordering, marks 'absorbed iff
    oriented towards the earlier endpoint' give p_v + a_v = indeg(v), hence
    p_v + max(2,a_v) <= k+2.
Run: python3 -I schedule_orient_ref.py
"""
import sys, os, random, itertools, time

HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_schedule_orient.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def rand_graph(n, p, rng):
    return [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < p]


def ap_counts(n, order, edges, mark):
    pos = {v: i for i, v in enumerate(order)}
    a = {v: 0 for v in range(n)}
    pp = {v: 0 for v in range(n)}
    for (u, v), m in zip(edges, mark):
        e, l = (u, v) if pos[u] < pos[v] else (v, u)   # e earlier, l later
        if m == "A":
            a[e] += 1        # absorbed edge joining e to a later vertex
        else:
            pp[l] += 1       # paid edge joining l to an earlier vertex
    return a, pp


def simulate(n, order, edges, mark, level):
    """returns (ok, reason). Simulates the proof of lem:schedule."""
    lev = dict(level)
    alive = set(range(n))
    E = {frozenset(e): m for e, m in zip(edges, mark)}
    for idx, h in enumerate(order):
        nbrs = [u for u in alive if u != h and frozenset((h, u)) in E]
        J = [u for u in nbrs if E[frozenset((h, u))] == "A"]
        if any(lev[u] < 2 for u in nbrs):
            return False, f"neighbour of {h} below level 2"
        if len(J) > lev[h]:
            return False, f"|J|>l_h at {h}"
        if J and lev[h] < 2:
            return False, f"l_h<2 with J nonempty at {h}"
        if lev[h] < 1:
            return False, "level < 1"
        for u in nbrs:
            if u not in J:
                lev[u] -= 1
        alive.remove(h)
        # inherited hypothesis for the remaining graph
        rest = order[idx + 1:]
        if rest:
            sub_edges = [(e, m) for e, m in zip(edges, mark) if e[0] in alive and e[1] in alive]
            a2, p2 = ap_counts(n, order, [e for e, _ in sub_edges], [m for _, m in sub_edges])
            for v in rest:
                if p2[v] + max(2, a2[v]) > lev[v]:
                    return False, f"hypothesis not inherited at {v}"
    return True, ""


def part1(rng):
    trials = 20000
    bad = 0
    sanity_fail = 0
    sanity_trials = 0
    for _ in range(trials):
        n = rng.randint(1, 12)
        edges = rand_graph(n, rng.uniform(0.1, 0.9), rng)
        order = list(range(n))
        rng.shuffle(order)
        mark = [rng.choice("AP") for _ in edges]
        a, pp = ap_counts(n, order, edges, mark)
        level = {v: pp[v] + max(2, a[v]) + rng.choice([0, 0, 0, 1]) for v in range(n)}
        ok, why = simulate(n, order, edges, mark, level)
        if not ok:
            bad += 1
            if bad <= 3:
                log(f"    FAIL: {why} n={n} order={order} edges={edges} mark={mark} level={level}")
        # sanity: lower one vertex with an edge below the bound
        cands = [v for v in range(n) if any(v in e for e in edges)]
        if cands:
            v = rng.choice(cands)
            lv = dict(level)
            lv[v] = pp[v] + max(2, a[v]) - 1
            sanity_trials += 1
            ok2, _ = simulate(n, order, edges, mark, lv)
            if not ok2:
                sanity_fail += 1
    log(f"(1) lem:schedule: {trials} random (G, ordering, marks, levels) with the hypothesis: "
        f"proof-simulation failures {bad} (must be 0)")
    log(f"    sanity: one level lowered below the bound: hypothesis check fails in {sanity_fail}/{sanity_trials} "
        f"(the lemma's hypothesis is sufficient, not necessary; failures show the checker is live)")


def min_max_indegree(n, edges):
    best = None
    m = len(edges)
    for bits in range(1 << m):
        indeg = [0] * n
        for i, (u, v) in enumerate(edges):
            if bits >> i & 1:
                indeg[v] += 1
            else:
                indeg[u] += 1
        k = max(indeg) if n else 0
        if best is None or k < best[0]:
            best = (k, bits)
    return best


def pseudo(n, edges):
    best = 0
    for X in range(1, 1 << n):
        sz = bin(X).count("1")
        e = sum(1 for (u, v) in edges if X >> u & 1 and X >> v & 1)
        best = max(best, -(-e // sz))
    return best


def degeneracy(n, edges):
    adj = {v: set() for v in range(n)}
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


def euler_orientation_maxin(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    E = list(edges)
    new = n
    for v in range(n):
        if deg[v] % 2:
            E.append((v, new))
    N = n + 1
    adj = {v: [] for v in range(N)}
    for i, (u, v) in enumerate(E):
        adj[u].append((v, i))
        adj[v].append((u, i))
    used = [False] * len(E)
    indeg = [0] * N
    # Hierholzer on each component, orienting edges along the circuit
    for s in range(N):
        if all(used[i] for _, i in adj[s]):
            continue
        stack = [(s, -1)]
        ptr = {v: 0 for v in range(N)}
        while stack:
            v, _ = stack[-1]
            while ptr[v] < len(adj[v]) and used[adj[v][ptr[v]][1]]:
                ptr[v] += 1
            if ptr[v] == len(adj[v]):
                stack.pop()
            else:
                w, i = adj[v][ptr[v]]
                used[i] = True
                indeg[w] += 1     # traverse v -> w
                stack.append((w, i))
    # in-degree in the original graph: drop edges to the new vertex
    orig_in = [0] * n
    # recompute: easier to re-run with recorded directions
    return max(indeg[:n]) if n else 0, deg


def part2(rng):
    trials = 1500
    bad_hakimi = bad_bounds = bad_euler = bad_conv = 0
    tight_half = 0
    better = 0
    for _ in range(trials):
        n = rng.randint(2, 8)
        edges = rand_graph(n, rng.uniform(0.2, 1.0), rng)
        if len(edges) > 16:
            edges = rng.sample(edges, 16)
        k, bits = min_max_indegree(n, edges)
        p = pseudo(n, edges)
        d = degeneracy(n, edges)
        Delta = 0
        deg = [0] * n
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
        Delta = max(deg)
        if k != p:
            bad_hakimi += 1
        if not (d <= 2 * p and p <= d):
            bad_bounds += 1
        if 2 * p == d or 2 * p == d + 1:
            tight_half += 1
        if p + 2 < max(2, d):
            better += 1
        mi, _ = euler_orientation_maxin(n, edges)
        # the Euler in-degree counted edges to the new vertex too; original in-degree <= that
        if mi > -(-Delta // 2) + 1:
            bad_euler += 1
        # conversion
        order = list(range(n))
        rng.shuffle(order)
        pos = {v: i for i, v in enumerate(order)}
        indeg = [0] * n
        a = [0] * n
        pp = [0] * n
        for i, (u, v) in enumerate(edges):
            head, tail = (v, u) if bits >> i & 1 else (u, v)
            indeg[head] += 1
            if pos[head] < pos[tail]:
                a[head] += 1      # oriented towards earlier endpoint: absorbed, counted at earlier (=head)
            else:
                pp[head] += 1     # paid, counted at later endpoint (=head)
        if any(pp[v] + a[v] != indeg[v] or pp[v] + max(2, a[v]) > k + 2 for v in range(n)):
            bad_conv += 1
    log(f"(2) prop:orient: {trials} random graphs (n<=8, <=16 edges): min max-indegree != p(H): {bad_hakimi}; "
        f"violations of dgn/2 <= p <= dgn: {bad_bounds}; Euler bound violations: {bad_euler}; "
        f"conversion violations: {bad_conv}; cases with p+2 < max(2,dgn): {better}")


def euler_exact_check(rng):
    """exact in-degree check of the Euler construction (original edges only)."""
    bad = 0
    T = 3000
    for _ in range(T):
        n = rng.randint(1, 14)
        edges = rand_graph(n, rng.uniform(0.1, 1.0), rng)
        deg = [0] * n
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
        Delta = max(deg) if n else 0
        E = list(edges) + [(v, n) for v in range(n) if deg[v] % 2]
        N = n + 1
        adj = {v: [] for v in range(N)}
        for i, (u, v) in enumerate(E):
            adj[u].append((v, i))
            adj[v].append((u, i))
        used = [False] * len(E)
        direc = {}
        for s in range(N):
            if all(used[i] for _, i in adj[s]):
                continue
            stack = [s]
            ptr = {v: 0 for v in range(N)}
            while stack:
                v = stack[-1]
                while ptr[v] < len(adj[v]) and used[adj[v][ptr[v]][1]]:
                    ptr[v] += 1
                if ptr[v] == len(adj[v]):
                    stack.pop()
                else:
                    w, i = adj[v][ptr[v]]
                    used[i] = True
                    direc[i] = (v, w)
                    stack.append(w)
        indeg = [0] * n
        for i in range(len(edges)):
            v, w = direc[i]
            indeg[w] += 1
        # every vertex balanced in the augmented graph?
        if n and max(indeg) > -(-Delta // 2):
            bad += 1
    log(f"(2b) Euler-tour orientation, exact: {T} random graphs (n<=14): in-degree > ceil(Delta/2) in {bad} (must be 0)")


rng = random.Random(17)
t0 = time.time()
part1(rng)
part2(rng)
euler_exact_check(rng)
log(f"time {time.time()-t0:.1f}s")
out.close()
