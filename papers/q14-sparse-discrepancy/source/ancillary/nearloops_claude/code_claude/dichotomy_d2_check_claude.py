#!/usr/bin/env python3
"""Near-dichotomy with the WEAKER hypothesis dist(P,N) >= 2 (dense2_claude): W near-loop-free,
complement's 1-step components labelled P/N arbitrarily.  Check: W u N or W u P has no near-loop."""
import random, itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nearloop_check_claude import has_nearloop, pc
def comps1(A, n):
    A = set(A); seen = set(); out = []
    for z in A:
        if z in seen: continue
        c = [z]; seen.add(z); st = [z]
        while st:
            y = st.pop()
            for i in range(n):
                y2 = y ^ (1 << i)
                if y2 in A and y2 not in seen:
                    seen.add(y2); c.append(y2); st.append(y2)
        out.append(c)
    return out
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
for n in (3, 4, 5, 6):
    N = 1 << n; tests = 0; bad = 0; nontriv = 0
    for trial in range({3: 3000, 4: 3000, 5: 1500, 6: 400}[n]):
        W = []
        order = list(range(N)); rng.shuffle(order)
        target = rng.randint(1, N // 2)
        for x in order:
            if len(W) >= target: break
            if not has_nearloop(W + [x], n):
                W.append(x)
        rest = [x for x in range(N) if x not in set(W)]
        cs = comps1(rest, n)
        if len(cs) > 1: nontriv += 1
        asgs = list(itertools.product((0, 1), repeat=len(cs))) if len(cs) <= 10 else [tuple(rng.randint(0,1) for _ in cs) for _ in range(300)]
        for asg in asgs:
            P = [x for c, a in zip(cs, asg) if a == 0 for x in c]
            Nn = [x for c, a in zip(cs, asg) if a == 1 for x in c]
            tests += 1
            if has_nearloop(W + Nn, n) and has_nearloop(W + P, n):
                bad += 1
                if bad <= 3: print("VIOLATION n=%d W=%s P=%s N=%s" % (n, sorted(W), sorted(P), sorted(Nn)))
    print("n=%d: %d labellings (%d W with >1 complement component), %d violations" % (n, tests, nontriv, bad))
