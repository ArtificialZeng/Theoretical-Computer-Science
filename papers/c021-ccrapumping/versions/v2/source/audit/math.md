# Fresh mathematical review

Job: `c021-ccrapumping-referee-a7ba97c08c76`.
Review date: 2026-11-01 UTC / 2026-11-02 Asia/Shanghai.
Frozen snapshot: `c56f3440ebba4e41358a93f526e776e26091d3e07c234d06ecd41eb565a274b0`.

**Verdict: accept the exact combined resolution-paper claim.** The sufficiency
implication in immutable `source.md` is disproved. The rational position-sum
function satisfies its complete uniform antecedent and has no finite-state
polynomial rational CCRA of any finite register count. The accompanying
all-word-unipotent characterization and the stated explicit-pattern algorithms
also pass. This is this job's mathematical assessment, not external peer review,
a truth certificate, a venue decision, or permission for external submission.

## Scope and independence of this pass

I read `source.md`, `problem.md`, `claim.json`, the snapshot and its enumerated
inputs, and current primary sources needed for the comparison below. The
required project instructions and outer-root note were read as instructions
and adverse-check prompts, not as mathematical verdicts. I did not consult
checkpoint/state files, earlier job transcripts, earlier audit reports, or
historical manuscript/release files. No other agent or model process was used.

All 22 snapshot file hashes and its canonical mapping digest were independently
recomputed and matched. The original source digest remains
`688e017d0cb9e92733e81d94a4b79b563f2c44592795597818c63e616df13c0c`.
No frozen input was edited. The submitted research diagnostics were read as
finite evidence, not as acceptance or a substitute for the following proof.

The accepted scope includes arbitrary deterministic complete finite control,
arbitrary rational constants and any finite register count, singular/reset/merge
maps, and nonlinear syntactically copyless polynomial updates and outputs.
There is no physical-invertibility, positivity, one-state, bounded-register,
positive-characteristic, general-membership, or rectangular-length assumption
silently added to the original resolution. The extension is explicitly over Q
and requires every word matrix of a minimal representation to be unipotent.

## Reconstructed compression argument

Let V be the space of squarefree register monomials, including 1. A copyless
tuple has multiaffine coordinate polynomials with disjoint variable supports.
Products of distinct coordinates consequently stay multiaffine. Thus pullback
T_P(h)=h composed with P preserves V, including when coordinates disappear by
cancellation. Copyless composition follows by substituting expressions that
have disjoint supports. The reachable polynomial space W and its unobservable
subspace N in the dossier are invariant. Their quotient is the minimal weighted
representation: mapping a polynomial to its evaluations after all prefixes
identifies its kernel with N and identifies the quotient with residual functions.
The order T_uv=T_u T_v is consistent with reading uv and the row convention.

A nonconstant multiaffine polynomial over Q is onto Q. In a genuinely occurring
variable write it as ax+b, specialize the remaining variables so the polynomial
a is nonzero, and solve the resulting linear equation. Infinitude of Q supplies
that specialization. Disjoint supports allow simultaneous independent choices
for different output coordinates. Therefore a copyless map P maps onto the
coordinate affine space L determined by its constant coordinates. If k outputs
are nonconstant, its pullback has rank 2^k, and its kernel consists exactly of
polynomials vanishing on L. These assertions concern polynomial maps, not just
values reached from the automaton's initial valuation.

Choose a word e with the minimum number k of active output coordinates. The
outer P_e fixes the same constant coordinates in P_e squared. Its active count
cannot fall below k. Hence the restriction A=P_e|L has k nonconstant coordinates
on k variables. Disjoint supports force each output to use one distinct input;
multiaffinity makes it an affine coordinate permutation with nonzero slopes.
This proves invertibility only on L. It does not assert invertibility of P_e.

Normalize to the copyless retraction Q=A^{-1}P_e onto L and set E=T_Q.
Surjectivity onto L gives equal kernels for T_Q and T_e. Affine changes of the
free output coordinates give equal images. Since Q fixes L, E is the projection
onto im T_e along ker T_e. Equivalently rank T_e squared equals rank T_e, so
the zero-primary part is just the kernel. The polynomial Chinese remainder
construction, with p=0 modulo X and p=1 modulo the nonzero-primary minimal
polynomial, gives E=p(T_e).

