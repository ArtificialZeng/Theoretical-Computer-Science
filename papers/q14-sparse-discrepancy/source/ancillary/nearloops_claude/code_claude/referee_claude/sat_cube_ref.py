"""SAT checks (kissat and cadical) for larger cubes.

 cover n   : is there U subset of Q_n such that neither U nor its complement contains a
             near-loop?  (counterexample to lem:nearcover)
 dich n    : is there a partition Q_n = P + W + N with dist(P,N) >= 3, W near-loop-free,
             W+N and W+P both containing a near-loop? (counterexample to lem:neardichotomy)

"No near-loop in A" is encoded exactly by certificate sets X_z (z in A): X_z contains z,
is closed under G_S-adjacency inside A, and avoids the closed 1-ball around -z.
"A contains a near-loop" is encoded by a unique start a_z and reachability layers.
SAT answers are decoded and re-verified in Python.
Run: python3 -I sat_cube_ref.py cover 5 | dich 5 ...
"""
import sys, os, subprocess, time, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube

HERE = os.path.dirname(os.path.abspath(__file__))


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, cl):
        self.clauses.append(cl)

    def write(self, path):
        with open(path, "w") as f:
            f.write(f"p cnf {self.nv} {len(self.clauses)}\n")
            for cl in self.clauses:
                f.write(" ".join(map(str, cl)) + " 0\n")


def solve(cnf, solver, tag):
    path = os.path.join(HERE, f"tmp_{tag}.cnf")
    cnf.write(path)
    t0 = time.time()
    if solver == "kissat":
        p = subprocess.run(["kissat", "-q", path], capture_output=True, text=True)
    else:
        p = subprocess.run(["cadical", "-q", path], capture_output=True, text=True)
    dt = time.time() - t0
    res = None
    model = set()
    for line in p.stdout.splitlines():
        if line.startswith("s "):
            res = line[2:].strip()
        elif line.startswith("v "):
            for t in line[2:].split():
                v = int(t)
                if v > 0:
                    model.add(v)
    os.remove(path)
    return res, model, dt


def no_nearloop(cnf, c, member):
    """member[y] = literal 'y in A'. Adds clauses forcing A to contain no near-loop."""
    N = c.N
    X = [[cnf.var() for y in range(N)] for z in range(N)]
    for z in range(N):
        cnf.add([-member[z], X[z][z]])
        for y in range(N):
            for y2 in c.nb2[y]:
                cnf.add([-X[z][y], -member[y2], X[z][y2]])
        nz = c.neg(z)
        for y in [nz] + c.nb1[nz]:
            cnf.add([-X[z][y], -member[y]])
    return X


def contains_nearloop(cnf, c, member):
    """Adds clauses forcing A (member literals) to contain a near-loop."""
    N = c.N
    K = N - 1
    a = [cnf.var() for _ in range(N)]
    cnf.add(a[:])
    for i in range(N):
        for j in range(i + 1, N):
            cnf.add([-a[i], -a[j]])
    for z in range(N):
        cnf.add([-a[z], member[z]])
    r = [[cnf.var() for y in range(N)] for t in range(K + 1)]
    for y in range(N):
        cnf.add([-r[0][y], a[y]])
    for t in range(1, K + 1):
        for y in range(N):
            cnf.add([-r[t][y], member[y]])
            cnf.add([-r[t][y], r[t - 1][y]] + [r[t - 1][y2] for y2 in c.nb2[y]])
    e = [cnf.var() for _ in range(N)]
    cnf.add(e[:])
    for y in range(N):
        cnf.add([-e[y], r[K][y]])
        # dist(y, -z) <= 1  <=>  z in ball1(-y)
        ny = c.neg(y)
        cnf.add([-e[y]] + [a[z] for z in [ny] + c.nb1[ny]])
    return a, r, e


def cover(n, solver):
    c = Cube(n)
    cnf = CNF()
    u = [cnf.var() for _ in range(c.N)]
    no_nearloop(cnf, c, u)
    no_nearloop(cnf, c, [-x for x in u])
    res, model, dt = solve(cnf, solver, f"cover{n}{solver}")
    msg = f"cover n={n} solver={solver}: vars={cnf.nv} clauses={len(cnf.clauses)} result={res} time={dt:.1f}s"
    if res == "SATISFIABLE":
        U = sum(1 << z for z in range(c.N) if u[z] in model)
        msg += f"  U={c.bits(U)} check: nl(U)={c.has_nearloop(U)} nl(V)={c.has_nearloop(c.full ^ U)}"
    return msg


