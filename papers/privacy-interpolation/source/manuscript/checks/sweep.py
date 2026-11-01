"""Exact rational sweep, extracted from the frozen research implementation."""
from fractions import Fraction as F

def cell_minimum_squared(a, b, lo, hi):
    candidates = [(a*v+b)**2/v for v in (lo, hi)]
    if a and b and lo <= b/a <= hi:
        candidates.append(4*a*b)
    return min(candidates)

def all_certificates(p, q, z):
    """A common order, one linear scan per designated coordinate."""
    n = len(p)
    order = sorted(range(n), key=lambda i: q[i]/p[i])
    groups = []
    for i in order:
        v = z*q[i]/p[i]
        if groups and groups[-1][0] == v:
            groups[-1][1].append(i)
        else:
            groups.append((v, [i]))
    result = []
    for j in range(n):
        a, b, lo = 1-p[j], F(0), F(1)
        best = None
        for hi, group in groups:
            value = cell_minimum_squared(a, b, lo, hi)
            best = value if best is None else min(best, value)
            for i in group:
                if i != j:
                    a -= p[i]
                    b += z*q[i]
            lo = hi
        result.append(min(best, cell_minimum_squared(a, b, lo, z*z)))
    return result
