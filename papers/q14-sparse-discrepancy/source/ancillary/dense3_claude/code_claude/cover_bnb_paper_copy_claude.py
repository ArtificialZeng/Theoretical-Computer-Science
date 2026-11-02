#!/usr/bin/env python3
"""
Independent exact branch-and-bound checker (written from scratch).

Setting.  J = {0..j-1} fractional coordinates, p in (0,1)^j, product weights
w(x) = prod_k p_k^[x_k=+1] (1-p_k)^[x_k=-1].  Function i reads only the local
coordinates J_i (a tuple of indices into J) and is 2-Lipschitz (Hamming metric on
J_i) with E_w h_i = 0.  "Bad" for i at a corner x means |h_i(x)| > c.

Necessary conditions used for the bad sets U_i^+ = {h_i > c}, U_i^- = {h_i < -c}
(as sets of local patterns in {+-1}^{J_i}):
  (N1) U^+ nonempty  =>  E_w d(X, U^+) > c/2      (same for U^-)
       proof: h(x) >= h(u) - 2 d(x,u) > c - 2 d(x,U^+) for all x, take E_w.
  (N2) d(U^+, U^-) > c, i.e. >= floor(c)+1.
       proof: 2c < h(u)-h(v) <= 2 d(u,v).
Both conditions are inherited by subsets, so the family of "possibly bad"
(U^+,U^-) pairs is down-closed; a cover exists iff a cover by such pairs exists.

Box relaxation: on a closed box P = prod [lo_k,hi_k] subset [0,1/2]^j, the map
p -> E_p d(X,U) is multilinear, so its max over P is attained at a vertex; we call
U possibly-bad-on-P if max_vertex E d > c/2 (each (i,sign) is relaxed separately).
If on P no choice of possibly-bad pairs covers {+-1}^J, then no p in P admits an
all-bad configuration.  All arithmetic is exact: endpoints are dyadic, weights are
integers over den^r with den = 2^D.

Search for a cover: DFS that repeatedly picks the uncovered corner with the fewest
feasible labels (function i, sign s) and adds its local pattern to U_i^s.
Symmetry breaking (complete, see report): the first sign used for each function is
'+', and among functions with identical J_i they are opened in index order.
"""
import sys, time, itertools
from fractions import Fraction
from math import floor
import numpy as np

POP = [bin(i).count('1') for i in range(1 << 12)]
DT = {r: np.array([[POP[u ^ y] for y in range(1 << r)] for u in range(1 << r)], dtype=np.int64)
      for r in range(0, 7)}


class Problem:
    def __init__(self, j, Js, c, name='', sort_coords=False, symbreak=True):
        self.j = j
        self.N = 1 << j
        self.Js = [tuple(J) for J in Js]
        self.n = len(self.Js)
        self.name = name
        cf = Fraction(c)
        self.c = cf
        self.cn, self.cd = cf.numerator, cf.denominator
        self.dmin = floor(cf) + 1          # integer distance > c  <=>  >= floor(c)+1
        self.active = [i for i in range(self.n) if len(self.Js[i]) > 0]
        # projection of full corners to local patterns
        self.proj = [[sum(((x >> k) & 1) << t for t, k in enumerate(J)) for x in range(self.N)]
                     for J in self.Js]
        # lift: local pattern y -> bitmask of full corners projecting to y
        self.lift = []
        for i, J in enumerate(self.Js):
            L = [0] * (1 << len(J))
            for x in range(self.N):
                L[self.proj[i][x]] |= 1 << x
            self.lift.append(L)
        # symmetry classes (identical J_i)
        self.prev_same = [None] * self.n
        for i in range(self.n):
            for i2 in range(i - 1, -1, -1):
                if self.Js[i2] == self.Js[i]:
                    self.prev_same[i] = i2
                    break
        self.symbreak = symbreak
        if not symbreak:
            self.prev_same = [None] * self.n
        self.sort_coords = sort_coords   # only valid if the pattern is invariant
                                         # under all coordinate permutations
        self.full = (1 << self.N) - 1

    # ---- box utilities: box[k] = (lo, hi, d) meaning [lo/2^d, hi/2^d] ----
    def vertex_data(self, box, i):
        J = self.Js[i]
        r = len(J)
        D = max(box[k][2] for k in J)
        den = 1 << D
        ends = []
        for k in J:
            lo, hi, d = box[k]
            sh = D - d
            ends.append(sorted({lo << sh, hi << sh}))
        verts = list(itertools.product(*ends))
        W = []
        for e in verts:
            row = []
            for y in range(1 << r):
                w = 1
                for t in range(r):
                    w *= e[t] if (y >> t) & 1 else den - e[t]
                row.append(w)
            W.append(row)
        # S > thr/(2cd)  <=>  S > floor(thr/(2cd)) for integer S
        thr = (self.cn * den ** r) // (2 * self.cd)
        # int64 safety: sum_y W(y) d(y) <= r * den^r
        safe = (r * den ** r) < (1 << 62) and thr < (1 << 62)
        dt = np.int64 if safe else object
        Wm = np.array(W, dtype=dt)          # V x N
        return Wm, (thr if not safe else np.int64(thr)), dt

    def find_cover(self, box):
        """Return a cover (list of (U+,U-) masks per function) or None."""
        n = self.n
        act = self.active
        WT = [None] * n
        THR = [None] * n
        DTi = [None] * n
        base = [None] * n   # candidate S for the first point: (N x V)
        for i in act:
            Wm, thr, dt = self.vertex_data(box, i)
            r = len(self.Js[i])
            WT[i] = Wm.T.copy()
            THR[i] = thr
            DTi[i] = DT[r].astype(dt)
            base[i] = DTi[i] @ WT[i]      # row y: S_v for U = {y}
        masks = [[0, 0] for _ in range(n)]
        dvec = [[None, None] for _ in range(n)]
        opened = [False] * n
        dmin = self.dmin
        proj = self.proj
        lift = self.lift
        prev_same = self.prev_same
        Nfull = self.N
        full = self.full
        state = {'cov': 0, 'nodes': 0}

        def feas(i, s):
            """For (i,s) return (cand_d matrix or None, feasible bool array over local y)."""
            if dvec[i][s] is None:
                S = base[i]
                cd_ = None
            else:
                cd_ = np.minimum(dvec[i][s][None, :], DTi[i])
                S = cd_ @ WT[i]
            ok = (S > THR[i]).any(axis=1)
            o = dvec[i][1 - s]
            if o is not None:
                ok &= (o >= dmin)
            # cannot add a pattern already in either set (it would already be covered)
            return cd_, ok

        def rec():
            state['nodes'] += 1
            cov = state['cov']
            if cov == full:
                return True
            fc = {}
            def get(i, s):
                key = (i, s)
                if key not in fc:
                    fc[key] = feas(i, s)
                return fc[key]
            labels = []
            for i in act:
                if opened[i] or not self.symbreak:
                    labels.append((i, 0)); labels.append((i, 1))
                else:
                    ps = prev_same[i]
                    if ps is not None and not opened[ps]:
                        continue
                    labels.append((i, 0))
            best = None
            bestopts = None
            unc = full & ~cov
            x = 0
            while unc:
                if unc & 1:
                    opts = []
                    for (i, s) in labels:
                        y = proj[i][x]
                        _, ok = get(i, s)
                        if ok[y]:
                            opts.append((i, s, y))
                    if best is None or len(opts) < len(bestopts):
                        best, bestopts = x, opts
                        if not opts:
                            return False
                unc >>= 1
                x += 1
            for (i, s, y) in bestopts:
                cd_, _ = get(i, s)
                newd = DTi[i][y].copy() if cd_ is None else cd_[y].copy()
                sv = (masks[i][s], dvec[i][s], opened[i], state['cov'])
                masks[i][s] |= 1 << y
                dvec[i][s] = newd
                opened[i] = True
                state['cov'] = sv[3] | lift[i][y]
                if rec():
                    return True
                masks[i][s], dvec[i][s], opened[i], state['cov'] = sv
            return False

        found = rec()
        self.last_nodes = state['nodes']
        if found:
            return [tuple(m) for m in masks]
        return None


