#!/usr/bin/env python3
"""
Search for D-covers (= lower-bound witnesses) for the t-sparse nonlinear discrepancy problem.

Model (t arbitrary, given as a hypergraph): items = hyperedges ("edges"), functions = vertices.
Each vertex v reads the items E(v).  A family has discrepancy >= D  iff  there are sets
P_v subset {+-1}^{E(v)} that are D-agreeing (any z,w in P_v satisfy dist(z,-w) >= D, i.e.
dist(z,w) <= d_v - D) such that every global x in {+-1}^E has x|_{E(v)} in P_v or -P_v
for some v.  (Given such P_v, g_v(z) = dist(z,-P_v) - dist(z,P_v) is odd, 2-Lipschitz and
|g_v| >= D on P_v u -P_v; conversely P_v = {g_v > D-1} for an optimal family.)

We solve  EXISTS P  FORALL x  EXISTS v  by CEGAR with a SAT solver (kissat / cadical).
"""
import itertools, subprocess, sys, os, random, tempfile, time
import numpy as np

SOLVER = os.environ.get("SATSOLVER", "kissat")


def popcount_table(d):
    return np.array([bin(i).count("1") for i in range(1 << d)], dtype=np.int64)


class Instance:
    def __init__(self, n, edges):
        """edges: list of tuples of vertex ids (an item relevant to those functions)."""
        self.n = n
        self.edges = [tuple(e) for e in edges]
        self.m = len(edges)
        self.Ev = [[j for j, e in enumerate(self.edges) if v in e] for v in range(n)]
        self.deg = [len(x) for x in self.Ev]



_AP = {}
def agreement_pairs(d, D):
    key = (d, D)
    if key not in _AP:
        pc = popcount_table(d)
        masks = np.nonzero(pc > d - D)[0]
        Z = np.arange(1 << d)
        out = []
        for mk in masks:
            W = Z ^ mk
            sel = Z < W
            out.append(np.stack([Z[sel], W[sel]], axis=1))
        _AP[key] = np.concatenate(out).tolist() if out else []
    return _AP[key]

def build_cnf(inst, D, xs, extra=None):
    """Return (clauses, varmap). xs: iterable of global assignments as int bitmasks over items."""
    var = {}
    nv = 0
    clauses = []
    for v in range(inst.n):
        d = inst.deg[v]
        if d < D:  # P_v must be empty
            continue
        pc = popcount_table(d)
        for z in range(1 << d):
            nv += 1
            var[(v, z)] = nv
        # agreement clauses: z,w with dist(z,w) > d - D cannot both be in P_v
        base = var[(v, 0)]
        for (z, w) in agreement_pairs(d, D):
            clauses.append([-(base + z), -(base + w)])
    full = [(1 << inst.deg[v]) - 1 for v in range(inst.n)]
    for x in xs:
        cl = []
        for v in range(inst.n):
            if inst.deg[v] < D:
                continue
            z = 0
            for k, j in enumerate(inst.Ev[v]):
                if (x >> j) & 1:
                    z |= 1 << k
            cl.append(var[(v, z)])
            cl.append(var[(v, z ^ full[v])])
        clauses.append(cl)
    if extra:
        clauses.extend(extra)
    return clauses, var, nv


def run_sat(clauses, nv, timeout=None):
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as f:
        f.write(f"p cnf {nv} {len(clauses)}\n")
        f.write("".join(" ".join(map(str, c)) + " 0\n" for c in clauses))
        fn = f.name
    cmd = [SOLVER, fn]
    if SOLVER == "kissat":
        cmd = [SOLVER, "-q", fn]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except subprocess.TimeoutExpired:
        os.unlink(fn)
        return None, None
    os.unlink(fn)
    status = None
    model = set()
    for line in out.splitlines():
        if line.startswith("s "):
            status = line.split()[1]
        elif line.startswith("v "):
            for t in line.split()[1:]:
                t = int(t)
                if t > 0:
                    model.add(t)
    return status, model


