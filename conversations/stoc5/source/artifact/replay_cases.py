#!/usr/bin/env python3
"""Replay archived inputs and outputs directly, without invoking any RNG."""
import pathlib,json,gzip,itertools,ctypes as C,platform,hashlib
from validate import floyd,canon,decide_model,coherent,sparse_eliminate,digest,encode,potential,scc
b=pathlib.Path(__file__).resolve().parent
refs=[json.loads(s) for s in gzip.decompress((b/'reference_cases.jsonl.gz').read_bytes()).splitlines()]
for r in refs:
 name=r['suite'];N=r['N']
 if name.startswith('incremental'):
  edges=[tuple(e) for e in r['initial_edges']];p=r['r'];outputs=[]
  for k in range(p):
   edges+=coherent([(2*(p+k),2*(2*p+k),0)])
   d=canon(N,edges,True);outputs.append(digest(d))
   assert all(d[2*i][2*(3*p+j)]==min(r['A'][i][z]+r['B'][z][j] for z in range(k+1)) for i in range(p) for j in range(p))
  assert outputs==r['prefix_output_sha256']
 elif name.startswith('elimination'):
  d,k=sparse_eliminate(N,r['edges'],r['order']);assert d==floyd(N,r['edges']) and k==r['induced_width']
 elif name.startswith('direct'):
  d=floyd(N,r['edges']);edges=coherent([(2*u,2*v,w) for u,v,w in r['edges']])
  for integer in (False,True):
   c=canon(2*N,edges,integer);assert (d is None)==(c is None)
   if c is not None:assert [[c[2*u][2*v] for v in range(N)] for u in range(N)]==d
 else:
  edges=[tuple(e) for e in r['edges']];d=canon(N,edges,True)
  if name.startswith('parity'):
   assert (d is None)==(decide_model(N,edges) is None)
   h=potential(N,edges)
   if h is not None:
    c=scc(N,[(u,v) for u,v,w in edges if h[v]-h[u]==w])
    assert (d is not None)==(not any(c[u]==c[u^1] and (h[u]-h[u^1])%2 for u in range(N)))
  elif name.startswith('integer'):
   pts=[]
   for x in itertools.product(range(-3,4),repeat=r['n']):
    z=[y for v in x for y in (v,-v)]
    if all(z[v]-z[u]<=w for u,v,w in edges):pts.append(z)
   expected=[[max(z[v]-z[u] for z in pts) for v in range(N)] for u in range(N)] if pts else None
   assert d==expected
  elif name.startswith('static'):
   p=r['r']
   for integer in (False,True):
    d=canon(N,edges,integer)
    assert all(d[2*i][2*(2*p+j)]==min(r['A'][i][k]+r['B'][k][j] for k in range(p)) for i in range(p) for j in range(p))
 assert encode(d)==r['output'] and digest(d)==r['output_sha256'],(name,r['case'])
print('Reference archive replay:',len(refs),'cases; all exact outputs and assertions match')
class Oct(C.Structure):
 _fields_=[('mat',C.POINTER(C.c_double)),('acl',C.c_void_p),('nni',C.c_int),('is_top',C.c_byte),('is_dense',C.c_byte),('ti',C.c_byte)]
suffix='.dylib' if platform.system()=='Darwin' else '.so'
lib=C.CDLL(str(b/('elina_scalar'+suffix)));fn=lib.strong_closure_dense_scalar
fn.argtypes=[C.POINTER(Oct),C.POINTER(C.c_double),C.POINTER(C.c_double),C.c_int,C.c_byte];fn.restype=C.c_byte
from validate import matrix
def pos(i,j):
 if j>i:i,j=j^1,i^1
 return j+(i+1)*(i+1)//2
rows=[json.loads(s) for s in gzip.decompress((b/'elina_cases.jsonl.gz').read_bytes()).splitlines()];entries=0
for r in rows:
 N=r['N'];a=(C.c_double*(N*(N+2)//2))();d=matrix(N,r['edges'])
 for i in range(N):
  for j in range(N):a[pos(i,j)]=d[i][j]
 oo=Oct(a,None,len(a),0,1,0);t1=(C.c_double*N)();t2=(C.c_double*N)()
 assert not fn(C.byref(oo),t1,t2,N//2,0)
 expected=canon(N,r['edges'],False);actual=[[a[pos(i,j)] for j in range(N)] for i in range(N)]
 assert encode(expected)==r['output'] and encode(actual)==r['kernel_output'] and actual==expected
 assert digest(expected)==r['output_sha256'];entries+=N*N
print('ELINA archive replay:',len(rows),'cases;',entries,'entries; all exact outputs match')
(b/'replay_results.json').write_text(json.dumps({'reference_cases':len(refs),'elina_cases':len(rows),'elina_entries':entries,'failures':0,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()},indent=2)+'\n')
