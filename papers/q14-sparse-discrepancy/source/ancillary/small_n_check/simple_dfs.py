#!/usr/bin/env python3
"""
Second, deliberately naive verifier of the leaf boxes: pure Python + Fractions, no numpy,
no MRV, no symmetry breaking.  DFS: take the lowest uncovered corner, try every
(function, sign) whose extended set still satisfies (N1) at some box vertex and (N2).
Used to re-verify every certified leaf produced by cover_bnb.bnb.
"""
import sys, itertools, time
from fractions import Fraction as F
from math import floor
sys.path.insert(0, '/private/tmp/claude-503/-Users-mac-Documents-ChatGPT-STOC-----/40ee0f7a-1229-418b-b9f7-ff7898d5b546/scratchpad/indepH')


def has_cover(j, Js, c, fbox, symbreak=False):
    c = F(c)
    half = c / 2
    dmin = floor(c) + 1
    N = 1 << j
    funcs = [i for i, J in enumerate(Js) if J]
    info = {}
    for i in funcs:
        J = Js[i]; r = len(J)
        verts = list(itertools.product(*[sorted({fbox[k][0], fbox[k][1]}) for k in J]))
        W = []
        for v in verts:
            row = []
            for y in range(1 << r):
                w = F(1)
                for t in range(r):
                    w *= v[t] if (y >> t) & 1 else 1 - v[t]
                row.append(w)
            W.append(row)
        proj = [sum(((x >> k) & 1) << t for t, k in enumerate(J)) for x in range(N)]
        info[i] = (r, W, proj)
    sets = {i: [set(), set()] for i in funcs}

    def ok(i, s, y):
        r, W, proj = info[i]
        opp = sets[i][1 - s]
        if any(bin(y ^ u).count('1') < dmin for u in opp):
            return False
        U = sets[i][s] | {y}
        d = [min(bin(z ^ u).count('1') for u in U) for z in range(1 << r)]
        return any(sum(w * dz for w, dz in zip(row, d)) > half for row in W)

    def covered(x):
        for i in funcs:
            y = info[i][2][x]
            if y in sets[i][0] or y in sets[i][1]:
                return True
        return False

    def rec():
        x = next((x for x in range(N) if not covered(x)), None)
        if x is None:
            return True
        for i in funcs:
            y = info[i][2][x]
            empty = not sets[i][0] and not sets[i][1]
            if symbreak and empty and any(Js[i2] == Js[i] and not sets[i2][0] and not sets[i2][1]
                                          for i2 in funcs if i2 < i):
                continue          # identical-J functions are opened in index order
            for s in ((0,) if (symbreak and empty) else (0, 1)):   # sign symmetry h -> -h
                if ok(i, s, y):
                    sets[i][s].add(y)
                    if rec():
                        return True
                    sets[i][s].discard(y)
        return False
    return rec()


def verify_problem(args):
    from cover_bnb import Problem, bnb
    name, j, Js, c = args
    pr = Problem(j, Js, c)
    leaves = []
    res = bnb(pr, record=leaves)
    t0 = time.time()
    bad = 0
    vol = F(0)
    for b in leaves:
        fb = [(F(lo, 1 << d), F(hi, 1 << d)) for lo, hi, d in b]
        v = F(1)
        for lo, hi in fb:
            v *= hi - lo
        vol += v
        if has_cover(j, Js, c, fb):
            bad += 1
    return name, res['status'], len(leaves), vol == F(1, 2 ** j), bad, round(time.time() - t0, 2)


if __name__ == '__main__':
    from multiprocessing import Pool
    from cover_bnb import full_pattern
    from patterns import all_patterns, to_Js
    jobs = [('K3<=2 j=%d' % j, j, full_pattern(3, j), 2) for j in (1, 2, 3)]
    jobs += [('Claim1 j=%d' % j, j, full_pattern(4, j), 3) for j in (1, 2, 3, 4)]
    P = all_patterns()
    for j in range(6):
        for e in P[j]:
            if len(sys.argv) > 2 and sys.argv[2] == 'skiphard' and e == ((0, 1),) * 5:
                continue   # verified separately in parallel by simple_hard.py
            jobs.append(('C2 %s' % (e,), j, to_Js(e), 2))
    # longest first
    jobs.sort(key=lambda a: -max([len(J) for J in a[2]] + [0]) * 10 - a[1])
    nproc = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    t0 = time.time()
    tot = dict(problems=0, leaves=0, volok=0, bad=0)
    with Pool(nproc) as pool:
        for name, st, nl, vok, bad, tt in pool.imap_unordered(verify_problem, jobs):
            tot['problems'] += 1; tot['leaves'] += nl; tot['volok'] += vok; tot['bad'] += bad
            if True:
                print(name, st, 'leaves', nl, 'volok', vok, 'covers-found', bad, f'{tt}s', flush=True)
    print('TOTAL', tot, 'wall', round(time.time() - t0, 1), flush=True)
