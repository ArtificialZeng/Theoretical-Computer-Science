# Independent necessity check for the c021 invertible-sector criterion (written separately from the c021 agent).
# Random CCRAs with multi-state control, products, resets, singular updates -> minimal rep via Hankel ->
# if all letter matrices invertible: test (1) M_u^N has rational spectrum, (2) group commutators of
# such powers are unipotent, (3) unipotent Jordan parts of powers commute pairwise.
import random, itertools, sys
from fractions import Fraction as F
import sympy as sp
R=random.Random(int(sys.argv[1]) if len(sys.argv)>1 else 0)
COEF=[F(1),F(-1),F(2),F(-2),F(1,2),F(3),F(-1,3)]
def rand_expr(vars_):
    if not vars_:
        c=R.choice([F(0),F(0),F(1),F(-1),F(2),F(3)]); return ('c',c)
    e=('v',vars_[0],R.choice(COEF))
    for v in vars_[1:]:
        e=('add' if R.random()<0.55 else 'mul', e, ('v',v,R.choice(COEF)))
    if R.random()<0.6: e=('add',e,('c',R.choice(COEF)))
    return e
def ev(e,x):
    t=e[0]
    if t=='c': return e[1]
    if t=='v': return e[2]*x[e[1]]
    a,b=ev(e[1],x),ev(e[2],x)
    return a+b if t=='add' else a*b
MODE={'inv':0.6}
def rand_update(r):
    if R.random()<MODE['inv']:
        perm=list(range(r)); R.shuffle(perm)
        groups=[[perm[i]] for i in range(r)]
        if r>=2 and R.random()<0.25:   # occasional product/merge plus a fresh constant register
            i,j=R.sample(range(r),2); groups[i]=groups[i]+groups[j]; groups[j]=[]
    else:
        used=[i for i in range(r) if R.random()<0.85]; R.shuffle(used)
        groups=[[] for _ in range(r)]
        for v in used: groups[R.randrange(r)].append(v)
    return [rand_expr(g) for g in groups]
def rand_ccra(r,c):
    trans={(q,a):(R.randrange(c),rand_update(r)) for q in range(c) for a in '01'}
    outs=[rand_expr([i for i in range(r) if R.random()<0.7]) for _ in range(c)]
    x0=[F(R.randint(-2,3)) for _ in range(r)]
    return trans,outs,x0
def run(A,w):
    trans,outs,x=A; q=0
    for a in w:
        q2,up=trans[(q,a)]; x=[ev(e,x) for e in up]; q=q2
    return ev(outs[q],x)
def words(n): 
    for L in range(n+1):
        for t in itertools.product('01',repeat=L): yield ''.join(t)
def minimal_rep(f, depth=4):
    P=list(words(depth)); S=list(words(depth))
    H=sp.Matrix([[f(p+s) for s in S] for p in P])
    rows=[]; cur=sp.zeros(0,len(S))
    for i in range(len(P)):
        t=cur.col_join(H[i,:])
        if t.rank()>cur.rows: cur=t; rows.append(i)
    d=len(rows)
    if d==0: return None
    cols=[]; cc=sp.zeros(d,0); Hr=H.extract(rows,list(range(len(S))))
    for j in range(len(S)):
        t=cc.row_join(Hr[:,j])
        if t.rank()>cc.cols: cc=t; cols.append(j)
    B=H.extract(rows,cols); Binv=B.inv()
    Pw=[P[i] for i in rows]; Sw=[S[j] for j in cols]
    lam=sp.Matrix([[f(s) for s in Sw]])*Binv
    M={a:sp.Matrix([[f(p+a+s) for s in Sw] for p in Pw])*Binv for a in '01'}
    gam=sp.Matrix([f(p) for p in Pw])
    return lam,M,gam,d
def Mw(M,w,d):
    X=sp.eye(d)
    for a in w: X=X*M[a]
    return X
def unip_part(A):
    P,J=A.jordan_form()
    D=sp.diag(*[J[i,i] for i in range(J.rows)])
    S=P*D*P.inv(); return sp.simplify(S.inv()*A)
def is_unipotent(A):
    x=sp.symbols('x'); return sp.expand(A.charpoly(x).as_expr()-(x-1)**A.rows)==0
def rational_spectrum(A):
    x=sp.symbols('x'); _,fac=sp.factor_list(A.charpoly(x).as_expr())
    return all(sp.degree(p,x)==1 for p,_ in fac)
def test_rep(M,d,N,nw=4,maxlen=3):
    ws=list({''.join(R.choice('01') for _ in range(R.randint(1,maxlen))) for _ in range(nw)})
    pw={w:Mw(M,w,d)**N for w in ws}
    for w,A in pw.items():
        if not rational_spectrum(A): return ('irrational-spectrum',w)
    for u,v in itertools.combinations(ws,2):
        C=pw[u]*pw[v]*pw[u].inv()*pw[v].inv()
        if not is_unipotent(C): return ('nonunipotent-commutator',u,v)
    U={w:unip_part(A) for w,A in pw.items()}
    for u,v in itertools.combinations(ws,2):
        if U[u]*U[v]!=U[v]*U[u]: return ('unipotent-parts-noncommuting',u,v)
    return 'pass'
if __name__=='__main__':
    trials=int(sys.argv[2]) if len(sys.argv)>2 else 40
    stats={}
    for t in range(trials):
        r=R.choice([1,2,2,3]); c=R.choice([1,2,2,3])
        A=rand_ccra(r,c); f=lambda w,A=A: run(A,w)
        rep=minimal_rep(f)
        if rep is None: stats['zero']=stats.get('zero',0)+1; continue
        lam,M,gam,d=rep
        if any((lam*Mw(M,w,d)*gam)[0]!=f(w) for w in words(7)): stats['hankel-too-short']=stats.get('hankel-too-short',0)+1; continue
        if any(M[a].det()==0 for a in '01') or d<2: stats['singular-or-trivial']=stats.get('singular-or-trivial',0)+1; continue
        res=test_rep(M,d,N=12)
        key='CCRA:'+(res if isinstance(res,str) else res[0])
        stats[key]=stats.get(key,0)+1
        if res!='pass': print('COUNTEREXAMPLE?',r,c,d,res,A,flush=True)
    # control: random invertible integer matrices (not from CCRA)
    for t in range(15):
        d=R.choice([2,3])
        M={a:sp.Matrix(d,d,lambda i,j:R.randint(-2,2)) for a in '01'}
        if any(M[a].det()==0 for a in '01'): continue
        res=test_rep(M,d,N=12)
        key='control:'+(res if isinstance(res,str) else res[0]); stats[key]=stats.get(key,0)+1
    print(stats)
