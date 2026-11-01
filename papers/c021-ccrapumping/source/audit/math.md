# Fresh mathematical referee report

Job: c021-ccrapumping-referee-d846876ce849. Role: referee.
Snapshot: fb196911906a12d3f006a58d590694062481bf6aa44e05c6691883c3e220d3cf.

**Verdict: accept the exact frozen resolution-paper candidate.** The
sufficiency implication in immutable source.md is disproved. Its original
scope is resolved by the stated rational-field counterexample, with
substantive new mathematical value. No change to the claim or decisive
proof files was required. Remaining mathematical gaps: none identified.

This is an actual fresh local review, not external peer review or a
mathematical truth certificate. I read the authorized original statement,
precise interpretation, claim, snapshot and decisive evidence, and actual
primary results. I did not consult checkpoint.md, state.json, earlier job
transcripts or earlier referee/confidence records. The assertions in the
proposer's dossier were treated as claims requiring reconstruction.

## Scope and integrity

All 17 snapshot file hashes and the canonical mapping digest were
independently verified. The unchanged source.md SHA-256 is
688e017d0cb9e92733e81d94a4b79b563f2c44592795597818c63e616df13c0c.

The candidate proves that the exact Example 26 function, the sum of the
positions of the 1 symbols, satisfies the single-ring/single-exponent
antecedent but has no finite-state rational CCRA. The conclusion allows
arbitrarily many registers, rational constants and polynomial copyless
updates, including resets and merges. A counterexample over Q suffices to
disprove the full field-quantified implication; no positive-characteristic
theorem is needed. The status `disproved` refers to sufficiency, while the
source's conjecture of insufficiency is confirmed. The candidate does not
claim a rectangular-polyregular bridge, reversal theorem, or resolution of
another project's problem.

## Reconstruction of the decisive argument

### 1. Linearization and the actual minimal action

Copylessness gives multiaffine coordinate polynomials with pairwise
disjoint variable supports. Substitution into any squarefree monomial
therefore remains multiaffine. Thus the pullbacks B_P preserve the full
2^r-dimensional squarefree space V_r. This permits multiplication updates
and cancellation; it is not a restriction to linear register updates.

The order is consistent: P_uv=P_v composed with P_u and B_uv=B_u B_v.
For output o and initial evaluation lambda, g(w)=lambda B_w o. The spaces
W=span{B_w o} and N={h in W: lambda B_v h=0 for every v} are invariant.
Mapping B_w o to the residual t -> g(tw) has kernel N. This identifies
W/N with the canonical residual representation. In particular a reachable,
observable displayed weighted realization determines its action up to
simultaneous similarity. There is no replacement of a quotient by an
unjustified physical register subspace.

### 2. Image lemma and minimum-rank normalization

For a nonconstant multiaffine q, select an occurring variable and write
q=x_i a+b, with a a nonzero polynomial independent of x_i. Infinitude
of Q allows a rational specialization with a nonzero; solving for x_i
then attains every rational value. Disjoint supports allow this for all
nonconstant coordinates independently. Hence the image of a copyless P
is exactly the coordinate affine space L obtained by fixing its constant
outputs. Restriction followed by injective pullback proves rank B_P=2^k
and ker B_P={h: h restricted to L is zero}.

Choose an actual word e minimizing its number k of nonconstant outputs
over all words, including the empty word. This is an attained minimum
of an integer in [0,r], not a compactness or limiting assertion. For
P=P_e, the map P|_L maps L into itself. The word ee cannot have fewer
than k active outputs, so all k free output coordinates remain
nonconstant on L. On k input variables, k disjoint nonempty output
supports must each contain exactly one variable. Multiaffinity therefore
makes A=P|_L an invertible affine coordinate permutation.

The map Q=A^{-1} composed with P is still copyless, maps onto L and
restricts to the identity there. Its pullback E is a projection. Affine
coordinate changes preserve the squarefree space on L, so im E=im B_e;
both pullbacks have the same kernel, namely restriction-zero on L.
Rank B_e^2=rank B_e proves the direct-sum decomposition into this kernel
and image. If q is the minimal polynomial on the invertible image,
q(0) is nonzero. The polynomial congruences p=0 mod T and p=1 mod q
produce E=p(B_e). These steps justify the rational functional calculus
even when the full register map is singular.

### 3. Why the observable quotient survives

