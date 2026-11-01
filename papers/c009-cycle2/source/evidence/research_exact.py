"""Adversarial exact diagnostics, independent standard-basis and combinatorial forms.
This finite experiment is not a proof of a universally quantified inequality.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import random, json, time, hashlib, datetime
ROOT=Path(__file__).resolve().parent.parent
JOB='c009-cycle2-research-347a4f87d1ce'
SEED=347487
rng=random.Random(SEED)
def tr(A): return [list(x) for x in zip(*A)]
def mm(A,B):
    cols=tr(B)
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in cols] for row in A]
def mv(A,x): return [sum((a*b for a,b in zip(row,x)),F(0)) for row in A]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))
def plus(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(c,A): return [[c*x for x in row] for row in A]
def out(x,y): return [[a*b for b in y] for a in x]
def ident(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def trace(A): return sum((A[i][i] for i in range(len(A))),F(0))
start=time.monotonic()
identity_cases=[]
for n in range(1,10):
  for case in range(30):
    # Rational Householder image of e1: general rational unit vectors.
    v=[F(rng.randrange(-4,5)) for _ in range(n)]
    if not any(v):v[0]=F(1)
    u=[F(i==0)-2*v[i]*v[0]/dot(v,v) for i in range(n)]
    assert dot(u,u)==1
    P=out(u,u); Pi=plus(ident(n),scale(-1,P))
    raw=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):
        raw[i][j]=F(rng.randrange(-9,10),rng.randrange(1,8))*(10**(case%5-2) if case%5>=2 else F(1,10**(2-case%5)))
        raw[j][i]=-raw[i][j]
    if case%10==0: B=mm(mm(Pi,raw),Pi) # b=0 in arbitrary basis
    elif case%10==1:
      w=mv(Pi,[F(rng.randrange(-3,4)) for i in range(n)])
      B=plus(out(w,u),scale(-1,out(u,w))) # D=0
    else:B=raw
    T=plus(scale(F(1,2),P),B); M=mm(T,T)
    b=mv(B,u); a=dot(b,b); D=mm(mm(Pi,B),Pi)
    Db=mv(D,b); DD_b=mv(D,Db)
    x=[ui+2*bi for ui,bi in zip(u,b)]; z=mv(tr(M),x)
    expansion=[ui/4-(F(1,2)+2*a)*bi+di+2*ddi for ui,bi,di,ddi in zip(u,b,Db,DD_b)]
    assert z==expansion
    residual=dot(z,z)-dot(x,x)/16
    rhs=2*a*a+4*a*a*a+(3+8*a)*dot(Db,Db)+4*dot(DD_b,DD_b)
    assert residual==rhs and residual>=0
    Q=mm(M,tr(M)); R=plus(mm(D,D),scale(-1,out(b,b))); y=[bi/2+di for bi,di in zip(b,Db)]
    assert mm(mm(Pi,Q),Pi)==plus(out(y,y),mm(R,R))
    identity_cases.append({'n':n,'case':case,'degeneracy':'b=0' if case%10==0 else 'D=0' if case%10==1 else 'unrestricted','residual':str(residual)})
# Exhaust all explicitly stated weighted grids, without symmetry reduction.
density_counts={}; min_ratios={}; direct_cases=[]
for n,grid,maxell in [(2,[F(k,4) for k in range(5)],8),(3,[F(k,4) for k in range(5)],6),(4,[F(0),F(1,2),F(1)],4)]:
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    cnt=0; minratio=None
    for vals in product(grid,repeat=len(pairs)):
      A=[[F(1,2) for _ in range(n)] for _ in range(n)]
      for (i,j),val in zip(pairs,vals):A[i][j]=val;A[j][i]=1-val
      T=scale(F(1,n),A); M=mm(T,T); Q=mm(M,tr(M)); W=ident(n)
      for ell in range(1,maxell+1):
        W=mm(W,Q); density=trace(W); baseline=F(1,16)**ell
        assert density>=baseline
        if A!=[[F(1,2) for _ in range(n)] for _ in range(n)]:assert density>baseline
        ratio=density/baseline; minratio=ratio if minratio is None else min(minratio,ratio)
      cnt+=1
    density_counts[str(n)]={'grid':[str(x) for x in grid],'matrices':cnt,'ell_range':[1,maxell],'trace_tests':cnt*maxell,'minimum_density_to_baseline_ratio':str(minratio)}
# Independently sum vertex maps at selected extreme nonregular cases, ell=1,2.
for n,ell in [(2,3),(3,2),(4,1)]:
    A=[[F(1,2) for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(i+1,n):A[i][j]=F((3*i+2*j+1)%5,4);A[j][i]=1-A[i][j]
    total=F(0)
    for f in product(range(n),repeat=4*ell):
      p=F(1)
      for i in range(4*ell):
        j=(i+1)%(4*ell)
        p*=A[f[i]][f[j]] if i%4<2 else A[f[j]][f[i]]
      total+=p
    M=mm(A,A); Q=mm(M,tr(M)); W=ident(n)
    for _ in range(ell):W=mm(W,Q)
    assert total==trace(W)
    direct_cases.append({'n':n,'ell':ell,'vertex_maps':n**(4*ell),'density':str(total/n**(4*ell))})
# Exact regular-host sharpness family in n=3 and ell up to 12.
K=[[F(0),F(1),F(-1)],[F(-1),F(0),F(1)],[F(1),F(-1),F(0)]]
sharp=[]
for r in [F(1,2),F(1,7),F(1,31),F(1,101)]:
    A=plus([[F(1,2)]*3 for _ in range(3)],scale(r,K)); T=scale(F(1,3),A); M=mm(T,T); Q=mm(M,tr(M)); W=ident(3)
    for ell in range(1,13):
      W=mm(W,Q); E=trace(W)-F(1,16)**ell
      assert E==2*(r*r/3)**(2*ell)
      sharp.append({'r':str(r),'ell':ell,'excess':str(E)})
result={'job_id':JOB,'seed':SEED,'scope':'Finite exact identities, exhaustive specified weighted grids and independent vertex-map normalization. Not universal certification or review.','identity_tests':len(identity_cases),'identity_dimensions':[1,9],'identity_degeneracies':['b=0 in rational rotated basis','D=0 in rational rotated basis','arbitrary real-skew rational entries at five scales'],'identity_cases':identity_cases,'weighted_grid_tests':density_counts,'direct_density_tests':direct_cases,'sharpness_tests':sharp,'failures':[],'elapsed_seconds':round(time.monotonic()-start,3),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()}
(ROOT/'evidence/research-exact-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['identity_tests','weighted_grid_tests','direct_density_tests','failures','elapsed_seconds']}))
