#!/usr/bin/env python3
"""Bounded exact bug checks for R2. No fast rectangular exponent implemented.

New generic-k scheduler and explicit queue oracle; no prior checker imports.
The tiny product backend is ordinary exact integer multiplication modulo p>N.
"""
from collections import deque, Counter
from itertools import product, combinations
from pathlib import Path
import json
import random
import time

JOB = 'c032-dspdag-research-5f16f6951448'


def insert(c, i, x):
    return c[:i] + (x,) + c[i:]


def queue_oracle(graphs, seed):
    reached = {tuple(seed)}
    todo = deque(reached)
    while todo:
        q = todo.popleft()
        i = q.index(min(q))
        for x, allowed in enumerate(graphs[i][q[i]]):
            if allowed and x not in q:
                p = q[:i] + (x,) + q[i+1:]
                if p not in reached:
                    reached.add(p)
                    todo.append(p)
    return reached


def prime_above(n):
    for p in range(n+1, 2*n+2):
        if all(p % d for d in range(2, int(p**0.5)+1)):
            return p
    raise AssertionError('prime search failed')


def rectangular_schedule(graphs, seed, counts):
    k, n0 = len(graphs), len(graphs[0])
    N = 1 << (n0-1).bit_length()
    p = prime_above(N)
    a = [[list(row)+[0]*(N-n0) for row in g]
         + [[0]*N for _ in range(N-n0)] for g in graphs]
    F = bytearray(N**k)
    def index(q):
        z = 0
        for x in q:
            z = z*N+x
        return z
    F[index(seed)] = 1
    def solve(l, r):
        if l == r:
            return
        h = (l+r)//2
        b = h-l+1
        solve(l, h)
        L, R, S, T = range(l,h+1), range(h+1,r+1), range(h+1,N), range(r+1,N)
        node_calls = 0
        for i in range(k):
            domains = [(list(product(S, repeat=k-1)), R)]
            for j in range(k-1):
                coords = [T]*j + [R] + [S]*(k-2-j)
                domains.append((list(product(*coords)), T))
            for contexts, targets0 in domains:
                targets = list(targets0)
                for z in range(0, len(contexts), b**(k-1)):
                    cs = contexts[z:z+b**(k-1)]
                    for start in range(0, len(targets), b):
                        xs = targets[start:start+b]
                        # Fully padded matrices, to charge the real schedule.
                        A = [[a[i][u][x] for u in L] for x in xs]
                        A += [[0]*b for _ in range(b-len(A))]
                        B = [[F[index(insert(c,i,u))] for c in cs]
                             + [0]*(b**(k-1)-len(cs)) for u in L]
                        out = [[sum(A[x][u]*B[u][c] for u in range(b)) % p
                                for c in range(b**(k-1))] for x in range(b)]
                        node_calls += 1
                        counts['products'] += 1
                        counts['padded_entries'] += b*b+2*b**k
                        for x0, x in enumerate(xs):
                            for c0, c in enumerate(cs):
                                q = insert(c,i,x)
                                if out[x0][c0] and len(set(q)) == k:
                                    F[index(q)] = 1
        assert node_calls <= k*k*(N//b)**(k-1)
        counts['nodes'] += 1
        counts['largest_half_width'] = max(counts['largest_half_width'],b)
        solve(h+1,r)
    solve(0,N-1)
    seen = {q for q in product(range(N),repeat=k) if F[index(q)]}
    return seen


def all_shortest(n, edges, s, t):
    adj = [[] for _ in range(n)]
    for u,v,w in edges:
        adj[u].append((v,w))
    paths=[]
    def dfs(u, cost, q):
        if u == t:
            paths.append((cost,q))
        else:
            for v,w in adj[u]:
                dfs(v,cost+w,q+(v,))
    dfs(s,0,(s,))
    if not paths:
        return []
    d=min(w for w,q in paths)
    return [q for w,q in paths if w==d]


def normalize(n, edges, pairs, mode):
    k=len(pairs)
    if mode=='strict' and any(set(pairs[i])&set(pairs[j]) for i,j in combinations(range(k),2)):
        return None
    terminals=set(x for pair in pairs for x in pair)
    copies=[]
    for v in range(n):
        if mode=='strict' or v not in terminals or mode=='internal_only':
            copies.append((v,-1))
        if mode!='strict':
            copies.extend((v,i) for i in range(k) if v in pairs[i])
    rank={x:i for i,x in enumerate(copies)}
    def at(v,i):
        if mode=='strict' or v not in terminals:
            return rank[v,-1]
        if v in pairs[i]:
            return rank[v,i]
        return rank[v,-1] if mode=='internal_only' else None
    size=len(copies)+k
    graphs=[[[0]*size for _ in range(size)] for _ in pairs]
    seeds=[]
    for i,(s,t) in enumerate(pairs):
        seeds.append(at(s,i))
        ds=[None]*n
        ds[s]=0
        for u in range(n):
            if ds[u] is not None:
                for a,b,w in edges:
                    if a==u and (ds[b] is None or ds[b]>ds[u]+w):
                        ds[b]=ds[u]+w
        for u,v,w in edges:
            cu,cv=at(u,i),at(v,i)
            if cu is not None and cv is not None and v!=s and u!=t and ds[u] is not None and ds[v]==ds[u]+w:
                graphs[i][cu][cv]=1
        graphs[i][at(t,i)][len(copies)+i]=1
    return graphs,tuple(seeds),tuple(range(len(copies),size))


def path_answer(n,edges,pairs,mode):
    families=[all_shortest(n,edges,s,t) for s,t in pairs]
    for ps in product(*families):
        valid=True
        for i,j in combinations(range(len(pairs)),2):
            common=set(ps[i])&set(ps[j])
            if mode=='endpoints_only':
                common-=set(pairs[i])&set(pairs[j])
            if mode=='internal_only':
                common=set(ps[i][1:-1])&set(ps[j][1:-1])
            if common:
                valid=False
                break
        if valid:
            return True
    return False


def check_partition(N,k):
    checked=0
    def node(l,r):
        nonlocal checked
        if l==r:return
        h=(l+r)//2
        for p in product(range(h+1,N),repeat=k):
            if len(set(p))<k:continue
            for i in range(k):
                x=p[i]; c=p[:i]+p[i+1:]
                matches=int(h<x<=r)
                matches+=sum(int(x>r and h<c[j]<=r and all(y>r for y in c[:j])) for j in range(k-1))
                assert matches==int(min(p)<=r)
                checked+=1
        node(l,h);node(h+1,r)
    node(0,N-1)
    return checked


def main():
    start=time.monotonic()
    rng=random.Random(321502)
    counts=Counter(); cases=Counter(); yes=Counter()
    # Labelled graphs with arbitrary source order; full state sets, not only final answers.
    for k, sizes in [(2,[3,4,5,7]),(3,[3,4,5,7,9]),(4,[4,5,7]),(5,[5,7])]:
        for n in sizes:
            for trial in range(5):
                density=[0,.15,.5,.9,1][trial]
                graphs=[[[int(u<v and rng.random()<density) for v in range(n)] for u in range(n)] for _ in range(k)]
                seed=tuple(rng.sample(range(n),k))
                expected=queue_oracle(graphs,seed)
                observed=rectangular_schedule(graphs,seed,counts)
                assert observed==expected,(k,n,trial,sorted(observed^expected))
                cases[f'labelled_k{k}']+=1
                counts['full_state_set_equalities']+=1
    # Fresh weighted cases, repeated/trivial/reversed endpoints, large integer weights.
    for trial in range(28):
        n=6
        edges=[(u,v,(1<<150)+rng.randrange(1,5) if trial%4==0 else v-u if trial%2 else rng.randrange(1,8))
               for u in range(n) for v in range(u+1,n) if rng.random()<[.2,.6,1][trial%3]]
        pairs=[tuple(rng.randrange(n) for _ in range(2)) for _ in range(3)]
        if trial%7==0:pairs=[(0,3),(1,4),(2,5)]
        for mode in ['strict','endpoints_only','internal_only']:
            expected=path_answer(n,edges,pairs,mode)
            normalized=normalize(n,edges,pairs,mode)
            if normalized is None:
                observed=False
            else:
                graphs,seed,target=normalized
                states=rectangular_schedule(graphs,seed,counts)
                assert states==queue_oracle(graphs,seed)
                counts['full_state_set_equalities']+=1
                observed=target in states
            assert observed==expected,(trial,mode,pairs)
            cases[f'weighted_{mode}']+=1
            yes[mode]+=observed
    fixtures=[
        ('shared_source',6,[(0,3,1),(0,4,1),(1,5,1)],[(0,3),(0,4),(1,5)]),
        ('endpoint_internal',6,[(0,1,1),(1,3,1),(1,4,1),(2,5,1)],[(0,3),(1,4),(2,5)]),
        ('shared_trivial',5,[(0,3,1),(1,4,1)],[(0,0),(0,3),(1,4)]),
        ('early_completion',6,[(0,1,1),(2,5,1),(3,4,1)],[(0,1),(2,5),(3,4)]),
        ('shortest_conflict',7,[(i,3,1) for i in range(3)]+[(3,4+i,1) for i in range(3)]+[(i,4+i,5) for i in range(3)],[(0,4),(1,5),(2,6)])]
    fixture_results={}
    for name,n,edges,pairs in fixtures:
        fixture_results[name]={}
        for mode in ['strict','endpoints_only','internal_only']:
            expected=path_answer(n,edges,pairs,mode)
            normalized=normalize(n,edges,pairs,mode)
            if normalized is None:
                observed=False
            else:
                graphs,seed,target=normalized
                states=rectangular_schedule(graphs,seed,counts)
                assert states==queue_oracle(graphs,seed)
                counts['full_state_set_equalities']+=1
                observed=target in states
            assert observed==expected,(name,mode)
            fixture_results[name][mode]=observed
            cases[f'fixture_{mode}']+=1
    partitions={f'N{N}_k{k}':check_partition(N,k) for N,k in [(4,2),(8,3),(8,4),(16,3)]}
    result={'job_id':JOB,'status':'passed','seed':321502,'cases':dict(cases),'yes_weighted':dict(yes),'fixture_results':fixture_results,'counts':dict(counts),'partition_combinations':partitions,'elapsed_seconds':time.monotonic()-start,'scope':'New generic-k rectangular schedule; entire reachable sets versus independent queue traversal; weighted final answers versus direct original shortest-path enumeration under three endpoint conventions. Finite tests only.','backend':'Exact naive integer rectangular product modulo a deterministically selected prime p>N, including full padding.','fast_rectangular_algorithm_implemented':False,'exponent_benchmark':False,'fresh_referee':False}
    Path(__file__).with_name('validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
