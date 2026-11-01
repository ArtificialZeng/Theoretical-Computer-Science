"""Independent bounded exact diagnostics. No finite run certifies all dimensions."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import random,json,hashlib,datetime
P=Path(__file__).parent
JOB='c009-cycle2-triage-408b44cde59f'
def mt(M): return list(map(list,zip(*M)))
def mul(M,N): return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*N)] for row in M]
def vec(M,v): return [sum((x*y for x,y in zip(row,v)),F(0)) for row in M]
def sq(v): return sum((x*x for x in v),F(0))
def trace(M): return sum(M[i][i] for i in range(len(M)))
def check(B):
 n=len(B); a=sum(B[i][0]**2 for i in range(n)); b=[B[i][0] for i in range(n)]
 D=[[B[i][j] if i and j else F(0) for j in range(n)] for i in range(n)]
 T=[row[:] for row in B]; T[0][0]+=F(1,2)
 M=mul(T,T); x=[F(i==0)+2*b[i] for i in range(n)]
 z=vec(mt(M),x); Db=vec(D,b); D2b=vec(D,Db)
 expected=[F(i==0,4)-(F(1,2)+2*a)*b[i]+Db[i]+2*D2b[i] for i in range(n)]
 assert z==expected
 residual=sq(z)-sq(x)/16
 assert residual==2*a*a+4*a**3+(3+8*a)*sq(Db)+4*sq(D2b)
 Q=mul(M,mt(M)); R=[[D[i][j] for j in range(n)] for i in range(n)]
 DD=mul(D,D)
 R=[[DD[i][j]-b[i]*b[j] for j in range(n)] for i in range(n)]
 R2=mul(R,R); y=[b[i]/2+Db[i] for i in range(n)]
 for i in range(1,n):
  for j in range(1,n): assert Q[i][j]==y[i]*y[j]+R2[i][j]
 return residual
rng=random.Random(40844); counts={}; failures=[]
for n in range(1,8):
 for trial in range(36):
  B=[[F(0) for _ in range(n)] for _ in range(n)]
  for i in range(n):
   for j in range(i+1,n):
    value=F(rng.randrange(-15,16),rng.randrange(1,8))
    if trial%6==0 and i==0: value=F(0)
    if trial%6==1 and i>0: value=F(0)
    B[i][j]=value;B[j][i]=-value
  try: check(B)
  except AssertionError: failures.append({'dimension':n,'trial':trial});raise
 counts[str(n)]=36
rows=[]
for n,ell in [(1,1),(2,1),(2,2),(2,3),(3,1),(3,2)]:
 for trial in range(3):
  A=[[F(1,2) for j in range(n)] for i in range(n)]
  for i in range(n):
   for j in range(i+1,n): A[i][j]=F(rng.randrange(9),8);A[j][i]=1-A[i][j]
  M=mul(A,A); Q=mul(M,mt(M)); Qpower=Q
  for k in range(1,ell): Qpower=mul(Qpower,Q)
  density=trace(Qpower)/n**(4*ell)
  total=F(0)
  for f in product(range(n),repeat=4*ell):
   value=F(1)
   for k in range(4*ell):
    i,j=f[k],f[(k+1)%(4*ell)]
    value*=A[i][j] if k%4 in (0,1) else A[j][i]
   total+=value
  assert total/n**(4*ell)==density
  assert density>=F(1,16)**ell
  rows.append({'n':n,'ell':ell,'trial':trial,'vertex_maps':n**(4*ell),'density':str(density)})
result={'job_id':JOB,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact finite tests of Rayleigh identity, compression identity, and cycle trace normalization; no all-parameter certification or novelty conclusion','seed':40844,'block_tests_by_dimension':counts,'block_tests':sum(counts.values()),'density_tests':rows,'failures':failures,'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest()}
(P/'triage-exact-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'block_tests':sum(counts.values()),'density_tests':len(rows),'failures':failures}))
