"""Near-dichotomy on Q_n (n = 6, 7) by counterexample-guided search.
Candidates: Q_n = P + W + N, dist(P,N) >= 3, P,N nonempty, W near-loop-free (exact SAT
encoding), corner 0 in P (WLOG by vertex-transitivity of the signed-permutation group,
which commutes with negation; P is nonempty in any counterexample).
A candidate is a counterexample iff W+P and W+N both contain near-loops (checked in Python).
Otherwise, if A = W+P (or W+N) has no near-loop, every candidate with W'+P' (or W'+N')
contained in A, or in -A, is excluded; we add the blocking clauses
    OR_{z not in A} (w_z or p_z),  OR_{z not in A} (w_z or q_z)   and the same for -A.
Terminates with UNSAT (near-dichotomy verified for this n) or a counterexample.
Run: python3 -I neardich_cegar_ref.py n [solver] [maxiter]"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_ref import Cube
from sat_cube_ref import CNF, solve, no_nearloop

HERE = os.path.dirname(os.path.abspath(__file__))
n = int(sys.argv[1])
solver = sys.argv[2] if len(sys.argv) > 2 else "cadical"
maxiter = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
nimg = int(sys.argv[4]) if len(sys.argv) > 4 else 0
mindist = int(sys.argv[5]) if len(sys.argv) > 5 else 3   # sanity probe: 2
import random, itertools
rng = random.Random(1)
c = Cube(n)
perms = list(itertools.permutations(range(n)))


def apply(g, A):
    pi, eps = g
    r = 0
    for z in c.bits(A):
        y = 0
        for i in range(n):
            if z >> i & 1:
                y |= 1 << pi[i]
        r |= 1 << (y ^ eps)
    return r


def maximal_extension(A):
    order = list(range(N))
    rng.shuffle(order)
    for v in order:
        if not (A >> v) & 1 and not c.has_nearloop(A | (1 << v)):
            A |= 1 << v
    return A
N = c.N
cnf = CNF()
p = [cnf.var() for _ in range(N)]
q = [cnf.var() for _ in range(N)]
w = [cnf.var() for _ in range(N)]
for z in range(N):
    cnf.add([-p[z], -q[z]])
    cnf.add([w[z], p[z], q[z]])
    cnf.add([-w[z], -p[z]])
    cnf.add([-w[z], -q[z]])
    for y in ([z] + c.nb2[z] if mindist == 3 else [z] + c.nb1[z]):
        cnf.add([-p[z], -q[y]])
cnf.add(q[:])
cnf.add([p[0]])
no_nearloop(cnf, c, w)
log = open(os.path.join(HERE, f"log_neardich_cegar_n{n}_d{mindist}.txt"), "a")
t0 = time.time()
it = 0
blocked = set()
result = None
while it < maxiter:
    it += 1
    res, model, dt = solve(cnf, solver, f"cegar{n}")
    if res != "SATISFIABLE":
        result = res
        break
    P = sum(1 << z for z in range(N) if p[z] in model)
    Q = sum(1 << z for z in range(N) if q[z] in model)
    W = c.full ^ P ^ Q
    assert not c.has_nearloop(W)
    nlP = c.has_nearloop(W | P)
    nlN = c.has_nearloop(W | Q)
    if nlP and nlN:
        result = "COUNTEREXAMPLE"
        log.write(f"COUNTEREXAMPLE P={c.bits(P)} N={c.bits(Q)}\n")
        break
    added = 0
    for A, ok in ((W | P, nlP), (W | Q, nlN)):
        if ok:
            continue
        M = maximal_extension(A)
        imgs = [M, c.negset(M)]
        for _ in range(nimg):
            g = (rng.choice(perms), rng.randrange(N))
            imgs.append(apply(g, M))
        for B in imgs:
            if B in blocked:
                continue
            blocked.add(B)
            outside = [z for z in range(N) if not (B >> z) & 1]
            cnf.add([w[z] for z in outside] + [p[z] for z in outside])
            cnf.add([w[z] for z in outside] + [q[z] for z in outside])
            added += 1
    if added == 0:
        result = "STUCK"
        break
    if it % 25 == 0:
        msg = f"iter {it}: blocked sets {len(blocked)}, last |W|={bin(W).count('1')} |P|={bin(P).count('1')} |N|={bin(Q).count('1')}, elapsed {time.time()-t0:.0f}s"
        print(msg, flush=True)
        log.write(msg + "\n")
        log.flush()
msg = f"near-dichotomy CEGAR n={n} mindist={mindist} nimg={nimg} solver={solver}: result={result} after {it} iterations, {len(blocked)} blocked sets, time {time.time()-t0:.0f}s"
print(msg)
log.write(msg + "\n")
log.close()
