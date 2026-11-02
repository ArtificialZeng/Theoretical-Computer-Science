#!/usr/bin/env python3
"""Exhaustive check of the near-dichotomy with the weak hypothesis dist(P,N) >= 2 (dense2_claude).
Enumerate all near-loop-free W in Q_n (DFS over sets, adding points in increasing order, pruning
when a near-loop appears, since containing a near-loop is monotone); for each W, label every
1-step component of the complement P or N in all ways (exactly the labellings with dist(P,N)>=2
and cube = P u W u N); check that W u N or W u P has no near-loop."""
import sys, itertools
n = int(sys.argv[1]); N = 1 << n; full = N - 1; ALL = (1 << N) - 1
pc = [bin(i).count("1") for i in range(N)]
NB2 = [[y for y in range(N) if 1 <= pc[x ^ y] <= 2] for x in range(N)]
NB1 = [[x ^ (1 << i) for i in range(n)] for x in range(N)]
CLOSE = [[x] + NB1[x] for x in range(N)]   # points within distance 1
def nearloop(mask):
    seen = 0
    m = mask
    while m:
        z = (m & -m).bit_length() - 1
        m &= m - 1
        if seen >> z & 1: continue
        comp = 1 << z; st = [z]; seen |= 1 << z
        while st:
            y = st.pop()
            for y2 in NB2[y]:
                if mask >> y2 & 1 and not seen >> y2 & 1:
                    seen |= 1 << y2; comp |= 1 << y2; st.append(y2)
        c = comp
        while c:
            a = (c & -c).bit_length() - 1; c &= c - 1
            for b in CLOSE[a ^ full]:
                if comp >> b & 1: return True
    return False
def comps1(mask):
    out = []; seen = 0; m = mask
    while m:
        z = (m & -m).bit_length() - 1; m &= m - 1
        if seen >> z & 1: continue
        comp = 1 << z; st = [z]; seen |= 1 << z
        while st:
            y = st.pop()
            for y2 in NB1[y]:
                if mask >> y2 & 1 and not seen >> y2 & 1:
                    seen |= 1 << y2; comp |= 1 << y2; st.append(y2)
        out.append(comp)
    return out
cntW = 0; cntL = 0; bad = 0; nontriv = 0
def check(W):
    global cntL, bad, nontriv
    cs = comps1(ALL ^ W)
    if len(cs) > 1: nontriv += 1
    for asg in itertools.product((0, 1), repeat=len(cs)):
        P = 0; Nn = 0
        for c, a in zip(cs, asg):
            if a: Nn |= c
            else: P |= c
        cntL += 1
        if nearloop(W | Nn) and nearloop(W | P):
            bad += 1
            if bad < 5: print("VIOLATION", bin(W), bin(P), bin(Nn))
def dfs(W, start):
    global cntW
    cntW += 1
    check(W)
    for x in range(start, N):
        W2 = W | (1 << x)
        if not nearloop(W2):
            dfs(W2, x + 1)
dfs(0, 0)
print("n=%d: %d near-loop-free W (incl. empty), %d with disconnected complement, %d labellings, %d violations" % (n, cntW, nontriv, cntL, bad))
