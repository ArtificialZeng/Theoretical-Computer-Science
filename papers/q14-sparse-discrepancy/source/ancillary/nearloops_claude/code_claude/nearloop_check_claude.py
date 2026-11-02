#!/usr/bin/env python3
"""
Exact brute-force checks of the near-loop lemmas (dense2_claude).

near-loop in A (subset of {+-1}^n, points = bitmasks): a walk in A with steps of Hamming length
1 or 2 from z to w with dist(w,-z) <= 1.

  dichotomy : {+-1}^n = P u W u N, dist(P,N) >= 3, W has no near-loop
              ==> (W u N) or (W u P) has no near-loop.          [Lemma C]
  cover     : U u V = cube ==> U or V has a near-loop.           [Lemma D]
  transfer  : psi odd 2-Lipschitz on S u T, l >= 2, antipodal l-path in T ==> some slice
              {|psi(.,rho)| <= l} has a near-loop.               [Lemma E]
Exhaustive for n=3 (dichotomy, cover), random otherwise.  Usage: python3 -I nearloop_check_claude.py
"""
import itertools, random, sys

def pc(a):
    return bin(a).count("1")

def has_nearloop(A, n):
    full = (1 << n) - 1
    A = set(A)
    seen = set()
    for z in A:
        if z in seen:
            continue
        comp = [z]; seen.add(z); st = [z]
        while st:
            y = st.pop()
            for i in range(n):
                for j in range(i, n):
                    y2 = y ^ (1 << i) ^ ((1 << j) if j != i else 0)
                    if y2 in A and y2 not in seen:
                        seen.add(y2); comp.append(y2); st.append(y2)
        cs = set(comp)
        for a in comp:
            m = a ^ full  # -a
            if m in cs:
                return True
            for i in range(n):
                if (m ^ (1 << i)) in cs:
                    return True
    return False

def dist(a, b):
    return pc(a ^ b)

def check_dichotomy_labelling(lab, n):
    N = 1 << n
    P = [x for x in range(N) if lab[x] == 1]
    Nn = [x for x in range(N) if lab[x] == 2]
    for p in P:
        for q in Nn:
            if dist(p, q) <= 2:
                return None  # not admissible
    W = [x for x in range(N) if lab[x] == 0]
    if has_nearloop(W, n):
        return None
    a = has_nearloop(W + Nn, n)
    b = has_nearloop(W + P, n)
    return not (a and b)

def main():
    rng = random.Random(12345)
    # --- dichotomy, n = 3 exhaustive
    n = 3; N = 1 << n; cnt = 0; bad = 0
    for lab in itertools.product(range(3), repeat=N):
        r = check_dichotomy_labelling(lab, n)
        if r is None:
            continue
        cnt += 1
        if not r:
            bad += 1; print("DICHOTOMY COUNTEREXAMPLE", lab)
    print("dichotomy n=3 exhaustive: %d admissible failing labellings, %d violations" % (cnt, bad))
    # --- dichotomy, n = 4,5 random (structured: random P-blob, N-blob far apart)
    for n in (4, 5):
        N = 1 << n; cnt = 0; bad = 0
        for trial in range(20000 if n == 4 else 4000):
            lab = [0] * N
            # grow random P and N sets respecting dist >= 3
            order = list(range(N)); rng.shuffle(order)
            k = rng.randint(1, N)
            for x in order[:k]:
                c = rng.randint(1, 2)
                other = 3 - c
                if all(not (lab[y] == other and dist(x, y) <= 2) for y in range(N)):
                    lab[x] = c
            r = check_dichotomy_labelling(lab, n)
            if r is None:
                continue
            cnt += 1
            if not r:
                bad += 1; print("DICHOTOMY COUNTEREXAMPLE", n, lab)
        print("dichotomy n=%d random: %d failing labellings tested, %d violations" % (n, cnt, bad))
    # --- cover, n = 3 exhaustive over (U,V) with U u V = cube: each point in U only, V only, both
    n = 3; N = 1 << n; bad = 0; cnt = 0
    for lab in itertools.product(range(3), repeat=N):
        U = [x for x in range(N) if lab[x] in (0, 2)]
        V = [x for x in range(N) if lab[x] in (1, 2)]
        cnt += 1
        if not has_nearloop(U, n) and not has_nearloop(V, n):
            bad += 1; print("COVER COUNTEREXAMPLE", lab)
    print("cover n=3 exhaustive: %d covers, %d violations" % (cnt, bad))
    for n in (4, 5, 6):
        N = 1 << n; bad = 0; T = 20000 if n < 6 else 3000
        for trial in range(T):
            p = rng.random()
            lab = [rng.choices((0, 1, 2), weights=(1, 1, p))[0] for _ in range(N)]
            U = [x for x in range(N) if lab[x] in (0, 2)]
            V = [x for x in range(N) if lab[x] in (1, 2)]
            if not has_nearloop(U, n) and not has_nearloop(V, n):
                bad += 1; print("COVER COUNTEREXAMPLE", n, lab)
        print("cover n=%d random: %d covers, %d violations" % (n, T, bad))
    # --- transfer: psi = signed distance certificate of random P with dist(P,-P) >= l+1
    for (nS, nT, l) in ((3, 2, 2), (4, 2, 2), (4, 3, 2), (5, 3, 2), (4, 3, 3), (5, 4, 3), (5, 4, 2)):
        n = nS + nT; N = 1 << n; full = N - 1; fS = (1 << nS) - 1; fT = (1 << nT) - 1
        bad = 0; tests = 0
        for trial in range(300):
            # random maximal-ish P with dist(x,-y) >= l+1 for x,y in P
            P = []
            order = list(range(N)); rng.shuffle(order)
            for x in order:
                if all(n - pc(x ^ y) >= l + 1 for y in P) and n - 0 >= l + 1:
                    if rng.random() < 0.7:
                        P.append(x)
            Ps = set(P); Ms = set(x ^ full for x in P)
            # psi = dist(.,-P) - dist(.,P)
            def psi(x):
                if not P:
                    return 0
                return min(pc(x ^ m) for m in Ms) - min(pc(x ^ p) for p in Ps)
            vals = [psi(x) for x in range(N)]
            # random antipodal l-paths in T
            for pt in range(5):
                start = rng.randrange(1 << nT); cur = start; path = [cur]
                for _ in range(rng.randint(0, 4)):
                    bits = rng.sample(range(nT), rng.randint(1, min(l, nT)))
                    for b in bits: cur ^= 1 << b
                    path.append(cur)
                tgt = start ^ fT
                while cur != tgt:
                    diff = [b for b in range(nT) if ((cur ^ tgt) >> b) & 1]
                    for b in rng.sample(diff, min(len(diff), rng.randint(1, l))): cur ^= 1 << b
                    path.append(cur)
                ok = False
                for rho in path:
                    Wsl = [s for s in range(1 << nS) if abs(vals[s | (rho << nS)]) <= l]
                    if has_nearloop(Wsl, nS):
                        ok = True; break
                tests += 1
                if not ok:
                    bad += 1; print("TRANSFER COUNTEREXAMPLE", nS, nT, l, P, path)
        print("transfer nS=%d nT=%d l=%d: %d (psi,path) pairs, %d violations" % (nS, nT, l, tests, bad))

if __name__ == "__main__":
    main()
