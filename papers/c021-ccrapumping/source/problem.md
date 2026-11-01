# Precise interpretation of the frozen question

Job: c021-ccrapumping-triage-d79f905080dc. Phase: triage, 2026-11-01.
The original statement is source.md, unchanged; its SHA-256 is
688e017d0cb9e92733e81d94a4b79b563f2c44592795597818c63e616df13c0c.

## Objects and quantifiers

For every field K, finite alphabet Sigma, and weighted-automaton recognizable
function f:Sigma* -> K, consider this implication:

There exist a finitely generated subsemiring R of K and an integer m >= 1
such that, for every triple u,w,v in Sigma*, the entire sequence

    h_{u,w,v}(n) = f(u w^{m(n+1)} v), n = 0,1,2,...

is R-generable in Definition 11. Does this imply that f is recognizable by
a copyless polynomial cost register automaton over K?

The quantifier order is exists R, exists m, for all u,w,v. R and m may depend
on f, but cannot depend on the triple. Empty words are allowed, including w.
The conclusion allows any finite number of states and registers and any
constants in K; it does not require the same R. A negative answer requires
one field/function satisfying the antecedent and violating the conclusion.
A positive answer must cover the entire quantified model. The source's
insufficiency conjecture is the negative answer to this implication.

Weighted-automaton recognizable means that there exist a finite dimension d,
row I, column F, and matrices M_a over K such that
f(a_1...a_l)=I M_{a_1}...M_{a_l} F, with the empty product the identity.

An R-generable EPS is in the closure under finitely many pointwise sums and
products of the following K-valued sequences indexed by n >= 0:

* constants alpha in R;
* n times 1_K;
* alpha^n for alpha in R;
* (alpha^n-1)/(alpha-1) for alpha in R with alpha != 1, equivalently the
  geometric partial sum with n terms (zero at n=0).

This is the generation definition, not a replacement by an eventual
asymptotic formula. In characteristic zero also retain the source's condition
that every degree-k coefficient sum S_k belongs to R. Namely, in the
exponential-polynomial normal form sum_lambda q_lambda(n) lambda^n,
S_k is the sum over lambda of the coefficients of n^k in q_lambda.
Lemma 25 derives this condition from R-generation; it is not omitted.

A CCRA has deterministic complete finite control, a fixed finite register
tuple in K^r, state/letter dependent polynomial updates, an initial valuation,
and a state dependent scalar polynomial output. Every update tuple and every
output has a sum/product expression in which each old variable occurs at most
once in total. This is syntactic copylessness across all coordinates, not
just multilinearity of each coordinate. Updates may reset, merge, multiply,
permute, and use negative constants when K permits. No linearity, physical
invertibility, fixed register bound, sign constraint, or one-state restriction
is imposed on the original question.

## Proposed witness and nearest prior results

For K=Q and Sigma={0,1}, Example 26 is
f(w)=sum of the 1-symbol positions, positions starting at 1. The proposed
resolution is to prove that this exact function has no CCRA in the full model.
Its weighted representation and pumping property are already known baseline.
One may use R=Z[1/2] (generated as a semiring by -1 and 1/2) and m=1.
The source's set (1/2)Z in Example 26 is not itself a subsemiring; enlarging
it to Z[1/2] supplies the required single finitely generated subsemiring.
Example 27, the sum of 2^position, is CCRA recognizable and is a control.

Mazowiecki, Puch, Smertnig, STACS 2026, Theorem 15, pp. 67:8 and 67:13,
proves necessity. Section 3.2/Examples 26-27, p. 67:13, explicitly leaves
the converse unresolved. Full version arXiv:2502.07356v2, Appendix B.4,
p. 23:28, proves the witness's pumping calculation.

Puch and Smertnig, arXiv:2410.03444v2, Theorem 3.4/Corollary 3.5 and
Proposition 9.4, characterize invertible weighted representations via
block-triangular monomial covers for polynomial ambiguity. These are not
CCRA characterizations. The proposed independent delta is a valid
minimum-rank compression obstruction for arbitrary-register CCRA, followed
by removal of finite control. No such delta is established at triage.

Bojanczyk and Lohrey, ICALP 2026, Theorems 17-18, concern rectangular
polyregular functions and compression. No bridge from those results to the
present full CCRA question is assumed. See evidence/literature-triage.md.

## Admission and verification route

Source status: open-supported by the inspected primary versions, with a
bounded current search finding no equivalent resolution; not a priority
certificate. Suitability: advance to a bounded research audit. A full proof
would settle an explicitly stated expressiveness conjecture; significance
and originality remain subject to fresh review.

First research test: adversarially audit intake/root-working-proof.md,
starting with singular reset/merge maps and their invertible observable
quotients. Establish or falsify the minimum-rank retraction E, its polynomial
functional calculus and invariant-subquotient action, and the compressed
affine-coordinate maps before using the algebraic-group obstruction. Then
check the finite-control return-word argument without restricting the source
model. Finite searches cannot prove the all-register statement.

Only a complete substantively new original-scope resolution may become a
candidate. At triage candidate_kind=none; original_status=unresolved.

## Research pass 1: proposed full-scope resolution awaiting fresh referee

Job c021-ccrapumping-research-44e54bf7c116, 2026-11-01 UTC. The exact
original objects and quantifiers above are unchanged. A complete proposed
counterexample proof for the original Example 26 is now in
evidence/resolution-proof.md, with supplementary exact adversarial checks
in evidence/research_checks.py and evidence/research-checks.json and a
current primary-source comparison in evidence/literature-research.md.

The proof justifies the minimum-rank retraction and observable-subquotient
transfer, then replaces the proposed algebraic-group-image step by an
elementary Jordan-factor argument: powers of the compressed coordinate
permutations have commuting translation unipotent parts. It removes finite
control through two return words at a reachable bottom SCC state, and
proves both reachability and observability of the noncommuting unipotent
three-dimensional realization. Physical maps remain allowed to be singular.
The rectangular bridge remains unused and outside the claim.

The resulting claim.json requests review as resolution-paper with
original_status=disproved, referring to the sufficiency implication.
It does not represent independent acceptance. No manuscript/PDF is
authorized before the required fresh correctness, novelty and significance
review and actual check-math gate. The easy pumping formula and standard
CCRA-to-WA translation remain explicitly attributed to prior work.
