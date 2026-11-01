"""Fresh pure-bisection executions and direct primal/dual checks."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('old_oracle', ROOT/'evidence/prefix_oracle.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

cases = [
    (3,F(3,2),{1:F(2,5),2:F(3,5)}),
    (3,F(3,2),{1:F(1,2),2:F(1,2)}),
    (3,F(29,20),{i:F(1,3) for i in range(1,4)}),
    (5,F(5**5,5**5-4**5),{i:F(1,5) for i in range(1,6)}),
    (2,F(7,5),{1:F(9,10),10**12:F(1,10)}),
    (7,F(2),{1:F(1,3),5:F(1,3),100:F(1,3)})
]
records=[]
for b,R,p in cases:
    out=old.optimize(b,R,p,max_chord_probes=0)
    assert not out.get('chord_probes',0)
    f,lam,alpha,y=(out[k] for k in ('policy','lam','alpha','y'))
    r=R-1
    assert sum(f.values())==1 and min(f.values())>0 and lam>=0 and min(y.values())>=0
    for x in range(1,b):
        assert sum((b-1+t-x)*v for t,v in f.items() if t<=x)<=r*x
    assert sum((t-1)*v for t,v in f.items())<=r*b
    # Every prefix day and every tail interval's left endpoint.
    days=sorted(set(range(1,b+1)) | {d+1 for d,v in p.items() if v and d>=b})
    def g(t):
        return sum(v*(b+t-1 if t<=d else d) for d,v in p.items())
    for t in days:
        assert g(t)+lam*(t-1)+sum((b-1+t-x)*v for x,v in y.items() if x>=t)>=alpha
    # On any omitted tail interval, g(t)+lam*(t-1) has slope Pr[D>=t]+lam>=0.
    J=sum(g(t)*v for t,v in f.items())
    assert J==alpha-r*sum(x*v for x,v in y.items())-lam*r*b
    assert len(f)<=b+1 and sum(t>=b for t in f)<=2
    records.append({'b':b,'R':R,'p':p,'value':J,'certificate':out})
result={'status':'passed','job_id':'robust-stopping-research-cd75b220d422',
        'cases':len(records),'actual_bisection_steps':[r['certificate']['isolation_steps'] for r in records],
        'chord_probes':0,'records':records,
        'scope':'Six new exact executions, not proof of the universal algorithm.'}
(ROOT/'revision/pure-bisection-checks.json').write_text(json.dumps(result,default=str,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
