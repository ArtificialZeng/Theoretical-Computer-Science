#!/usr/bin/env python3
"""Bounded exact orientation/critical-cut tests; no asymptotic certification.

Every directed input edge becomes a distinct, freely oriented undirected item.
Path reversal is cross-checked against independent enumeration and integer
successive-shortest-path min-cost flow. No third-party modules required.
"""
from pathlib import Path
from itertools import combinations
from collections import deque
from fractions import Fraction
import hashlib, heapq, json, random, time, sys

JOB = 'c049-dualpreserve-research-2396269cbd5d'
PREFIX = 'research-2396269cbd5d'

def path_reverse(n, edges):
    heads=[]; load=[0]*n; outgoing=[set() for _ in range(n)]
    for e,(u,v) in enumerate(edges):
        h=v if load[v]<=load[u] else u
        heads.append(h); load[h]+=1; outgoing[u if h==v else v].add(e)
    iterations=0
    while True:
        found=None
        for s in sorted(range(n), key=lambda u:load[u]):
            pred={s:None}; queue=[s]
            for u in queue:
                if load[u]>=load[s]+2:
                    found=(s,u,pred);break
                for e in outgoing[u]:
                    v=heads[e]
                    if v not in pred:pred[v]=(u,e);queue.append(v)
            if found:break
        if found is None:break
        s,v,pred=found; t=v
        while v!=s:
            u,e=pred[v];outgoing[u].remove(e);outgoing[v].add(e);heads[e]=u;v=u
        load[s]+=1;load[t]-=1;iterations+=1
    assert sum(load)==len(edges)
    # Exhaustively check the no-improving-directed-path optimality certificate.
    for s in range(n):
        seen={s};queue=[s]
        for u in queue:
            assert load[u]<=load[s]+1
            for e in outgoing[u]:
                v=heads[e]
                if v not in seen:seen.add(v);queue.append(v)
    # Explicit integer Lagrangian dual certificate.  For each vertex v let
    # r(v) be the largest load reachable from v.  No improving path gives
    # a(v)<=r(v)<=a(v)+1; z(v)=max(0,2r(v)-1) is a discrete subgradient.
    z=[]
    for s in range(n):
        seen={s};queue=[s]
        for u in queue:
            for e in outgoing[u]:
                v=heads[e]
                if v not in seen:seen.add(v);queue.append(v)
        z.append(max(0,2*max((load[u] for u in seen),default=0)-1))
    for e,(u,v) in enumerate(edges):assert z[heads[e]]==min(z[u],z[v])
    primal=sum(x*x for x in load)
    dual=sum(min(z[u],z[v]) for u,v in edges)-sum(x*x//4 for x in z)
    assert primal==dual
    return primal,load,heads,iterations

def brute_energy(n,edges):
    best=None
    for bits in range(1<<len(edges)):
        a=[0]*n
        for e,(u,v) in enumerate(edges):a[v if bits>>e&1 else u]+=1
        z=sum(x*x for x in a)
        if best is None or z<best:best=z
    return best

def flow_energy(n,edges):
    m=len(edges);src=m+n;sink=src+1;N=sink+1;adj=[[] for _ in range(N)]
    def add(u,v,cost):
        adj[u].append([v,len(adj[v]),1,cost]);adj[v].append([u,len(adj[u])-1,0,-cost])
    degree=[0]*n
    for e,(u,v) in enumerate(edges):
        add(src,e,0);add(e,m+u,0);add(e,m+v,0);degree[u]+=1;degree[v]+=1
    for v,d in enumerate(degree):
        for k in range(1,d+1):add(m+v,sink,2*k-1)
    potential=[0]*N;cost=0
    for step in range(m):
        dist=[10**30]*N;prev=[None]*N;dist[src]=0;queue=[(0,src)]
        while queue:
            d,u=heapq.heappop(queue)
            if d!=dist[u]:continue
            for k,(v,rev,cap,c) in enumerate(adj[u]):
                if cap:
                    reduced=c+potential[u]-potential[v]
                    assert reduced>=0
                    nd=d+reduced
                    if nd<dist[v]:dist[v]=nd;prev[v]=(u,k);heapq.heappush(queue,(nd,v))
        assert prev[sink] is not None
        for u in range(N):
            if dist[u]<10**30:potential[u]+=dist[u]
        v=sink
        while v!=src:
            u,k=prev[v];a=adj[u][k];cost+=a[3];a[2]-=1;adj[v][a[1]][2]+=1;v=u
    # Residual negative-cycle exclusion: Bellman-Ford from a super-source.
    dual=[0]*N
    for iteration in range(N):
        changed=False
        for u in range(N):
            for v,rev,cap,c in adj[u]:
                if cap and dual[v]>dual[u]+c:dual[v]=dual[u]+c;changed=True
        if not changed:break
    assert not changed, 'negative residual cycle: not minimum cost'
    return cost

def closure(n,edges,vertexmask):
    rows=[(1<<v) if vertexmask>>v&1 else 0 for v in range(n)]
    for u,v in edges:
        if vertexmask>>u&1 and vertexmask>>v&1:rows[u]|=1<<v
    for k in range(n):
        for u in range(n):
            if rows[u]>>k&1:rows[u]|=rows[k]
    return rows

def witness_masks(n,edges):
    # Exact cut characterization, with all nonreflexive demand pairs encoded.
    cover=[0]*len(edges);full=(1<<n)-1
    for A in range(1,full):
        cut=[e for e,(u,v) in enumerate(edges) if A>>u&1 and not A>>v&1]
        if not 1<=len(cut)<=3:continue
        left=closure(n,edges,A);right=closure(n,edges,full^A)
        for e in cut:
            u,v=edges[e]
            for s in range(n):
                if left[s]>>u&1:
                    for t in range(n):
                        if right[v]>>t&1:cover[e]|=1<<(s*n+t)
    return cover

def min_demands(n,edges,masks):
    if not edges:return []
    if any(x==0 for x in masks):return None
    pairs=[]
    for s in range(n):
        for t in range(n):
            if s!=t:
                cov=sum(1<<e for e,x in enumerate(masks) if x>>(s*n+t)&1)
                if cov:pairs.append(((s,t),cov))
    target=(1<<len(edges))-1
    # Enumerate demand subsets in increasing cardinality, stopping at the first.
    for k in range(1,len(pairs)+1):
        for ix in combinations(range(len(pairs)),k):
            cov=0
            for j in ix:cov|=pairs[j][1]
            if cov==target:return [pairs[j][0] for j in ix]
    raise AssertionError('cover should exist')

def save(data):
    data['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_name(PREFIX+'-energy-results.json').write_text(json.dumps(data,indent=2)+'\n')

def main():
    start=time.monotonic();rng=random.Random(490323)
    result={'job_id':JOB,'status':'in progress','orientation_crosschecks':[],
            'critical_graph_screens':[], 'limits':'Finite tests only. No asymptotic ENERGY proof and no original-scope resolution.'}
    # All simple undirected graphs through five vertices: independent 2^m enumeration.
    for n in range(6):
        universe=list(combinations(range(n),2));count=0
        for mask in range(1<<len(universe)):
            ed=[e for j,e in enumerate(universe) if mask>>j&1]
            energy,*_=path_reverse(n,ed);assert energy==brute_energy(n,ed)
            if n<=4 or mask%31==0:assert energy==flow_energy(n,ed)
            count+=1
        result['orientation_crosschecks'].append({'n':n,'all_simple_undirected_graphs':count,'brute_force_all_orientations':True})
        save(result)
    # Random antiparallel-item instances independently checked by min-cost flow.
    for k in range(100):
        n=rng.randrange(2,13);universe=[(u,v) for u in range(n) for v in range(n) if u!=v]
        ed=rng.sample(universe,rng.randrange(min(60,len(universe))+1))
        energy,*_=path_reverse(n,ed);assert energy==flow_energy(n,ed)
    result['antiparallel_flow_crosschecks']=100;save(result)
    # Fresh criterion, not replay of the earlier cut-equivalence computation:
    # all loop-free digraphs through n=4, each with a MINIMUM witness-demand cover.
    for n in range(2,5):
        universe=[(u,v) for u in range(n) for v in range(n) if u!=v]
        best=Fraction(0);bestcase=None;count=0;notcritical=0
        for mask in range(1<<len(universe)):
            ed=[e for j,e in enumerate(universe) if mask>>j&1]
            masks=witness_masks(n,ed);P=min_demands(n,ed,masks)
            if P is None:notcritical+=1;continue
            energy,load,heads,iterations=path_reverse(n,ed)
            ratio=Fraction(energy,n*(len(P)+1));count+=1
            if ratio>best:
                best=ratio;bestcase={'n':n,'edges':ed,'demands':P,'p_min':len(P),
                    'energy':energy,'load':load,'heads':heads,'ratio_energy_over_n_p_plus_1':str(ratio)}
        result['critical_graph_screens'].append({'n':n,'all_loop_free_digraphs':1<<len(universe),
            'graphs_admitting_some_critical_demand_set':count,'graphs_without_full_edge_cover':notcritical,
            'maximum_ratio':str(best),'maximizer':bestcase})
        save(result);print(json.dumps(result['critical_graph_screens'][-1]),flush=True)
    result['status']='all declared checks passed';result['elapsed_seconds']=time.monotonic()-start;save(result)
    print(json.dumps({'status':result['status'],'elapsed_seconds':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
