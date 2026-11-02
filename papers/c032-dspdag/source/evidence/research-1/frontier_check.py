#!/usr/bin/env python3
"""Exact finite validation; not a universal correctness/complexity proof."""
import hashlib, itertools, json, math, pathlib, random, time
JOB='c032-dspdag-research-2c4a21894757'

def mm_naive(a,b):
    n=len(a)
    return [[sum(a[i][q]*b[q][j] for q in range(n)) for j in range(n)] for i in range(n)]

def add(a,b,sign=1):
    return [[x+sign*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def mm_strassen(a,b):
    n=len(a)
    if n<=2:return mm_naive(a,b)
    h=n//2
    def quad(c):return [[r[:h] for r in c[:h]],[r[h:] for r in c[:h]],[r[:h] for r in c[h:]],[r[h:] for r in c[h:]]]
    A,B,C,D=quad(a);E,F,G,H=quad(b)
    p=mm_strassen(add(A,D),add(E,H));q=mm_strassen(add(C,D),E)
    r=mm_strassen(A,add(F,H,-1));s=mm_strassen(D,add(G,E,-1))
    t=mm_strassen(add(A,B),H);u=mm_strassen(add(C,A,-1),add(E,F));v=mm_strassen(add(B,D,-1),add(G,H))
    aa=add(add(add(p,s),t,-1),v);bb=add(r,t);cc=add(q,s);dd=add(add(add(p,q,-1),r),u)
    return [aa[i]+bb[i] for i in range(h)]+[cc[i]+dd[i] for i in range(h)]

def tight_graphs(n,edges,pairs):
    out=[[] for _ in range(n)]
    for u,v,w in edges:out[u].append((v,w))
    graphs=[]
    for s,t in pairs:
        d=[None]*n;d[s]=0
        for u in range(n):
            if d[u] is None:continue
            for v,w in out[u]:
                if d[v] is None or d[v]>d[u]+w:d[v]=d[u]+w
        a=[[False]*(n+3) for _ in range(n+3)]
        for u,v,w in edges:
            if d[u] is not None and d[v]==d[u]+w:a[u][v]=True
        graphs.append(a)
    for i,(s,t) in enumerate(pairs):graphs[i][t][n+i]=True
    return graphs

def path_oracle(n,edges,pairs):
    out=[[] for _ in range(n)]
    for u,v,w in edges:out[u].append((v,w))
    sets=[]
    for s,t in pairs:
        paths=[]
        def walk(v,length,mask):
            if v==t:paths.append((length,mask));return
            for z,w in out[v]:walk(z,length+w,mask|(1<<z))
        walk(s,0,1<<s)
        if not paths:return False
        d=min(x[0] for x in paths)
        sets.append([mask for length,mask in paths if length==d])
    def pack(i,mask):
        if i==3:return True
        return any(not(mask&p) and pack(i+1,mask|p) for p in sets[i])
    return pack(0,0)

def tables(graphs,sources,do_cdq):
    n0=len(graphs[0]);N=1<<(n0-1).bit_length();size=N**3
    a=[]
    for g in graphs:a.append([list(row)+[False]*(N-n0) for row in g]+[[False]*N for _ in range(N-n0)])
    F=[False]*size
    def idx(q):return (q[0]*N+q[1])*N+q[2]
    F[idx(sources)]=True
    products=0
    def put(i,u,c):
        q=list(c);q.insert(i,u);return q
    if not do_cdq:
        for u in range(N):
            for i in range(3):
                for c in itertools.product(range(u+1,N),repeat=2):
                    q=put(i,u,c)
                    if len(set(q))<3 or not F[idx(q)]:continue
                    for x in range(u+1,N):
                        z=put(i,x,c)
                        if a[i][u][x] and len(set(z))==3:F[idx(z)]=True
    else:
        def rec(l,r):
            nonlocal products
            if l==r:return
            h=(l+r)//2;b=h-l+1;rec(l,h)
            L=list(range(l,h+1));R=list(range(h+1,r+1));T=list(range(r+1,N));S=list(range(h+1,N))
            for i in range(3):
                classes=[(list(itertools.product(S,S)),R),(list(itertools.product(R,S)),T),(list(itertools.product(T,R)),T)]
                for contexts,targets in classes:
                    for start in range(0,len(contexts),b):
                        rows=contexts[start:start+b]
                        for tx in range(0,len(targets),b):
                            cols=targets[tx:tx+b]
                            B=[[int(F[idx(put(i,u,c))]) for u in L] for c in rows]
                            B += [[0]*b for _ in range(b-len(B))]
                            C=[[int(a[i][u][x]) for x in cols]+[0]*(b-len(cols)) for u in L]
                            D=mm_strassen(B,C);products+=1
                            for rr,c in enumerate(rows):
                                for cc,x in enumerate(cols):
                                    z=put(i,x,c)
                                    if D[rr][cc]>0 and len(set(z))==3:F[idx(z)]=True
            rec(h+1,r)
        rec(0,N-1)
    return F,N,products

def check_case(n,edges,pairs):
    graphs=tight_graphs(n,edges,pairs)
    baseline,N,_=tables(graphs,tuple(s for s,t in pairs),False)
    batched,N,products=tables(graphs,tuple(s for s,t in pairs),True)
    if baseline!=batched:
        bad=next(i for i,(a,b) in enumerate(zip(baseline,batched)) if a!=b)
        raise AssertionError(('table mismatch',n,edges,pairs,bad))
    q=(n,n+1,n+2);answer=batched[(q[0]*N+q[1])*N+q[2]]
    oracle=path_oracle(n,edges,pairs)
    if answer!=oracle:raise AssertionError(('oracle mismatch',n,edges,pairs,answer,oracle))
    return products,answer

def main():
    started=time.monotonic();rng=random.Random(32017);counts={'strassen_matrices':0,'exhaustive_hub_dags':0,'random_weighted_dags':0,'random_potential_dags':0,'structured_cases':0};yes=0;products=0
    for n in (1,2,4,8):
        for _ in range(12):
            a=[[rng.randrange(2) for j in range(n)] for i in range(n)];b=[[rng.randrange(2) for j in range(n)] for i in range(n)]
            assert mm_strassen(a,b)==mm_naive(a,b);counts['strassen_matrices']+=1
    pairs=[(0,4),(1,5),(2,6)];poss=[(i,4+i) for i in range(3)]+[(i,3) for i in range(3)]+[(3,4+i) for i in range(3)]
    for mask in range(1<<len(poss)):
        edges=[(u,v,v-u) for j,(u,v) in enumerate(poss) if mask>>j&1]
        p,a=check_case(7,edges,pairs);products+=p;yes+=a;counts['exhaustive_hub_dags']+=1
    for mode in ('weighted','potential'):
        for n in range(6,11):
            for trial in range(16):
                terminals=rng.sample(range(n),6);pairs=[tuple(sorted(terminals[2*i:2*i+2])) for i in range(3)]
                density=(.15,.4,.75,1)[trial%4]
                edges=[(u,v,(rng.randrange(1,10) if mode=='weighted' else v-u)) for u in range(n) for v in range(u+1,n) if rng.random()<density]
                p,a=check_case(n,edges,pairs);products+=p;yes+=a;counts['random_'+mode+'_dags']+=1
    for n in (6,7,9,10):
        pairs=[(0,n-3),(1,n-2),(2,n-1)]
        for family in ('empty','complete','chain'):
            edges=[(u,v,v-u) for u in range(n) for v in range(u+1,n) if family=='complete' or family=='chain' and v==u+1]
            p,a=check_case(n,edges,pairs);products+=p;yes+=a;counts['structured_cases']+=1
    result={'job_id':JOB,'status':'all_checks_passed','counts':counts,'dag_instances':sum(v for k,v in counts.items() if k!='strassen_matrices'),'yes_instances':yes,'square_products_executed':products,'rng_seed':32017,'n_original_range':[6,10],'padded_frontier_vertices':16,'integer_arithmetic':'exact Python integers, Strassen recursion threshold 2','comparison':'entire reachable frontier table against scalar earliest-token recurrence; final answer against independently enumerated shortest path masks','exhaustiveness':'All 512 subsets of the nine stated hub-family edges only; random and structured tests are not exhaustive over all DAGs.','elapsed_seconds':time.monotonic()-started}
    path=pathlib.Path(__file__).with_name('frontier-check.json');path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