def box_str(box):
    return '[' + ', '.join(f'[{Fraction(lo, 1 << d)},{Fraction(hi, 1 << d)}]' for lo, hi, d in box) + ']'


def bnb(prob, max_depth=24, max_boxes=10**7, verbose=False, time_limit=None, record=None,
        full_range=False, root=None):
    """Branch and bound over [0,1/2]^j.  Returns dict with status and stats."""
    j = prob.j
    t0 = time.time()
    if root is None:
        root = [(0, 2, 1) if full_range else (0, 1, 1)] * j      # [0,1] or [0, 1/2]
    stack = [root]
    nboxes = 0
    ncert = 0
    maxd = 0
    nodes = 0
    skipped = 0
    while stack:
        box = stack.pop()
        if prob.sort_coords:
            # region p_0 <= p_1 <= ... : drop boxes with lo_k > hi_{k+1}
            bad = False
            for k in range(j - 1):
                lo1, _, d1 = box[k]
                _, hi2, d2 = box[k + 1]
                if Fraction(lo1, 1 << d1) > Fraction(hi2, 1 << d2):
                    bad = True
                    break
            if bad:
                skipped += 1
                continue
        nboxes += 1
        cov = prob.find_cover(box)
        nodes += prob.last_nodes
        if cov is None:
            ncert += 1
            if record is not None:
                record.append(box)
            continue
        # split the widest coordinate (smallest depth); tie -> lowest index
        k = min(range(j), key=lambda kk: (box[kk][2], kk))
        lo, hi, d = box[k]
        if d >= max_depth:
            return dict(status='FAIL', box=box, cover=cov, boxes=nboxes, certified=ncert,
                        maxdepth=maxd, nodes=nodes, time=time.time() - t0)
        lo2, hi2 = 2 * lo, 2 * hi
        mid = lo + hi
        maxd = max(maxd, d + 1)
        c1 = list(box); c1[k] = (lo2, mid, d + 1)
        c2 = list(box); c2[k] = (mid, hi2, d + 1)
        stack.append(c2)
        stack.append(c1)
        if nboxes >= max_boxes or (time_limit and time.time() - t0 > time_limit):
            return dict(status='ABORT', boxes=nboxes, certified=ncert, maxdepth=maxd,
                        nodes=nodes, time=time.time() - t0, pending=len(stack))
        if verbose and nboxes % 1000 == 0:
            print(f'   ... {nboxes} boxes, {ncert} cert, stack {len(stack)}, maxd {maxd}, '
                  f'{time.time()-t0:.1f}s', flush=True)
    return dict(status='PROVED', boxes=nboxes, certified=ncert, maxdepth=maxd, nodes=nodes,
                time=time.time() - t0, skipped=skipped)


def point_box(ps):
    """Degenerate box at exact dyadic point(s) ps (list of Fractions with power-of-2 denominators)."""
    box = []
    for p in ps:
        p = Fraction(p)
        d = p.denominator.bit_length() - 1
        assert p.denominator == 1 << d
        num = p.numerator
        box.append((num, num, d))
    return box


def full_pattern(n, j):
    return [tuple(range(j))] * n


if __name__ == '__main__':
    pass
