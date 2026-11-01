# Full-scope proof submitted for mathematical review

Proposer job: c021-ccrapumping-research-44e54bf7c116, research pass 1,
2026-11-01. This is a research proof dossier, not an accepted manuscript or
an independent audit. The original statement is the unmodified source.md;
problem.md fixes its interpretation. No rectangular/compression claim is
made. The supplied prospective proof is replaced below by an explicit
argument; in particular, no algebraic-group image theorem is needed.

## Exact proposed resolution

Let f:{0,1}* -> Q be the sum of the positions occupied by 1, counting from
1. Then f is weighted-automaton recognizable and satisfies the uniform
R-generable EPS condition of source.md with R=Z[1/2] and m=1, including
every characteristic-zero coefficient-sum condition. However, no finite-state
copyless polynomial cost register automaton over Q, with any finite number
of registers and arbitrary rational constants, recognizes f.

This is a counterexample to sufficiency in the full frozen question. It
confirms the source's insufficiency conjecture; the status `disproved`
refers to the proposed sufficiency implication, not to that conjecture.

## 1. Multiaffine pullbacks and the canonical minimal representation

For r registers let V_r be the Q-vector space spanned by the 2^r squarefree
monomials in x_1,...,x_r, including 1. A copyless polynomial tuple P has
multiaffine coordinates with pairwise disjoint variable supports. Composition
of copyless tuples is copyless: substituting a tuple into an expression
uses each component at most once, and components have disjoint variables.
Consequently B_P:h -> h o P preserves V_r. This fact uses only the original
syntactic copyless condition, and allows resets, merges, multiplication,
negative constants and cancellations.

For a one-state CCRA, let P_a be the letter maps, x_0 the initial valuation,
and o in V_r the output polynomial. Reading uv gives P_{uv}=P_v o P_u.
Therefore B_{uv}=B_u B_v and

    g(w) = lambda B_w o,       lambda(h)=h(x_0).

Put

    W = span{B_w o : w in Sigma*},
    N = {h in W : lambda B_v h=0 for every v in Sigma*}.

W and N are invariant under every B_a: B_a B_w=B_{aw} and
lambda B_v B_a=lambda B_{va}. The induced representation on D=W/N is
reachable from o+N and observable by lambda. It is minimal, and any other
reachable and observable representation of g is isomorphic to it.

For completeness, send B_w o to the residual function
t -> lambda B_t B_w o=g(tw). The kernel on W is exactly N, so D is
identified with the span of these right residuals. This construction gives
minimal dimension and the same letter action for every representation of
g. Equivalently, the Hankel matrix (g(tw))_{t,w} factors through any weighted
representation; reachability and observability make its rank equal to the
representation's dimension. Thus a displayed reachable/observable realization
can be used to determine the matrices on D up to simultaneous similarity.

## 2. Images of copyless polynomial maps

For a copyless map P:Q^r -> Q^r let k(P) be the number of its nonconstant
coordinates and let L_P be the coordinate affine subspace obtained by
fixing each constant coordinate to its value in P.

**Image/rank lemma.** P(Q^r)=L_P(Q), and rank(B_P)=2^{k(P)}.

Proof. A nonconstant multiaffine polynomial q over Q is surjective on Q:
choose an occurring variable x_i and write q=x_i a+b with a nonzero
polynomial in the other variables. Since Q is infinite, those other
variables can be specialized to rational values with a nonzero. Varying
x_i then gives every rational value. Nonconstant coordinates of P use
disjoint variable sets, so their specializations can be made independently.
Thus all points of L_P are attained. Restricting a multiaffine polynomial
to L_P gives the 2^{k(P)}-dimensional space V(L_P) of multiaffine
polynomials in its free coordinates. Pullback by P factors through that
restriction and is injective on V(L_P), by surjectivity and infinitude of
Q. This proves the rank formula and also

    ker B_P = {h in V_r : h|_{L_P}=0}.                  (2.1)

The claim that a nonzero rational polynomial is nonzero at some rational
point follows by induction on its number of variables from the elementary
one-variable root bound. No algebraic closure or physical invertibility
is assumed here.

## 3. Minimum-rank retraction, including singular physical maps

Choose a word e minimizing k(P_e) over ALL words, including the empty
word. A minimum exists because these counts lie in {0,...,r}. Write
k=k(P_e), P=P_e and L=L_P. The k free coordinates of L are exactly the
nonconstant output positions of P.

