"""Direct exact certificate checks, independent of the optimization code.

No optimizer is imported here. Tail interval dominance and the limiting
moment extend the finite checks to the two unbounded integer domains.
"""
from fractions import Fraction as F


def cost(b, t, x):
    return x if x < t else b + t - 1


def check_full(b, R, p, out):
    assert isinstance(b, int) and b >= 2
    assert R >= F(b**b, b**b - (b-1)**b)
    assert p and all(x >= 1 and v >= 0 for x, v in p.items())
    assert sum(p.values()) == 1
    f, lam, alpha, y = (out[k] for k in ('policy', 'lam', 'alpha', 'y'))
    assert f and all(isinstance(t, int) and t >= 1 and v >= 0 for t, v in f.items())
    assert sum(f.values()) == 1
    assert lam >= 0 and set(y) == set(range(1, b)) and min(y.values()) >= 0
    mu = sum(v*(t-1) for t, v in f.items())
    assert mu <= (R-1)*b
    for x in range(1, b):
        assert sum(v*cost(b, t, x) for t, v in f.items()) <= R*x
    # Prefix bounds plus b + mu <= Rb prove every actual horizon x >= b.
    for x in set(f) | {b, b+1, max(f)+1}:
        assert sum(v*cost(b, t, x) for t, v in f.items()) <= R*min(x, b)
    g = lambda t: sum(v*cost(b, t, x) for x, v in p.items())
    allowed = set(range(1, b+1)) | {x+1 for x, v in p.items() if v and x >= b}
    assert set(f) <= allowed
    assert sum(t >= b for t in f) <= 2
    # g(t)+lam(t-1) is nondecreasing within each forecast tail interval.
    for t in allowed | {x for x, v in p.items() if v and x >= b}:
        lhs = g(t) + lam*(t-1) + sum(
            (b+t-1-x)*v for x, v in y.items() if x >= t)
        assert lhs >= alpha
    primal = sum(v*g(t) for t, v in f.items())
    dual = alpha - (R-1)*sum(x*v for x, v in y.items()) - lam*(R-1)*b
    assert primal == dual
    assert lam*(mu-(R-1)*b) == 0
    return primal


def check_linear(b, R, c, f, alpha, y):
    assert f and set(f) <= set(c)
    assert sum(f.values()) == 1 and min(f.values()) >= 0
    assert set(y) == set(range(1, b)) and min(y.values()) >= 0
    for x in range(1, b):
        assert sum(v*cost(b, t, x) for t, v in f.items()) <= R*x
    for t in c:
        assert c[t]+sum((b+t-1-x)*v for x, v in y.items() if x >= t) >= alpha
    value = sum(c[t]*v for t, v in f.items())
    assert value == alpha-(R-1)*sum(x*v for x, v in y.items())
    return value


def decode_result(out):
    return {'policy': {int(t): F(v) for t, v in out['policy'].items()},
            'lam': F(out['lam']), 'alpha': F(out['alpha']),
            'y': {int(t): F(v) for t, v in out['y'].items()}}
