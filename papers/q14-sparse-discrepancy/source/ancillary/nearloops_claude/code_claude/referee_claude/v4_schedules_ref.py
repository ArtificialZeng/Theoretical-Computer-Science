"""Insert v4 combinatorics.
 (1) K_n deletion-schedule DP with the v4 cheap-deletion rule (members of J may have any level
     >= 1; only N(h)\\J needs level >= 2; J nonempty needs l_h >= 2), with and without the
     five-vertex base of Thm H; least uniform level for K_n.
 (2) The explicit two-step reductions of Cor (iv): K_{2L} at level L -> K_{2L-2} at levels >= L-1,
     and K_{2L+1} at level L -> K_{2L-1} at level L-1, checked step by step for L = 3..30.
 (3) The wheel schedule of Cor (i): (p,a) values and a simulation with the v4 rule, m = 3..40.
 (4) Theorem thm:orient: random graphs, random orientation with max in-degree k (from a random
     orientation), random ordering; check lem:schedule (v4) hypotheses with l = k+1 and simulate.
Run: python3 -I v4_schedules_ref.py [nmax_dp]
"""
import sys, os, random, time
from functools import lru_cache
from itertools import product

sys.setrecursionlimit(100000)
HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_v4_schedules.txt"), "w")


def log(s):
    print(s, flush=True)
    out.write(s + "\n")
    out.flush()


def make_good(base5):
    @lru_cache(maxsize=None)
    def good(state):
        m = len(state)
        if m <= 1:
            return True
        if m == 2:
            return max(state) >= 2
        if base5 and m <= 5 and min(state) >= 2:
            return True
        levels = sorted(set(state), reverse=True)
        counts = {v: state.count(v) for v in levels}
        for lh in levels:
            others = dict(counts)
            others[lh] -= 1
            if others[lh] == 0:
                del others[lh]
            vals = sorted(others)
            maxJ = lh if lh >= 2 else 0
            ranges = [range(0, min(others[v], maxJ) + 1) for v in vals]
            for js in product(*ranges):
                if sum(js) > maxJ:
                    continue
                # non-J vertices need level >= 2
                if any(v < 2 and others[v] - j > 0 for v, j in zip(vals, js)):
                    continue
                new = []
                for v, j in zip(vals, js):
                    new += [v] * j + [v - 1] * (others[v] - j)
                m2 = m - 1
                new = tuple(sorted((min(x, m2 + 1) for x in new), reverse=True))
                if good(new):
                    return True
        return False
    return good


def least_uniform(n, good):
    L = 1
    while not good(tuple([min(L, n + 1)] * n)):
        L += 1
    return L


def cheap_step(levels, h, J):
    """apply v4 cheap deletion to complete graph with level list; returns new list or raises."""
    lh = levels[h]
    others = [i for i in range(len(levels)) if i != h]
    assert set(J) <= set(others) and len(J) <= lh and (not J or lh >= 2)
    for i in others:
        if i not in J:
            assert levels[i] >= 2
    new = []
    for i in others:
        new.append(levels[i] if i in J else levels[i] - 1)
    assert min(new) >= 1
    return new


def part2():
    for L in range(3, 31):
        # K_{2L} at level L
        lev = [L] * (2 * L)
        lev = cheap_step(lev, 0, list(range(1, L + 1)))          # J = first L others
        # now indices 0..L-1 have level L (J), L..2L-2 have level L-1
        dropped = [i for i, x in enumerate(lev) if x == L - 1]
        firstJ = [i for i, x in enumerate(lev) if x == L]
        assert len(dropped) == L - 1 and len(firstJ) == L
        h = dropped[0]
        J = dropped[1:] + [firstJ[0]]
        lev = cheap_step(lev, h, J)
        assert len(lev) == 2 * L - 2 and min(lev) >= L - 1
        # K_{2L+1} at level L
        lev = [L] * (2 * L + 1)
        lev = cheap_step(lev, 0, list(range(1, L + 1)))
        dropped = [i for i, x in enumerate(lev) if x == L - 1]
        assert len(dropped) == L
        lev = cheap_step(lev, dropped[0], dropped[1:])
        assert len(lev) == 2 * L - 1 and all(x == L - 1 for x in lev)
    log("(2) Cor (iv) two-step reductions verified step by step for L = 3..30 (v4 cheap rule)")


