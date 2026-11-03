#!/usr/bin/env python3
"""Exact bounded deterministic-transfer tests on all orders of five n=7 metrics.
Only uniform weighted-order steps are optimized. No source-model simulation,
no completeness claim beyond the stated finite metrics/orders/weights.
"""
from itertools import permutations,combinations
from fractions import Fraction
from pathlib import Path
import json
N=7

def rects(r):
    out=[]
    for A in combinations(range(N),r):
        for B in combinations([i for i in range(N) if i not in A],r):
            if A<B: out.append([(i,j,abs(i-j)) for i in A for j in B])
    return out

def ultrametric(shape,base):
    d=[[0]*N for _ in range(N)]
    def rec(v):
        if isinstance(v,int): return [v],0
        a,ha=rec(v[0]); b,hb=rec(v[1]); h=base**(max(ha,hb)+1)
        for i in a:
            for j in b:d[i][j]=d[j][i]=h
        return a+b,max(ha,hb)+1
    rec(shape)
    return d

def mst(d):
    remaining=set(range(1,N)); nearest={i:d[0][i] for i in remaining}; val=0
    while remaining:
        v=min(remaining,key=lambda i:nearest[i]); val+=nearest[v]; remaining.remove(v)
        for u in remaining:nearest[u]=min(nearest[u],d[v][u])
    return val

balanced=(((0,1),(2,3)),(4,(5,6)))
comb=((((((0,1),2),3),4),5),6)
metrics=[('line',[[abs(i-j) for j in range(N)] for i in range(N)])]
for b in [2,10]:
    metrics.append(('balanced-base-'+str(b),ultrametric(balanced,b)))
    metrics.append(('comb-base-'+str(b),ultrametric(comb,b)))
R={r:rects(r) for r in [2,3]}
records=[]; total_rects=0; total_orders=0
for name,d in metrics:
    m=mst(d)
    maxima={(2,1):None,(3,1):None,(3,2):None,(3,3):None}
    winners={}
    for order in permutations(range(N)):
        total_orders+=1
        dist=[[d[order[i]][order[j]] for j in range(N)] for i in range(N)]
        cost=sum(dist[i][i+1] for i in range(N-1))
        for r in [2,3]:
            hs=[1] if r==2 else [1,2,3]
            steps={h:Fraction(0) for h in hs}
            for rect in R[r]:
                total_rects+=1
                thresholds=sorted(Fraction(dist[i][j],gap) for i,j,gap in rect)
                for h in hs:steps[h]=max(steps[h],thresholds[h-1])
            for h in hs:
                step=steps[h]; ratio=Fraction(cost)/(step*(N-1)+m)
                key=(r,h)
                if maxima[key] is None or ratio>maxima[key]:
                    maxima[key]=ratio
                    winners[key]={'metric':name,'r':r,'required_good_pairs':h,'order':order,
                                  'minimum_uniform_step':str(step),'path_true_cost':cost,
                                  'true_mst':m,'ratio_cost_over_W_plus_MST':str(ratio)}
    for key,w in winners.items():
        order=w['order']; step=Fraction(w['minimum_uniform_step']); r=w['r']; h=w['required_good_pairs']
        mingood=min(sum(d[order[i]][order[j]]<=step*gap for i,j,gap in rect) for rect in R[r])
        assert mingood>=h
        w['minimum_good_pairs_reverified']=mingood
        records.append(w)
out={'job_id':'c037-msthalf-research-82a59cd9a4af','arithmetic':'exact rational',
     'n':N,'metric_families':[x[0] for x in metrics],
     'all_orders_per_metric':5040,'orders_checked':total_orders,
     'rectangle_order_tests':total_rects,
     'scope_limit':'Five explicit metrics only; uniform order weights only. Threshold h corresponds to density h/r^2; relevant p densities require h=1 for r=2 and h=1,2,3 for r=3.',
     'maxima':records,'conclusion':'Finite tests only; no proof or disproof of arbitrary multiscale transfer or the immutable source question.'}
Path(__file__).with_name('rectangle-multiscale-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'orders':total_orders,'rectangle_tests':total_rects,'largest_ratio':str(max(Fraction(x['ratio_cost_over_W_plus_MST']) for x in records))}))
