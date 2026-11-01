"""Check the exact overlap with KF26 Theorem C.1(ii), y=b."""
from fractions import Fraction as F
from pathlib import Path
import json
from uniform_frontier import frontier,policy

records=[]
for b in range(2,31):
    data=frontier(b)
    cap=F(b-1,b)
    tested=0
    for row in data['segments']:
        for r in {row['lower'],(row['lower']+row['upper'])/2,row['upper']}:
            f=policy(b,r)['policy']
            P=sum(v for t,v in f.items() if t<=b)
            G=[r*(F(b,b-1)**x-1) for x in range(1,b+1)]
            Phi=lambda q: sum(min(v,q) for v in G)
            assert all(sum(v for t,v in f.items() if t<=x)==min(G[x-1],P) for x in range(1,b+1))
            assert Phi(P)==b*(1-r)
            if r<=cap:
                cheap=min(G[0],F(1))
                assert Phi(cheap)<=b*(1-r)
                # Phi is strictly increasing below G(b), so this is its first root.
                assert Phi(P)==max(b*(1-r),Phi(cheap))
                tested+=1
            else:
                assert P==1-r and set(f)<= {1,b+1}
                # One-hot-b objective equals b on these two days.
                assert sum((b+t-1 if t<=b else b)*v for t,v in f.items())==b
    records.append({'b':b,'exact_C1_selected_policy_cases':tested})
result={'status':'passed','source':'https://arxiv.org/html/2603.29233v1#A3.SS4',
        'statement':'For r<=1-1/b the uniform candidate coincides with C.1(ii), y=b; above that cut it selects another one-hot-b optimum.',
        'records':records,'selected_policy_cases':sum(r['exact_C1_selected_policy_cases'] for r in records),
        'limitation':'This is overlap evidence, not an additional novelty claim.'}
(Path(__file__).parent/'prior-overlap-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