Since P maps onto L, the restriction A=P|_L maps L to L. The constant
coordinates of P o P are the same outside those k positions, so
k(P o P)<=k. Minimality, applied to the word ee, implies equality. Hence
each of the k free output coordinates of A is nonconstant on L.
Restriction by constants preserves copylessness. With k input variables
and k nonconstant output coordinates, each output must use exactly one
input variable and every input is used once. Each coordinate is multiaffine,
so necessarily

    A_i(t)=alpha_i t_{pi(i)}+beta_i,   alpha_i != 0,

for a permutation pi. Thus A is an invertible affine coordinate permutation
of L. This conclusion concerns A on L, not P on the original register
space. If k=0, L is a point and A is its unique invertible map.

Define the full-register map Q=A^{-1} o P:Q^r -> L, with the constant
coordinates of L restored in the tuple. It is copyless, maps onto L, and
Q|_L=id_L. Hence Q o Q=Q. Put E=B_Q on V_r.

**Projection lemma.** E is the projection onto im B_P along ker B_P;
in particular E is a polynomial in B_P with rational coefficients.

Proof. Let i:V(L)->V_r embed a polynomial in the free coordinates by
ignoring the other coordinates. The image of B_P consists of pullbacks of
V(L). The same holds for B_Q. Replacing the free output coordinates by
the affine coordinate inverse A^{-1} is an automorphism of V(L), so
im B_Q=im B_P. Both maps have image L in register space, so (2.1) gives
ker B_Q=ker B_P. E is idempotent because Q is a retraction. This proves
the projection assertion.

More explicitly B_P^2 has the same rank as B_P by the image/rank lemma and
k(P o P)=k. Thus V_r=ker B_P direct-sum im B_P, and B_P is invertible
on its image. If q(T) is the minimal polynomial of that invertible
restriction, then q(0)!=0. By the polynomial Chinese remainder theorem
there is p(T) in Q[T] with

    p(T)=0 mod T,       p(T)=1 mod q(T).

p(B_P) is zero on ker B_P and identity on im B_P, so p(B_P)=E.
This also covers invertible B_P, when its kernel is zero. If k=0 the
same argument applies to the one-dimensional image.

Now suppose the minimal matrices M_a on D=W/N are invertible. In particular
M_e is invertible. Since E=p(B_e), both W and N are E-invariant. On V_r,

    (I-E)B_e=0.

On D this becomes (I-E_bar)M_e=0, so E_bar=I. This proves the identity
action on the observable subquotient without transferring physical
invertibility from M_e to P_e.

## 4. Compressing each letter without losing the minimal subquotient

Set C_a=E B_a E on im E. Identify V(L) with im E by

    J(h)=h o Q,       J^{-1}(g)=g|_L.

Indeed restriction after J is identity since Q|_L=id_L, and J followed
by restriction is E on V_r. A direct substitution shows

    C_a J = J B_{R_a},       R_a=Q o P_a|_L : L -> L.  (4.1)

In detail C_a J(h)=h o Q o P_a o Q, which is exactly the right side
of (4.1). This fixes the pullback order explicitly.

R_a is copyless, by restriction and composition. Its k outputs are all
nonconstant. To prove this, write P_e=A o Q; then the actual word eae
has register map

    P_e o P_a o P_e = A o R_a o A o Q.

The map A o Q=P_e is onto L, and the outer A only permutes, rescales
and translates the k coordinates. Therefore the number of nonconstant
outputs of this word map is exactly the number for R_a. Minimality of
e makes it at least k; R_a has only k free outputs, so it is k. The
same variable-count argument as in Section 3 now proves that every R_a
is an invertible affine coordinate permutation of L.

Let W'=EW and N'=W' intersect N. They are invariant under C_a. The map

    W'/N' -> W/N,       h+N' -> h+N

is an isomorphism, because E acts as identity on W/N and fixes W'. The
induced C_a action agrees with M_a, since the two E factors act as identity
there. Thus the original minimal letter matrices are a common invariant
subquotient of the pullbacks of the affine coordinate permutations R_a.
Both invariant spaces are finite dimensional; invertibility of C_a on
im E also implies their invariance under C_a^{-1}, although only polynomial
invariance will be needed below.

## 5. An elementary commuting-unipotents obstruction

**Affine-coordinate subquotient lemma.** Let R_a be any finite family of
invertible affine coordinate permutations of Q^k. On V_k let T_a=B_{R_a}.
If a common invariant subquotient has induced matrices M_a that are all
unipotent, then the M_a commute pairwise.

Proof. For k=0 all spaces have dimension at most one. Otherwise put
t=k!. For each a the permutation disappears in R_a^t, giving

    (R_a^t)_i(x)=alpha_{a,i} x_i+beta_{a,i},
    alpha_{a,i} != 0.

