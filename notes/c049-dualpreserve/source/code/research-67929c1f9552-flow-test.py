#!/usr/bin/env python3
"""Exact bounded tests of NEW shared-flow/cut rules; no asymptotic inference."""
from collections import deque
from itertools import combinations
from pathlib import Path
import hashlib, json, random, time

JOB = 'c049-dualpreserve-research-67929c1f9552'

def reach(n, edges, active, source):
    seen = 1 << source
    todo = [source]
    adj = [[] for _ in range(n)]
    for k in active:
        u,v = edges[k]; adj[u].append(v)
    for u in todo:
        for v in adj[u]:
            if not (seen >> v & 1):
                seen |= 1 << v; todo.append(v)
    return seen

def mincost(n, edges, s, t, costs, cap=3):
    """Unit capacities; Bellman-Ford shortest residual augmentations, exact ints."""
    used = set(); value = 0
    while value < cap:
        dist = [None]*n; dist[s] = 0; prev = [None]*n
        residual = [(v,u,-costs[k],k,-1) if k in used else
                    (u,v,costs[k],k,1) for k,(u,v) in enumerate(edges)]
        for _ in range(n-1):
            changed = False
            for u,v,c,k,d in residual:
                if dist[u] is not None and (dist[v] is None or dist[v]>dist[u]+c):
                    dist[v] = dist[u]+c; prev[v]=(u,k,d); changed=True
            if not changed: break
        if dist[t] is None: break
        v=t; seen=set()
        while v!=s:
            assert v not in seen; seen.add(v)
            u,k,d = prev[v]
            if d==1: used.add(k)
            else: used.remove(k)
            v=u
        value += 1
    balance=[0]*n
    for k in used:
        u,v=edges[k]; balance[u]+=1; balance[v]-=1
    assert balance[s]==value and balance[t]==-value
    assert all(x==0 for v,x in enumerate(balance) if v not in (s,t))
    return value,used

def potential(flows, m, p):
    loads=[sum(k in f for f in flows) for k in range(m)]
    return sum((2*p+1)*x-x*x for x in loads)

def select(n,edges,pairs):
    p=len(pairs); m=len(edges)
    initial=[mincost(n,edges,s,t,[1]*m) for s,t in pairs]
    values=[a for a,b in initial]; flows=[b for a,b in initial]
    history=[potential(flows,m,p)]; bestresponses=0
    while True:
        changed=False
        for i,(s,t) in enumerate(pairs):
            costs=[2*p-2*sum(k in f for j,f in enumerate(flows) if j!=i) for k in range(m)]
            val,other=mincost(n,edges,s,t,costs,values[i]); bestresponses+=1
            assert val==values[i]
            oldcost=sum(costs[k] for k in flows[i]); newcost=sum(costs[k] for k in other)
            assert newcost<=oldcost
            if newcost<oldcost:
                before=history[-1]; flows[i]=other
                after=potential(flows,m,p)
                assert after-before==newcost-oldcost and after<before
                history.append(after); changed=True
        if not changed: break
    return values,flows,history,bestresponses

def cut_masks(n,edges,pairs):
    """Complete critical-edge masks for these pairs, by exact active small cuts."""
    masks=[0]*len(edges); cuts=[]
    for a in range(1,(1<<n)-1):
        out=[k for k,(u,v) in enumerate(edges) if a>>u&1 and not(a>>v&1)]
        if not out or len(out)>3: continue
        inside=[k for k,(u,v) in enumerate(edges) if a>>u&1 and a>>v&1]
        outside=[k for k,(u,v) in enumerate(edges) if not(a>>u&1) and not(a>>v&1)]
        active=[i for i,(s,t) in enumerate(pairs) if a>>s&1 and not(a>>t&1)]
        if not active: continue
        source_reach={s:reach(n,edges,inside,s) for i in active for s in [pairs[i][0]]}
        suffix={v:reach(n,edges,outside,v) for k in out for v in [edges[k][1]]}
        for k in out:
            u,v=edges[k]
            for i in active:
                s,t=pairs[i]
                if source_reach[s]>>u&1 and suffix[v]>>t&1:
                    masks[k]|=1<<i
        cuts.append((a,out,active))
    return masks,cuts

def prune(n,edges,pairs):
    current=list(edges); pos=0
    while pos<len(current):
        masks,_=cut_masks(n,current,pairs)
        if masks[pos]: pos+=1
        else: current.pop(pos)
    assert all(cut_masks(n,current,pairs)[0])
    return current

def verify_cuts(n,edges,pairs,values,flows,cuts):
    checks=0; off=0
    for a,out,active in cuts:
        entering=[k for k,(u,v) in enumerate(edges) if not(a>>u&1) and a>>v&1]
        for i in active:
            incoming=sum(k in flows[i] for k in entering)
            unused=sum(k not in flows[i] for k in out)
            assert len(out)-values[i]==incoming+unused
            if values[i]==3: assert unused==incoming==0
            if values[i]==2 and unused: assert unused==1 and incoming==0 and len(out)==3
            checks+=1; off+=unused
    return checks,off

