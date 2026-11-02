# Current primary-source comparison for revision 2

Researcher: c021-ccrapumping-research-b9b720512ca2. Checked 2026-11-01 UTC
(2026-11-02 local). This is a bounded proposer comparison, not an independent
review, exhaustive priority finding, or a significance certificate.

## Frozen source and original-scope delta

Mazowiecki, Puch and Smertnig, [Pumping-Like Results for Copyless Cost
Register Automata and Polynomially Ambiguous Weighted Automata, STACS
2026, article 67](https://doi.org/10.4230/LIPIcs.STACS.2026.67),
Definition 11, Theorem 15, Section 3.2 and Example 26 were rechecked in
the official local PDF and both official page images. The theorem uses K,
whereas the later ambiguity theorem uses its algebraic closure; the lost
overbars in text extraction do not change our target. Example 26 supplies
the position-sum candidate but leaves non-CCRA expressibility unproved.
The [current arXiv record](https://arxiv.org/abs/2502.07356) still lists
v2, last revised 12 January 2026. Its Appendix B.4 gives the known pumping
calculation; Lemma 50 gives the known squarefree-monomial WA translation.

The submitted difference is the proof of full-model nonrecognizability,
retained in evidence/resolution-proof.md, together with the finite-control
algebra transfer and complete characterization in pass2-proof.md. The
uniform pumping formula itself is prior work. The full rational witness
resolves source.md's implication, rather than merely a restricted sector.

## Journal normal forms: access resolved during this pass

Mazowiecki and Riveros, [Copyless cost-register automata: Structure,
expressiveness, and closure properties, JCSS 100 (2019), 1--29,
DOI 10.1016/j.jcss.2018.07.002](https://criveros.ing.uc.cl/papers/jcss19.pdf).
The working author URL gave the actual 29-page journal PDF. Inspected
Section 3, Propositions 1--3 and Lemma 5, and Section 4, Theorem 1.
Propositions 1--2 provide normal form and reset words. Proposition 3's
growth statement requires a non-zero semiring and a non-zero automaton;
these assumptions cannot be imported into Q with cancellation. Theorem 1
excludes Fibonacci over N, and Section 5's reversal separation is max-plus.
These do not establish the proposed rational minimal-subquotient
commuting-unipotent characterization. The new projection handles singular
physical maps and cancellation without those positivity assumptions.
The conference version was also read at its author-hosted URL
[STACS 2016 full text](https://fmazowiecki.github.io/papers/copyless2.pdf).
Failed access to the obsolete journal-host URL remains recorded separately;
it is no longer a journal-body access gap. No claim of exhaustive inspection
of every journal proof is made.

## Nearby matrix and register algorithms

Puch and Smertnig, [Factoring through monomial representations: arithmetic
characterizations and ambiguity of weighted automata](https://arxiv.org/abs/2410.03444),
current record v2, 29 October 2024. Rechecked the local full version,
Theorem 3.4, Corollary 3.5 and Proposition 9.4. They concern invertible
representations and monomial/block-triangular covers characterizing
ambiguity. A noncommutative upper-unitriangular pattern representation
already has one-dimensional monomial diagonal blocks. Those criteria
therefore do not exclude it from polynomial ambiguity or establish the
copyless obstruction; the new proof does not invoke them as dependencies.

Benalioua, Lhote and Reynier, [Minimizing Cost Register Automata over a
Field, MFCS 2024, article 23](https://doi.org/10.4230/LIPIcs.MFCS.2024.23).
Read the actual official PDF's abstract, introduction and Section 2 model.
Its main bounds concern minimization for linear/affine CRA, allowing
arbitrary linear combinations. Their efficient WA minimization is known
background here. Its register/state minimization result does not impose
global copylessness or decide existence of an arbitrary-register polynomial
copyless realization. The [current full-version record](https://arxiv.org/abs/2307.13505)
still lists v2, revised 28 June 2024. The present commutator and trace
tests, rational linear algebra, scattered-embedding WA, symmetrization and
falling-factorial counter construction are routine tools, not separate
novelty claims.

## Current search limits and proposed substantive value

Queries covered copyless with unipotent, commutative, Parikh, scattered,
subword, polynomial growth, polynomial in counts and binomial; plus the
exact source title. The current primary author publication pages of
[Mazowiecki](https://fmazowiecki.github.io/papers.html) and
[Smertnig](https://math.smertnig.at/publications.html) were rechecked.
No equivalent resolution or characterization was identified in these
bounded primary leads. Absence of search results is not a proof of novelty.
Unsearched literature and alternative deductions remain possible.

The proposed nonroutine step is retaining the FULL minimal weighted
algebra after passage to common control return words: polynomial unipotent
roots recover each sandwiched letter, while the actual prefix acts as a
unit. This extends the one-witness finite-control argument to every
all-word-unipotent rational recognizable function. In conjunction with the
singular-map minimum-rank obstruction it rules out every finite-state
polynomial copyless realization of noncommutative functions in this
sector, and yields a polynomial-bit membership algorithm with constructive
YES and short NO evidence for explicit scattered-pattern inputs. It is
submitted as one strengthening of the original full resolution. A fresh
referee must decide whether this delta is correct, new and theoretically
significant; standard algorithms alone would not justify publication.
