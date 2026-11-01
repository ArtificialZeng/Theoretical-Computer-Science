#!/usr/bin/env python3
"""Exact, dependency-free validation of OctaFine's reductions and rounding.
This is a reference checker; its potential oracle is Bellman--Ford, not BNW.
"""
import itertools, json, math, random, time, pathlib, hashlib, platform, gzip, argparse, collections, datetime, sys
INF=math.inf
R=random.Random(20271031)

def matrix(n,edges):
 d=[[0 if i==j else INF for j in range(n)] for i in range(n)]
 for u,v,w in edges:d[u][v]=min(d[u][v],w)
 return d

def floyd(n,edges):
 d=matrix(n,edges)
 for k in range(n):
  for i in range(n):
   if d[i][k]==INF:continue
   for j in range(n):
    if d[k][j]!=INF:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 return None if any(d[i][i]<0 for i in range(n)) else d

def canon(n,edges,integer=False):
 d=floyd(n,edges)
 if d is None:return None
 a=[(d[u][u^1]//2 if integer else d[u][u^1]/2) if d[u][u^1]!=INF else INF for u in range(n)]
 if integer and any(a[u]+a[u^1]<0 for u in range(n)):return None
 return [[min(d[u][v],a[u]+a[v^1]) for v in range(n)] for u in range(n)]

def coherent(edges):
 return list(set(edges+[(v^1,u^1,w) for u,v,w in edges]))

def potential(n,edges):
 h=[0]*n
 for _ in range(n):
  changed=False
  for u,v,w in edges:
   if h[v]>h[u]+w:h[v]=h[u]+w;changed=True
  if not changed:return h
 return None

def scc(n,edges):
 a=[[] for _ in range(n)];b=[[] for _ in range(n)]
 for u,v in edges:a[u].append(v);b[v].append(u)
 seen=set();order=[]
 def visit(v):
  seen.add(v)
  for u in a[v]:
   if u not in seen:visit(u)
  order.append(v)
 for v in range(n):
  if v not in seen:visit(v)
 comp=[-1]*n
 def back(v,c):
  comp[v]=c
  for u in b[v]:
   if comp[u]<0:back(u,c)
 c=0
 for v in reversed(order):
  if comp[v]<0:back(v,c);c+=1
 return comp # Topological component indices increase along arcs.

def decide_model(n,edges):
 h=potential(n,edges)
 if h is None:return None
 k=[h[v]-h[v^1] for v in range(n)] # twice the symmetrized potential
 tight=[(u,v) for u,v,w in edges if k[v]-k[u]==2*w and k[u]%2]
 c=scc(n,tight)
 if any(k[v]%2 and c[v]==c[v^1] for v in range(n)):return None
 z=[(k[v]+(1 if c[v]<c[v^1] else -1))//2 if k[v]%2 else k[v]//2 for v in range(n)]
 assert all(z[v^1]==-z[v] for v in range(n))
 assert all(z[v]-z[u]<=w for u,v,w in edges)
 return z

def sparse_eliminate(n,edges,ordering=None):
 ordering=list(range(n)) if ordering is None else ordering
 rank={v:i for i,v in enumerate(ordering)}
 adj=[set() for _ in range(n)];weights={}
 for u,v,w in edges:
  if u==v:continue
  adj[u].add(v);adj[v].add(u);weights[u,v]=min(weights.get((u,v),INF),w)
 records=[];width=0
 for v in ordering:
  nb=list(adj[v]);width=max(width,len(nb))
  records += [(v,u,weights.get((v,u),INF)) for u in nb]
  records += [(u,v,weights.get((u,v),INF)) for u in nb]
  for u in nb:
   for z in nb:
    if u==z:continue
    weights[u,z]=min(weights.get((u,z),INF),weights.get((u,v),INF)+weights.get((v,z),INF))
    adj[u].add(z)
  for u in nb:adj[u].discard(v)
  adj[v].clear()
 up=[[] for _ in range(n)];down=[[] for _ in range(n)]
 for u,v,w in records:
  if w==INF:continue
  (up if rank[u]<rank[v] else down)[u].append((v,w))
 out=[]
 for s in range(n):
  d=[INF]*n;d[s]=0
  for u in ordering:
   for v,w in up[u]:d[v]=min(d[v],d[u]+w)
  for u in reversed(ordering):
   for v,w in down[u]:d[v]=min(d[v],d[u]+w)
  out.append(d)
 return out,width

def encode(obj):
 if isinstance(obj,float) and math.isinf(obj):return "inf" if obj>0 else "-inf"
 if isinstance(obj,(list,tuple)):return [encode(x) for x in obj]
 if isinstance(obj,dict):return {k:encode(v) for k,v in obj.items()}
 return obj

def digest(obj):
 return hashlib.sha256(json.dumps(encode(obj),sort_keys=True,separators=(",",":")).encode()).hexdigest()

def run():
 parser=argparse.ArgumentParser()
 parser.add_argument('--verify-fixtures',type=pathlib.Path)
 args=parser.parse_args()
 R.seed(20271031)
 rows=[];records=[]
 def suite(name,count,fn):
  t=time.perf_counter()
  first=len(records)
  for case in range(count):
   record=fn();record.update({'suite':name,'case':case,'status':'pass'})
   records.append(encode(record))
  batch=records[first:]
  stats={k:{'min':min(x[k] for x in batch),'max':max(x[k] for x in batch)} for k in ['n','N','m']}
  stats['rational_feasible']=sum(x['rational_feasible'] for x in batch)
  stats['integer_feasible']=sum(x['integer_feasible'] for x in batch) if 'integer_feasible' in batch[0] else None
  stats['input_digest']=digest(batch)
  rows.append({'suite':name,'cases':count,'failures':0,'seconds':time.perf_counter()-t,'parameters':stats})
 def parity():
  n=R.randrange(1,7)*2
  e=coherent([(R.randrange(n),R.randrange(n),R.randrange(-7,9)) for _ in range(R.randrange(0,n*n+1))])
  assert (decide_model(n,e) is None)==(canon(n,e,True) is None)
  # Also verify Lahiri--Musuvathi's original, unsymmetrized SCC test.
  h=potential(n,e)
  if h is not None:
   c=scc(n,[(u,v) for u,v,w in e if h[v]-h[u]==w])
   lm=not any(c[u]==c[u^1] and (h[u]-h[u^1])%2 for u in range(n))
   assert lm==(decide_model(n,e) is not None)
  d=canon(n,e,True)
  return {'n':n//2,'N':n,'m':len(e),'edges':e,'rational_feasible':h is not None,'integer_feasible':d is not None,'output':d,'output_sha256':digest(d)}
 def brute():
  p=R.randrange(1,4);n=2*p
  e=coherent([(R.randrange(n),R.randrange(n),R.randrange(-5,6)) for _ in range(R.randrange(0,12))]+[(u,u^1,6) for u in range(n)])
  pts=[]
  for x in itertools.product(range(-3,4),repeat=p):
   z=[y for v in x for y in (v,-v)]
   if all(z[v]-z[u]<=w for u,v,w in e):pts.append(z)
  d=canon(n,e,True)
  assert (d is None)==(not pts)
  if pts:
   expected=[[max(z[v]-z[u] for z in pts) for v in range(n)] for u in range(n)]
   assert d==expected
  return {'n':p,'N':n,'m':len(e),'edges':e,'rational_feasible':floyd(n,e) is not None,'integer_feasible':bool(pts),'enumerated_points':7**p,'output':d,'output_sha256':digest(d)}
 def reduction():
  p=R.randrange(1,9);n=6*p
  a=[[R.randrange(-20,21) for _ in range(p)] for _ in range(p)]
  b=[[R.randrange(-20,21) for _ in range(p)] for _ in range(p)]
  e=coherent([(2*i,2*(p+k),a[i][k]) for i in range(p) for k in range(p)]+[(2*(p+k),2*(2*p+j),b[k][j]) for k in range(p) for j in range(p)])
  for integer in (False,True):
   d=canon(n,e,integer)
   assert all(d[2*i][2*(2*p+j)]==min(a[i][k]+b[k][j] for k in range(p)) for i in range(p) for j in range(p))
  return {'n':3*p,'N':n,'m':len(e),'r':p,'A':a,'B':b,'edges':e,'rational_feasible':True,'integer_feasible':True,'output':d,'output_sha256':digest(d)}
 def incremental():
  p=R.randrange(1,7);n=8*p
  a=[[R.randrange(-9,10) for _ in range(p)] for _ in range(p)]
  b=[[R.randrange(-9,10) for _ in range(p)] for _ in range(p)]
  e=coherent([(2*i,2*(p+k),a[i][k]) for i in range(p) for k in range(p)]+[(2*(2*p+k),2*(3*p+j),b[k][j]) for k in range(p) for j in range(p)])
  initial=[list(edge) for edge in e];prefix=[]
  for k in range(p):
   e+=coherent([(2*(p+k),2*(2*p+k),0)])
   d=canon(n,e,True)
   assert all(d[2*i][2*(3*p+j)]==min(a[i][z]+b[z][j] for z in range(k+1)) for i in range(p) for j in range(p))
   prefix.append(digest(d))
  return {'n':4*p,'N':n,'m':len(e),'initial_m':len(initial),'r':p,'A':a,'B':b,'initial_edges':initial,'rational_feasible':True,'integer_feasible':True,'prefix_output_sha256':prefix,'output':d,'output_sha256':digest(d)}
 def elimination():
  n=R.randrange(2,24);h=[R.randrange(-20,21) for _ in range(n)]
  e=[(u,v,R.randrange(0,10)+h[v]-h[u]) for u in range(n) for v in range(n) if u!=v and R.random()<.15]
  order=list(range(n));R.shuffle(order)
  d,k=sparse_eliminate(n,e,order)
  assert d==floyd(n,e)
  return {'n':n,'N':n,'m':len(e),'edges':e,'order':order,'induced_width':k,'rational_feasible':True,'integer_feasible':True,'output':d,'output_sha256':digest(d)}
 def embedding():
  p=R.randrange(1,10)
  e=[(u,v,R.randrange(-9,10)) for u in range(p) for v in range(p) if u!=v and R.random()<.3]
  d=floyd(p,e)
  doubled=coherent([(2*u,2*v,w) for u,v,w in e])
  for integer in (False,True):
   c=canon(2*p,doubled,integer)
   assert (c is None)==(d is None)
   if d is not None:assert [[c[2*u][2*v] for v in range(p)] for u in range(p)]==d
  return {'n':p,'N':p,'m':len(e),'edges':e,'rational_feasible':d is not None,'integer_feasible':d is not None,'output':d,'output_sha256':digest(d)}
 suite('parity, model and LM criterion',5000,parity)
 suite('integer canonical entries vs enumeration',600,brute)
 suite('static min-plus reduction, both closures',400,reduction)
 suite('incremental min-plus reduction, every prefix',250,incremental)
 suite('elimination and up-down reconstruction',500,elimination)
 suite('direct graph embedding, both closures',500,embedding)
 payload=''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in records).encode()
 if args.verify_fixtures:
  assert gzip.decompress(args.verify_fixtures.read_bytes())==payload,'fixture replay differs'
  print('Archived input/output-digest fixture replay: identical')
 base=pathlib.Path(__file__).resolve().parent
 (base/'reference_cases.jsonl.gz').write_bytes(gzip.compress(payload,mtime=0))
 result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':sys.argv,'fixture_sha256':hashlib.sha256(payload).hexdigest(),'seed':20271031,'python':platform.python_version(),'platform':platform.platform(),'rows':rows,'total_cases':sum(r['cases'] for r in rows),'failures':0,'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
 pathlib.Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
 pathlib.Path(__file__).with_name('validation_rows.tex').write_text('\n'.join(r['suite'].replace('&','\\&')+' & '+str(r['cases'])+' & 0 \\\\' for r in rows)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':run()