Decompose this coordinatewise affine map as S_a o U_a=U_a o S_a,
where U_a is the translation by beta_{a,i} on coordinates for which
alpha_{a,i}=1, and is identity on the other coordinates; S_a is identity
on the former coordinates and equals alpha_{a,i}x_i+beta_{a,i} on the
latter. Therefore U_a and U_b commute for every a,b: both are translations
in the same coordinate system.

The pullback B_{S_a} is semisimple: on each coordinate with alpha != 1,
replace x_i by x_i+beta/(alpha-1). These coordinate changes conjugate S_a
to diagonal scaling and preserve V_k. Its pullback is consequently
diagonal in the squarefree-monomial basis of the shifted coordinates.
The pullback B_{U_a} is unipotent: translation sends each squarefree
monomial to itself plus terms of lower total degree. The two pullbacks
commute and their product is T_a^t. Hence they are the multiplicative
Jordan factors of T_a^t.

Here is the needed finite-dimensional linear algebra, stated explicitly
so no algebraic-group closure assertion is hidden. If an invertible matrix
T over Q has a commuting factorization T=S U with S semisimple and U
unipotent, then these factors are unique and are polynomials in T. One
can extend scalars to an algebraic closure, decompose into generalized
eigenspaces, and on the lambda-eigenspace set S=lambda I and U=lambda^{-1}T.
Polynomial interpolation modulo the powers (X-lambda)^{d_lambda} gives
S as a polynomial in T, and T's invertibility gives U likewise. In the
present application all eigenvalues are products of the rational alpha_i,
so the interpolation can be done over Q itself. Uniqueness also follows
on each such eigenspace. Every T-invariant subspace is therefore invariant
under S and U. On any invariant subquotient, their induced maps are still
semisimple and unipotent respectively, and still form its Jordan factors.

Apply this to T_a^t and the given common invariant subquotient. Since
M_a^t is unipotent, its semisimple factor is identity. Thus the induced
B_{U_a} equals M_a^t. Commutativity of the full-space translations implies

    M_a^t M_b^t = M_b^t M_a^t.

For a unipotent d-dimensional matrix M in characteristic zero,

    M = sum_{j=0}^{d-1} binom(1/t,j) (M^t-I)^j.        (5.1)

For example (5.1) follows from the formal binomial identity modulo the
nilpotent ideal generated by M-I; the substitution is finite, and the
unipotent t-th root with constant term 1 is unique in Q[X]/(X^d).
Thus M_a and M_b are polynomials in their commuting t-th powers, so
they commute. This proves the lemma.

Combining Sections 1-5 gives the following full-register structural
obstruction, with no hypothesis on invertibility of physical register maps:

**One-state obstruction.** If the minimal weighted representation of a
one-state Q-CCRA has unipotent letter matrices, those matrices commute.

Indeed unipotent matrices are invertible, so Sections 3-4 compress to the
affine-coordinate subquotient lemma. No assumption about the algebraic
group generated by the minimal matrices is needed.

## 6. The proposed witness has the required uniform pumping property

Write l(w)=|w|, c(w)=number of 1s, and f(w)=sum of their positions.
Concatenation gives f(uv)=f(u)+f(v)+l(u)c(v). On column coordinates
(f,l,1), appending bit b acts by

    A_b = [[1,b,b], [0,1,1], [0,0,1]].

For a whole word define A_w by appending its letters, so

    A_w = [[1,c(w),f(w)], [0,1,l(w)], [0,0,1]],
    A_{uv}=A_v A_u.

Thus a standard row-convention weighted representation has letter matrices
A_b^T, initial row (0,0,1), and final column (1,0,0)^T. It recognizes f.

For every u,w,v and every integer n>=0, direct summation gives

    f(uw^n v)=C+A n+B n(n-1)/2,
    C=f(u)+f(v)+l(u)c(v),
    A=f(w)+l(u)c(w)+l(w)c(v),
    B=l(w)c(w).

The j-th copy of w, indexed from zero, contributes
f(w)+(l(u)+j l(w))c(w), and the final v contributes
f(v)+(l(u)+n l(w))c(v), proving the formula also for empty words.
Replacing n by n+1 gives

    f(uw^{n+1}v)=(C+A)+(A+B/2)n+(B/2)n^2.            (6.1)