def analyze(n,edges,pairs,label,cut_check=True):
    vals,fs,hist,br=select(n,edges,pairs)
    union=set().union(*fs) if fs else set()
    if cut_check:
        masks,cuts=cut_masks(n,edges,pairs)
        cc,off=verify_cuts(n,edges,pairs,vals,fs,cuts)
        crit=[k for k,mask in enumerate(masks) if mask]
    else: cc=off=0; crit=None
    indeg=[0]*n
    for u,v in edges: indeg[v]+=1
    return dict(label=label,n=n,m=len(edges),p=len(pairs),values=vals,
                selected_edges=len(union),critical_edges=None if crit is None else len(crit),
                critical_off_union=None if crit is None else sum(k not in union for k in crit),
                cut_identity_checks=cc,unused_cut_occurrences=off,
                potential_history=hist,bestresponses=br,
                degree_square_sum=sum(d*d for d in indeg),np=n*len(pairs)),fs

def chain(r,L):
    e=[]; n=2*r*L
    a=lambda i,k:i*L+k
    b=lambda j,k:r*L+j*L+k
    for i in range(r):
        for k in range(L-1):e.extend([(a(i,k),a(i,k+1)),(b(i,k),b(i,k+1))])
    for k in range(L):
        for i in range(r):
            for j in range(r):e.append((a(i,k),b(j,k)))
    return n,e,[(a(i,0),b(j,L-1)) for i in range(r) for j in range(r)]

def lift(base_n,base_edges,base_pairs,L):
    """ICALP2020 Section5, K=L. Base paths certified separately."""
    levels=2*L; n=6*L*base_n+2*len(base_pairs); e=[]; central=[]
    c=lambda v,k:v*levels+k
    left=lambda v,k:base_n*levels+v*levels+k
    right=lambda v,k:2*base_n*levels+v*levels+k
    for u,v in base_edges:
        for k in range(1,levels):
            central.extend([len(e),len(e)+1]);e.extend([(c(u,k),c(v,k-1)),(c(v,k),c(u,k-1))])
    for v in range(base_n):
        for k in range(levels):
            e.extend([(left(v,k),c(v,k)),(c(v,k),right(v,k))])
            if k+1<levels:e.extend([(left(v,k),left(v,k+1)),(right(v,k),right(v,k+1))])
    pairs=[];direct=[]
    for i,(x,y) in enumerate(base_pairs):
        s=6*L*base_n+2*i;t=s+1;pairs.append((s,t)); f=set()
        f.update(k for k,(u,v) in enumerate(e) if any(u==side(w,j) and v==side(w,j+1)
                 for side,w in [(left,x),(right,y)] for j in range(levels-1)))
        for edge in [(s,left(x,0)),(s,right(y,0)),(left(x,levels-1),t),(right(y,levels-1),t)]:
            f.add(len(e));e.append(edge)
        direct.append(f)
    return n,e,pairs,central,direct

def direct_critical_witness(n,edges,s,t,failed,k):
    assert k not in failed and len(failed)<=2
    active=set(range(len(edges)))-set(failed)
    return bool(reach(n,edges,active,s)>>t&1) and not(reach(n,edges,active-{k},s)>>t&1)

