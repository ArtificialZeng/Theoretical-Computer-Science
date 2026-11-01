"""Independent exact arithmetic verification of saved full-domain certificates.

Does not import the optimizer or vertex enumerator. For all buy-days above
M=max(b,N+1), g is constant, the prefix dual sum is empty, and lambda>=0;
thus the dual inequality at M extends to every such day. Prefixes and the
limiting moment certify hard robustness at every actual integer horizon.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import hashlib


def check_original(rec):
    b,R = rec['b'],Q(rec['R'])
    p={int(x):Q(v) for x,v in rec['p'].items()}
    r=rec['result']
    f={int(t):Q(v) for t,v in r['policy'].items()}
    y={int(x):Q(v) for x,v in r['y'].items()}
    lam,alpha=Q(r['lam']),Q(r['alpha'])
    assert b>=2 and R>=Q(b**b,b**b-(b-1)**b)
    assert min(p)>=1 and min(p.values())>=0 and sum(p.values())==1
    assert min(f)>=1 and min(f.values())>=0 and sum(f.values())==1
    assert set(y)==set(range(1,b)) and min(y.values())>=0 and lam>=0
    def cost(t,x): return b+t-1 if t<=x else x
    def g(t): return sum(v*cost(t,x) for x,v in p.items())
    K=(R-1)*b
    mu=sum((t-1)*v for t,v in f.items())
    assert mu<=K
    for x in range(1,b):
        prefix=sum((b+t-1-x)*v for t,v in f.items() if t<=x)
        assert prefix<=(R-1)*x
    M=max(b,max(p)+1,max(f))
    for t in range(1,M+1):
        adjusted=g(t)+lam*(t-1)+sum((b+t-1-x)*y[x] for x in range(t,b))
        assert adjusted>=alpha
    for x in range(1,M+1):
        assert sum(v*cost(t,x) for t,v in f.items())<=R*min(x,b)
    value=sum(v*g(t) for t,v in f.items())
    dual=alpha-(R-1)*sum(x*v for x,v in y.items())-lam*K
    assert value==dual==Q(rec['value'])
    assert lam*(K-mu)==0
    return value


def check_linear(rec):
    b,R=rec['b'],Q(rec['R'])
    costs={int(t):Q(v) for t,v in rec['costs'].items()}
    f={int(t):Q(v) for t,v in rec['policy'].items()}
    y={int(t):Q(v) for t,v in rec['y'].items()}
    alpha=Q(rec['alpha'])
    assert sum(f.values())==1 and min(f.values())>=0 and set(f)<=set(costs)
    assert min(y.values())>=0
    for x in range(1,b):
        assert sum((b+t-1-x)*v for t,v in f.items() if t<=x)<=(R-1)*x
    for t,c in costs.items():
        assert c+sum((b+t-1-x)*y[x] for x in range(t,b))>=alpha
    val=sum(costs[t]*v for t,v in f.items())
    assert val==alpha-(R-1)*sum(x*v for x,v in y.items())==Q(rec['value'])


def main():
    counts={}
    files=['evidence/oracle-test-cases.json','evidence/bisection-test-cases.json',
           'evidence/linear-oracle-test-cases.json']
    for name in files:
        cases=json.loads(Path(name).read_text())
        for rec in cases:
            (check_linear if 'linear-oracle' in name else check_original)(rec)
        counts[name]=len(cases)
    result=dict(job_id='robust-stopping-research-a43d444f406e',
                status='all serialized rational inequalities verified',counts=counts,
                hashes={name:hashlib.sha256(Path(name).read_bytes()).hexdigest()
                        for name in files},
                meaning='Same-worker independent arithmetic checker; no fresh referee')
    Path('evidence/oracle-certificates.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
