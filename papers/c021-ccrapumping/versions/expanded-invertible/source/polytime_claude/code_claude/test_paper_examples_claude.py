# Sanity checks of the polynomial-time procedure on the examples of the c021 paper.
import sys, random
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import flint
from linalg_claude import Q
from polyccra_claude import to_fmpq_mat as T, decide, decide_qu, Setup, u_layers, is_finite_cr


def show(name, gens, expect, qu=False):
    if qu:
        v, det = decide_qu(gens)
    else:
        v, det = decide(gens, random.Random(7))
    status = "OK " if v == expect else "MISMATCH"
    print(f"{status} {name}: verdict={v} expected={expect}")
    for k in ['d', 'dimA', 'dimJ', 'm', 'u', 'nonabelian_level', 'dimU', 'finite_semisimple_part']:
        if k in det:
            print(f"     {k} = {det[k]}")
    if 'a' in det:
        print(f"     a-test = {det['a']}")
    if det.get('hist'):
        for h in det['hist']:
            print("     level", h)
    return v == expect


ok = True
# Example ex:heis: M_a = 2(I+E12), M_b = 3(I+E23): not CCRA
Ma = T([[2, 2, 0], [0, 2, 0], [0, 0, 2]])
Mb = T([[3, 0, 0], [0, 3, 3], [0, 0, 3]])
ok &= show("heis 2^a 3^b [w:ab]", [Ma, Mb], False)

# Corollary (MPS Example 17): not CCRA
Ma = T([[2, 2, 0], [0, 2, 0], [0, 0, 1]])
Mb = T([[1, 0, 0], [0, 1, 1], [0, 0, 1]])
ok &= show("MPS Example 17", [Ma, Mb], False)

# BS(1,2): g(w) = sum 2^i b_i : CCRA
M0 = T([[1, 0], [0, 2]])
M1 = T([[1, 0], [2, 2]])
ok &= show("BS(1,2) sum 2^i b_i", [M0, M1], True)

# alternating sum sum (-1)^i b_i : CCRA, quasi-unipotent
M0 = T([[1, 0], [0, -1]])
M1 = T([[1, 0], [-1, -1]])
ok &= show("alternating sum", [M0, M1], True)
ok &= show("alternating sum (qu-sector algorithm)", [M0, M1], True, qu=True)

# alternating position sum sum (-1)^i i b_i : not CCRA, quasi-unipotent
def Ab(b):
    return [[1, -b, -b], [0, -1, -1], [0, 0, -1]]
M0 = T([list(r) for r in zip(*Ab(0))])
M1 = T([list(r) for r in zip(*Ab(1))])
ok &= show("alternating position sum", [M0, M1], False)
ok &= show("alternating position sum (qu-sector)", [M0, M1], False, qu=True)

# position sum (unipotent): not CCRA
A0 = [[1, 0, 0], [0, 1, 1], [0, 0, 1]]
A1 = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
M0 = T([list(r) for r in zip(*A0)])
M1 = T([list(r) for r in zip(*A1)])
ok &= show("position sum (unipotent)", [M0, M1], False)
ok &= show("position sum (qu-sector)", [M0, M1], False, qu=True)

# letter counts |w|_a |w|_b (unipotent, commuting): CCRA
Ma = T([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
Mb = T([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]])
ok &= show("|w|_a |w|_b", [Ma, Mb], True)

# SL2(Z)-type irreducible (not virtually solvable): not CCRA
M0 = T([[1, 1], [0, 1]])
M1 = T([[1, 0], [1, 1]])
ok &= show("SL2(Z) generators", [M0, M1], False)

# Gamma = <[[0,2],[1,0]]>: M^2 = 2I, so H^o = scalars (split): CCRA (parity control, x:=2x every other step)
M0 = T([[0, 2], [1, 0]])
ok &= show("M^2=2I (H^o = split scalar torus, F=Z/2)", [M0], True)
# finite irreducible group: rotation of order 4 together with reflection: CCRA (finite)
M0 = T([[0, -1], [1, 0]])
M1 = T([[1, 0], [0, -1]])
ok &= show("dihedral of order 8", [M0, M1], True)
# infinite subgroup of O_2(Q) (Pythagorean rotation): non-split torus -> not CCRA
M0 = T([[Q(3, 5), Q(-4, 5)], [Q(4, 5), Q(3, 5)]])
ok &= show("Pythagorean rotation (anisotropic torus)", [M0], False)
print("ALL OK" if ok else "SOME MISMATCH")
# genuinely non-split torus: Gamma = <[[1,1],[1,2]]> (eigenvalues (3+-sqrt5)/2, infinite order): not CCRA
M0 = T([[1, 1], [1, 2]])
ok2 = show("golden matrix (non-split torus)", [M0], False)
# 2 x 2 irreducible with Q(i) torus but finite index? <[[2,-1],[1,2]]>: eigenvalues 2+-i: not CCRA
M0 = T([[2, -1], [1, 2]])
ok2 &= show("2+i rotation (non-split torus)", [M0], False)
print("EXTRA OK" if ok2 else "EXTRA MISMATCH")
