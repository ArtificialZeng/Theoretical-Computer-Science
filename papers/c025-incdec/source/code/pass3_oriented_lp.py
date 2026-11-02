#!/usr/bin/env python3
"""Independent full-table LP attack on oriented one-sided objective greedy."""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,vstack
from pass2_residual import build
OUT=Path('evidence/research-pass-3')
def main():
    start=time.monotonic();limit=75;stats=[];found=None
    for n in [3,4,5,6,7,8]:
        fv,rows,eq,states,order=build(n,'L'*n);N=(1<<n)-1;V=2*(N+1)
        # h(E)>=g(E), exactly the analyzed orientation.
        orient=np.zeros(V,dtype=int);orient[N]=-1;orient[2*N+1]=1;rows.append(orient)
        A=csr_matrix(np.array(rows));s=dict(n=n,calls=0,failures=0,maximum_violation=0.0,complete=False)
        for O in range(1,N):
            k=O.bit_count();P=(1<<k)-1;obj=fv[O].astype(int)-2*fv[P]
            r=linprog(-obj,A_ub=A,b_ub=np.zeros(len(rows)),A_eq=eq,b_eq=[0,0,1],bounds=(0,None),method='highs',options={'time_limit':2.0});s['calls']+=1
            if not r.success:s['failures']+=1
            else:
                val=float(obj@r.x);s['maximum_violation']=max(s['maximum_violation'],val)
                if val>1e-7:
                    found=dict(n=n,O=O,P=P,numerical_gap=val);break
            if time.monotonic()-start>limit:break
        else:s['complete']=True
        stats.append(s)
        if found or time.monotonic()-start>limit:break
    result=dict(seconds=time.monotonic()-start,limit_seconds=limit,stats=stats,numerical_witness=found,scope='Numerical adversarial screening, not proof. All full-table monotonicity/submodularity and every greedy comparison for canonical one-sided trace; endpoint orientation imposed. Canonical trace covers every tie-admissible greedy order up to relabeling. Universal analytic proof is separate.')
    (OUT/'oriented-greedy-lp.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
