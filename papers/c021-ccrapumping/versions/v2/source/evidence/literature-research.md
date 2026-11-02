# Current primary-source comparison for research pass 1

Job c021-ccrapumping-research-44e54bf7c116. Checked 2026-11-01 UTC.
This is the proposer's bounded novelty screen, not an independent novelty
or significance verdict. The prior triage record remains unchanged.

## Nearest source and precise difference

Filip Mazowiecki, Antoni Puch and Daniel Smertnig,
[Pumping-Like Results for Copyless Cost Register Automata and Polynomially
Ambiguous Weighted Automata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.67),
STACS 2026, article 67, DOI 10.4230/LIPIcs.STACS.2026.67.
The official local input is intake/ccra-official-STACS2026-67.pdf.
Rechecked its model, pp. 67:7-8, and Section 3.2/Example 26, p. 67:13.
Both stored official page images were visually inspected again in this job.
Theorem 15 uses K, while Theorem 28 uses the algebraic closure in its
different assertion. No overbar is silently discarded in our target.

The [current arXiv record](https://arxiv.org/abs/2502.07356) still lists
v2, revised 12 January 2026. The local full version is
intake/ccra-2502.07356v2.pdf. Its Lemma 50/Appendix B.1 is the standard
squarefree-monomial translation to weighted automata; Appendix B.4 is
the known pumping calculation for Example 26. Those facts are explicitly
prior work in our proof. The official Section 3.2 leaves nonrecognizability
of the position-sum function unproved.

Proposed substantive difference: Sections 2-5 of resolution-proof.md justify
minimum-active-output normalization of arbitrary singular copyless maps
on the common invariant observable subquotient. Their elementary Jordan
argument excludes noncommuting unipotent minimal letters in every one-state
CCRA. Section 7 applies this obstruction after arbitrary finite control by
two return words with different 1-densities. This supplies the missing
nonrecognizability half of the exact source Example 26. It is a complete
counterexample to the original sufficiency implication, not a finite
register lower bound or a new presentation of the known pumping formula.

The minimum-rank route was supplied in intake/root-working-proof.md as
prospective evidence. This job completed its projection/subquotient
justification and replaced the proposed group-image argument by a
finite-dimensional Jordan-factor argument. No independent external review
of that route has occurred.

## Other primary comparisons

Antoni Puch and Daniel Smertnig,
[Factoring through monomial representations: arithmetic characterizations
and ambiguity of weighted automata](https://arxiv.org/abs/2410.03444).
The current record still shows v2, 29 October 2024. Rechecked local
intake/monomial-2410.03444v2.pdf, Theorem 3.4/Corollary 3.5 (p. 16) and
Proposition 9.4 (pp. 49-50). These characterize invertible representations
and polynomial ambiguity via block-triangular monomial covers. They neither
give the copyless minimum-rank retraction used here nor imply that arbitrary
unipotent minimal letters of a CCRA commute. In particular UT_3 matrices
already have monomial one-dimensional diagonal blocks, so merely invoking
their cover criterion would not exclude our witness. None of those
theorems is a dependency of the proposed proof.

Filip Mazowiecki and Cristian Riveros,
[Copyless Cost-Register Automata: Structure, Expressiveness, and Closure
Properties](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.53),
STACS 2016, article 53, DOI 10.4230/LIPIcs.STACS.2016.53.
Read its structural discussion (Section 3, pp. 53:5-7), the extra assumptions
before Proposition 7, and Theorem 8 (pp. 53:8-9). The separation there is
for a max-plus function and uses that setting's growth argument. It is not
the rational-field position-sum theorem. The 2026 source cites the 2019
JCSS journal version, DOI 10.1016/j.jcss.2018.07.002; that journal version
was not separately read in this job. Do not infer an exhaustive comparison
with that version from the conference-body inspection.

[Minimizing Cost Register Automata over a Field](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2024.23),
Yahia Idriss Benalioua, Nathan Lhote and Pierre-Alain Reynier, MFCS 2024,
article 23, DOI 10.4230/LIPIcs.MFCS.2024.23, was additionally screened at
the publisher's abstract level. It concerns linear/affine register
minimization, and was not used to infer any claim about unrestricted
copyless polynomial realizability. Its body was not audited here.

For the linear-algebra background only, primary course notes by
[J. S. Milne, Algebraic Groups, Section 11](https://www.jmilne.org/math/CourseNotes/iAG200.pdf)
and [MIT 18.737, Theorem 12.4](https://www.mit.edu/~NivenT/assets/pdf/18_737_Notes.pdf)
were checked for preservation of multiplicative Jordan decomposition.
The actual proof dossier gives the needed polynomial-factor argument,
so neither algebraic-group homomorphisms nor these notes are dependencies.

## Current search scope, adverse checks and limits

The current primary search covered exact title and identifier; position
sum/positions with copyless; copyless with noncommuting, unipotent, Jordan,
minimal rank, minimum-rank, affine coordinate, polynomial automata,
sufficiency and reversal; and the nearby field-minimization title.
No equivalent proof or resolution was found in those bounded searches.
Search results alone were not used to certify theorem scope.

The authors' current publication pages were inspected:
[Mazowiecki](https://fmazowiecki.github.io/papers.html) lists the STACS 2026
paper and later work, and
[Smertnig](https://math.smertnig.at/publications.html), last changed
16 October 2026, lists the source and monomial-representation preprint.
No equivalent follow-up was identified on those pages. These are useful
current primary indexes, not proof that no other paper exists.

No historical/global registry was available within this assigned project;
no other project or queue state was edited. The adjacent rectangular
polyregular/compression question in the supplied handoff remains outside
the claim, with its bridge unaudited and unused.

Why this is submitted as potentially substantive: if correct and new, the
argument resolves an explicitly posed 2026 expressiveness problem in its
full model and produces a reusable observable-quotient obstruction that
survives singular register maps. The known EPS computation alone would
have no such value. Current novelty and significance still require the
fresh referee's own reasoned assessment; neither is certified by this file.
