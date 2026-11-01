# Writing-phase primary-source and format check

Job: `c012-upcycles-write-e722c4031892`. Inspected 1 November 2026.

## Exact mathematical scope

`release_gate.py check-math .` passed before authoring. The accepted frozen
scope is a binary n=12, d=3, L=512 existence witness, resolving the full
existential question in immutable `source.md`. The writer did not alter the
claim, decisive evidence, source, accepted referee records or research-pass
counters. No theorem of minimality, classification, general construction or
d=2 existence was added. The standalone printed verifier reconstructs the
same serialized witness as the accepted packet.

## Primary references and attribution

Publisher full text and metadata were reopened:

- [Fillmore, Goeckner, Kirsch, Martin and McGinnis (2026)](https://link.springer.com/article/10.1007/s10623-026-01841-x):
  title, all five authors, volume 94, article 152, date and DOI verified.
  Theorem 3.1 provides binary n8/d1 examples. Theorem 5.1 and Corollary 5.2
  preserve n,d under alphabet multiplication. Corollary 8.14 is a restriction
  for period-four/five frames, not an existence construction. Question 9.2
  asks d>1 existence; the following paragraph raises n not dividing cycle
  length. These are exactly the attributions used in the manuscript.
- [Carey, Kearney, Kirsch and Popescu (2025)](https://link.springer.com/article/10.1007/s10623-025-01609-9):
  title, all four authors, volume 93, pages 2803-2822 and DOI verified.
  Definition 8.2 permits multiple cyclic words in a quasi-family; the paper
  is cited for that precise distinction. No two-dimensional result is
  represented as providing the one-cycle witness.

Searches for `upcycle diamondicity 3 2026`, `universal partial cycles 12 512`
and `universal partial cycles diamondicity greater than one` located no
equivalent resolution in the inspected primary sources. The manuscript
uses a bounded literature comparison, without an exhaustive priority claim.
The prior fresh referee's own source comparison remains in
`audit/referee-literature.md`. No Excel bibliography was designated, as
recorded in `literature/user_bibliography_check.md`; no arbitrary citation
was inserted. DOI links are printed in the bibliography.

## Current official STOC format

The current [STOC 2027 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html)
was opened directly. Its submission-format and author-identification
paragraphs specify named/nonanonymous submissions, a title page with
title/authors/affiliations/abstract, 11-point or larger fonts, single column,
single spacing, letter paper and one-inch margins. There is no CFP
submission page limit; the user's stricter cap remains **12 total pages**.
The sigconf instruction is for the proceedings version, not this submission
layout. The CFP requires disclosure of substantive AI use; the final body
contains a factual AI methodology statement. No venue suitability or
acceptance is inferred from formatting.

The unmodified user-designated official acmart v2.20 class is copied locally.
Its hash and original path are in `write-start.json`. Document-level geometry
sets letter paper and one-inch margins; acmsmall/nonacm/11pt gives single
spacing without editing the class. Small body/abstract/reference text is
promoted to the normal 11pt size. The title, institution and sole author
are visible. The class-required location fields use the university's main
[official address](https://www.ucsiuniversity.edu.my/contact); no ORCID,
funding, submission status or human review is invented.

## Authoring and build controls

The PDF skill was read. Its artifact-operation marker ran successfully
exactly once immediately before the first authoring command. The first
build stopped because acmart required country metadata; the affiliation
fields were supplied and later builds succeeded. Benign class notices
about the consumed natbib option and listing-internal vspace are retained
in logs; they are not missing references or mathematical evidence.
The final clean-build result, full-page visual inspection and exact source
integrity checks are recorded separately in `write-verification.json`.

The writer prepares and freezes a local draft only. A separate fresh
citation/build/visual release review remains necessary. No external
submission, upload, message or contact was made.
