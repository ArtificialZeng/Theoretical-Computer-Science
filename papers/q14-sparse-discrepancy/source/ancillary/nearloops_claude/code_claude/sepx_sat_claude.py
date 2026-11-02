#!/usr/bin/env python3
"""Separation-X test: is there a cover U u V = cube with neither U nor V containing a
2-path z->w with dist(w,-z) <= 1 ?  (dense2_claude)"""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from switch_sat_claude import CNF, no_path, pc
n = int(sys.argv[1]); N = 1 << n; full = N - 1
cnf = CNF()
u = [cnf.new() for _ in range(N)]; v = [cnf.new() for _ in range(N)]
for x in range(N):
    cnf.add([u[x], v[x]])
defic = lambda z, y: pc(y ^ (z ^ full)) <= 1
no_path(cnf, n, u, 2, defic); no_path(cnf, n, v, 2, defic)
with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as f:
    f.write("p cnf %d %d\n" % (cnf.nv, len(cnf.cl)))
    for c in cnf.cl: f.write(" ".join(map(str, c)) + " 0\n")
    fn = f.name
out = subprocess.run(["kissat", "-q", fn], capture_output=True, text=True).stdout
os.unlink(fn)
res = "UNSAT" if "s UNSATISFIABLE" in out else "SAT"
print("n=%d separation-X cover exists? %s" % (n, res))
if res == "SAT":
    vals = set(int(t) for line in out.splitlines() if line.startswith("v ") for t in line[2:].split() if int(t) > 0)
    print("U:", [x for x in range(N) if u[x] in vals]); print("V:", [x for x in range(N) if v[x] in vals])
