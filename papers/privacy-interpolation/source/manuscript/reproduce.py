#!/usr/bin/env python3
"""Portable standard-library reproduction of the fresh-referee finite checks.
Reads bundled certificates and prints JSON; never writes research evidence.
Finite checks supplement the analytic proofs.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parent



def nonnegative_on_interval(a, b, c, left, right, strict=False):
    """Check a*u^2+b*u+c by rescaling to [0,1] and discriminant."""
    width = right-left
    alpha = a*width*width
    beta = (2*a*left+b)*width
    gamma = a*left*left+b*left+c
    ends = (gamma, alpha+beta+gamma)
    assert all(x > 0 if strict else x >= 0 for x in ends)
    if alpha > 0 and -2*alpha < beta < 0:
        discriminant_margin = 4*alpha*gamma-beta*beta
        assert discriminant_margin > 0 if strict else discriminant_margin >= 0


def value(row, u):
    a, b, c = row
    return a*u+b/u+c


def check_paths(relative):
    source = ROOT/relative
    records = json.loads(source.read_text())['certificates']
    stats = dict(records=0, half_cells=0, coordinate_cells=0,
                 degenerate_cells=0, large_b_records=0,
                 minimum_budget_records=0, constant_reservoir_records=0)
    for record in records:
        p = list(map(F, record['p']))
        q = list(map(F, record['q']))
        B, Z, peak = (F(record[k]) for k in ('B', 'Z', 'peak'))
        c, a, b = p
        assert 0 < a < b and a+b < 1 and sum(p) == sum(q) == 1
        assert q == [c,b,a] and Z == B*B
        minimum_Z = b/a if b <= F(1,2) else 1/(4*a*(1-b))
        assert Z >= minimum_Z and B <= (a+b)/(2*a)
        assert peak == 1-2*a*B and peak >= c
        last_u, last_point = F(1), p
        for cell in record['half_cells']:
            lo, hi = map(F, cell['interval'])
            rows = [list(map(F,row)) for row in cell['coefficients']]
            assert lo == last_u and lo <= hi <= B
            assert [sum(row[k] for row in rows) for k in range(3)] == [0,0,1]
            assert [value(row,lo) for row in rows] == last_point
            for aa, bb, cc in rows:
                # u*r, u*(r+dr/ds), u*(r-dr/ds), where s=log(u).
                nonnegative_on_interval(aa,cc,bb,lo,hi,strict=True)
                nonnegative_on_interval(2*aa,cc,F(0),lo,hi)
                nonnegative_on_interval(F(0),cc,2*bb,lo,hi)
                stats['coordinate_cells'] += 1
            aa, bb, cc = rows[0]
            nonnegative_on_interval(-aa,peak-cc,-bb,lo,hi)
            last_u = hi
            last_point = [value(row,hi) for row in rows]
            stats['half_cells'] += 1
            stats['degenerate_cells'] += lo == hi
        assert last_u == B and last_point == [peak,a*B,a*B]
        # Reflection swaps changing coordinates: continuous midpoint, final q,
        # same speed inequalities. Endpoint envelopes force peak >= 1-2*a*B.
        assert [p[0],p[2],p[1]] == q
        stats['records'] += 1
        stats['large_b_records'] += b > F(1,2)
        stats['minimum_budget_records'] += Z == minimum_Z
        stats['constant_reservoir_records'] += peak == c
    return dict(input=relative, sha256=hashlib.sha256(source.read_bytes()).hexdigest(), **stats)


def squared_envelope(p,q,Z,j,v):
    # Direct branch evaluation at v, without a maintained prefix/suffix state.
    A = sum((p[i] for i in range(len(p)) if i != j and p[i]*v <= Z*q[i]),F(0))
    B = sum((Z*q[i] for i in range(len(p)) if i != j and p[i]*v > Z*q[i]),F(0))
    return (A*v+B)**2/v


def direct_oracle(p,q,Z,j):
    # Reconstruct each cell from its midpoint, never transfer a branch sum.
    cuts = sorted({F(1),Z*Z} | {Z*q[i]/p[i] for i in range(len(p)) if i != j})
    answers = [squared_envelope(p,q,Z,j,v) for v in cuts]
    for lo,hi in zip(cuts,cuts[1:]):
        mid = (lo+hi)/2
        A = sum((p[i] for i in range(len(p)) if i != j and p[i]*mid <= Z*q[i]),F(0))
        B = sum((Z*q[i] for i in range(len(p)) if i != j and p[i]*mid > Z*q[i]),F(0))
        if A and lo <= B/A <= hi:
            answers.append(4*A*B)
    return min(answers)


def check_sweep():
    # Load only the already inspected implementation, without running main or
    # importing its verifier; this namespace never invokes any file writes.
    namespace = {'__name__':'frozen_candidate', '__file__':str(ROOT/'checks/sweep.py')}
    exec(compile((ROOT/'checks/sweep.py').read_text(),
                 'frozen_candidate','exec'),namespace)
    sweep = namespace['all_certificates']
    rng = random.Random(4776272744)
    pairs = []
    for n in range(2,9):
        for _ in range(32):
            x = [rng.randrange(1,60) for _ in range(n)]
            y = [rng.randrange(1,60) for _ in range(n)]
            pairs.append((tuple(F(a,sum(x)) for a in x),tuple(F(a,sum(y)) for a in y)))
        uniform = tuple(F(1,n) for _ in range(n))
        pairs.append((uniform,uniform))
    pairs.extend([
        ((F(1,5),F(2,5),F(2,5)),(F(2,5),F(1,5),F(2,5))),
        ((F(1,1000000),F(1,3),F(1999997,3000000)),
         (F(1,3),F(1,1000000),F(1999997,3000000)))])
    comparisons = 0
    for p,q in pairs:
        endpoint = max(max(x/y,y/x) for x,y in zip(p,q))
        for Z in (endpoint,endpoint*F(13,11),endpoint*3):
            result = sweep(p,q,Z)
            for j,got in enumerate(result):
                assert got == direct_oracle(p,q,Z,j)
                assert got <= (1-max(p[j],q[j]))**2
                comparisons += 1
    return dict(held_out_endpoint_pairs=len(pairs),budget_instances=3*len(pairs),
                designated_coordinate_comparisons=comparisons,
                dimensions=list(range(2,9)),seed=4776272744,
                method='Rebuild each interval from its midpoint and directly evaluate branches; compare frozen grouped sweep.')


def main():
    paths = [check_paths(name) for name in (
        'checks/research-excursion-path-certificates.json',
        'checks/research-swapped-path-certificates.json')]
    result = dict(status='passed',paths=paths,sweep=check_sweep(),
                  limits='Finite exact checks; universal statements follow from the manuscript proofs.')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
