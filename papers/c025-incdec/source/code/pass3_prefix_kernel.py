#!/usr/bin/env python3
"""Bounded prefix-only residual attack. Solver nonfindings are not proofs."""
import itertools,json,random,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack
from pass2_residual import build
from chain_dp import verify_function
OUT=Path('evidence/research-pass-3')

def exact(n,word,L,T,O,vals):
    N=(1<<n)-1;size=N+1;h=vals[:size];g=vals[size:2*size]
    verify_function(h,n);verify_function(g,n)
    assert h[0]==g[0]==0 and h[N]+g[N]==1
    f=[h[s]+g[N^s] for s in range(size)];S=0;B=N;trace=[]
    for i,sd in enumerate(word):
        a=f[S|1<<i]-f[S] if sd=='L' else f[B^1<<i]-f[B]
        assert a==max([f[S|1<<j]-f[S] for j in range(i,n)]+[f[B^1<<j]-f[B] for j in range(i,n)])
        trace.append(dict(step=i,side=sd,item=i,L=S,T=B,gain=str(a)))
        if sd=='L':S|=1<<i
        else:B^=1<<i
    assert (S,B)==(L,T) and O.bit_count()==L.bit_count()
    U=T^L;d=max([f[L|1<<j]-f[L] for j in range(n) if U>>j&1]+[f[T^1<<j]-f[T] for j in range(n) if U>>j&1],default=Q(0))
    gap=f[O]-f[L]-g[N]-L.bit_count()*d;assert gap>0
    return dict(n=n,word=word,L=L,T=T,O=O,d=str(d),gap=str(gap),h=list(map(str,h)),g=list(map(str,g)),f=list(map(str,f)),trace=trace,scope='Counterexample to residual kernel only, not original problem.')

def main():
    start=time.monotonic();limit=70;rng=random.Random(2511303);calls=0;failures=0;witness=None;cases=[]
    for n in [7,8,9]:
        words=[]
        for t in [2,3,4,5,n-2,n-1]:
            if not 1<=t<n:continue
            for _ in range(5):
                w=''.join(rng.choice('LR') for i in range(t-1))+'L'
                if 'R' in w:words.append(w)
        rng.shuffle(words)
        for word in dict.fromkeys(words):
            if time.monotonic()-start>limit:break
            fv,rows,eq,states,order=build(n,word);L,T,_=states[-1];size=1<<n;V=2*size;k=L.bit_count()
            M=hstack([csr_matrix(np.array(rows)),csr_matrix((len(rows),1))],format='csr')
            extra=[]
            for j in range(len(word),n):
                for v in [fv[L|1<<j]-fv[L],fv[T^1<<j]-fv[T]]:
                    z=np.zeros(V+1,dtype=np.int8);z[:V]=v;z[V]=-1;extra.append(z)
            M=vstack([M,csr_matrix(np.array(extra))],format='csr');eq=hstack([csr_matrix(eq),csr_matrix((3,1))],format='csr')
            # Remaining items are interchangeable: O uses its first a items.
            seen=0
            masks=list(range(1<<len(word)));rng.shuffle(masks)
            for chosen in masks:
                a=k-chosen.bit_count()
                if not 0<=a<=n-len(word):continue
                O=chosen|(((1<<a)-1)<<len(word))
                obj=np.zeros(V+1,dtype=int);obj[:V]=fv[O].astype(int)-fv[L];obj[size+size-1]-=1;obj[V]=-k
                r=linprog(-obj,A_ub=M,b_ub=np.zeros(M.shape[0]),A_eq=eq,b_eq=[0,0,1],bounds=(0,None),method='highs',options={'time_limit':2.0});calls+=1;seen+=1
                if not r.success:failures+=1
                elif obj@r.x>1e-7:
                    vals=[Q(float(x)).limit_denominator(10**7) for x in r.x]
                    try:witness=exact(n,word,L,T,O,vals)
                    except AssertionError:pass
                if witness or time.monotonic()-start>limit:break
            cases.append(dict(n=n,word=word,comparators_tested=seen))
            if witness or time.monotonic()-start>limit:break
        if witness or time.monotonic()-start>limit:break
    result=dict(limit_seconds=limit,seconds=time.monotonic()-start,lp_calls=calls,solver_failures=failures,cases=cases,exact_witness=witness,scope='Prefix-only greedy constraints with d constrained above every current gain. Arbitrary monotone submodular h,g represented by full tables. Random subset of prefix words and comparators, not exhaustion. No numerical nonfinding is a proof.')
    (OUT/'prefix-kernel-screen.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='exact_witness'},indent=2));print('exact_witness',witness is not None)
if __name__=='__main__':main()
