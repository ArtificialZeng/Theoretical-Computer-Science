# Current primary-source check, research pass 1

Job c034-group3sum-research-3974e7a3f8f0. Actual check 2026-11-02 UTC,
approximately 16:08-16:19. Bounded comparison, not a global priority certificate.

* Ruhollah Majdoddin, arXiv:2610.17420v1, exact frozen PDF/text in intake/primary/.
  Rechecked Model, Theorem 19.17 embedding, both light/heavy proofs and their
  complete operation accounting, Lemmas 19.6-19.7, Definition 2.1/Lemma 2.2,
  and Open Problem 19.26/Remark 20.6. Existing p^2 and elementary-group algorithms
  are prior; Z4^d x F2^d is already covered. Source proposes layer induction,
  which itself cannot be claimed as our contribution.
* Live primary record https://arxiv.org/abs/2610.17420 still showed v1 only.
  Live author primary README at
  https://raw.githubusercontent.com/Majdoddin/formal-math/main/groups/README.md
  still describes the p^2 scope, not all bounded exponents; inspected preserved
  intake/Majdoddin-groups-current-README.md as well. No new repository-tree
  audit or Lean build was performed. Lack of formalized running time is not
  a reason to reopen an existing prior theorem.
* Josh Alman and Virginia Vassilevska Williams, arXiv:2610.06783v1,
  https://arxiv.org/html/2610.06783v1 Section 4.1, Corollary 26, inspected
  directly. Its input dimensions, entry-size restriction, preprocessing and
  query bounds imply the exact Hdet(1/18,0.063) interface used here on 0/1
  matrices. Local complete downloaded primary HTML:
  intake/primary/2610.06783v1.html. Checked theorem extraction:
  intake/primary/2610.06783v1-corollary26.txt. This independently verifies the
  cited theorem's actual statement, not a full reproof of its matrix algorithm.

Bounded searches included '3SUM bounded exponent abelian groups',
'3SUM Majdoddin Z8', '3SUM divisor bounded exponent',
'3SUM abelian randomized 2026', 'Majdoddin 19.26',
'3SUM bounded exponent randomized', '3SUM Z_8 F_2', and exact variants.
No primary full-scope equivalent was located. Nonprimary results were leads
only and support no novelty or correctness assertion. Unsearched unindexed
work, unpublished work, and a complete citation-network review remain limits.

Proposed substantive difference: the source's suggested per-layer induction is
replaced by simultaneous original-coset divisor-size profiles and a discrete
maximum-slope certificate selecting the quotient AND row count. This reduces
all nonzero order layers to one elementary p-middle product, handles fragmented
profile cosets, and pays for all polylogarithmically many list subinstances.
Randomized caps replace computable exact counting potentials. This is a proposed
general algorithmic method beyond the source's p^2 scopes, not a proof that it
is novel, accepted or STOC competitive. A fresh referee must decide correctness,
nonroutine value and venue significance independently.
