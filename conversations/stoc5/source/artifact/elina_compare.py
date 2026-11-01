#!/usr/bin/env python3
"""Compare ELINA's unmodified scalar rational closure kernel with exact reference.
Build elina_scalar.dylib with the command recorded in README.md first.
This is a kernel check, not whole-program SV-COMP validation.
"""
import ctypes as C,json,pathlib,random,subprocess,time,hashlib,platform,gzip,argparse,datetime,sys
from validate import coherent,canon,matrix,digest,encode
BASE=pathlib.Path(__file__).resolve().parent
class Oct(C.Structure):
 _fields_=[('mat',C.POINTER(C.c_double)),('acl',C.c_void_p),('nni',C.c_int),('is_top',C.c_byte),('is_dense',C.c_byte),('ti',C.c_byte)]
parser=argparse.ArgumentParser();parser.add_argument('--verify-fixtures',type=pathlib.Path);args=parser.parse_args()
suffix='.dylib' if platform.system()=='Darwin' else '.so'
lib=C.CDLL(str(BASE/('elina_scalar'+suffix)))
fn=lib.strong_closure_dense_scalar
fn.argtypes=[C.POINTER(Oct),C.POINTER(C.c_double),C.POINTER(C.c_double),C.c_int,C.c_byte];fn.restype=C.c_byte
rng=random.Random(20271032)
def pos(i,j):
 if j>i:i,j=j^1,i^1
 return j+(i+1)*(i+1)//2
start=time.perf_counter();entries=0;records=[]
for case in range(1000):
 n=2*rng.randrange(1,17)
 # Known antisymmetric integer potential, allowing negative finite weights.
 z=[y for _ in range(n//2) for v in [rng.randrange(-40,41)] for y in (v,-v)]
 edges=coherent([(u,v,z[v]-z[u]+rng.randrange(0,9)) for u in range(n) for v in range(n) if u!=v and rng.random()<.2])
 d=matrix(n,edges);a=(C.c_double*(n*(n+2)//2))()
 for i in range(n):
  for j in range(n):a[pos(i,j)]=d[i][j]
 oo=Oct(a,None,len(a),0,1,0);t1=(C.c_double*n)();t2=(C.c_double*n)()
 negative=fn(C.byref(oo),t1,t2,n//2,0)
 assert not negative
 expected=canon(n,edges,False)
 for i in range(n):
  for j in range(n):assert a[pos(i,j)]==expected[i][j],(case,i,j,a[pos(i,j)],expected[i][j])
 entries+=n*n
 records.append(encode({'case':case,'n':n//2,'N':n,'m':len(edges),'edges':edges,'potential':z,'rational_feasible':True,'status':'pass','entries':n*n,'output':expected,'kernel_output':[[a[pos(i,j)] for j in range(n)] for i in range(n)],'output_sha256':digest(expected)}))
payload=''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in records).encode()
if args.verify_fixtures:
 assert gzip.decompress(args.verify_fixtures.read_bytes())==payload,'ELINA fixture replay differs'
 print('Archived ELINA input/output-digest fixture replay: identical')
(BASE/'elina_cases.jsonl.gz').write_bytes(gzip.compress(payload,mtime=0))
revision=(BASE/'vendor/ELINA/REVISION').read_text().strip() if not (BASE/'vendor/ELINA/.git').exists() else subprocess.check_output(['git','-C',str(BASE/'vendor/ELINA'),'rev-parse','HEAD'],text=True).strip()
result={'cases':1000,'entries_compared':entries,'failures':0,'seed':20271032,'seconds':time.perf_counter()-start,'elina_revision':revision,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':sys.argv,'fixture_sha256':hashlib.sha256(payload).hexdigest(),'n_distribution':{str(n):sum(r['n']==n for r in records) for n in range(1,17)},'m_min':min(r['m'] for r in records),'m_max':max(r['m'] for r in records),'kernel':'elina_oct/opt_oct_closure_dense_scalar.c','platform':platform.platform(),'compiler':subprocess.check_output([__import__('os').environ.get('CC','clang' if platform.system()=='Darwin' else 'cc'),'--version'],text=True).splitlines()[0],'kernel_sha256':hashlib.sha256((BASE/'vendor/ELINA/elina_oct/opt_oct_closure_dense_scalar.c').read_bytes()).hexdigest(),'semantics':'rational strong closure, feasible generated inputs','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
(BASE/'elina_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
