# Independent check of a tiny one-state CCRA whose reversal has an affine context (found by the referee subagent).
# Registers (x0,x1) start at (1,1); on a: (x0,x1):=(x1-1, x0); on b: (x0,x1):=(x0*x1-1, 1/2); output x1/2+1.
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import affine_context_search as acs
def run(w):
    x0, x1 = sp.Integer(1), sp.Integer(1)
    for ch in w:
        if ch == 'a': x0, x1 = x1 - 1, x0
        else: x0, x1 = x0 * x1 - 1, sp.Rational(1, 2)
    return x1 / 2 + 1
frev = lambda w: run(w[::-1].replace('a', '0').replace('b', '1').replace('0', 'a').replace('1', 'b'))
f2 = lambda w: run(w.replace('0', 'a').replace('1', 'b'))
frev2 = lambda w: f2(w[::-1])
rep = acs.rep_from_function(frev2, '01', 4)
assert acs.check_rep(rep, frev2, '01', 9)
lam, M, gam, d = rep
print('minimal dimension of the reversal:', d, ' ranks', {a: M[a].rank() for a in '01'})
l = sp.symbols('l', integer=True, nonnegative=True)
def W(w):
    X = sp.eye(d)
    for ch in w: X = X * M[ch]
    return X
Y = W('00'); P, J = Y.jordan_form(); Yl = sp.simplify(P * J ** l * P.inv())
for t in range(5): assert sp.simplify(Yl.subs(l, t) - Y ** t) == sp.zeros(d)
B = sp.simplify(Yl * W('1'))                 # b_l = (aa)^l b   (x1 = eps, w = aa, x2 = b)
v0 = lam * W('01')                           # u = ab
v1 = sp.simplify(v0 * B.subs(l, 1))
s_, t_ = sp.symbols('s t'); rr = s_ * v0 + t_ * v1
eqs = []
for t in range(4): eqs += list(sp.simplify(rr * B.subs(l, t) - rr))
sol = sp.solve(eqs, [s_, t_], dict=True)[0]
r1 = sp.simplify(rr.subs(sol).subs({t_: 1, s_: 1}))
a_, b_ = sp.symbols('A Bc')
img = sp.simplify(v0 * B)
s2 = sp.solve(list(img - b_ * r1 - a_ * v0), [a_, b_], dict=True)[0]
print('r1 fixed:', sp.simplify(r1 * B - r1) == sp.zeros(1, d), '; v0 not in Q r1:', sp.Matrix.vstack(r1, v0).rank() == 2)
print('alpha(l) =', sp.factor(s2[a_]), '  beta(l) =', sp.factor(s2[b_]), '  beta/(alpha-1) =', sp.simplify(s2[b_] / (s2[a_] - 1)))
print('identity symbolic:', sp.simplify(img - s2[b_] * r1 - s2[a_] * v0) == sp.zeros(1, d))
