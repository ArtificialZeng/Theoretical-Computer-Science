"""Evidence for Cor (i) of insert v4 (wheels have disc <= 2): SAT encoding of lem:cover with D=3
for wheels W_m (hub 0, rim 1..m) with small bundle sizes.  UNSAT = consistent.
Run: python3 -I wheel_disc_sat_ref.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fan_disc_sat_ref import build
from sat_cube_ref import solve
HERE = os.path.dirname(os.path.abspath(__file__))
out = open(os.path.join(HERE, "log_wheel_disc_sat.txt"), "w")
def wheel(m):
    E = [(0, i) for i in range(1, m + 1)] + [(i, i % m + 1) for i in range(1, m + 1)]
    return m + 1, E
cases = []
for m in (3, 4, 5, 6):
    nv, E = wheel(m)
    cases.append((f"W_{m} bundles 1", nv, E, {}, {}))
nv, E = wheel(4); cases.append(("W_4 spokes 2", nv, E, {e: 2 for e in E if e[0] == 0}, {}))
nv, E = wheel(5); cases.append(("W_5 rim 2, hub private 1", nv, E, {e: 2 for e in E if e[0] != 0}, {0: 1}))
nv, E = wheel(3); cases.append(("W_3=K_4 all bundles 2", nv, E, {e: 2 for e in E}, {}))
for name, nvv, EE, bs, pr in cases:
    cnf, m = build(nvv, EE, bs, pr, 3)
    res, _, dt = solve(cnf, "kissat", "wheel")
    msg = f"{name}: items={m} clauses={len(cnf.clauses)} kissat: {res} ({dt:.1f}s)"
    print(msg, flush=True); out.write(msg + "\n")
out.close()
