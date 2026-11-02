"""Evidence check of Cor. cor:maxtwod(i) on fans (2-degenerate, not reducible by the old rules):
SAT encoding of Lemma lem:cover (Section 9) with D = 3: some instance with the given supports
has discrepancy > 2 iff there are P_v with 3-agreement covering the cube.  UNSAT = consistent
with disc <= 2.  (Independent re-implementation.)
Run: python3 -I fan_disc_sat_ref.py
"""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sat_cube_ref import CNF, solve

HERE = os.path.dirname(os.path.abspath(__file__))


def build(nverts, edges, bsize, priv, D):
    items = []          # list of support sets
    for (u, v) in edges:
        for _ in range(bsize.get((u, v), 1)):
            items.append((u, v))
    for v, k in priv.items():
        for _ in range(k):
            items.append((v,))
    m = len(items)
    U = [[j for j, sup in enumerate(items) if v in sup] for v in range(nverts)]
    cnf = CNF()
    X = []
    for v in range(nverts):
        k = len(U[v])
        X.append([cnf.var() for _ in range(1 << k)])
        mask = (1 << k) - 1
        for z in range(1 << k):
            for z2 in range(z, 1 << k):
                if (z ^ (z2 ^ mask)).bit_count() < D:   # dist(z, -z2) < D
                    cnf.add([-X[v][z], -X[v][z2]])
    for x in range(1 << m):
        cl = []
        for v in range(nverts):
            loc = 0
            for i, j in enumerate(U[v]):
                if x >> j & 1:
                    loc |= 1 << i
            k = len(U[v])
            cl.append(X[v][loc])
            cl.append(X[v][loc ^ ((1 << k) - 1)])
        cnf.add(cl)
    return cnf, m


def fan(k):
    # apex 0, path 1..k
    edges = [(0, i) for i in range(1, k + 1)] + [(i, i + 1) for i in range(1, k)]
    return k + 1, edges


if __name__ == "__main__":
    out = open(os.path.join(HERE, "log_fan_disc_sat.txt"), "w")
    cases = []
    nv, E = fan(5)
    cases.append(("F_6 (apex+P5), all bundles 1", nv, E, {}, {}))
    cases.append(("F_6, spokes bundles 2", nv, E, {e: 2 for e in E if e[0] == 0}, {}))
    cases.append(("F_6, path bundles 2, 1 private item at apex", nv, E, {e: 2 for e in E if e[0] != 0}, {0: 1}))
    nv7, E7 = fan(6)
    cases.append(("F_7 (apex+P6), all bundles 1", nv7, E7, {}, {}))
    cases.append(("F_7, alternate spokes bundles 2", nv7, E7, {(0, i): 2 for i in (1, 3, 5)}, {}))
    for name, nvv, EE, bs, pr in cases:
        cnf, m = build(nvv, EE, bs, pr, 3)
        for s in ["kissat", "cadical"]:
            res, model, dt = solve(cnf, s, "fan")
            msg = f"{name}: items={m} vars={cnf.nv} clauses={len(cnf.clauses)} {s}: {res} ({dt:.1f}s)"
            print(msg, flush=True)
            out.write(msg + "\n")
            out.flush()
    # sanity: K_2 with one bundle of 2 items at D=2 must be SAT (disc > 1 exists: x1+x2, x1-x2)
    cnf, m = build(2, [(0, 1)], {(0, 1): 2}, {}, 2)
    res, _, _ = solve(cnf, "kissat", "fansanity")
    msg = f"sanity K_2 bundle 2, D=2 (expect SAT): {res}"
    print(msg)
    out.write(msg + "\n")
    cnf, m = build(2, [(0, 1)], {(0, 1): 2}, {}, 3)
    res, _, _ = solve(cnf, "kissat", "fansanity")
    msg = f"sanity K_2 bundle 2, D=3 (expect UNSAT since K_2=2): {res}"
    print(msg)
    out.write(msg + "\n")
    out.close()
