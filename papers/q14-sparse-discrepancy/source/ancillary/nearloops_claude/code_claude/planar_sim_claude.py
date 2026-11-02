#!/usr/bin/env python3
"""Planar triangulations (Delaunay of random points): orientation with in-degree <= 3, greedy order,
simulate deletions at level 4 checking Lemma cheap hypotheses (dense2_claude)."""
import random, sys, os
import numpy as np
from scipy.spatial import Delaunay
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from schedule_sim_claude import min_indeg_orientation, simulate
    from mad_sim_claude import greedy_order
rng = np.random.default_rng(11); cnt = 0
for trial in range(200):
    n = int(rng.integers(6, 60))
    pts = rng.random((n, 2))
    tri = Delaunay(pts)
    E = set()
    for s in tri.simplices:
        for i in range(3):
            a, b = sorted((int(s[i]), int(s[(i + 1) % 3])))
            E.add((a, b))
    E = sorted(E)
    assert len(E) <= 3 * n - 6
    k, owner = min_indeg_orientation(n, E)
    assert k <= 3
    for t in range(3):
        order = greedy_order(n, E, owner, 3)
        simulate(n, E, order, owner, {v: 4 for v in range(n)})
        cnt += 1
print("planar: %d schedules on Delaunay triangulations (6<=n<60) at level 4: all hypotheses hold" % cnt)
