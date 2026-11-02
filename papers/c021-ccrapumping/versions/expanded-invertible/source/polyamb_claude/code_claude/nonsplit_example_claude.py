"""Illustration: series whose G_f^o is a non-split torus or SL_2-like are not PA (Theorem thm:polyamb),
and the (a)-test of the paper rejects them; triangular examples (MPS Ex. 17, Example ex:heis) pass (a)."""
import sys, os, random
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import polyamb_check_claude as P

def verdict(name, mats, expect):
    S = P.Setup([P.to_fmpq_mat(A) for A in mats])
    ok, info = P.a_test(S, random.Random(3))
    extra = ''
    if ok:
        extra = ' R_u ' + P.u_layers(S)[0]
    print(f"{'OK ' if ok == expect else 'MISMATCH'} {name}: (a)={ok} expected={expect}{extra}")
    return ok == expect

F = Fr
good = True
# rotation by an angle of infinite order: G^o = SO(2), a non-split torus over Q
rot = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
good &= verdict("rotation (3+4i)/5, one letter", [rot], False)
good &= verdict("rotation and diag(2,2)", [rot, [[F(2), F(0)], [F(0), F(2)]]], False)
# all letters have rational eigenvalues, but G^o = GL_2
good &= verdict("diag(2,1), I+E12, I+E21", [[[F(2), F(0)], [F(0), F(1)]], [[F(1), F(1)], [F(0), F(1)]],
                                          [[F(1), F(0)], [F(1), F(1)]]], False)
# triangular examples: PA (and not CCRA)
good &= verdict("MPS Example 17", [[[F(2), F(2), F(0)], [F(0), F(2), F(0)], [F(0), F(0), F(1)]],
                                   [[F(1), F(0), F(0)], [F(0), F(1), F(1)], [F(0), F(0), F(1)]]], True)
good &= verdict("Example ex:heis", [[[F(2), F(2), F(0)], [F(0), F(2), F(0)], [F(0), F(0), F(2)]],
                                    [[F(3), F(0), F(0)], [F(0), F(3), F(3)], [F(0), F(0), F(3)]]], True)
# monomial, non-diagonal: G^o split torus (PA, in fact finitely ambiguous)
good &= verdict("weighted swap and diag(2,3)", [[[F(0), F(2)], [F(1), F(0)]], [[F(2), F(0)], [F(0), F(3)]]], True)
print("ALL OK" if good else "SOME MISMATCH")
