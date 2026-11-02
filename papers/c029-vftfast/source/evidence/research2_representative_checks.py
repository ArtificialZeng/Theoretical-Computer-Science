#!/usr/bin/env python3
"""Exact finite-field implementation test; not an infinite theorem certificate."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json,random,time
P=101

def determinant(a):
    a=[list(row) for row in a]; out=1
    for j in range(len(a)):
        z=next((i for i in range(j,len(a)) if a[i][j]%P),None)
        if z is None:return 0
        if z!=j:a[z],a[j]=a[j],a[z];out=-out
        val=a[j][j]%P;out=out*val%P;inv=pow(val,-1,P)
        for i in range(j+1,len(a)):
            fac=a[i][j]*inv%P
            for k in range(j,len(a)):a[i][k]=(a[i][k]-fac*a[j][k])%P
    return out%P

@lru_cache(None)
def wedge(T,support):
    return tuple(determinant([[pow(v+1,r,P) for v in support] for r in rows])
                 for rows in combinations(range(T),len(support)))

def reduce_family(paths,T):
    basis={};keep=[];seen=set()
    for path in paths:
        support=tuple(sorted(path))
        if support in seen:continue
        seen.add(support);vec=list(wedge(T,support))
        for j in range(len(vec)):
            if not vec[j]:continue
            if j in basis:
                fac=vec[j]
                for k in range(j,len(vec)):vec[k]=(vec[k]-fac*basis[j][k])%P
            else:
                inv=pow(vec[j],-1,P)
                basis[j]=[z*inv%P for z in vec];keep.append(path);break
    return keep

def families(g,x,d,f):
    T=min(len(g),f+d+1);old={v:[] for v in range(len(g))};old[x]=[(x,)]
    for _ in range(d):
        new={v:[] for v in range(len(g))}
        for u,paths in old.items():
            for path in paths:
                for v in g[u]:
                    if v not in path:new[v].append(path+(v,))
        old={v:reduce_family(paths,T) for v,paths in new.items()}
    return old

def full_paths(g,x,d):
    paths=[(x,)]
    for _ in range(d):paths=[a+(v,) for a in paths for v in g[a[-1]] if v not in a]
    out={v:[] for v in range(len(g))}
    for a in paths:out[a[-1]].append(a)
    return out

def main():
    start=time.monotonic();graphs=0;configs=0;checks=0;records=[]
    for n in range(2,7):
        edges=list(combinations(range(n),2));bound=1<<len(edges)
        masks=list(range(bound)) if n<=4 else sorted({0,bound-1,*[random.Random(290200+n*100+i).randrange(bound) for i in range(16)]})
        for mask in masks:
            graphs+=1;g=[set() for _ in range(n)]
            for i,(u,v) in enumerate(edges):
                if mask&(1<<i):g[u].add(v);g[v].add(u)
            for d in range(1,min(n,5)):
                for x in range(n):
                    full=full_paths(g,x,d)
                    for f in range(n-d):
                        configs+=1;small=families(g,x,d,f)
                        for y in range(n):
                            assert all(len(a)==d+1 and a[0]==x and a[-1]==y and len(set(a))==d+1 for a in small[y])
                            others=[v for v in range(n) if v not in (x,y)]
                            for size in range(min(f,len(others))+1):
                                for ft in combinations(others,size):
                                    F=set(ft);a=any(not F.intersection(a) for a in full[y]);b=any(not F.intersection(a) for a in small[y]);assert a==b
                                    checks+=1
        records.append({'n':n,'graph_masks_checked':len(masks),'all_labeled_graphs':n<=4})
    out={'job_id':'c029-vftfast-research-36ff17e1eeb1','field_prime':P,'graphs':graphs,'DP_configurations':configs,'fault_disjointness_comparisons':checks,'failures':0,'coverage':records,'d_range':'1..min(n-1,4)','f_range':'0..n-d-1','elapsed_seconds':round(time.monotonic()-start,6),'scope':'Exact finite representative-DP test. No complete spanner test or infinite original resolution.'}
    Path('evidence/research2-representative-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