def main():
    rng=random.Random(67929); rows=[]; cuts=br=small=0; maximum=None
    # Independent exact min-cost optimum checks on every support subset in 40
    # separately chosen n=4 instances (includes cyclic graphs and infeasible values).
    brute_checks=0
    for trial in range(40):
        n=4; es=[(u,v) for u in range(n) for v in range(n) if u!=v and rng.random()<.6]
        costs=[rng.randrange(1,12) for e in es]
        val,chosen=mincost(n,es,0,3,costs)
        opt=None; maxval=-1
        for mask in range(1<<len(es)):
            bal=[0]*n; cost=0
            for k,(u,v) in enumerate(es):
                if mask>>k&1: bal[u]+=1;bal[v]-=1;cost+=costs[k]
            f=bal[0]
            if bal[1] or bal[2] or bal[3]!=-f or not(0<=f<=3):continue
            if f>maxval:maxval=f;opt=cost
            elif f==maxval:opt=min(opt,cost)
        assert val==maxval and sum(costs[k] for k in chosen)==opt
        brute_checks+=1
    # All labelled four-vertex loop-free graphs, for two fixed crossing demands.
    n=4; universe=[(u,v) for u in range(n) for v in range(n) if u!=v]
    for mask in range(1<<len(universe)):
        edges=[e for k,e in enumerate(universe) if mask>>k&1]
        pairs=[(0,2),(1,3)]
        row,_=analyze(n,edges,pairs,'all-n4')
        cuts+=row['cut_identity_checks'];br+=row['bestresponses'];small+=1
        if mask%512==0:print('n4 progress',mask,flush=True)
    for n in range(5,9):
        for run in range(12):
            density=[.2,.35,.5][run%3]
            edges=[(u,v) for u in range(n) for v in range(n) if u!=v and rng.random()<density]
            universe=[(u,v) for u in range(n) for v in range(n) if u!=v]
            pairs=rng.sample(universe, min(n,1+run%7))
            edges=prune(n,edges,pairs)
            row,_=analyze(n,edges,pairs,f'critical-random-{n}-{run}')
            assert row['critical_edges']==len(edges)
            rows.append(row);cuts+=row['cut_identity_checks'];br+=row['bestresponses']
            ratio=row['degree_square_sum']/row['np']
            if maximum is None or ratio>maximum['ratio']:maximum=dict(ratio=ratio,row=row)
    # NEW tests of flow selection; no replay of the historical lower-bound checker.
    for r,L in [(1,4),(2,4),(3,5),(4,8),(8,8)]:
        n,edges,pairs=chain(r,L)
        row,fs=analyze(n,edges,pairs,f'published-chain-{r}-{L}',n<=16)
        assert all(v==2 for v in row['values'])
        expected=2*r*(L-1)+2*r*r
        assert row['selected_edges']==expected
        assert row['m']-row['selected_edges']==(L-2)*r*r
        # Every maximum 2-flow has these two extreme crossings for its pair.
        for (s,t),f in zip(pairs,fs):
            crossings=[(u,v) for k,(u,v) in enumerate(edges) if k in f and u<r*L<=v]
            assert set(crossings)=={(s,t-L+1),(s+L-1,t)}
        rows.append(row)
    # Small exact lift of edge-disjoint unique shortest paths: a star with arms L/2.
    # This validates the lift/mechanism, NOT the asymptotic Theorem26 base family.
    for arms,half in [(2,2),(3,2),(3,3)]:
        base_edges=[];tips=[];v=1
        for arm in range(arms):
            last=0
            for j in range(half):base_edges.append((last,v));last=v;v+=1
            tips.append(last)
        base_pairs=[(tips[0],tips[j]) for j in range(1,arms)]
        L=2*half
        n,edges,pairs,central,direct=lift(v,base_edges,base_pairs,L)
        row,fs=analyze(n,edges,pairs,f'2020-lift-star-{arms}-{half}',False)
        # Both selected direct routes have strictly fewer hops than ANY central route;
        # other commodities can alter prices, so inspect actual coordinate optimum.
        row['central_selected']=sum(any(k in f for f in fs) for k in central)
        row['direct_basis_selected']=all(f==d for f,d in zip(fs,direct))
        # Explicit interior shifts of the first demand force each central edge of its path.
        x,y=base_pairs[0]; levels=2*L
        base_adj=[[] for _ in range(v)]
        for u,w in base_edges:base_adj[u].append(w);base_adj[w].append(u)
        prev={x:None};q=[x]
        for u in q:
            for w in base_adj[u]:
                if w not in prev:prev[w]=u;q.append(w)
        path=[y]
        while path[-1]!=x:path.append(prev[path[-1]])
        path=path[::-1]; assert len(path)==L+1
        idx={edge:k for k,edge in enumerate(edges)};count=0
        for shift in range(2,L):
            f=[idx[(v*levels+x*levels+(shift+L-1),v*levels+x*levels+(shift+L))],
               idx[(2*v*levels+y*levels+(shift-2),2*v*levels+y*levels+(shift-1))]]
            for j,(u,w) in enumerate(zip(path,path[1:])):
                k=idx[(u*levels+shift+L-1-j,w*levels+shift+L-2-j)]
                assert direct_critical_witness(n,edges,*pairs[0],f,k)
                count+=1
        row['central_critical_witnesses']=count
        rows.append(row)
    data=dict(job_id=JOB,status='declared exact checks passed',
              independent_exhaustive_mincost_instances=brute_checks,
              all_labelled_n4_graphs=small,n4_demand_pattern=[[0,2],[1,3]],
              random_critical_graphs=48,cut_identity_checks=cuts,bestresponses=br,
              maximum_random_degree_moment_ratio=maximum,rows=rows,
              limits='No full graph/demand enumeration above n=4; only one demand pattern for n=4. Lift bases are small trees, not asymptotic Theorem26 extremizers. No original-scope resolution or asymptotic bound.',
              code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    out=Path(__file__).with_name('research-67929c1f9552-flow-results.json')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ['status','all_labelled_n4_graphs','random_critical_graphs','cut_identity_checks','bestresponses']}),flush=True)
    print(json.dumps(rows[-8:],indent=2),flush=True)

if __name__=='__main__':main()
