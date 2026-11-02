#!/usr/bin/env python3
"""Exact adversarial checks for endpoint-oriented one-sided objective greedy."""
import json,hashlib,itertools
from pathlib import Path
from fractions import Fraction as Q
from chain_dp import source_cases,random_cases,enc
OUT=Path('evidence/research-pass-3')

def run(name,h,g):
    n=(len(h)-1).bit_length();N=(1<<n)-1
    reverse=h[N]<g[N]
    if reverse:h,g=g,h
    G=g[N];H=h[N];assert H>=G
    f=[h[s]+g[N^s] for s in range(N+1)]
    S=0;order=[];gains=[];states=[]
    for k in range(n):
        a,e=max((f[S|1<<e]-f[S],-e) for e in range(n) if not S>>e&1);e=-e
        if gains:assert gains[-1]>=a
        gains.append(a);S|=1<<e;order.append(e)
        d=max((f[S|1<<j]-f[S] for j in range(n) if not S>>j&1),default=Q(0))
        opt=max(f[o] for o in range(N+1) if o.bit_count()==k+1)
        assert opt<=2*f[S],(name,k+1,opt,f[S])
        if k+1<n and d>=0:
            assert (k+1)*d<=f[S]-G
            for O in range(N+1):
                if O.bit_count()==k+1:
                    assert f[O]<=f[S|O]+G
                    assert f[S|O]<=f[S]+(O&~S).bit_count()*d
        elif k+1<n:
            assert f[S]>=H
        states.append(dict(k=k+1,S=S,value=str(f[S]),opt=str(opt),d=str(d)))
    original_h,original_g=(g,h) if reverse else (h,g)
    p=order[::-1] if reverse else order
    fs=[original_h[s]+original_g[N^s] for s in range(N+1)]
    S=0
    for k,e in enumerate(p,1):
        S|=1<<e
        assert max(fs[o] for o in range(N+1) if o.bit_count()==k)<=2*fs[S]
    return dict(name=name,n=n,reversed=reverse,order=p,gains=list(map(str,gains)),states=states)

def main():
    cases=list(itertools.chain(source_cases(),random_cases()))
    for file in ['template-screen.json','comparator-screen.json']:
        data=json.loads((Path('evidence/research-pass-2')/file).read_text())
        for key,w in data['exact_witnesses'].items():cases.append((key,list(map(Q,w['h'])),list(map(Q,w['g'])),{}))
    w=json.loads((OUT/'prefix-kernel-screen.json').read_text())['exact_witness']
    if w:cases.append(('new-prefix-kernel-witness',list(map(Q,w['h'])),list(map(Q,w['g'])),{}))
    result=[]
    for name,h,g,desc in cases:result.append(run(name,h,g))
    # Zero function and empty ground set; n=0 needs no greedy choice.
    result.append(run('empty',[Q(0)],[Q(0)]))
    result.append(run('all-zero-n4',[Q(0)]*16,[Q(0)]*16))
    (OUT/'oriented-greedy-exact.json').write_text(json.dumps(dict(job_id='c025-incdec-research-76b5f4e5209a',case_count=len(result),all_checks_pass=True,cases=result,scope='Finite exact validation of algorithm and proof steps; the universal proof is separate.'),indent=2)+'\n')
    print(json.dumps(dict(case_count=len(result),all_checks_pass=True,source_unchanged=hashlib.sha256(Path('source.md').read_bytes()).hexdigest()=='12956c470e37f8a548f510c7eb1781eda7b961999c5fa1163df43b56513b45a4')))
if __name__=='__main__':main()
