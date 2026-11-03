#!/usr/bin/env python3
"""Exact deterministic-transfer tests, not a source-model impossibility search.
Enumerates restricted-growth cluster strings (all labeled orders modulo color
renaming), 2<=n<=8, 2<=k<=6, r=2,3, and all disjoint r-by-r rectangles.
For each density eta, finds the least UNIFORM order-edge weight at leading
intercluster scale that permits that density of dominated pairs. Fractions
are exact. A finite M=10**6 independently verifies each extremal record.
"""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json

PS=(Fraction(1,3),Fraction(2,5),Fraction(49,100))

def cluster_orders(n):
    a=[0]*n
    def rec(i,m):
        if i==n:
            if 2<=m+1<=6: yield tuple(a)
            return
        for c in range(min(m+1,5)+1):
            a[i]=c
            yield from rec(i+1,max(m,c))
    yield from rec(1,0)

def rectangles(n,r):
    allv=set(range(n))
    for A in combinations(range(n),r):
        for B in combinations(sorted(allv-set(A)),r):
            if A<B:
                yield tuple((i,j,abs(i-j)) for i in A for j in B)

def required(eta,r):
    x=eta*r*r
    return (x.numerator+x.denominator-1)//x.denominator

def min_denominator(colors,rects,h):
    best=None
    for rect in rects:
        z=sum(colors[i]==colors[j] for i,j,_ in rect)
        need=h-z
        if need>0:
            gaps=sorted((g for i,j,g in rect if colors[i]!=colors[j]),reverse=True)
            D=gaps[need-1]
            best=D if best is None else min(best,D)
    return best

def finite_verify(rec):
    a=rec['order']; n=len(a); r=rec['r']; M=10**6
    D=rec['leading_step_denominator']
    step=Fraction(M,D) if D is not None else Fraction(1)
    h=rec['required_good_pairs']
    actual_min=r*r
    for rect in rectangles(n,r):
        good=sum((1 if a[i]==a[j] else M)<=step*g for i,j,g in rect)
        actual_min=min(actual_min,good)
        assert good>=h
    k=max(a)+1
    s=sum(a[i]!=a[i+1] for i in range(n-1))
    cost=Fraction(n-1-s+s*M)
    mst=Fraction(n-k+(k-1)*M)
    W=(n-1)*step
    assert cost<=6*r*W+(6*r+2)*mst
    return {'M':M,'step':str(step),'minimum_good_pairs':actual_min,
            'path_true_cost':str(cost),'true_mst':str(mst),'observed_order_cost':str(W),
            'exact_ratio_cost_over_W_plus_MST':str(cost/(W+mst))}

out={'job_id':'c037-msthalf-research-82a59cd9a4af',
     'arithmetic':'exact integer/rational',
     'scope':'two-level cluster metrics; uniform order edge weights optimized at leading scale; all orders modulo cluster renaming; not all metrics/weights/adversaries',
     'n_range':[2,8],'cluster_count_range':[2,6],'r_values':[2,3],
     'metric_within':1,'metric_between':'M >= 1',
     'density':'eta=3*(1-2*p)/4; all r-by-r rectangles, hence all larger rectangles by averaging',
     'orders_total':0,'configurations_total':0,'rectangle_configurations_total':0,
     'maxima':[]}
for r in (2,3):
    for p in PS:
        eta=3*(1-2*p)/4
        h=required(eta,r)
        maximum=None; winner=None; orders=0; tests=0
        for n in range(max(2,2*r),9):
            rects=list(rectangles(n,r))
            for a in cluster_orders(n):
                orders+=1; tests+=len(rects)
                D=min_denominator(a,rects,h)
                switches=sum(a[i]!=a[i+1] for i in range(n-1))
                k=max(a)+1
                leadingW=Fraction(n-1,D) if D is not None else Fraction(0)
                ratio=Fraction(switches)/(leadingW+k-1)
                if maximum is None or ratio>maximum:
                    maximum=ratio
                    winner={'r':r,'p':str(p),'eta':str(eta),'required_good_pairs':h,
                            'order':a,'leading_step_denominator':D,
                            'switches':switches,'clusters':k,
                            'leading_ratio_cost_over_W_plus_MST':str(ratio)}
        winner['finite_verification']=finite_verify(winner)
        winner['orders_checked']=orders; winner['rectangles_checked']=tests
        out['maxima'].append(winner)
        out['configurations_total']+=orders
        out['rectangle_configurations_total']+=tests
out['orders_total']=sum(1 for n in range(2,9) for _ in cluster_orders(n))
out['conclusion']='No transfer failure in this specified finite family. The general two-level bound is proved separately; this search does not prove a general multiscale theorem.'
Path(__file__).with_name('rectangle-cluster-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'configurations':out['configurations_total'],'rectangle_tests':out['rectangle_configurations_total'],'maxima':[(x['r'],x['p'],x['leading_ratio_cost_over_W_plus_MST']) for x in out['maxima']]}))