This polynomial identity is the essential subquotient safeguard: W and N are
E-invariant. If M_e on W/N is invertible, (I-E)T_e=0 implies that E induces
identity on W/N. This step does not transfer invertibility to the physical map.

Under the restriction/extension isomorphism between V(L) and im E, E T_a E is
pullback by R_a=Q composed with P_a restricted to L. The identity follows by
substitution in the order h composed with Q composed with P_a composed with Q.
The actual word eae has map A composed with R_a composed with A composed with Q.
Surjectivity of the inner map onto L and the outer coordinate permutation show
that a lost active coordinate in R_a would contradict minimum rank. Thus each
R_a is also an affine coordinate permutation. The spaces EW and EW intersect N
are invariant under all compressed operators; their quotient maps isomorphically
to W/N and retains exactly the original minimal letter action. This closes the
possible observable-subquotient gap.

## Reconstructed unipotent obstruction

Take a common power t=k! to remove the coordinate permutations. Each resulting
coordinate map is x_i -> alpha_i x_i+beta_i. Its unipotent factor is translation
by beta_i exactly on coordinates where alpha_i=1, and identity on the others.
All these translation factors, for all letters, commute in the same coordinates.
The complementary factors are semisimple: on coordinates with alpha_i not equal
to 1, the variable x_i+beta_i/(alpha_i-1) is a scaling eigenvariable. Products of
such variables diagonalize their pullbacks on squarefree polynomials.

These are the commuting multiplicative Jordan factors of each powered
pullback. The factors are polynomial functions of that operator, obtained by
interpolation on generalized eigenspaces. Their rationality here also follows
from the rational scaling eigenvalues. They therefore preserve the same two
invariant spaces and descend to the subquotient. Semisimplicity and unipotence
are preserved on invariant subquotients. When its induced matrix M_a is
unipotent, the semisimple factor becomes identity and the induced translation
factor equals M_a^t. Hence the M_a^t commute. Finally the finite binomial
polynomial for the unipotent t-th root expresses M_a in M_a^t-I over Q. The
M_a themselves commute. The k=0 case has at most one-dimensional ambient
space and causes no exception.

This proves the submitted one-state obstruction for all registers and singular
physical maps. No assertion about the image of an algebraic group is needed.

## Finite control and the exact original counterexample

The extension's finite-control transfer is valid. In a reachable bottom SCC
choose a minimum-rank word transformation t with image size r. Rank stability
of t squared means t permutes its image. Therefore e=t^(r!) is identity on
its image R. Each eae maps R bijectively to R: its image on the whole SCC
equals its image on R, lies in R, and has size at least r. Consequently
h_a=(eae)^(r!) and h_*=e are common return words at any chosen q in R.
There is an actual prefix p from the initial state to q.

Let A denote the unital algebra of the original minimal matrices. The block
machine has matrices M_e and (M_e M_a M_e)^(r!), and initial row lambda M_p.
Every one of these matrices, the sandwiched M_e M_a M_e, and M_p is unipotent
under the stated all-word hypothesis. The algebra B of the block matrices
contains M_e^{-1}, and the finite polynomial root of each powered sandwich.
Thus M_a=M_e^{-1}(M_e M_a M_e)M_e^{-1} lies in B and A=B. Both directions of
this algebra inclusion are explicit. Also M_p is a unit of A, so lambda M_p B
is the entire original reachable row space, while B gamma is the entire
original observable column space. The block realization is genuinely minimal
in the original dimension. The one-state obstruction makes its generators
commute, whence B, A and the original letter matrices are commutative.
This argument does not replace the original control graph by a one-state
machine without proving preservation of its minimal algebra.

For the position-sum witness, a rational weighted realization has transposed
letter matrices of [[1,b,b],[0,1,1],[0,0,1]], b in {0,1}. Every word matrix is
unipotent. Its values on 01 and 10 are respectively 2 and 1. The proved
finite-control theorem therefore forbids a CCRA. Independently, Section 7 of
the baseline proof gives return words of different 1-densities at a bottom
SCC state. Their block commutator is a nonzero multiple of E_13. The displayed
reachable vectors and observable covectors span dimension three because the
return word has positive length, the 1-rich word contains a 1, and their
density determinant is nonzero. This is a valid second full-control reduction.

