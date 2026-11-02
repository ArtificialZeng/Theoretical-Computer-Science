# Primary-source triage and decision

Job: c021-ccrapumping-triage-d79f905080dc. Checked 2026-11-01 UTC.
Decision: advance. Source status: open-supported in the inspected versions;
original_status=unresolved; candidate_kind=none.

## Inspected primary records and bodies

1. Filip Mazowiecki, Antoni Puch, Daniel Smertnig,
   [Pumping-Like Results for Copyless Cost Register Automata and Polynomially
   Ambiguous Weighted Automata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.67),
   STACS 2026, article 67, published 2026-02-25. Official input:
   intake/ccra-official-STACS2026-67.pdf. Read Section 2.2 (model),
   Definition 11/Theorem 15 (p. 67:8), Lemma 25 and Section 3.2/Examples 26-27
   (p. 67:13). Inspected rendered official pages in evidence/official-p08.png
   and evidence/official-p13.png. Necessity is proved; sufficiency is presented
   as a conjectural failure, and the proposed position-sum witness lacks a
   nonrecognizability proof. The coefficient-sum condition is in R.
   In Lemma 13's discussion the algebraic closure has an overbar; it must not
   replace K in the original model. Theorem 28 has a different closure-field
   statement and is not the target.

2. [Full version, arXiv:2502.07356](https://arxiv.org/abs/2502.07356).
   Current primary record lists v2, 2026-01-12, with no later version shown
   on the access date. Read local v2 Section 3.2 and Appendix B.4,
   p. 23:28. The latter supplies the polynomial pumping calculation.
   The source's (1/2)Z-generability implies Z[1/2]-generability; the latter
   is the single finitely generated subsemiring required by the target.

3. Antoni Puch and Daniel Smertnig,
   [Factoring through monomial representations: arithmetic characterizations
   and ambiguity of weighted automata](https://arxiv.org/abs/2410.03444).
   Current record lists v2, 2024-10-29. Inspected local v2 Theorem 3.1,
   Corollary 3.2 (pp. 15-16), Theorem 3.4/Corollary 3.5 (p. 16),
   and Proposition 9.4 (pp. 49-50). These concern invertible representations,
   arithmetic properties, and ambiguity via monomial/block-triangular
   covers. They do not by themselves imply the proposed arbitrary-register
   copyless retraction or exclude noncommuting unipotent CCRA quotients.
   The subquotient/compression step is an additional burden.

4. Mikolaj Bojanczyk and Markus Lohrey,
   [Transducers on Compressed Strings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.170),
   ICALP 2026. Inspected local introduction p. 170:4 and Definition 16 /
   Theorems 17-18 p. 170:9. Rectangular polyregular functions suffice for
   compression compatibility; necessity is left open there. These results
   do not supply a bridge from rectangular output length to full CCRA.
   No adjacent compression question is claimed resolved here.

## Current search scope and limitations

Queried exact title/identifier and combinations of:

* "Pumping-Like Results" "Copyless" sufficient conjecture;
* "sum of the positions" "copyless";
* "copyless cost register" "pumping" "2026" sufficiency;
* "copyless" "nonrecognizability" polynomial automata;
* "copyless" "affine" "unipotent".

The final three searches were restricted to arxiv.org and drops.dagstuhl.de.
Additional broad queries covered pumping sufficiency, positions, and
unipotent automata. Primary results led back to the STACS source. No
equivalent resolution was found in this bounded screen. This is not an
exhaustive literature review or a priority guarantee. Search snippets were
leads; the scope decision uses the primary bodies listed above.

No historical registry exists inside the assigned project. No cross-project
registry comparison was performed under the project-only instruction;
global duplicate screening remains unverified. The supplied shared-mechanism
warning was retained: do not split one eventual discovery into marginal papers.

## Cheapest exact tests and interpretation

Reproducer: python3 evidence/triage_checks.py.
Results: evidence/triage-checks.json. Pure rational/integer arithmetic.

For all words, direct position counting gives the known identity

    f(u w^n v) = C + A*n + B*n*(n-1)/2,
    C = f(u)+f(v)+|u|*ones(v),
    A = f(w)+|u|*ones(w)+|w|*ones(v),
    B = |w|*ones(w).

Indeed, copy j (indexed from zero) of w contributes
f(w)+(|u|+j|w|)*ones(w), and v contributes
f(v)+(|u|+n|w|)*ones(v). Summing proves the identity, including empty words.
Both it and its n+1 shift use only polynomials with coefficients in Z[1/2],
so the EPS generators suffice, with m=1. This reproduces known work.
The script also checked 3,375 triples with each word length at most 3 and
n=0,...,6, both before and after the shift (23,625 paired cases), and 255
weighted-matrix computations through word length 7.

A finite stress check used eight explicit two-register copyless maps
(identity, reset, merge, multiplication, swap, translation, and affine
scaling examples) and every composition of length at most 3: 585 cases,
including 500 singular pullbacks. Their multiaffine pullback ranks equaled
2^(nonconstant output count). This tests one early assertion only. It is
neither an enumeration of all two-register CCRAs nor a certificate for
minimum-rank normalization, observable quotient transfer, group structure,
finite control removal, or nonrecognizability.

## Research admission

Nearest result: the uniform necessary condition and proposed witness in
STACS Section 3.2. Proposed delta: exclude that witness from the full
finite-state polynomial CCRA model using a valid structural obstruction.
Payoff: resolve the explicit insufficiency conjecture and, if correct,
establish a mechanism beyond the known pumping computation. This is a
plausible substantive target, not a significance acceptance.

First bounded research test (one pass, at most 25 minutes): adversarially
audit intake/root-working-proof.md in full, starting by attempting to falsify
Claim A's minimum-rank retraction and invariant-subquotient compression with
singular reset/merge maps. In particular verify E=p(B_e), identity action
on W/N, and E B_a E as pullback of Q composed with P_a restricted to L.
If that bridge survives with a general proof, check the algebraic-group
image and return-word finite-control argument. Stop or revise the route on
an exact counterexample. A failed bridge is not a disproof of the original
sufficiency statement; a finite search without one is not a proof.

No manuscript, mathematical audit verdict, candidate, or release was made.
