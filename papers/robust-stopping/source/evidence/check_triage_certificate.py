"""Recompute the two affine certificates, independently of vertex enumeration.

The unbounded portions are constant g(t) with decreasing affine lower
bounds, so checking the first tail index proves the inequalities for all t.
This deterministic check is not a fresh mathematical referee report.
"""
from fractions import Fraction as Q
import json

b, R = 3, Q(3, 2)
p = {1: Q(2, 5), 2: Q(3, 5)}
K = (R-1)*b


def g(t):
    return sum(v*(b+t-1 if t <= x else x) for x,v in p.items())


def robust(f):
    # Exact all-horizon equivalence is proved in triage-findings.md.
    prefix = [sum(v*(b+t-1-x) for t,v in f.items() if t <= x)
              for x in range(1,b)]
    moment = sum((t-1)*v for t,v in f.items())
    assert sum(f.values()) == 1 and min(f.values()) >= 0
    assert all(h <= (R-1)*x for x,h in enumerate(prefix,1))
    assert moment <= K
    return prefix,moment


f = {1:Q(1,4),3:Q(3,4)}
q = {2:Q(1,2),3:Q(1,2)}
robust(f)
robust(q)
assert R >= Q(27,19)
assert [g(t) for t in [1,2,3]] == [Q(3),Q(14,5),Q(8,5)]
# For t>=3, g is constant and both minorants decrease.
assert all(g(t) >= 3-Q(7,10)*(t-1) for t in [1,2,3])
assert all(g(t) >= 4-Q(6,5)*(t-1) for t in [2,3])
v = sum(g(t)*w for t,w in f.items())
w = sum(g(t)*u for t,u in q.items())
assert v == 3-Q(7,10)*K == Q(39,20)
assert w == 4-Q(6,5)*K == Q(11,5)
assert Q(2) > K  # Any support confined to t>=3 is infeasible.
assert g(3) < g(2) < g(1)
print(json.dumps({
    'job_id':'robust-stopping-triage-ef6eadc61ec7',
    'scope':'deterministic exact check; no fresh review',
    'optimal_expected_cost':str(v),
    'minimum_feasible_support_level':str(g(2)),
    'best_expected_cost_at_minimum_support_level':str(w),
    'expected_cost_gap':str(w-v),
    'original_status':'unresolved'
},indent=2))