The one ring R=Z[1/2] is a finitely generated subsemiring of Q (generators
-1 and 1/2 suffice, with the usual 0 and 1). Every coefficient in (6.1)
belongs to R. Constants and the sequence n generate (6.1) under pointwise
sum and product, exactly as required by Definition 11. Use m=1 uniformly
for every triple. Its sole exponential base is 1, so every degree's
coefficient sum is precisely its coefficient in (6.1), in R. This is the
known easy half of Example 26, not a novelty claim. It uses the actual
subsemiring Z[1/2], rather than the nonmultiplicatively-closed set (1/2)Z.

## 7. Removing arbitrary finite control

Suppose, toward contradiction, that some finite-state Q-CCRA recognizes
f. Its complete deterministic control graph has a reachable bottom
strongly connected component S. Let s=|S|>=1, choose q in S, and choose
a prefix p taking the initial state to q.

Reading 0^s from q stays in S. From its endpoint choose a shortest return
path to q; it has length at most s-1. Let u be 0^s followed by that path.
Likewise let v be 1^s followed by a return path of length at most s-1.
They are nonempty return words at q, and

    c(u)/l(u) < 1/2 < c(v)/l(v).                     (7.1)

Indeed the added path in u has fewer than s letters and contains all of
u's 1s; the added path in v has fewer than s letters and contains all of
v's possible 0s. In particular

    delta = c(v)l(u)-c(u)l(v) != 0.                 (7.2)

Use U,V as a new two-letter alphabet and substitute h(U)=u,h(V)=v.
The composed register maps for the two return words, the valuation after
p, and the output expression at q form a one-state Q-CCRA recognizing

    g(z)=f(p h(z)).

This is legitimate for every input z because both blocks return to q,
and composition preserves copylessness. No assumption that 0 or 1 is a
loop, no encoding of states by registers, and no restriction of the
original finite-state model is used.

The three-dimensional column realization of g starts from

    z_p=(f(p),l(p),1)^T,

uses the block matrices A_u,A_v above, and observes row e_1^T. Each
matrix is unipotent, and

    D_0=A_v A_u-A_u A_v=delta E_{13}.                 (7.3)

They do not commute. This realization is minimal:

* The reachable column span contains z_p, D_0 z_p=delta e_1, and
  (A_u-I)z_p=(c(u)l(p)+f(u),l(u),0)^T. Because l(u)>0 and the last
  coordinate of z_p is 1, these three vectors span Q^3.
* The observable row span contains e_1^T, e_1^T D_0=delta e_3^T,
  and e_1^T(A_v-I)=(0,c(v),f(v)). Here c(v)>=s>0, so these span
  the dual of Q^3.

All these differences are in the indicated spans: the products in (7.3)
come from the two block words UV and VU, regardless of their order in
the column convention. In the standard row convention the matrices are
A_u^T,A_v^T, so the same reachability and observability assertions give
a minimal weighted representation. Transposition preserves unipotence
and failure to commute.

By the one-state obstruction in Section 5 the two minimal unipotent
letter matrices of g must commute. Equation (7.3) contradicts this.
Hence no finite-state Q-CCRA recognizes f. Together with Section 6 this
disproves sufficiency in the immutable full-scope question.

## 8. Dependencies, adversarial checks and declared limits

The proof uses only copyless composition, elementary polynomial
surjectivity over an infinite field, finite-dimensional weighted
representation minimization (proved in Section 1), polynomial projection
and multiplicative Jordan decomposition (proved in Sections 3 and 5),
and elementary properties of a finite complete directed graph. In
particular it does not use monomial-cover theorems, a group-image
assertion, a positive-characteristic extension, or a rectangular-length
bridge.

Known gap list for this proposed proof: []

This records the proposer's completed proof, not a referee acceptance or a
mathematical truth certificate. The fresh referee must challenge Sections
2-5 and the full-model passage in Section 7, and separately decide current
novelty and theoretical significance.

The exact finite stress tests in research_checks.py and research-checks.json
check a singular nonlinear four-register family, including an actual
invertible observable quotient; all 288 explicitly specified two-coordinate
affine permutations and 82,944 translation-factor pairs; and all 746
complete binary DFAs with one, two or three states. These tests do not
replace any general argument above. The previous triage checks and all
their limitations are retained unchanged.

The nearest source result is Mazowiecki--Puch--Smertnig, STACS 2026,
Theorem 15 and Section 3.2/Example 26; its Appendix B.4 supplies the
known pumping calculation. The proposed new contribution is the
minimum-active-output retraction and invariant-subquotient normalization,
followed by the commuting-unipotent obstruction and its application after
arbitrary finite control. Current primary-source comparison and search
limits are recorded in literature-research.md. No global priority or STOC
acceptance is claimed. No independent audit has yet occurred.