For all u,w,v, put l=length, c=number of 1s, and let f be the position sum.
Concatenation gives f(uv)=f(u)+f(v)+l(u)c(v), and summing the copies gives

    f(uw^n v)=C+A n+B n(n-1)/2,
    C=f(u)+f(v)+l(u)c(v),
    A=f(w)+l(u)c(w)+l(w)c(v),   B=l(w)c(w).

After replacing n by n+1 all coefficients lie in the single subsemiring
Z[1/2], finitely generated by -1 and 1/2. Constants and n, with pointwise
sum/product, generate these sequences exactly, from n=0 onward. Thus m=1 works
for every triple, including empty words. The only exponential base is 1, so
every coefficient sum is in the same R; degrees above two give zero. This
meets the immutable quantifier order. Enlarging the source's generating set
(1/2)Z to a genuine subsemiring is legitimate, and not a weakening of the
antecedent. A single rational counterexample disproves the full sufficiency
implication over fields.

## Extension and algorithm audit

Within the all-word-unipotent minimal sector, commuting letters yield a
polynomial in the counts by the finite expansion (I+N_a)^m. Permutation
invariance forces every contextual commutator scalar to vanish; minimal
reachability and observability force the matrix commutator itself to vanish.
Conversely, any fixed rational polynomial in the counts has a copyless
construction by separate counter registers for every occurrence in its
monomials. Thus all four equivalences have their stated directions. The
construction does not promise polynomial size for compact arbitrary matrices.

The promise test is also correct: all word matrices are unipotent iff every
word trace equals the minimal dimension d. To prove the reverse implication,
apply the universal trace condition to the first d powers of each fixed word;
Newton identities and Cayley-Hamilton give (M_w-I)^d=0. The invariant span of
(vec(M_w),1), dimension at most d^2+1, decides that universal linear trace
condition. Its retained actual-word basis has length at most d^2. It is
essential to minimize first; an invisible eigenvalue 2 would otherwise
incorrectly reject the intrinsic promise. Polynomial word lengths and the
usual common-denominator and minor bounds justify polynomial bit complexity,
not merely polynomial arithmetic complexity. Pairwise commutator testing in
the promised sector is an established linear-algebra tool, now deciding CCRA
realizability because of the structural theorem above.

For explicit patterns, the direct-sum upper-unitriangular representation is
correct even for adjacent equal pattern letters: one input letter advances
at most one edge of a run. Unipotence passes to a minimal subquotient. Basis
rows and columns with words of length at most D-1 make contextual commutator
testing complete, giving the advertised equal-Parikh NO witnesses of length
at most 2D. Matrices count embeddings; along words of polynomial length their
entries and the needed rational minors have polynomially many bits.

On YES, sorting the input kills every unsorted pattern and gives the product
of binomial count polynomials for each sorted one. Separate registers with
initial values -j and letter increments evaluate their falling factorials.
Each register appears only in its own update and one final product. Register
count is at most the sum of the listed pattern lengths, and factorial
denominators and the explicitly listed updates have polynomial encoding size.
Repeated patterns, signed rational cancellations, empty patterns, zero and
the empty alphabet cause no division or domain problem. Zero and empty input
lists are handled separately as claimed. No general CCRA-membership algorithm
or efficient general compact synthesis has been inferred.

## Independent finite checks actually executed

`audit/referee_check.py` uses only Python's exact Fraction arithmetic and no
submitted program imports. `audit/referee_check.json` records its results:

* A different five-register singular nonlinear family, ambient squarefree
  dimension 32 and physical rank 8, was reconstructed by Boolean-grid
  evaluations and Mobius inversion. The nonzero-primary polynomial
  (T-1)^3(T-2)^3 gives the retraction 1-(T-1)^3(T-2)^3/8. Idempotence,
  rank stability and identity/compression on an actual observable quotient
  of dimension 8 all passed.
* All 746 complete binary controls on one through three states passed the
  idempotent-image, common-return-word and polynomial-root recovery checks
  in a rational four-dimensional noncommutative unipotent realization.
  Actual prefix multiplication retained full row and column spans.
* 163 signed rational ternary pattern inputs, maximum pattern length four,
  were checked at all 121 words through length four: 19,723 direct value
  evaluations. The independent coefficient-class criterion agreed with
  the observed permutation invariance; all YES sorted/binomial formulas
  matched. There were 60 YES and 103 NO cases.