def local_index_arrays(inst):
    """For each vertex, an array mapping global x (int) -> local z.  Only feasible for m <= ~26."""
    m = inst.m
    X = np.arange(1 << m, dtype=np.int64)
    loc = []
    for v in range(inst.n):
        z = np.zeros(1 << m, dtype=np.int64)
        for k, j in enumerate(inst.Ev[v]):
            z |= ((X >> j) & 1) << k
        loc.append(z)
    return loc


def uncovered(inst, D, P, loc):
    """P[v]: boolean array over local patterns (P_v u -P_v already symmetrized). Return uncovered xs."""
    m = inst.m
    cov = np.zeros(1 << m, dtype=bool)
    for v in range(inst.n):
        if inst.deg[v] < D:
            continue
        cov |= P[v][loc[v]]
    return np.nonzero(~cov)[0]


def cegar(inst, D, seed=0, init=64, maxit=2000, verbose=True, timeout=None):
    rnd = random.Random(seed)
    m = inst.m
    loc = local_index_arrays(inst)
    if m <= int(os.environ.get("FULLM", "21")):
        xs = set(range(1 << (m - 1)))  # x and -x give identical clauses
    else:
        xs = set(rnd.randrange(1 << m) for _ in range(init))
    t0 = time.time()
    for it in range(maxit):
        clauses, var, nv = build_cnf(inst, D, sorted(xs))
        st, model = run_sat(clauses, nv, timeout=timeout)
        if st is None:
            return "TIMEOUT", None
        if st == "UNSATISFIABLE":
            if verbose:
                print(f"  it={it} |xs|={len(xs)} UNSAT -> no {D}-cover  ({time.time()-t0:.1f}s)")
            return "NOCOVER", None
        P = []
        for v in range(inst.n):
            d = inst.deg[v]
            arr = np.zeros(1 << d, dtype=bool)
            if d >= D:
                for z in range(1 << d):
                    if var[(v, z)] in model:
                        arr[z] = True
                        arr[z ^ ((1 << d) - 1)] = True
            P.append(arr)
        unc = uncovered(inst, D, P, loc)
        if len(unc) == 0:
            if verbose:
                print(f"  it={it} |xs|={len(xs)} FOUND {D}-cover ({time.time()-t0:.1f}s)")
            Psets = []
            for v in range(inst.n):
                d = inst.deg[v]
                Psets.append([z for z in range(1 << d) if d >= D and var[(v, z)] in model])
            return "COVER", Psets
        # add a few counterexamples
        pick = unc if len(unc) <= 8 else np.random.default_rng(it).choice(unc, 8, replace=False)
        for x in pick:
            xs.add(int(x))
        if verbose and it % 20 == 0:
            print(f"  it={it} |xs|={len(xs)} uncovered={len(unc)} ({time.time()-t0:.1f}s)")
    return "MAXIT", None


def verify_cover(inst, D, Psets):
    """Independent check: build g_v and compute min over x of max_v |g_v|."""
    loc = local_index_arrays(inst)
    m = inst.m
    best = np.zeros(1 << m)
    for v in range(inst.n):
        d = inst.deg[v]
        pc = popcount_table(d)
        Z = np.arange(1 << d)
        full = (1 << d) - 1
        if d < D or not Psets[v]:
            continue
        P = np.array(Psets[v])
        # check agreement
        for a in P:
            for b in P:
                assert pc[a ^ (b ^ full)] >= D
        dP = np.min(pc[(Z[:, None] ^ P[None, :])], axis=1)
        dmP = np.min(pc[(Z[:, None] ^ (P[None, :] ^ full))], axis=1)
        g = dmP - dP
        # check odd and 2-Lipschitz
        assert np.all(g[Z ^ full] == -g)
        for k in range(d):
            assert np.all(np.abs(g - g[Z ^ (1 << k)]) <= 2)
        best = np.maximum(best, np.abs(g[loc[v]]))
    return best.min()


if __name__ == "__main__":
    pass