def simulate_schedule(n, edges, order, mark, level):
    pos = {v: i for i, v in enumerate(order)}
    lev = dict(level)
    alive = set(range(n))
    E = {frozenset(e): m for e, m in zip(edges, mark)}
    for h in order:
        nb = [u for u in alive if u != h and frozenset((h, u)) in E]
        J = [u for u in nb if E[frozenset((h, u))] == "A"]
        if len(J) > lev[h] or (J and lev[h] < 2) or lev[h] < 1:
            return False
        if any(lev[u] < 2 for u in nb if u not in J):
            return False
        if any(lev[u] < 1 for u in J):
            return False
        for u in nb:
            if u not in J:
                lev[u] -= 1
        alive.remove(h)
    return True


def ap(n, edges, order, mark):
    pos = {v: i for i, v in enumerate(order)}
    a = [0] * n
    p = [0] * n
    for (u, v), m in zip(edges, mark):
        e, l = (u, v) if pos[u] < pos[v] else (v, u)
        if m == "A":
            a[e] += 1
        else:
            p[l] += 1
    return a, p


def part3():
    bad = 0
    for m in range(3, 41):
        h = m
        edges = [(i, (i + 1) % m) for i in range(m)] + [(i, h) for i in range(m)]
        order = list(range(1, m)) + [0, h]
        mark = []
        for (u, v) in edges:
            s = {u, v}
            mark.append("P" if s == {0, 1} or s == {0, h} else "A")
        a, p = ap(m + 1, edges, order, mark)
        vals = [(p[v], a[v]) for v in range(m + 1)]
        ok_vals = all(vals[i] == (0, 2) for i in range(1, m)) and vals[0] == (1, 0) and vals[h] == (1, 0)
        ok_hyp = all(2 >= p[v] + max(1, a[v]) and (a[v] == 0 or 2 >= p[v] + 2) for v in range(m + 1))
        ok_sim = simulate_schedule(m + 1, edges, order, mark, {v: 2 for v in range(m + 1)})
        if not (ok_vals and ok_hyp and ok_sim):
            bad += 1
            log(f"   wheel m={m}: vals={vals} hyp={ok_hyp} sim={ok_sim}")
    log(f"(3) wheel schedules m=3..40 (level 2, v4 rule): failures {bad}")


def part4(rng):
    bad = 0
    T = 4000
    for _ in range(T):
        n = rng.randint(1, 14)
        edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < rng.uniform(0.1, 0.9)]
        heads = [rng.choice(e) for e in edges]
        indeg = [0] * n
        for hd in heads:
            indeg[hd] += 1
        k = max(indeg) if n else 0
        order = list(range(n))
        rng.shuffle(order)
        pos = {v: i for i, v in enumerate(order)}
        mark = []
        for (u, v), hd in zip(edges, heads):
            earlier = u if pos[u] < pos[v] else v
            mark.append("A" if hd == earlier else "P")
        a, p = ap(n, edges, order, mark)
        L = k + 1
        hyp = all(L >= p[v] + max(1, a[v]) and (a[v] == 0 or L >= p[v] + 2) for v in range(n))
        sim = simulate_schedule(n, edges, order, mark, {v: L for v in range(n)})
        if not (hyp and sim and all(p[v] + a[v] == indeg[v] for v in range(n))):
            bad += 1
    log(f"(4) thm:orient: {T} random (graph, orientation, ordering): failures {bad} (must be 0)")


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    part2()
    part3()
    part4(random.Random(3))
    gH = make_good(True)
    g0 = make_good(False)
    for n in range(2, nmax + 1):
        t0 = time.time()
        a = least_uniform(n, gH)
        b = least_uniform(n, g0)
        log(f"(1) K_{n}: least uniform level, v4 rules + five-vertex base: {a} (floor(n/2)={n//2}); "
            f"v4 rules, no Thm H: {b} (ceil(n/2)={(n+1)//2}) ({time.time()-t0:.1f}s)")
    out.close()