* The explicit trap I+E_12, I+E_21 has individually unipotent letters but
  trace(AB)=3 in dimension two. It confirms why the extension's all-word
  promise cannot be weakened to testing just letters.

These are finite diagnostics with those exact bounds. The universal claims
are accepted on the mathematical reconstruction above, not on enumeration.

## Current primary comparison and contribution assessment

The official STACS PDF's model page and both supplied page images were
inspected, recovering K versus its algebraic closure accurately. Its Definition
11, Theorem 15, Section 3.2 and Example 26 establish the necessary condition
and propose the same unresolved witness. The current arXiv record still has
v2 (12 January 2026); Appendix B.4 supplies the pumping calculation and
Lemma 50 the squarefree translation. Those ingredients are prior work.
[Mazowiecki--Puch--Smertnig, STACS 2026](https://doi.org/10.4230/LIPIcs.STACS.2026.67),
[current full-version record](https://arxiv.org/abs/2502.07356).

The journal normal forms and reset analysis do not by themselves provide the
present cancellation-safe observable compression. In particular Proposition 3
and Lemma 5 require a non-zero semiring, an assumption unavailable over Q with
arbitrary signs. They cannot be imported as rational no-cancellation results.
[Mazowiecki--Riveros, JCSS 100 (2019), Sections 3--4](https://criveros.ing.uc.cl/papers/jcss19.pdf).

Theorem 3.4, Corollary 3.5 and Proposition 9.4 concern invertible weighted
representations and block-triangular monomial covers. Noncommuting
unitriangular pattern matrices already have monomial diagonal blocks, so
these results do not imply the CCRA obstruction. The current record remains
v2 (29 October 2024).
[Puch--Smertnig, arXiv:2410.03444](https://arxiv.org/abs/2410.03444).

Clemente's Introduction explicitly gives polynomial-time rational-series
commutativity via minimal matrices; Theorem 1 gives a broader effective-
prevariety decision result. Its current record remains v2 (16 May 2025).
This existing algorithm is credited, and is not the mathematical innovation
accepted here. It does not assert that permutation invariance characterizes
copyless realizability in the all-word-unipotent sector.
[Clemente, LICS 2025 full version](https://arxiv.org/html/2503.21697v2).

I additionally checked the current official 2026 follow-up: Theorem 1 and
Corollary 2 classify bilinear associative commutative product rules; Theorem 3
decides equivalence of the corresponding polynomial P-automata, and Section
1.2 discusses series commutativity. These concern products of series and
equivalence/commutativity, and do not give the submitted CCRA-realizability
transfer. No copyless theorem was found in that inspected official text.
[Clemente, Commutative Algebras of Series, LICS 2026](https://doi.org/10.4230/LIPIcs.LICS.2026.29).

The MFCS 2024 official abstract confines its minimization results to linear
and affine CRA; it does not assert arbitrary polynomial copyless realizability.
[Benalioua--Lhote--Reynier, MFCS 2024](https://doi.org/10.4230/LIPIcs.MFCS.2024.23).

Current searches included copyless with unipotent, commutative, Parikh,
scattered subword, and position-sum/counterexample terms, the exact source
title, and the current primary author publication pages of
[Mazowiecki](https://fmazowiecki.github.io/papers.html) and
[Smertnig](https://math.smertnig.at/publications.html). No equivalent resolution
or realizability characterization was identified in this bounded screen.
This is not an exhaustive priority assertion; the inspected sources and
their precise differences are the basis of this contribution assessment.

The substantive delta is the singular-map minimum-rank retraction with
faithful observable-subquotient compression, the consequent commuting-
unipotent obstruction, and recovery of the whole minimal algebra through
finite-control return blocks. This supplies a full proof of nonrecognizability
for a witness expressly left open by the source and a characterization of an
infinite recognizable sector. The efficient constructive explicit-pattern
membership result is a useful consequence of that structural distinction.
The known trace/commutator tests, symmetrization and counter evaluation alone
would not warrant acceptance. The structural work is nonroutine and has
substantive expressiveness and realizability value beyond a toy restriction.

Remaining mathematical or scope gaps identified in this pass: none.
The acceptance is limited to the exact frozen combined claim and its stated
rational hypotheses. The required structural/provenance check is recorded
separately in `audit/check-math-referee.json`; it is not mathematical evidence.
