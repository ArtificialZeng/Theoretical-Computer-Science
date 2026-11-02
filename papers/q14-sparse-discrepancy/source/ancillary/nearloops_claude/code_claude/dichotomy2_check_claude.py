#!/usr/bin/env python3
"""Stronger random test of Lemma C (near-dichotomy) and of the component-tree property in the
2-step graph (dense2_claude).  W is grown randomly subject to 'no near-loop'; the 2-step
components of the complement are then labelled P/N in all possible ways (any such labelling has
dist(P,N) >= 3)."""
import random, itertools, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from nearloop_check_claude import has_nearloop, pc

def comps(A, n):
    A = set(A); seen = set(); out = []
    for z in A:
        if z in seen: continue
        c = [z]; seen.add(z); st = [z]
        while st:
            y = st.pop()
            for y2 in A:
                if y2 not in seen and 1 <= pc(y ^ y2) <= 2:
                    seen.add(y2); c.append(y2); st.append(y2)
        out.append(c)
    return out

def is_tree(lab, n):
    N = 1 << n
    classes = {}
    nodes = []
    for L in set(lab):
        for c in comps([x for x in range(N) if lab[x] == L], n):
            nodes.append((L, set(c)))
    E = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if any(1 <= pc(a ^ b) <= 2 for a in nodes[i][1] for b in nodes[j][1]):
                E += 1
    # connected (cube 2-step graph connected) => tree iff E = V - 1
    return E == len(nodes) - 1

rng = random.Random(7)
for n in (4, 5, 6):
    N = 1 << n; tests = 0; bad = 0; badtree = 0
    for trial in range({4: 3000, 5: 1500, 6: 300}[n]):
        W = []
        order = list(range(N)); rng.shuffle(order)
        target = rng.randint(1, N // 2)
        for x in order:
            if len(W) >= target: break
            if not has_nearloop(W + [x], n):
                W.append(x)
        rest = [x for x in range(N) if x not in set(W)]
        cs = comps(rest, n)
        if len(cs) > 10: cs_assign = [tuple(rng.randint(0, 1) for _ in cs) for _ in range(200)]
        else: cs_assign = list(itertools.product((0, 1), repeat=len(cs)))
        for asg in cs_assign:
            P = [x for c, a in zip(cs, asg) if a == 0 for x in c]
            Nn = [x for c, a in zip(cs, asg) if a == 1 for x in c]
            tests += 1
            if has_nearloop(W + Nn, n) and has_nearloop(W + P, n):
                bad += 1; print("DICHOTOMY VIOLATION", n, W, P, Nn)
            if tests % 50 == 0:
                lab = [0] * N
                for x in P: lab[x] = 1
                for x in Nn: lab[x] = 2
                if not is_tree(lab, n):
                    badtree += 1; print("NOT A TREE", n, lab)
    print("n=%d: %d failing labellings tested, %d dichotomy violations, %d tree violations (sampled)" % (n, tests, bad, badtree))
