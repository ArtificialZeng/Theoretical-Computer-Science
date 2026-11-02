# Precise original problem and computational scope

Status at TRIAGE: open-supported; original unresolved; no publication candidate.
Immutable statement: `source.md`, SHA256
`12956c470e37f8a548f510c7eb1781eda7b961999c5fa1163df43b56513b45a4`.

For every finite ground set E of size n and every pair h,g:2^E -> R_{≥0},
assume h(empty)=g(empty)=0, monotonicity q(A)≤q(B) for A⊆B, and
submodularity q(A)+q(B)≥q(A∪B)+q(A∩B), for q in {h,g}.
There is no assumption that h(E)=g(E), and either function can vanish.
Define f(S)=h(S)+g(E\S) and OPT_k=max_{|S|=k} f(S).
A deterministic algorithm receives the instance and returns ONE permutation
pi=(e_1,...,e_n), with prefixes S_k={e_1,...,e_k} and S_0=empty.
For a uniform constant r≥1 its guarantee is

    for every n,E,h,g and every k in {0,...,n}, r f(S_k) >= OPT_k.

The k=0 and k=n conditions are automatic for r≥1. The paper defines its
ratio using k=1,...,n; adding k=0 changes no uniform optimal constant.
Use inequalities rather than undefined 0/0 when an objective value vanishes.
The empty instance is harmless.

Let rho(I,pi) be the infimum of feasible r≥1 for instance I and pi.
Distinguish

    C_struct = inf_{all deterministic algorithms A} sup_I rho(I,A(I)),
    C_poly   = inf_{deterministic polynomial-oracle algorithms A}
               sup_I rho(I,A(I)).

For unrestricted access C_struct also equals sup_I min_pi rho(I,pi), since
finite enumeration of all subsets and permutations selects an optimal order.
The source's Section 1 (PDF p.2) places no explicit polynomial restriction
on its infimum over algorithms. Section 1.1 promises polynomial-time upper
bounds; the displayed double-greedy algorithm uses only values of h and g
and admits O(n^2) oracle calls and polynomial additional arithmetic. It does
not formally specify a value-oracle input/bit model in that definition.
Consequently the requested polynomial value-oracle interpretation is an
explicit additional algorithmic requirement, not a justified replacement of
the unrestricted source infimum. Adopt exact-value queries with unit-cost
arithmetic/comparisons, and keep C_struct <= C_poly distinct. A bit-complexity
claim would additionally need an encoding/precision specification.

The frozen objective is matching achievable and impossible deterministic
ratios on the ENTIRE class. A polynomial-oracle 2-competitive algorithm,
combined with the existing structural lower bound 2, would settle both
constants at 2. If a different sharp value is proposed, matching upper and
lower bounds must address the source scope, with polynomial upper-bound
construction as required here; an oracle-hardness bound alone does not
establish a structural impossibility. Infima need not be attained; any
limiting family/epsilon dependence must be stated explicitly.

Unnormalized nonnegative monotone inputs are covered without a hidden
restriction: put h'=h-h(empty), g'=g-g(empty), B=h(empty)+g(empty)>=0.
Then f=f'+B and OPT_k=OPT'_k+B. If r f'(S_k)>=OPT'_k and r>=1, then
r f(S_k)>=OPT'_k+B=OPT_k. Normalized functions remain a subclass for
lower bounds. Thus the worst-case constants agree. This is the standard
normalization argument, also given in source Eq.(5), PDF pp.8-9.
Negative baselines are outside the model.

Nearest verified baseline: Disser, Klimm, Lutz and Strubberg, Acta Informatica
63:31 (2026), DOI 10.1007/s00236-026-00546-x: Corollary 2/Table 1 give
C_poly <= 1+e/(e-1); Proposition 11 at curvature 1 gives C_struct >= 2;
Section 5, pp.20-21 explicitly asks to close this gap. Proposition 17
already solves equal totals at 2. Proposition 19 and Corollary 20,
Appendix B pp.21-22, show this double-greedy algorithm itself has exact
worst-case ratio 1+e/(e-1), even with modular g. A better analysis of that
same unchanged algorithm cannot yield the target 2.
Primary URL: https://link.springer.com/article/10.1007/s00236-026-00546-x

Current adjacent work: Bienkowski et al., ESA 2026, 134:1-23,
DOI 10.4230/LIPIcs.ESA.2026.134, official abstract reports a 1.373
incremental bound and a 1.25 lower bound for the monotone incremental
problem. This concerns g=0 rather than arbitrary h,g. It is not a resolution
of the present sharp ratio, and shows why the older incremental comparison
must not be represented as the current unrestricted optimum.
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.134

Proposed substantive delta: a new deterministic construction of a single
2-good chain for arbitrary unequal-total monotone submodular pairs, with
polynomial oracle implementation, or a genuinely matching different sharp
ratio. Finite cases, equal totals, randomized/static/GS restrictions and
subsidiary algorithm counterexamples do not resolve the original.

Decisive first research test (not executed during TRIAGE): exact rational
Boolean-lattice DP on bounded coverage instances tests whether sets with
2f(S)>=OPT_|S| admit an empty-to-E chain, and separately whether reachable
good sets can become dead ends. It distinguishes the necessary chain claim
from the stronger, potentially false, every-good-set extension claim.
Details and mandatory source adversaries are in evidence/triage.md.
