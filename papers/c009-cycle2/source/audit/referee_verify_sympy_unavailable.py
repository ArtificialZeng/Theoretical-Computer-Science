"""Fresh, bounded exact diagnostics. This is not a universal proof certificate.

Does not import or execute proposer code and does not modify frozen inputs.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import random
import sympy as s

HERE = Path(__file__).resolve().parent
JOB = "c009-cycle2-referee-eb6d40fb0393"
rng = random.Random(90400393)

# An unrestricted symbolic 4-by-4 block, checked by expanding matrix products.
b = s.Matrix(s.symbols("b1:4", real=True))
d12, d13, d23 = s.symbols("d12 d13 d23", real=True)
D = s.Matrix([[0, d12, d13], [-d12, 0, d23], [-d13, -d23, 0]])
T = s.Matrix.vstack(s.Matrix([[s.Rational(1, 2)]]).row_join(-b.T), b.row_join(D))
x = s.Matrix([1, *list(2*b)])
M = T*T
z = M.T*x
a = (b.T*b)[0]
Db = D*b
D2b = D*Db
rhs = 2*a*a + 4*a*a*a + (3+8*a)*(Db.T*Db)[0] + 4*(D2b.T*D2b)[0]
assert s.expand((z.T*z)[0] - (x.T*x)[0]/16 - rhs) == 0
Q = M*M.T
R = D*D-b*b.T
y = b/2+D*b
assert all(s.expand(v) == 0 for v in (Q[1:, 1:]-y*y.T-R*R))

# New exact block inputs, including n=1 and both degeneracies.
exact_blocks = 0
for n in range(1, 9):
    for trial in range(12):
        B = s.zeros(n)
        for i in range(n):
            for j in range(i):
                v = s.Rational(rng.randrange(-20, 21), rng.randrange(1, 9))
                B[i, j], B[j, i] = v, -v
        if trial == 0:
            for i in range(1, n):
                B[0, i] = B[i, 0] = 0
        if trial == 1:
            for i in range(1, n):
                for j in range(1, n):
                    B[i, j] = 0
        u = s.eye(n)[:, 0]
        P = u*u.T
        Tn = P/2+B
        bn = B*u
        an = (bn.T*bn)[0]
        Dn = (s.eye(n)-P)*B*(s.eye(n)-P)
        xn = u+2*bn
        zn = Tn.T*Tn.T*xn
        db = Dn*bn
        ddb = Dn*db
        residual = (zn.T*zn)[0]-(xn.T*xn)[0]/16
        expected = 2*an**2+4*an**3+(3+8*an)*(db.T*db)[0]+4*(ddb.T*ddb)[0]
        assert residual == expected and residual >= 0
        exact_blocks += 1

# Separate scalar enumeration and trace computation, with all maps retained.
map_checks = []
forcing_checks = 0
for n, ell in [(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)]:
    for trial in range(3):
        A = [[F(1, 2) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                A[i][j] = F(rng.randrange(9), 8)
                A[j][i] = 1-A[i][j]
        count = F(0)
        for f in product(range(n), repeat=4*ell):
            weight = F(1)
            for k in range(4*ell):
                v, w = f[k], f[(k+1) % (4*ell)]
                weight *= A[v][w] if k % 4 in (0, 1) else A[w][v]
            count += weight
        density = count / n**(4*ell)
        An = s.Matrix([[s.Rational(v.numerator, v.denominator) for v in row] for row in A])
        Mn = An**2
        trace_density = s.trace((Mn*Mn.T)**ell)/n**(4*ell)
        assert density == trace_density and density >= F(1, 16)**ell
        # For real skew matrices of order <=3, beta^2 is this exact sum.
        beta2 = sum(((A[i][j]-F(1, 2))/n)**2 for i in range(n) for j in range(i))
        assert density-F(1, 16)**ell >= F(1, 16)**ell * beta2**(2*ell)
        forcing_checks += 1
        map_checks.append({"n": n, "ell": ell, "trial": trial, "maps": n**(4*ell), "density": str(density)})

# Sharpness formula on independent rational values, checked at higher lengths.
sharpness_checks = 0
K = s.Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
for r in [s.Rational(1, 3), s.Rational(1, 17), s.Rational(1, 97)]:
    An = s.ones(3)/2+r*K
    Mn = (An/3)**2
    Qn = Mn*Mn.T
    for ell in [1, 2, 3, 7, 13]:
        assert s.trace(Qn**ell)-s.Rational(1, 16)**ell == 2*(r*r/3)**(2*ell)
        sharpness_checks += 1

report = {
    "job_id": JOB,
    "scope": "Finite exact diagnostics supplementary to the analytic referee derivation; no proof by bounded search.",
    "independent_implementation": True,
    "symbolic_block_dimension": 4,
    "symbolic_residual_identity": True,
    "symbolic_compression_identity": True,
    "new_rational_block_checks": exact_blocks,
    "direct_map_checks": map_checks,
    "exact_forcing_checks_dimensions_at_most_3": forcing_checks,
    "sharpness_checks": sharpness_checks,
    "source_sha256": hashlib.sha256((HERE.parent/"source.md").read_bytes()).hexdigest(),
    "failures": []
}
(HERE/"referee-checks.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({k:v for k,v in report.items() if k != "direct_map_checks"}))
