#!/usr/bin/env python3
"""Independent exact verifier for saved finite witnesses, not an independent referee."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json, hashlib
ROOT=Path(__file__).resolve().parent.parent
z=json.loads((ROOT/'evidence/ultrametric-nonuniform-check.json').read_text())
count=0;rect_sides=0
for x in z['records']:
    d=x['metric_in_order'];n=x['n'];r=x['r'];w=x['weights']
    assert len(d)==n and len(w)==n-1
    assert all(isinstance(v,int) and v>=0 for v in w)
    assert sorted(x['order'])==list(range(n))
    for i in range(n):
        assert d[i][i]==0
        for j in range(n):
            assert d[i][j]==d[j][i]
            if i!=j:assert d[i][j]>0
            for k in range(n):assert d[i][j]<=max(d[i][k],d[k][j])
    # Kruskal, unlike the generator's Prim and hierarchy formula.
    parent=list(range(n))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    mst=0;edges=0
    for length,i,j in sorted((d[i][j],i,j) for i in range(n) for j in range(i)):
        a,b=find(i),find(j)
        if a!=b:parent[a]=b;mst+=length;edges+=1
    assert edges==n-1 and mst==x['MST']
    t=[sum(w[:i]) for i in range(n)]
    minimum=r*r
    for A in combinations(range(n),r):
        rect_sides+=1
        deg=[sum(d[a][b]<=abs(t[a]-t[b]) for a in A) for b in range(n) if b not in A]
        minimum=min(minimum,sum(sorted(deg)[:r]))
    assert minimum==x['minimum_good_pairs'] and minimum>=x['required_good_pairs']
    total=sum(d[i][i+1] for i in range(n-1));B=0
    for i in range(n-1):
        h=d[i][i+1]
        left=[j for j in range(n) if d[i][j]<h]
        right=[j for j in range(n) if d[i+1][j]<h]
        assert not set(left)&set(right)
        if len(left)>r and len(right)>r:B+=h
    assert total==x['true_path_cost'] and sum(w)==x['W']
    assert B==x['large_child_transition_cost']
    assert total-B==x['small_child_transition_cost']<=2*r*mst
    assert Fraction(total,r*(sum(w)+mst))==Fraction(x['cost_over_r_W_plus_MST'])
    count+=1
assert count==z['families_checked']==180
assert max(Fraction(x['cost_over_r_W_plus_MST']) for x in z['records'])==Fraction(z['largest_ratio'])
assert max(Fraction(x['B_over_rW']) for x in z['records'] if x['W'])==Fraction('7/3')
sha=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
assert sha=='d45cd6730fe3f8685cb796b9d75ebe8e7926c1584021d045a282021749e45128'
out={'job_id':'c037-msthalf-research-d9c4fc8e3237','source_sha256':sha,'source_unchanged':True,
 'saved_finite_witnesses_verified':count,'rectangle_A_sides_checked':rect_sides,
 'checks':['all ultrametric triples','exact Kruskal MST','complete rectangle densities for each saved witness','true order costs','thin/large child decomposition','rational maxima'],
 'scope_limit':'Exact finite verification only; same worker, no fresh referee or proof of universal K/B; no original resolution.',
 'candidate_created':False,'manuscript_created':False,'subagents_spawned':0}
(ROOT/'evidence/research-pass2-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'verified_witnesses':count,'rectangle_A_sides':rect_sides,'source_unchanged':True}))
