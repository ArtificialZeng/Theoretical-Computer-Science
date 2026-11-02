# TreeFlow manuscript delivery

Main artifact: `4.pdf`. Editable source: `4.tex`, `references.bib`, and the
retained local ACM bibliography style. The initial anonymous sigconf instruction
was superseded by the user's request to follow the official STOC submission
format. The final paper uses Letter, 11pt, a single column, single spacing,
1-inch margins, a separate identified title page, and references at the end.
Original ACM template samples remain preserved.

The title page lists, in the exact supplied order, Zijian Zeng (UCSI University),
Jiayin Cao (Ningbo University), Weinan Dai (Zhejiang University), Rui Wang
(Nanchang Institute of Technology), and Fei Ding (Alibaba Group), with the supplied
emails. The same names are in PDF author metadata.

Build and reproduce checks with:

```sh
sh build.sh
```

The manuscript contains complete proofs for the stated new results and explicit
citations for invoked prior results. All main theorem statements, motivation,
comparison table, and technical overview occur near the beginning. Its TikZ
architecture and both requested lower-bound encodings are editable in `4.tex`.

## Status

This is a proof-complete manuscript of the **weakened scope actually established**,
not a claimed solution of the originally proposed full characterization.
The submission layout is now aligned with the official CFP. In particular:

1. Target theorem A is contradicted by the stated model under OMv, even for
   path-shaped procedures and acyclic calls. The manuscript proves that barrier.
2. The positive theorem requires acyclic candidate calls and fixed decomposition
   certificates, and charges global summary-dependency propagation explicitly.
3. The D-dimensional lower bound is tight for the matrix-selector family only;
   the general dense-relation upper/lower gap remains.
4. The requested PhASAR/Heros integration, three analyses, repository history
   replay, and four-way performance comparison have not been performed. The
   finite executable checks are not presented as those experiments.
5. The official-format correction and the five-author title page are complete.
   The earlier anonymous sigconf source is retained only as historical material.
6. Novelty/significance and correctness still require independent expert review.

See `research/claim_audit.md` for the precise scope and source verification.
`estimated_values.md` confirms that no empirical estimates were inserted.

The final PDF has 10 pages: one title page, eight body pages, and one reference
page. This length is an editorial choice, not a submission limit. Rechecked on
2026-11-02: the STOC 2027 review submission has no total-page limit; its initial
twelve pages after the title page must present the merits (an optional contents
page immediately after the title page is excluded). The proceedings version's
12-page limit does not apply to submission. The erroneous total-page assertion
has been removed from the checker. Source:
https://acm-stoc.org/stoc2027/stoc2027-cfp.html .
All theorem statements and complete proofs are within the eight body pages. The final format/key audit is in
`research/final_checks.json`. There are no LaTeX warnings, undefined citations,
or overfull boxes. Fonts are embedded. Title, table, architecture, reduction
figures, and reference-page renderings were inspected.

`4_source.zip` contains the current manuscript, PDF, bibliography style, all
artifact programs and generated correctness counts, and the delivery/audit
documents. Large downloaded literature PDFs and historical drafts remain in
the workspace and are not needed to build the paper.

## Reviewer revision v2

`REVIEW_RESPONSE.md` maps the supplied report to each revision. The manuscript
now uses 11pt figure/table/caption text and alphabetic-year references.
Corollary 5 bounds propagation by ancestor call-target incidence and permits
shared callees; the call-diamond family has exponentially many call paths.
The strongest reduction has a new dedicated figure.

`treeflow-artifact-v2.zip` is embedded in the PDF and also delivered separately.
It includes per-record raw traces, complete code, actual runtime versions, an
independent replay auditor, and SHA-256 hashes. Extraction and execution from
the PDF in a clean directory passed, with byte-identical raw records.