Polynomiality of E ensures that both W and N are E-invariant. The
identity (I-E)B_e=0 descends to (I-E_bar)M_e=0. Invertibility of the
minimal matrix M_e then gives E_bar=I. This is the crucial distinction
between invertibility of the observed action and invertibility of the
physical register map; the latter is never assumed.

On im E, identify V(L) by J(h)=h composed with Q. Then E B_a E is
conjugate through J to pullback by R_a=Q composed with P_a restricted
to L. Direct substitution gives h composed with Q composed with P_a
composed with Q on both sides, confirming the order. The word eae has
physical map A composed with R_a composed with A composed with Q.
Surjectivity of A composed with Q and the outer affine permutation show
that its active output count is exactly the free-coordinate active count
of R_a. Minimality forces this to be k. The same variable-count argument
makes every R_a an invertible affine coordinate permutation.

W'=EW and N'=W' intersect N are invariant under these compressed
operators, and W'/N' -> W/N, h+N' -> h+N, is an isomorphism because
E_bar=I. Thus all minimal letter matrices occur on one common invariant
subquotient of affine-coordinate pullbacks. It would not suffice merely
to compare ranks or different quotients for different letters; the proof
establishes the simultaneous statement needed below.

### 4. Commuting unipotents

Raise each affine coordinate permutation to t=k! when k>0. Its coordinate
permutation disappears, leaving maps alpha_i x_i+beta_i. Split each
coordinate into a translation when alpha_i=1 and a semisimple affine map
when alpha_i differs from 1. The translations for all letters commute in
the same coordinates. The other factors are conjugate by coordinate
translations to diagonal scaling, so their squarefree pullbacks are
semisimple; translation pullbacks are unipotent by the degree filtration.

These are the multiplicative Jordan factors. They are polynomials in
each operator's t-th power (here its spectrum is rational). Consequently
they preserve the two common subspaces defining the subquotient. Their
induced factors remain semisimple and unipotent. If the minimal letter
matrix M_a is unipotent, its powered semisimple factor is identity and
its powered unipotent factor is M_a^t. The latter commute for different
letters, as induced translations. Finally the finite binomial polynomial
M=sum_{j<d} binom(1/t,j)(M^t-I)^j recovers any unipotent d-by-d matrix
in characteristic zero. Hence the original M_a commute. This argument
does not invoke an unchecked algebraic-group image or physical inverse.

### 5. The pumping antecedent

Independently deriving concatenation gives
f(uv)=f(u)+f(v)+|u|c(v), where c counts 1s. For arbitrary u,w,v,

    f(uw^n v)=C+A n+B n(n-1)/2,
    C=f(u)+f(v)+|u|c(v),
    A=f(w)+|u|c(w)+|w|c(v),  B=|w|c(w).

After shifting to n+1, its coefficients are C+A, A+B/2, B/2. They are
all in the one finitely generated subsemiring R=Z[1/2], generated by -1
and 1/2 together with the semiring identities. Constants and n generate
the polynomial using precisely Definition 11 operations. Thus m=1 works
for every triple. Its only exponential base is 1, so every degree's
coefficient sum is in R as well. Empty u,w,v and n=0 are included. The
explicit row-convention weighted representation using A_b^T is correct.
This half is known baseline and contributes no independent novelty.

### 6. Arbitrary finite control is genuinely covered

In a reachable bottom SCC with s states, choose q and a prefix p to it.
Starting at q, append to 0^s a shortest path back to q, and do the same
for 1^s. Each return path has length at most s-1 and stays within the
component. The resulting nonempty words u,v have 1-densities strictly
below and above 1/2. Thus delta=c(v)|u|-c(u)|v| is nonzero.

The two return-block updates, valuation after p and output at q form a
legitimate one-state CCRA for g(z)=f(p h(z)). This uses composition of
the state-dependent updates on the actual return paths, and never encodes
control states in registers or assumes either original letter is a loop.

On column coordinates (f,length,1), the block matrices are

    A_w = [[1,c(w),f(w)],[0,1,|w|],[0,0,1]].

They are unipotent and A_v A_u-A_u A_v=delta E_13. Their displayed
realization of g is minimal: the reachable columns include z_p,
delta e_1, and (A_u-I)z_p, independent since their relevant nonzero
coordinates are respectively 1, delta and |u|. Observable rows include
e_1^T, delta e_3^T and (0,c(v),f(v)), independent since c(v)>0.
These are actual linear combinations of word actions. Transposing to
the row convention preserves minimality, unipotence and noncommutation.
This contradicts the one-state obstruction and excludes every proposed
finite-state Q-CCRA for f.

