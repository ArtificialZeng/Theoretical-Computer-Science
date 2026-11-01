# Current primary-source screen

Job c012-upcycles-triage-8176c8933a92; inspected 2026-11-01 UTC.
Verdict on source status: **open-supported**, not exhaustive priority clearance.

1. Fillmore, Goeckner, Kirsch, Martin and McGinnis, *The existence and structure
   of universal partial cycles*, DCC 94, article 152, published 4 July 2026.
   [Publisher full text](https://link.springer.com/article/10.1007/s10623-026-01841-x).
   Inspected Sections 2, 8, 9, including Remark 6.6 and Question 9.2.
   The question is existence of any nontrivial upcycle with diamondicity >1;
   the publisher explicitly calls this unresolved. Section 8/Table 4 leaves
   binary n=8,d=2 and d=3 possible. These are allowed parameters, not examples.
   The known examples have d=1; alphabet multiplication preserves diamondicity.
2. [Current arXiv record](https://arxiv.org/abs/2310.13067) shows v3,
   revised 14 April 2025, as the latest version. The actual supplied
   [v3 PDF](https://arxiv.org/pdf/2310.13067v3) has SHA256
   `60ce1f11820777dbaf608ca21ae42ddb586ddcff19d10fb3ca71a9f6c72c3668`.
   Re-ran pdftotext: output `intake/triage-extracted.txt` is byte-identical
   to `intake/paper.txt`. Read Section 2 (printed pp. 2–3), complete Section 8
   (pp. 24–27), Section 9 (pp. 27–28), and Theorem 3.1 examples (p. 4).
   Its Question 9.2 agrees with the publisher. The curtains, frame-period
   restrictions and D(8)=4 were inspected, so their consequences are known work.
3. Carey, Kearney, Kirsch and Popescu, *Universal partial tori*, DCC 93,
   2803–2822 (2025), DOI 10.1007/s10623-025-01609-9, published 27 March 2025.
   [Primary full text](https://link.springer.com/article/10.1007/s10623-025-01609-9),
   Section 9, immediately before Theorem 9.3: still only diamondicity-one
   upcycles are known. Its higher-dimensional constructions do not provide
   a witness for the one-dimensional cyclic question.
4. [Rachel Kirsch's author-maintained publication list](https://mason.gmu.edu/~rkirsch4/),
   Published/Accepted and Preprints sections, inspected: lists the two papers
   above and no later listed solution to this target. A publication list is
   supplementary coverage, not a complete bibliography or a proof of openness.

Web confirmation output for the decisive publisher passages and author list is
saved in `evidence/triage-web-confirmation.json`. No search snippet alone is
used to establish the precise target or its open-supported status.

Bounded search queries included exact/equivalent phrases:

- `"upcycles" "d > 1"`
- `"universal partial cycles" 2026 2025 diamondicity`
- `"10.1007/s10623-026-01841-x"`
- `"universal partial cycles" "2026" diamondicity existence`
- `"upcycles" "diamondicity" "2"`
- `"universal partial cycle" "greater than one"`
- `"universal partial cycles" "diamondicity" after:2026-07-04`
- `"upcycles" "d>1" existence`
- `"universal partial cycles" higher diamondicity construction`

No equivalent resolution was located in these searches. MathDB, ResearchGate,
Paperity, and indexes were leads only; the actual publisher/arXiv texts control.
Kirin Martin's personal site appeared in search results but opening it failed
with a cache miss; its snippet is not used as verified evidence. Searches may
miss recent/unindexed work. A future candidate needs a fresh novelty audit.

## Duplicate screen

Read the 26 registered project titles in the existing queue (read-only); the
local snapshot and comparison are in `evidence/triage-duplicate-screen.json`.
The five historical originals concern correlation gaps, privacy paths, robust
stopping, submodular noise and advice matching. Their problem definitions have
different objects and quantifiers. The nearest superficially similar originals
were inspected directly: c010-skewgray concerns Hamiltonian listings of binary
vectors subject to adjacent transition coordinates; c009-cycle2 concerns
weighted-tournament densities; c003-compress concerns synchronizing automata.
None is the present unique-coverage existential question. For other entries,
this is a title/domain screen, not a line-by-line audit of every frozen packet.

## Triage interpretation

A new d>=2 witness would answer the full original question and cross a
documented structural boundary. Its payoff is plausible; neither novelty nor
conference-level significance is certified now. The exact finite Boolean
encoding and literal verifier are available. Advance for one bounded search;
the negative alternative still requires an unrestricted mathematical argument.
Do not produce a frame-only paper or a manuscript from finite negative results.
