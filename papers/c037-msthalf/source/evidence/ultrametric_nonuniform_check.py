#!/usr/bin/env python3
"""Bounded deterministic nonuniform-weight attacks; exact integer certificates.
Not an exhaustive search or source-model simulation. Coordinate descent is not
claimed optimal. Run synchronously, with a fixed finite family count.
"""
from pathlib import Path
from itertools import combinations
from random import Random
from fractions import Fraction
import json, time
JOB='c037-msthalf-research-d9c4fc8e3237'
rng=Random(3702)
checks=0

def metric(n,shape,heights):
    d=[[0]*n for _ in range(n)]
    nodes=[[i] for i in range(n)]
    hs=[0]*n
    mst=0
    while len(nodes)>1:
        if shape=='comb': a,b=0,1
        elif shape=='balanced':
            ids=sorted(range(len(nodes)),key=lambda i:len(nodes[i]))
            a,b=sorted(ids[:2])
        else: a,b=sorted(rng.sample(range(len(nodes)),2))
        A,B=nodes[a],nodes[b]
        h=max(hs[a],hs[b])+rng.choice(heights)
        mst+=h
        for i in A:
            for j in B:d[i][j]=d[j][i]=h
        nodes[a]=A+B; hs[a]=h
        nodes.pop(b); hs.pop(b)
    return d,mst

def feasible(d,w,r,h):
    global checks
    checks+=1
    n=len(d); t=[0]
    for x in w:t.append(t[-1]+x)
    bad=[]
    for i in range(n):
        mask=0
        for j in range(n):
            if i!=j and d[i][j]>abs(t[i]-t[j]):mask|=1<<j
        bad.append(mask)
    if h==1:
        for A in combinations(range(n),r):
            mask=(1<<n)-1
            for a in A:mask&=bad[a]
            for a in A:mask&=~(1<<a)
            if mask.bit_count()>=r:return False
    else:
        for A in combinations(range(n),r):
            scores=[]
            aset=set(A)
            for b in range(n):
                if b not in aset:scores.append(sum(not ((bad[a]>>b)&1) for a in A))
            if sum(sorted(scores)[:r])<h:return False
    return True

def prim(d):
    n=len(d); used={0}; near=d[0].copy(); total=0
    for _ in range(n-1):
        v=min((i for i in range(n) if i not in used),key=lambda i:near[i])
        total+=near[v];used.add(v)
        for i in range(n):near[i]=min(near[i],d[v][i])
    return total

records=[]; families=[]; start=time.monotonic()
for n in [8,12,16,24,32]:
 for shape in ['balanced','comb','random']:
  for increments in [[1],[1,2,7],[1,3,27,81]]:
   d,m=metric(n,shape,increments)
   assert prim(d)==m
   for trial in range(2):
    order=list(range(n));rng.shuffle(order)
    D=[[d[order[i]][order[j]] for j in range(n)] for i in range(n)]
    cost=sum(D[i][i+1] for i in range(n-1))
    # h=1 checks every r-by-r rectangle for nonemptiness. h=2 is stronger.
    configs=[(2,1),(2,2)] if n<=16 else [(2,1)]
    if n<=12:configs.append((3,2))
    for r,h in configs:
     w=[D[i][i+1] for i in range(n-1)]
     for sweep in range(2):
      idx=list(range(n-1));rng.shuffle(idx)
      for i in idx:
       lo,hi=0,w[i]
       while lo<hi:
        mid=(lo+hi)//2; old=w[i];w[i]=mid
        ok=feasible(D,w,r,h);w[i]=old
        if ok:hi=mid
        else:lo=mid+1
       w[i]=lo
     assert feasible(D,w,r,h)
     # Independent direct integer rectangle density verification of each saved witness.
     t=[0]
     for x in w:t.append(t[-1]+x)
     minimum=r*r
     for A in combinations(range(n),r):
      aset=set(A)
      scores=sorted(sum(D[a][b]<=abs(t[a]-t[b]) for a in A)
                    for b in range(n) if b not in aset)
      minimum=min(minimum,sum(scores[:r]))
     assert minimum>=h
     families.append({'n':n,'shape':shape,'increments':increments,'trial':trial,'r':r,'h':h})
     ratio=Fraction(cost,r*(sum(w)+m))
     records.append({'n':n,'shape':shape,'increments':increments,'trial':trial,
       'r':r,'required_good_pairs':h,'minimum_good_pairs':minimum,
       'order':order,'weights':w,'metric_in_order':D,'true_path_cost':cost,
       'W':sum(w),'MST':m,'cost_over_r_W_plus_MST':str(ratio)})
# The proposed stronger large-child kernel is separately labeled, not proved.
best=None
for rec in records:
    d=rec['metric_in_order'];n=len(d);r=rec['r'];B=0;small=0
    for i in range(n-1):
        height=d[i][i+1]
        cx=sum(d[i][j]<height for j in range(n))
        cy=sum(d[i+1][j]<height for j in range(n))
        if min(cx,cy)>r:B+=height
        else:small+=height
    assert small<=2*r*rec['MST']
    rec['large_child_transition_cost']=B
    rec['small_child_transition_cost']=small
    rec['B_over_rW']=str(Fraction(B,r*rec['W'])) if rec['W'] else ('0' if B==0 else 'infinite')
    if rec['W'] and (best is None or Fraction(rec['B_over_rW'])>Fraction(best['B_over_rW'])):best=rec
# Store all exact witnesses; search coverage is the deterministic pseudorandom list above.
out={'job_id':JOB,'seed':3702,'arithmetic':'exact integer and rational',
 'scope':'Finite sampled hierarchies/orders; arbitrary-integer coordinate descent, not optimization certificate; no exhaustive infinite theorem.',
 'families_checked':len(families),'feasibility_calls':checks,'elapsed_seconds':time.monotonic()-start,
 'largest_ratio':str(max(Fraction(x['cost_over_r_W_plus_MST']) for x in records)),
 'records':records,
 'large_child_test':{'statement_tested':'B_r <= constant*r*W',
   'largest_B_over_rW':best['B_over_rW'],'witness_index':records.index(best),
   'finite_evidence_only':True,'all_thin_bounds_verified':True}}
Path(__file__).with_name('ultrametric-nonuniform-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['families_checked','feasibility_calls','elapsed_seconds','largest_ratio']}))
