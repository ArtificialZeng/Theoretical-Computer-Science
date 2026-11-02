#!/usr/bin/env python3
"""New bounded LP attack on explicit residual templates; numerical discovery only."""
import argparse,itertools,json,time,random
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix
from chain_dp import verify_function

OUT=Path('evidence/research-pass-2')
def build(n,word):
    N=(1<<n)-1;V=2*(N+1)
    fv=np.zeros((N+1,V),dtype=np.int8)
    for s in range(N+1):fv[s,s]=fv[s,N+1+(N^s)]=1
    rows=[]
    for off in (0,N+1):
        for s in range(N+1):
            for i in range(n):
                if s>>i&1:continue
                v=np.zeros(V,dtype=np.int8);v[off+s]=1;v[off+(s|1<<i)]=-1;rows.append(v)
                for j in range(i+1,n):
                    if s>>j&1:continue
                    v=np.zeros(V,dtype=np.int8);v[off+s]=v[off+(s|1<<i|1<<j)]=1;v[off+(s|1<<i)]=v[off+(s|1<<j)]=-1;rows.append(v)
    base=list(rows);states=[];S=0;T=N;left=[];right=[]
    for i,sd in enumerate(word):
        chosen=fv[S|1<<i]-fv[S] if sd=='L' else fv[T^1<<i]-fv[T]
        for j in range(i,n):
            rows.append(fv[S|1<<j]-fv[S]-chosen)
            rows.append(fv[T^1<<j]-fv[T]-chosen)
        if sd=='L':S|=1<<i;left.append(i)
        else:T^=1<<i;right.append(i)
        states.append((S,T,len(rows)))
    eq=np.zeros((3,V),dtype=np.int8);eq[0,0]=eq[1,N+1]=eq[2,N]=eq[2,2*N+1]=1
    return fv,rows,eq,states,left+right[::-1]

def verify(n,word,vals,objective):
    N=(1<<n)-1;h=vals[:N+1];g=vals[N+1:]
    verify_function(h,n);verify_function(g,n)
    assert h[0]==g[0]==0 and h[N]+g[N]==1
    f=[h[s]+g[N^s] for s in range(N+1)]
    S=0;T=N;trace=[]
    for i,sd in enumerate(word):
        chosen=f[S|1<<i]-f[S] if sd=='L' else f[T^1<<i]-f[T]
        choices=[f[S|1<<j]-f[S] for j in range(i,n)]+[f[T^1<<j]-f[T] for j in range(i,n)]
        assert chosen==max(choices)
        if sd=='L':S|=1<<i
        else:T^=1<<i
        trace.append(dict(step=i,side=sd,S=S,T=T,gain=str(chosen)))
    val=sum((Q(int(c))*x for c,x in zip(objective,vals)),Q(0));assert val>0
    return dict(h=list(map(str,h)),g=list(map(str,g)),f=list(map(str,f)),trace=trace,violation=str(val))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--seconds',type=int,default=60);args=ap.parse_args();assert 1<=args.seconds<=90
    start=time.monotonic();rng=random.Random(25112);calls=0;witnesses={};failures=0;tested=[]
    # Strong h comparator and residual lemma are explicitly unproved templates.
    for n in [3,4,5,6,7]:
        words=list(itertools.product('LR',repeat=n));rng.shuffle(words)
        for word in words:
            if time.monotonic()-start>args.seconds:break
            fv,rows,eq,states,order=build(n,word);N=(1<<n)-1;V=2*(N+1);A=csr_matrix(np.array(rows));b=np.zeros(len(rows))
            for step,(S,T,cut) in enumerate(states):
                if word[step]!='L' or S==T:continue
                k=S.bit_count()
                dvec=fv[S|1<<(step+1)]-fv[S] if word[step+1]=='L' else fv[T^1<<(step+1)]-fv[T]
                for O in range(N+1):
                    if O.bit_count()!=k:continue
                    for kind in ['residual-f']:
                        if kind in witnesses:continue
                        objective=np.zeros(V,dtype=int);objective[O]+=1
                        objective=fv[O].astype(int)-fv[S]-k*dvec
                        objective[N+1+N]-=1
                        res=linprog(-objective,A_ub=A,b_ub=b,A_eq=eq,b_eq=[0,0,1],bounds=(0,None),method='highs',options={'time_limit':1.0});calls+=1
                        if not res.success:failures+=1;continue
                        val=float(objective@res.x)
                        if val>1e-7:
                            vals=[Q(float(x)).limit_denominator(10**6) for x in res.x]
                            try:exact=verify(n,word,vals,objective)
                            except AssertionError:continue
                            witnesses[kind]=dict(n=n,word=''.join(word),step=step,S=S,T=T,O=O,order=order,**exact)
                    if time.monotonic()-start>args.seconds or len(witnesses)==1:break
                if time.monotonic()-start>args.seconds or len(witnesses)==1:break
            tested.append(dict(n=n,word=''.join(word)))
            if time.monotonic()-start>args.seconds or len(witnesses)==1:break
        if time.monotonic()-start>args.seconds or len(witnesses)==1:break
    result=dict(seconds=time.monotonic()-start,limit_seconds=args.seconds,lp_calls=calls,solver_failures=failures,exact_witnesses=witnesses,trace_words=tested,scope='Templates only, not original problem; nonfindings numerical and bounded.')
    (OUT/'residual-screen.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
