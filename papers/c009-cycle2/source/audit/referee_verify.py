"""Fresh exact diagnostics; standard library only; no proposer code imported.
Finite diagnostics supplement the analytic review and are not a universal proof.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json, random
HERE=Path(__file__).resolve().parent
JOB='c009-cycle2-referee-eb6d40fb0393'
rng=random.Random(90400393)
def transpose(M): return list(map(list,zip(*M)))
def multiply(M,N):
 return [[sum((M[i][k]*N[k][j] for k in range(len(N))),F(0)) for j in range(len(N[0]))] for i in range(len(M))]
def vector(M,v): return [sum((c*x for c,x in zip(row,v)),F(0)) for row in M]
def dot(v,w): return sum((x*y for x,y in zip(v,w)),F(0))
def power(M,k):
 R=[[F(i==j) for j in range(len(M))] for i in range(len(M))]
 for _ in range(k): R=multiply(R,M)
 return R
def trace(M): return sum((M[i][i] for i in range(len(M))),F(0))
exact_blocks=0
compression_checks=0
for n in range(1,9):
 for trial in range(12):
  B=[[F(0) for _ in range(n)] for _ in range(n)]
  for i in range(n):
   for j in range(i):
    v=F(rng.randrange(-20,21),rng.randrange(1,9))
    B[i][j],B[j][i]=v,-v
  if trial==0:
   for i in range(1,n): B[0][i]=B[i][0]=F(0)
  if trial==1:
   for i in range(1,n):
    for j in range(1,n): B[i][j]=F(0)
  T=[row[:] for row in B]; T[0][0]=F(1,2)
  b=[B[i][0] for i in range(n)]; a=dot(b,b)
  D=[row[:] for row in B]
  for i in range(n): D[0][i]=D[i][0]=F(0)
  x=[F(i==0)+2*b[i] for i in range(n)]
  M=multiply(T,T); z=vector(transpose(M),x)
  db=vector(D,b); ddb=vector(D,db)
  expected_z=[F(i==0)/4-(F(1,2)+2*a)*b[i]+db[i]+2*ddb[i] for i in range(n)]
  assert z==expected_z
  residual=dot(z,z)-dot(x,x)/16
  expected=2*a*a+4*a*a*a+(3+8*a)*dot(db,db)+4*dot(ddb,ddb)
  assert residual==expected and residual>=0
  Q=multiply(M,transpose(M)); DD=multiply(D,D)
  R=[[DD[i][j]-b[i]*b[j] for j in range(n)] for i in range(n)]
  RR=multiply(R,R); y=[b[i]/2+db[i] for i in range(n)]
  assert all(Q[i][j]==y[i]*y[j]+RR[i][j] for i in range(1,n) for j in range(1,n))
  exact_blocks+=1; compression_checks+=1
map_checks=[]; forcing_checks=0
for n,ell in [(1,1),(1,3),(2,2),(3,1),(3,2)]:
 for trial in range(3):
  A=[[F(1,2) for _ in range(n)] for _ in range(n)]
  for i in range(n):
   for j in range(i):
    A[i][j]=F(rng.randrange(9),8); A[j][i]=1-A[i][j]
  count=F(0)
  for f in product(range(n),repeat=4*ell):
   weight=F(1)
   for k in range(4*ell):
    v,w=f[k],f[(k+1)%(4*ell)]
    weight*=A[v][w] if k%4 in (0,1) else A[w][v]
   count+=weight
  density=count/n**(4*ell)
  M=multiply(A,A)
  trace_density=trace(power(multiply(M,transpose(M)),ell))/n**(4*ell)
  assert density==trace_density and density>=F(1,16)**ell
  beta2=sum((((A[i][j]-F(1,2))/n)**2 for i in range(n) for j in range(i)),F(0))
  assert density-F(1,16)**ell>=F(1,16)**ell*beta2**(2*ell)
  forcing_checks+=1
  map_checks.append({'n':n,'ell':ell,'trial':trial,'maps':n**(4*ell),'density':str(density)})
sharpness_checks=0
K=[[0,1,-1],[-1,0,1],[1,-1,0]]
for r in [F(1,3),F(1,17),F(1,97)]:
 T=[[(F(1,2)+r*K[i][j])/3 for j in range(3)] for i in range(3)]
 M=multiply(T,T); Q=multiply(M,transpose(M))
 for ell in [1,2,3,7,13]:
  assert trace(power(Q,ell))-F(1,16)**ell==2*(r*r/3)**(2*ell)
  sharpness_checks+=1
report={'job_id':JOB,'scope':'Finite exact diagnostics supplementing the analytic referee derivation; no proof by bounded search.','independent_implementation':True,'seed':90400393,'rational_residual_checks':exact_blocks,'rational_compression_checks':compression_checks,'dimensions':[1,8],'direct_map_checks':map_checks,'exact_forcing_checks_dimensions_at_most_3':forcing_checks,'sharpness_checks':sharpness_checks,'source_sha256':hashlib.sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),'operational_failures':['First verifier required unavailable sympy and exited at import before any checks; preserved as referee_verify_sympy_unavailable.py. Replaced by standard-library implementation.','First replacement apply_patch was rejected for multiple operations on one path; no mathematical check ran in that failed call.'],'mathematical_failures':[]}
(HERE/'referee-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='direct_map_checks'}))
