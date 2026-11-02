#!/usr/bin/env python3
"""
Switch configuration test (dense2_claude).

Two labellings lam=(P,W,N), lam'=(P',W',N') of {+-1}^S with
  dist(P,N) >= 3, dist(P',N') >= 3, P cap N' = empty, N cap P' = empty,
  W and W' contain no 2-path z->w with dist(w,-z) <= 1   ("failing slices"),
  and a type switch: P is thick (cube minus P has no 1-loop) and N' is thick.
If UNSAT for all n, failing consecutive slices cannot switch thick-type.

mode 'thick': as above.   mode 'loop2': P contains a 2-loop and N' contains a 2-loop.
Usage: python3 -I switch_sat_claude.py n mode
"""
import sys, os, subprocess, tempfile


def pc(a):
    return bin(a).count("1")


class CNF:
    def __init__(self):
        self.nv = 0
        self.cl = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.cl.append(c)


def no_path(cnf, n, member, step, forbid):
    """member[s]: literal 'in set'. Forbid any step-path from z to w with forbid(z,w)."""
    N = 1 << n
    R = {}
    for z in range(N):
        for y in range(N):
            R[(z, y)] = cnf.new()
    NB = {y: [y2 for y2 in range(N) if 1 <= pc(y ^ y2) <= step] for y in range(N)}
    for z in range(N):
        cnf.add([-member[z], R[(z, z)]])
        for y in range(N):
            r = R[(z, y)]
            cnf.add([-r, member[y]])
            for y2 in NB[y]:
                cnf.add([-r, -member[y2], R[(z, y2)]])
            if forbid(z, y):
                cnf.add([-r])


def solve(n, mode):
    N = 1 << n
    full = N - 1
    cnf = CNF()
    p = [cnf.new() for _ in range(N)]
    q = [cnf.new() for _ in range(N)]  # n
    p2 = [cnf.new() for _ in range(N)]
    q2 = [cnf.new() for _ in range(N)]
    w = [cnf.new() for _ in range(N)]
    w2 = [cnf.new() for _ in range(N)]
    for x in range(N):
        cnf.add([-p[x], -q[x]]); cnf.add([-p2[x], -q2[x]])
        # w <-> not p and not q
        cnf.add([-w[x], -p[x]]); cnf.add([-w[x], -q[x]]); cnf.add([w[x], p[x], q[x]])
        cnf.add([-w2[x], -p2[x]]); cnf.add([-w2[x], -q2[x]]); cnf.add([w2[x], p2[x], q2[x]])
        cnf.add([-p[x], -q2[x]]); cnf.add([-q[x], -p2[x]])
        for y in range(N):
            if pc(x ^ y) <= 2:
                cnf.add([-p[x], -q[y]]); cnf.add([-p2[x], -q2[y]])
    defic = lambda z, y: pc(y ^ (z ^ full)) <= 1
    no_path(cnf, n, w, 2, defic)
    no_path(cnf, n, w2, 2, defic)
    if mode == "thick":
        notp = [cnf.new() for _ in range(N)]
        notq2 = [cnf.new() for _ in range(N)]
        for x in range(N):
            cnf.add([-notp[x], -p[x]]); cnf.add([notp[x], p[x]])
            cnf.add([-notq2[x], -q2[x]]); cnf.add([notq2[x], q2[x]])
        anti = lambda z, y: y == z ^ full
        no_path(cnf, n, notp, 1, anti)
        no_path(cnf, n, notq2, 1, anti)
    else:
        raise SystemExit("mode not implemented")
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as f:
        f.write("p cnf %d %d\n" % (cnf.nv, len(cnf.cl)))
        for c in cnf.cl:
            f.write(" ".join(map(str, c)) + " 0\n")
        fn = f.name
    out = subprocess.run(["kissat", "-q", fn], capture_output=True, text=True).stdout
    os.unlink(fn)
    if "s UNSATISFIABLE" in out:
        return "UNSAT", None
    vals = set()
    for line in out.splitlines():
        if line.startswith("v "):
            for t in line[2:].split():
                t = int(t)
                if t > 0:
                    vals.add(t)
    lab = lambda P, Q: "".join("P" if P[x] in vals else ("N" if Q[x] in vals else ".") for x in range(N))
    return "SAT", (lab(p, q), lab(p2, q2))


if __name__ == "__main__":
    n = int(sys.argv[1]); mode = sys.argv[2]
    r, d = solve(n, mode)
    print("n=%d mode=%s -> %s" % (n, mode, r))
    if d:
        print("  lam  =", d[0]); print("  lam' =", d[1])