The cases r=0 or k=0 cause no division or factorial problem: the
compressed squarefree space then has dimension one and cannot have
the three-dimensional minimal witness. All other divisions are by a
proved nonzero affine slope, q(0), t or 2 over Q.

## Independent exact diagnostics

I wrote and ran audit/referee-check.py without importing or running the
proposer's code. It reconstructs squarefree pullbacks by Boolean-grid
interpolation and exact rational arithmetic. Results are saved in
audit/referee-checks.json. Checks passed:

- A different singular nonlinear four-register example, with ambient
  dimension 16, physical pullback rank 4, W dimension 5 and minimal
  quotient dimension 4. Thus a genuine one-dimensional kernel is removed.
  Its explicit projection is 1-(T-1)^2(T-3)^2/9. Projection identity,
  invertible quotient letters and compressed/original agreement were
  checked on the full generated reachable/observable spaces.
- The shifted pumping formula for 148,955 cases: all three words of
  length at most 4 and n in {0,1,2,5,8}, including empty words.
- The row-convention weighted realization for all 511 binary words
  through length 8.
- The return-word construction on all 65,536 complete binary DFAs
  with exactly four labeled states, using actual bottom-SCC sizes.
- The unipotent-root formula in 192 exact cases, dimensions 1–6,
  powers 1,2,6,24, with explicitly generated upper-unitriangular matrices.

These are finite diagnostic checks, not an enumeration of all CCRAs or
a substitute for the universal proof above. Frozen computational files
were left unchanged.

## Novelty and theoretical significance

The independent primary-source inspection and search are recorded in
audit/referee-literature.md, including dates, versions and limitations.
The nearest result is [Mazowiecki–Puch–Smertnig, STACS 2026, Theorem 15
and Section 3.2 / Example 26](https://doi.org/10.4230/LIPIcs.STACS.2026.67).
Its full version's Lemma 50 and Appendix B.4 supply the acknowledged
linearization and pumping baseline. The candidate adds the missing
nonrecognizability theorem for exactly that proposed witness.

The other closest comparison is [Puch–Smertnig, arXiv:2410.03444v2,
Theorem 3.4, Corollary 3.5 and Proposition 9.4](https://arxiv.org/abs/2410.03444).
Their weighted-ambiguity characterization does not exclude noncommuting
upper-unitriangular matrices. It therefore cannot replace the new
copyless-specific compression step. I also checked the relevant journal
structural and separation results of [Mazowiecki–Riveros, JCSS 100 (2019),
Propositions 1–3 and Theorems 1–2](https://criveros.ing.uc.cl/papers/jcss19.pdf).
The semiring-specific growth arguments there do not provide this
rational-field separation.

The new minimum-active-output retraction, its polynomial projection on
the observable subquotient, and the resulting simultaneous unipotent
obstruction constitute a substantive method beyond a routine corollary
of those results. They handle rational cancellation and singular updates,
which a direct invertibility assumption would miss. Combined with the
finite-control reduction, they resolve the precise expressiveness
question rather than merely proving a bounded-register obstruction.

No equivalent resolution was found in the primary-source screen as of
the review date. That statement is bounded to the recorded search and
does not assert exhaustive priority. The theoretical value is a strict
separation between unary pumping information and full copyless streaming
expressibility, together with a reusable structural obstruction. This
passes the project's substantive-innovation requirement; it does not
imply STOC-level selection, acceptance or external endorsement.

## Final decision and handoff

Accept the unchanged claim as a resolution-paper, with original_status
disproved and original_scope_resolved=true. No unresolved mathematical
gap, scope downgrade or substantive proof repair is needed. The paired
innovation assessment is in audit/innovation.json. The required structural
check is run after recording this audit; its separate result concerns
integrity and provenance only. No manuscript/PDF or external submission
was created by this referee job.

Structural validation completed: `release_gate.py check-math` returned
exit code 0 with `ok=true`, binding the accepted report to the unchanged
snapshot and this actual referee job. The final captured invocation is
stored in audit/math-gate.json. This validates structure and provenance,
not mathematical truth.
