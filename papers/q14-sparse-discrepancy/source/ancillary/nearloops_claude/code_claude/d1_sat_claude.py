#!/usr/bin/env python3
"""
D1 test (dense2_claude).

Question D(delta, lam): let psi be odd 2-Lipschitz on {+-1}^{S u T}, Z = {|psi| <= ell}
(worst case: Z = complement of P u -P with dist(P,-P) >= ell+1).  Is it true that along every
antipodal (ell-lam)-path rho^0..rho^L in {+-1}^T, some slice
    W(rho) = {s : (s,rho) in Z}
contains a 1-path z=s_0,...,s_k=w (all in W, consecutive at Hamming distance 1) with
dist(w,-z) <= delta ?

We search for counterexamples: P (variables) + a FIXED path in T.  For each slice we add
reachability variables R(z,y) forced by Horn clauses; forbidden pairs make the formula UNSAT
whenever a delta-deficient path exists.  SAT => counterexample (re-verified by BFS).

Usage: python3 -I d1_sat_claude.py nS nT ell delta lam [path]
  path: 'jump' (rho, -rho; needs nT <= ell-lam) or 'walk' (flip T coordinates in blocks of
  size ell-lam, i.e. 1->...->-1).
"""
import sys, os, subprocess, tempfile, itertools

SOLVER = os.environ.get("SATSOLVER", "kissat")


def pc(a):
    return bin(a).count("1")


def build_path(nT, step, kind):
    full = (1 << nT) - 1
    if kind.startswith("rand"):
        import random
        seed = int(kind[4:]) if len(kind) > 4 else 0
        rng = random.Random(seed)
        start = rng.randrange(1 << nT)
        target = start ^ full
        path = [start]
        cur = start
        for _ in range(rng.randint(1, 6)):
            k = rng.randint(1, step)
            bits = rng.sample(range(nT), min(k, nT))
            for b in bits:
                cur ^= 1 << b
            path.append(cur)
        while cur != target:
            diff = [b for b in range(nT) if ((cur ^ target) >> b) & 1]
            k = min(len(diff), rng.randint(1, step))
            # occasionally also flip a wrong bit (non-monotone) if budget allows
            bits = rng.sample(diff, k)
            for b in bits:
                cur ^= 1 << b
            path.append(cur)
        return path
    if kind == "jump":
        assert nT <= step
        return [full, 0]
    # walk: start at all ones (bit=1 means +1), flip blocks of `step` coordinates to 0
    path = [full]
    cur = full
    i = 0
    while cur != 0:
        for _ in range(step):
            if i < nT:
                cur &= ~(1 << i)
                i += 1
        path.append(cur)
    return path


def solve(nS, nT, ell, delta, lam, kind="jump", timeout=3600, a=1):
    n = nS + nT
    N = 1 << n
    fullS = (1 << nS) - 1
    fullT = (1 << nT) - 1
    fullX = N - 1
    step = ell - lam
    path = build_path(nT, step, kind)
    nv = 0
    clauses = []
    Pv = {}
    for x in range(N):
        nv += 1
        Pv[x] = nv
    for x in range(N):
        for y in range(x, N):
            # dist(x,-y) = n - dist(x,y)
            if n - pc(x ^ y) <= ell:
                clauses.append([-Pv[x], -Pv[y]])
    # symmetry breaking: none (keep it simple)
    slices = path[:1] if kind == "jump" else path
    NB = {y: [y2 for y2 in range(1 << nS) if 1 <= pc(y ^ y2) <= a] for y in range(1 << nS)}
    Wv = {}
    Rv = {}
    for ti, rho in enumerate(slices):
        for s in range(1 << nS):
            nv += 1
            Wv[(ti, s)] = nv
            x = s | (rho << nS)
            xm = (s ^ fullS) | ((rho ^ fullT) << nS)
            # W <-> not P[x] and not P[xm]
            clauses.append([-nv, -Pv[x]])
            clauses.append([-nv, -Pv[xm]])
            clauses.append([nv, Pv[x], Pv[xm]])
        for z in range(1 << nS):
            for y in range(1 << nS):
                nv += 1
                Rv[(ti, z, y)] = nv
        for z in range(1 << nS):
            clauses.append([-Wv[(ti, z)], Rv[(ti, z, z)]])
            for y in range(1 << nS):
                r = Rv[(ti, z, y)]
                clauses.append([-r, Wv[(ti, y)]])
                for y2 in NB[y]:
                    clauses.append([-r, -Wv[(ti, y2)], Rv[(ti, z, y2)]])
                # forbidden: dist(y, -z) <= delta
                if pc(y ^ (z ^ fullS)) <= delta:
                    clauses.append([-r])
    with tempfile.NamedTemporaryFile("w", suffix=".cnf", delete=False) as f:
        f.write("p cnf %d %d\n" % (nv, len(clauses)))
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
        fn = f.name
    try:
        out = subprocess.run([SOLVER, "-q", fn], capture_output=True, text=True,
                             timeout=timeout).stdout
    except subprocess.TimeoutExpired:
        os.unlink(fn)
        return "TIMEOUT", None
    os.unlink(fn)
    if "s UNSATISFIABLE" in out:
        return "UNSAT", None
    if "s SATISFIABLE" in out:
        vals = set()
        for line in out.splitlines():
            if line.startswith("v "):
                for t in line[2:].split():
                    t = int(t)
                    if t > 0:
                        vals.add(t)
        P = [x for x in range(N) if Pv[x] in vals]
        ok = verify(nS, nT, ell, delta, P, path, a)
        return "SAT", (P, path, ok)
    return "UNKNOWN", out[-300:]


def verify(nS, nT, ell, delta, P, path, a=1):
    n = nS + nT
    fullX = (1 << n) - 1
    fullS = (1 << nS) - 1
    Pset = set(P)
    for x in P:
        for y in P:
            if n - pc(x ^ y) <= ell:
                return "BAD-P"
    bad = Pset | {x ^ fullX for x in P}
    for rho in path:
        W = [s for s in range(1 << nS) if (s | (rho << nS)) not in bad]
        Ws = set(W)
        seen = set()
        for z in W:
            if z in seen:
                continue
            comp = [z]
            seen.add(z)
            st = [z]
            while st:
                y = st.pop()
                for y2 in range(1 << nS):
                    if 1 <= pc(y ^ y2) <= a and y2 in Ws and y2 not in seen:
                        seen.add(y2)
                        comp.append(y2)
                        st.append(y2)
            # deficiency: min over z,w in comp of dist(w,-z)
            dmin = min(pc(a ^ (b ^ fullS)) for a in comp for b in comp)
            if dmin <= delta:
                return "NOT-A-COUNTEREXAMPLE"
    return "VERIFIED"


if __name__ == "__main__":
    nS, nT, ell, delta, lam = map(int, sys.argv[1:6])
    kind = sys.argv[6] if len(sys.argv) > 6 else "jump"
    a = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    res, data = solve(nS, nT, ell, delta, lam, kind, a=a)
    print("nS=%d nT=%d ell=%d delta=%d lam=%d path=%s a=%d -> %s" % (nS, nT, ell, delta, lam, kind, a, res))
    if res == "SAT":
        P, path, ok = data
        print("  verify:", ok, " |P|=", len(P))
        print("  P =", P)
        print("  path =", path)
    sys.stdout.flush()
