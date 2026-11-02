#!/usr/bin/env python3
"""Exact certificate and diagnostic verification, without numerical solvers."""
import json,hashlib,itertools
from fractions import Fraction as Q
from pathlib import Path
OUT=Path('evidence/research-pass-3')

def function(v,n):
    assert len(v)==1<<n and v[0]==0 and min(v)>=0
    for A in range(1<<n):
        for B in range(1<<n):
            if A&B==A:assert v[A]<=v[B]
            assert v[A]+v[B]>=v[A|B]+v[A&B]

def vec(*args):
    x={}
    for coef,term in args:
        for s,w in term.items():x[s]=x.get(s,0)+coef*w
    return {s:w for s,w in x.items() if w}
def F(s):return {('f',s):1}
def scalar(name):return {(name,0):1}

def certificate(n,k,O):
    P=(1<<k)-1;U=P|O;m=(O&~P).bit_count();N=(1<<n)-1
    marg={}
    for e in range(n):
        if O>>e&1 and not P>>e&1:marg=vec((1,marg),(1,F(P|1<<e)),(-1,F(P)))
    # A..E match the nonnegative summands in the proof's certificate identity.
    A=vec((1,scalar('G')),(1,F(U)),(-1,F(O)))
    B=vec((1,F(P)),(1,marg),(-1,F(U)))
    C=vec((m,scalar('d')),(-1,marg))
    D=vec((k-m,scalar('d')))
    E=vec((1,F(P)),(-1,scalar('G')),(-k,scalar('d')))
    assert vec((1,A),(1,B),(1,C),(1,D),(1,E))==vec((2,F(P)),(-1,F(O)))
    # Independently telescope the sum of greedy gains minus k*d.
    tel={}
    for i in range(1,k+1):tel=vec((1,tel),(1,F((1<<i)-1)),(-1,F((1<<(i-1))-1)),(-1,scalar('d')))
    assert vec((1,tel),(1,F(0)),(-1,scalar('G')))==E
    # Negative-tail identity, with H=f(E).
    a=vec((1,scalar('H')),(1,scalar('G')),(-1,F(O)))
    b=vec((1,scalar('H')),(-1,scalar('G')))
    c=vec((1,F(P)),(-1,scalar('H')))
    assert vec((1,a),(1,b),(2,c))==vec((2,F(P)),(-1,F(O)))

def diagnostic():
    w=json.loads((OUT/'prefix-kernel-screen.json').read_text())['exact_witness'];n=w['n'];N=(1<<n)-1
    h,g,f=([Q(x) for x in w[key]] for key in ['h','g','f']);function(h,n);function(g,n)
    assert f==[h[s]+g[N^s] for s in range(N+1)]
    L=0;T=N;left=[];right=[]
    for i,sd in enumerate(w['word']):
        a=f[L|1<<i]-f[L] if sd=='L' else f[T^1<<i]-f[T]
        allg=[f[L|1<<j]-f[L] for j in range(i,n)]+[f[T^1<<j]-f[T] for j in range(i,n)]
        assert a==max(allg)
        if sd=='L':L|=1<<i;left.append(i)
        else:T^=1<<i;right.append(i)
    assert (L,T)==(w['L'],w['T'])
    O=w['O'];k=L.bit_count();assert k==O.bit_count()
    d=max([f[L|1<<j]-f[L] for j in range(n) if T>>j&1 and not L>>j&1]+[f[T^1<<j]-f[T] for j in range(n) if T>>j&1 and not L>>j&1])
    gap=f[O]-f[L]-g[N]-k*d;assert gap==Q(w['gap'])==Q(1,29)
    # Reconstruct compact coverage descriptions from the independently stored table.
    hf=[(3,2),(6,2),(8,2),(9,10),(18,2),(34,2),(66,2),(130,2)];gf=[(3,5)]
    for q,features in [(h,hf),(g,gf)]:assert q==[sum((Q(v,29) for mask,v in features if mask&s),Q(0)) for s in range(N+1)]
    # Finish the prescribed prefix by a separate exact greedy implementation.
    while L!=T:
        options=[]
        for e in range(n):
            if T>>e&1 and not L>>e&1:
                options.extend([(f[L|1<<e]-f[L],0,-e,'L',e),(f[T^1<<e]-f[T],1,-e,'R',e)])
        gain,_,_,side,e=max(options);assert gain>=0
        if side=='L':L|=1<<e;left.append(e)
        else:T^=1<<e;right.append(e)
    order=left+right[::-1];P=0;ratios=[]
    for k,e in enumerate(order,1):
        P|=1<<e;opt=max(f[S] for S in range(N+1) if S.bit_count()==k);assert opt<=2*f[P]
        if f[P]:ratios.append(opt/f[P])
    return dict(n=n,prefix_word=w['word'],L=w['L'],T=w['T'],O=O,G=str(g[N]),H=str(h[N]),fL=str(f[w['L']]),fO=str(f[O]),d=str(d),residual_gap=str(gap),ratio2_gap_at_diagnostic=str(f[O]-2*f[w['L']]),all_pairwise_hypotheses_exact=True,compact_coverage_exact=True,maximal_prefix_exact=True,completed_order=order,completed_order_worst_ratio=str(max(ratios)),scope='Refutes only the old bidirectional residual kernel; not the new algorithm or original question.')

def main():
    count=0
    for n in range(2,10):
        for O in range(1,(1<<n)-1):certificate(n,O.bit_count(),O);count+=1
    # Direct lower-bound evaluation for finite n, plus symbolic formulas in proof.
    lower=[]
    for n in range(2,11):
        N=(1<<n)-1;q=[Q(n-1 if s&1 else s.bit_count()) for s in range(N+1)];function(q,n)
        f=[q[s]+q[N^s] for s in range(N+1)]
        assert max(f[s] for s in range(N+1) if s.bit_count()==1)==2*(n-1)
        assert max(f[s] for s in range(N+1) if s.bit_count()==n-1)==2*(n-1)
        for e in range(1,n):assert f[1<<e]==f[N^(1<<e)]==n
        lower.append(dict(n=n,ratio=str(Q(2*(n-1),n))))
    result=dict(job_id='c025-incdec-research-76b5f4e5209a',no_numerical_solver_used=True,coefficient_identity_cases=count,coefficient_identity_scope='Exact algebraic consistency of the displayed two universal proof identities for all comparator masks at n=2..9; their validity for arbitrary n is established by the written argument, not finite checking.',diagnostic=diagnostic(),lower_bound_finite_checks=lower,source_sha256=hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),fresh_referee_review=False)
    (OUT/'exact-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
