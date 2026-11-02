"""Is the near-dichotomy ever non-trivial?  SAT search for Q_n = P + W + N with
dist(P,N) >= 3, P and N nonempty, W near-loop-free.  (If UNSAT, then for this n every
near-loop-free W has G_S-connected complement and lem:neardichotomy holds trivially.)
Run: python3 -I nontrivial_split_ref.py n [solver]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from sat_cube_ref import CNF, solve, no_nearloop
n = int(sys.argv[1]); solver = sys.argv[2] if len(sys.argv) > 2 else "kissat"
c = Cube(n); N = c.N
cnf = CNF()
p = [cnf.var() for _ in range(N)]; q = [cnf.var() for _ in range(N)]; w = [cnf.var() for _ in range(N)]
for z in range(N):
    cnf.add([-p[z], -q[z]]); cnf.add([w[z], p[z], q[z]]); cnf.add([-w[z], -p[z]]); cnf.add([-w[z], -q[z]])
    for y in [z] + c.nb2[z]:
        cnf.add([-p[z], -q[y]])
cnf.add(p[:]); cnf.add(q[:])
cnf.add([p[0]])   # symmetry: WLOG corner 0 in P (cube is vertex-transitive)
no_nearloop(cnf, c, w)
res, model, dt = solve(cnf, solver, f"nontriv{n}{solver}")
msg = f"nontrivial split n={n} {solver}: vars={cnf.nv} clauses={len(cnf.clauses)} result={res} time={dt:.1f}s"
if res == "SATISFIABLE":
    P = sum(1 << z for z in range(N) if p[z] in model); Q = sum(1 << z for z in range(N) if q[z] in model)
    W = c.full ^ P ^ Q
    msg += (f"\n  |P|={bin(P).count('1')} |N|={bin(Q).count('1')} |W|={bin(W).count('1')} nl(W)={c.has_nearloop(W)}"
            f" nl(W+N)={c.has_nearloop(W|Q)} nl(W+P)={c.has_nearloop(W|P)}\n  P={c.bits(P)}\n  N={c.bits(Q)}")
print(msg)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_nontrivial_split.txt"), "a").write(msg + "\n")
