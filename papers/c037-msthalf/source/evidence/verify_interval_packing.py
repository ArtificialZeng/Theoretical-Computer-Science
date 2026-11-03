"""Separate exact verifier of saved metrics/rectangles/interval integrals.

This is same-worker recomputation, not a fresh mathematical referee.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

root = Path(__file__).resolve().parent
data = json.loads((root/'interval-packing-check.json').read_text())
rectangles = 0
expensive_edges = 0
max_overlap = 0
nonultrametric = 0
for rec in data['records']:
    d,w,r = rec['d'],rec['weights'],rec['r']
    n = len(d)
    assert len(w) == n-1 and all(x>=0 for x in w)
    is_ultra = True
    for i in range(n):
        assert d[i][i] == 0
        for j in range(n):
            assert d[i][j] == d[j][i] and (i==j or d[i][j]>0)
            for k in range(n):
                assert d[i][j] <= d[i][k]+d[k][j]
                if d[i][j] > max(d[i][k],d[k][j]):
                    is_ultra = False
    nonultrametric += not is_ultra
    t = [sum(w[:i]) for i in range(n)]
    adj = [sum(1<<j for j in range(n) if i!=j and d[i][j]<=abs(t[i]-t[j]))
           for i in range(n)]
    minimum = r*r
    # Directly enumerate BOTH sides; do not reuse the generator's degree-sort test.
    for aa in combinations(range(n),r):
        mask = sum(1<<i for i in aa)
        others = [i for i in range(n) if not(mask>>i&1)]
        degrees = {j:(adj[j]&mask).bit_count() for j in others}
        for bb in combinations(others,r):
            minimum = min(minimum,sum(degrees[j] for j in bb))
            rectangles += 1
    assert minimum == rec['minimum'] and minimum >= rec['required']
    eta = F(minimum,r*r)
    D = [d[i][i+1] for i in range(n-1)]
    events = {}
    costly = []
    for i,length in enumerate(D):
        if length > 64*w[i]:
            costly.append(length)
            left,right = 64*t[i]-length,64*t[i]+length
            events.setdefault(left,[0,0])[0] += 1
            events.setdefault(right,[0,0])[1] += 1
    depth = area = peak = 0
    previous = None
    for x,(starts,ends) in sorted(events.items()):
        if previous is not None:
            area += depth*(x-previous)
        depth += starts
        peak = max(peak,depth)  # closed intervals: starts precede ends
        depth -= ends
        previous = x
    assert depth == 0 and area == 2*sum(costly)
    L = -((-2*r*eta.denominator)//eta.numerator)
    assert peak < 2*(L+r)
    assert peak <= 8*r/eta
    assert sum(costly) <= 256*r/eta*sum(w)+8*r/eta*max(D)
    have = {0}
    M = 0
    while len(have)<n:
        length,vertex = min((d[i][j],j) for i in have for j in range(n) if j not in have)
        M += length
        have.add(vertex)
    assert max(D) <= M
    assert sum(D) <= 320*r/eta*sum(w)+8*r/eta*M
    expensive_edges += len(costly)
    max_overlap = max(max_overlap,peak)

summary = dict(job_id=data['job_id'], metric_witnesses=len(data['records']),
               nonultrametric_witnesses=nonultrametric,
               exact_rectangles_checked=rectangles,
               expensive_edges_checked=expensive_edges,
               largest_observed_interval_overlap=max_overlap,
               repair_masks_checked=sum(x['masks'] for x in data['repair_masks']),
               checks=['all metric triangles', 'full disjoint r-by-r rectangles',
                       'interval integral identity and closed-endpoint overlap',
                       'general metric transfer inequality',
                       'benchmark mask enumeration output'],
               limitations=['General metric families/orders/weights sampled, not exhaustive.',
                            'Coordinate descent has no global optimization guarantee.',
                            'Finite verification does not prove the universal theorem.',
                            'No fresh referee or novelty/STOC acceptance.'])
(root/'interval-packing-validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