def dich(n, solver):
    c = Cube(n)
    cnf = CNF()
    N = c.N
    p = [cnf.var() for _ in range(N)]
    q = [cnf.var() for _ in range(N)]   # q = N-membership
    w = [cnf.var() for _ in range(N)]
    for z in range(N):
        cnf.add([-p[z], -q[z]])
        # w <-> not p and not q
        cnf.add([w[z], p[z], q[z]])
        cnf.add([-w[z], -p[z]])
        cnf.add([-w[z], -q[z]])
        for y in [z] + c.nb2[z]:
            cnf.add([-p[z], -q[y]])
    no_nearloop(cnf, c, w)
    # W+N and W+P contain near-loops
    wn = [cnf.var() for _ in range(N)]
    wp = [cnf.var() for _ in range(N)]
    for z in range(N):
        cnf.add([-wn[z], w[z], q[z]])
        cnf.add([-wp[z], w[z], p[z]])
    contains_nearloop(cnf, c, wn)
    contains_nearloop(cnf, c, wp)
    res, model, dt = solve(cnf, solver, f"dich{n}{solver}")
    msg = f"near-dichotomy n={n} solver={solver}: vars={cnf.nv} clauses={len(cnf.clauses)} result={res} time={dt:.1f}s"
    if res == "SATISFIABLE":
        P = sum(1 << z for z in range(N) if p[z] in model)
        Q = sum(1 << z for z in range(N) if q[z] in model)
        W = c.full ^ P ^ Q
        msg += (f"  P={c.bits(P)} N={c.bits(Q)} check: nl(W)={c.has_nearloop(W)} "
                f"nl(W+N)={c.has_nearloop(W|Q)} nl(W+P)={c.has_nearloop(W|P)}")
    return msg


def selftest(n, solver):
    """Sanity: the encodings must find a partition with neither side containing a 2-loop
    when the defect is 0 -- emulate by checking that the 'contains' encoding is satisfiable
    for A = full cube and the 'no' encoding is satisfiable for a half-cube."""
    c = Cube(n)
    cnf = CNF()
    u = [cnf.var() for _ in range(c.N)]
    # force U = {z : bit0 = 0 and bit1 = 0} (subcube of codim 2, near-loop-free for n>=2)
    for z in range(c.N):
        cnf.add([u[z]] if (z & 3) == 0 else [-u[z]])
    no_nearloop(cnf, c, u)
    r1, _, _ = solve(cnf, solver, "self1")
    cnf2 = CNF()
    u2 = [cnf2.var() for _ in range(c.N)]
    for z in range(c.N):
        cnf2.add([u2[z]] if (z & 1) == 0 else [-u2[z]])   # half cube: contains near-loop
    contains_nearloop(cnf2, c, u2)
    r2, _, _ = solve(cnf2, solver, "self2")
    cnf3 = CNF()
    u3 = [cnf3.var() for _ in range(c.N)]
    for z in range(c.N):
        cnf3.add([u3[z]] if (z & 3) == 0 else [-u3[z]])
    contains_nearloop(cnf3, c, u3)
    r3, _, _ = solve(cnf3, solver, "self3")
    cnf4 = CNF()
    u4 = [cnf4.var() for _ in range(c.N)]
    for z in range(c.N):
        cnf4.add([u4[z]] if (z & 1) == 0 else [-u4[z]])
    no_nearloop(cnf4, c, u4)
    r4, _, _ = solve(cnf4, solver, "self4")
    return (f"selftest n={n} {solver}: codim2-subcube no-nl:{r1} (expect SAT); half-cube contains-nl:{r2} (expect SAT); "
            f"codim2 contains-nl:{r3} (expect UNSAT); half-cube no-nl:{r4} (expect UNSAT)")


if __name__ == "__main__":
    mode = sys.argv[1]
    n = int(sys.argv[2])
    solvers = sys.argv[3:] or ["kissat", "cadical"]
    out = open(os.path.join(HERE, f"log_sat_{mode}_{n}.txt"), "a")
    for s in solvers:
        if mode == "cover":
            m = cover(n, s)
        elif mode == "dich":
            m = dich(n, s)
        else:
            m = selftest(n, s)
        print(m, flush=True)
        out.write(m + "\n")
        out.flush()
    out.close()
