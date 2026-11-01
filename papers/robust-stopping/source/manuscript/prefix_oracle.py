"""Exact structured ski-rental optimizer. Python standard library only.

Research implementation, not an accepted mathematical result. See
research-argument.md for the proposed correctness and bit-complexity proof.
No generic LP solver is used here. All outputs use fractions.Fraction.
"""
from fractions import Fraction as Q
from math import factorial, lcm


def prefix_vertex(b, r, active):
    """Unnormalized zero/upper schedule of the triangular prefix polytope."""
    a = b - 1
    f, mass, previous = [Q(0)] * a, Q(0), 0
    for i in range(1,b):
        if i not in active: continue
        f[i-1] = Q(i-previous, a)*(r+mass)
        mass += f[i-1]
        previous = i
    return f


def dual_state(b, costs, alpha, active):
    """Dual y and right derivative h; sums make one pass linear in b."""
    a = b-1
    y, h, slack, speed = {}, {}, {}, {}
    Y = X = H = W = Q(0)
    for i in range(a, 0, -1):
        slack[i] = costs[i]-alpha+(a+i)*Y-X
        speed[i] = 1-(a+i)*H+W
        if i in active:
            y[i] = -slack[i]/a
            h[i] = speed[i]/a
            assert y[i] >= 0 and h[i] > 0
            Y += y[i]
            X += i*y[i]
            H += h[i]
            W += i*h[i]
        else:
            y[i] = h[i] = Q(0)
            assert slack[i] >= 0 and speed[i] > 0
    return y, h, slack, speed


def linear_oracle(b, R, costs):
    """Minimize costs*f under prefixes and normalization, without moment.

    Returns a normalized policy, alpha, prefix dual multipliers, and the
    number of activation events. costs contains every day 1,...,b and
    optionally later tail days; all tail constraints have zero prefix entries.
    """
    r, a = R-1, b-1
    tail = min((t for t in costs if t >= b), key=lambda t: (costs[t], t))
    cap = costs[tail]
    active = set()
    alpha = min(cap, min(costs[i] for i in range(1,b)))
    previous_f = [Q(0)] * a
    events = 0
    while True:
        y, h, slack, speed = dual_state(b, costs, alpha, active)
        additions = {i for i in range(1,b) if i not in active and not slack[i]}
        if additions:
            previous_f = prefix_vertex(b,r,active)
            active |= additions
            events += 1
            y, h, slack, speed = dual_state(b, costs, alpha, active)
        f = prefix_vertex(b,r,active)
        mass = sum(f)
        if mass >= 1:
            oldmass = sum(previous_f)
            assert oldmass < 1
            theta = (1-oldmass)/(mass-oldmass)
            f = [(1-theta)*u+theta*v for u,v in zip(previous_f,f)]
            policy = {i:v for i,v in enumerate(f,1) if v}
            break
        if alpha == cap:
            policy = {i:v for i,v in enumerate(f,1) if v}
            policy[tail] = 1-mass
            break
        next_alpha = min([cap] + [alpha+slack[i]/speed[i]
                                 for i in range(1,b) if i not in active])
        assert next_alpha > alpha
        alpha = next_alpha
    assert events <= a
    dual = alpha-sum(r*i*y[i] for i in range(1,b))
    obj = sum(costs[t]*v for t,v in policy.items())
    assert obj == dual
    return policy, alpha, y, events


def forecast_costs(b, p, days):
    return {t:sum(prob*(b+t-1 if t<=x else x) for x,prob in p.items())
            for t in days}


def support_days(b,p):
    return sorted(set(range(1,b+1)) | {d+1 for d,v in p.items() if v and d>=b})


def moment(f):
    return sum((t-1)*v for t,v in f.items())


def objective(g,f):
    return sum(g[t]*v for t,v in f.items())


def combine(f,h,theta):
    return {t:v for t in f.keys() | h.keys()
            if (v := theta*f.get(t,Q(0))+(1-theta)*h.get(t,Q(0)))}


