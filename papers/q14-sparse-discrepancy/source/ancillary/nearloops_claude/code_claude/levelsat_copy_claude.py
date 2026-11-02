#!/usr/bin/env python3
"""
Leveled cover search (dense_claude).

A 2-sparse (or general) support structure: items = tuples of vertices reading them.
Each vertex v has a level l_v >= 1.  The leveled system is *good* if every family of odd
2-Lipschitz g_v (support U_v) has x with |g_v(x)| <= l_v for all v.  By the cover lemma
(paper Lemma lem:cover with D_v = l_v + 1) it is NOT good iff there are P_v in {+-1}^{U_v}
with dist(z,-z') >= l_v + 1 for z,z' in P_v and every x has some v with x|U_v in P_v u -P_v.

We build the full CNF (2^{m-1} cover clauses) and call kissat.  SAT => counterexample
(verified by recomputing the min-max with g_v = dist(.,-P_v) - dist(.,P_v)).
UNSAT => the leveled structure is good (modulo solver correctness).
"""
import itertools, subprocess, sys, os, tempfile
import numpy as np

SOLVER = os.environ.get("SATSOLVER", "kissat")


def popcount(a):
    return bin(a).count("1")


def run(items, levels, verbose=True, timeout=1200):
    n = len(levels)
    m = len(items)
    Ev = [[j for j, e in enumerate(items) if v in e] for v in range(n)]
    deg = [len(x) for x in Ev]
    var = {}
    nv = 0
    clauses = []
    for v in range(n):
        d = deg[v]
        D = levels[v] + 1
        if d < D:
            continue  # P_v empty: dist(z,-z) = d < D
        for z in range(1 << d):
            nv += 1
            var[(v, z)] = nv
        full = (1 << d) - 1
        for z in range(1 << d):
            for w in range(z + 1, 1 << d):
                # dist(z,-w) = d - dist(z,w) must be >= D
                if d - popcount(z ^ w) < D:
                    clauses.append([-var[(v, z)], -var[(v, w)]])
    active = [v for v in range(n) if deg[v] >= levels[v] + 1]
    fullv = {v: (1 << deg[v]) - 1 for v in active}
    for x in range(1 << (m - 1)):
        cl = []
        for v in active:
            z = 0
            for k, j in enumerate(Ev[v]):
                if (x >> j) & 1:
                    z |= 1 << k
            cl.append(var[(v, z)])
            cl.append(var[(v, z ^ fullv[v])])
        if not cl:
            return ("UNSAT-trivial", None)
        clauses.append(cl)
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as f:
        f.write("p cnf %d %d\n" % (nv, len(clauses)))
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
        fn = f.name
    try:
        out = subprocess.run([SOLVER, "-q", fn] if SOLVER == "kissat" else [SOLVER, fn],
                             capture_output=True, text=True, timeout=timeout).stdout
    except subprocess.TimeoutExpired:
        os.unlink(fn)
        return ("TIMEOUT", None)
    os.unlink(fn)
    if "s UNSATISFIABLE" in out:
        return ("UNSAT", None)
    if "s SATISFIABLE" in out:
        vals = set()
        for line in out.splitlines():
            if line.startswith("v "):
                for t in line[2:].split():
                    t = int(t)
                    if t > 0:
                        vals.add(t)
        P = {v: [z for z in range(1 << deg[v]) if var[(v, z)] in vals] for v in active}
        # verify
        worst = verify(items, levels, Ev, deg, P)
        return ("SAT", (P, worst))
    return ("UNKNOWN", out[-500:])


def verify(items, levels, Ev, deg, P):
    """Compute min_x max_v (|g_v(x)| - l_v) with g_v = dist(.,-P_v) - dist(.,P_v)."""
    n = len(levels)
    m = len(items)
    G = {}
    for v, Pv in P.items():
        d = deg[v]
        full = (1 << d) - 1
        if not Pv:
            G[v] = np.zeros(1 << d)
            continue
        Z = np.arange(1 << d)
        pc = np.array([popcount(i) for i in range(1 << d)])
        dP = np.min(np.stack([pc[Z ^ p] for p in Pv]), axis=0)
        dN = np.min(np.stack([pc[Z ^ (p ^ full)] for p in Pv]), axis=0)
        G[v] = dN - dP
    best = None
    for x in range(1 << m):
        worst = -1e9
        for v in G:
            z = 0
            for k, j in enumerate(Ev[v]):
                if (x >> j) & 1:
                    z |= 1 << k
            worst = max(worst, abs(G[v][z]) - levels[v])
        if best is None or worst < best:
            best = worst
    return best  # > 0 means genuine counterexample


def multigraph(n, bundles, private=None):
    """bundles: dict {(u,v): size}; private: dict {v: size}. Return item list."""
    items = []
    for (u, v), s in bundles.items():
        items += [(u, v)] * s
    if private:
        for v, s in private.items():
            items += [(v,)] * s
    return items


if __name__ == "__main__":
    pass
