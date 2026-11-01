# Current primary literature screen, 1 November 2026

This record supports a candidate proposal, not a claim of exhaustive priority
verification. The source question is unchanged. The actual source question
and all quantifiers are in `source.md` and `problem.md`.

1. Fillmore, Goeckner, Kirsch, Martin and McGinnis, *The existence and structure
   of universal partial cycles*, Designs, Codes and Cryptography 94, article
   152 (4 July 2026), DOI 10.1007/s10623-026-01841-x.
   Primary full text: https://link.springer.com/article/10.1007/s10623-026-01841-x
   Reopened actual publisher text. Question 9.2 asks existence with d>1;
   Remark 6.6 says that case is open. Theorem 3.1 gives n8d1 examples;
   Theorem 5.1/Corollary 5.2 preserve d under alphabet multiplication.
   Theorem 8.2 constrains frame period; Corollary 8.14 permits the period-four,
   n12d3 frame. The paragraph after Question 9.2 raises n not dividing length,
   which the present 512-character n12 witness also realizes.

2. The same authors, arXiv:2310.13067, current record:
   https://arxiv.org/abs/2310.13067
   Reopened record reports v3, 14 April 2025, as latest revision. The downloaded
   source input remains in `intake/paper.pdf`, with extracted text alongside it.
   No later arXiv version was observed.

3. Carey, Kearney, Kirsch and Popescu, *Universal partial tori*, Designs, Codes
   and Cryptography 93, 2803–2822 (2025), DOI 10.1007/s10623-025-01609-9.
   https://link.springer.com/article/10.1007/s10623-025-01609-9
   Reopened primary text and Section 9's statement about the known
   diamondicity-one examples. Section 8 already studies quasi-families.
   Multiple closed components are prior objects and do not resolve upcycle
   existence. The proposed contribution here is the single-cycle d3 witness.

4. Rachel Kirsch's current publication page:
   https://mason.gmu.edu/~rkirsch4/
   Reopened author page; no inspected equivalent resolution was located.
   The paper's cited code repository was also reopened:
   https://github.com/wcarey-gmu/universal-partial-words
   No equivalent n12d3 existence result was identified in its inspected page.
   This was not a clone-wide audit or exhaustive search of unpublished work.

Searches included the exact paper title with 2026; upcycles with diamondicity
and 2026; upcycles with d>1; upcycle with 12 and diamondicity; universal partial
cycles with greater than one; upcycles with d=3; upcycle with n=12; and universal
partial with 512 and 12. General web results were used to locate primary
records. No conclusion relies on MathDB, ResearchGate, or search snippets as a
mathematical authority. The surfaced primary records were checked directly.

Saved records: `research2-primary-open-records.json`,
`research2-primary-exact-statements.json`, `research2-novelty-search.json`,
`research2-further-novelty-search.json`. Several broad queries also returned
irrelevant recycling uses of the term; those supply no mathematical evidence.

Proposed substantive delta: a verified explicit (a,n,d)=(2,12,3) upcycle,
where the inspected 2026 primary paper states existence for any d>1 is open.
This is an affirmative resolution of the unrestricted existential question,
not a replacement by the finite n12 problem. The finite witness proof is
substantive because it crosses the unresolved diamondicity boundary, even
though the SAT encoding and verification are elementary tools. Current novelty
and significance require the designated fresh referee; no acceptance or STOC
quality inference is made here.