def optimize(b,R,p, max_chord_probes=8):
    """Exact one-price bisection, with determinant-based rational isolation."""
    assert b>=2 and R>=Q(b**b,b**b-(b-1)**b)
    assert p and min(p)>=1 and sum(p.values())==1 and min(p.values())>=0
    days = support_days(b,p)
    g = forecast_costs(b,p,days)
    K = (R-1)*b
    calls = 0
    def oracle(lam):
        nonlocal calls
        calls += 1
        c = {t:v+lam*(t-1) for t,v in g.items()}
        return linear_oracle(b,R,c)
    left, alpha, y, events = oracle(Q(0))
    if moment(left) <= K:
        return dict(policy=left, lam=Q(0), alpha=alpha, y=y, calls=calls,
                    lambda_bound=Q(0), isolation_steps=0)
    D = factorial(b)*b**b
    qp = lcm(*(v.denominator for v in p.values()))
    H = qp*R.denominator*D
    L = max(days)+b
    Z = 2*L*H**4
    lo, hi = Q(0), Q(Z+1)
    right, _, _, _ = oracle(hi)
    assert moment(right)<=K, 'R may be below the classical robust ratio'
    # At most eight exact chord probes accelerate common instances. Each
    # either proves equality with an explicit dual, or preserves the bracket.
    assert 0<=max_chord_probes<=8
    for warmup in range(max_chord_probes):
        lam = (objective(g,right)-objective(g,left))/(moment(left)-moment(right))
        assert lo<=lam<=hi
        probe, alpha, y, _ = oracle(lam)
        endpoint = objective(g,left)+lam*moment(left)
        probed = objective(g,probe)+lam*moment(probe)
        assert probed<=endpoint
        if probed==endpoint or moment(probe)==K:
            if moment(probe)==K:
                f=probe
            else:
                theta=(K-moment(right))/(moment(left)-moment(right))
                f=combine(left,right,theta)
            val=objective(g,f)
            dual=alpha-sum((R-1)*i*y[i] for i in range(1,b))-lam*K
            assert val==dual
            return dict(policy=f,lam=lam,alpha=alpha,y=y,calls=calls,
                        lambda_bound=Z,isolation_steps=0,chord_probes=warmup+1)
        if moment(probe)>K:
            lo,left=lam,probe
        else:
            hi,right=lam,probe
    steps = 0
    while hi-lo >= Q(1,Z*Z):
        mid = (lo+hi)/2
        f, _, _, _ = oracle(mid)
        if moment(f)>K:
            lo,left = mid,f
        else:
            hi,right = mid,f
        steps += 1
    lam = (objective(g,right)-objective(g,left))/(moment(left)-moment(right))
    assert lo<=lam<=hi
    _, alpha, y, _ = oracle(lam)
    theta = (K-moment(right))/(moment(left)-moment(right))
    f = combine(left,right,theta)
    val = objective(g,f)
    dual = alpha-sum((R-1)*i*y[i] for i in range(1,b))-lam*K
    assert val==dual
    return dict(policy=f,lam=lam,alpha=alpha,y=y,calls=calls,
                lambda_bound=Z,isolation_steps=steps)


def verify(b,R,p,result):
    """Direct full-support dual/primal checks; no reliance on optimizer path."""
    f,lam,alpha,y = (result[k] for k in ('policy','lam','alpha','y'))
    days = support_days(b,p)
    g = forecast_costs(b,p,days)
    r = R-1
    assert set(f)<=set(days) and min(f.values())>=0 and sum(f.values())==1
    for x in range(1,b):
        prefix = sum((b+t-1-x)*v for t,v in f.items() if t<=x)
        assert prefix<=r*x
    assert moment(f)<=r*b and lam>=0 and min(y.values())>=0
    for t in days:
        lhs = g[t]+lam*(t-1)+sum((b+t-1-x)*y[x]
                                                for x in range(t,b))
        assert lhs>=alpha
    # Tail dominance from research-argument.md extends the last dual check
    # to every omitted integer buy-day. Prefixes + moment extend feasibility
    # to every actual horizon. This script checks the reduced inequalities.
    primal = objective(g,f)
    dual = alpha-sum(r*x*y[x] for x in range(1,b))-lam*r*b
    assert primal==dual
    return primal
