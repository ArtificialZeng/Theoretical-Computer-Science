# Claim and scope audit

Audit date: 2026-10-31 (Asia/Shanghai). No skills or subagents were used.

## Requested claims and their disposition

| Requested claim | Disposition in manuscript | Reason |
|---|---|---|
| A: per-procedure treewidth alone gives subpolynomial updates and O(D log n) queries | Refuted under OMv, not asserted | The path-procedure incidence gadget has t=1, D=1, acyclic call depth one, n=6k, and k online updates and queries per vector. |
| B: n-dimensional OMv barrier | Proved | Three-layer reachability gadget, n=2k+2, fixed source, identity transfers. |
| C: D-dimensional OMv barrier at treewidth one | Proved | Three control points, D=2k+1, fixed matrix relation and one-pair selector edits. |
| Matching D-dependent bounds in full generality | Not established | Linear selector threshold is tight only for the selector subfamily; general dense-relation cost remains D^(omega+eta). |
| TreeFlow upper bound | Weakened and proved | Fixed supplied certificates, acyclic candidate call graph, explicit dependency volume lambda, fast same-context queries. |
| Arbitrary endpoint fact queries | Supported with slower bound | Empty-stack valid-prefix search costs O((n+E)d^2), independently proved. |
| Recursive updates | Exact slow fallback | Restart-from-zero finite fixed point, at most Pd^2+1 evaluations. |
| Dynamic decomposition integration | Interface and missing adapter identified | No unsupported claim that a black box also bounds global summary propagation. |
| Repository experiments | Not done | Only actual finite correctness checks are reported. No performance numbers inferred. |

## Proof checks

- Treewidth refers to the local skeleton **including** each call/return interface edge.
- Multi-target call edges belong to the interprocedural incidence structure; they
  do not turn an individual procedure's path skeleton into a dense CFG.
- Call and return matching is enforced by site and callee identity.
- The added zero fact never generates ordinary facts in the lower-bound gadgets.
- The polynomial-preprocessing consequence is invoked from HKNS15, Theorem 2.2;
  an arbitrarily large preprocessing polynomial is not silently charged to k^3.
- If n counts edges/target occurrences as well as vertices, the dense lower bound
  becomes a square-root exponent. The manuscript states this explicitly.
- Elementary relation-pair changes and full relation replacements have different
  payload sizes. There is no constant-cost reading of a D^2-bit matrix.
- Bag combination requires closure, not just one matrix product.
- Pinning arbitrary same-procedure endpoints changes only two ancestor paths;
  the running-intersection argument is included in the proof.
- lambda counts all reached gates, not just outputs that happen to change.
- The unique-caller corollary bounds occurrences, not distinct callers alone.
- Recursion requires fixed points. Retaining a previous fixed point after deletion
  is unsound; the fallback restarts at zero.
- The matrix exponent is used as omega+eta for any fixed eta>0, not as an
  unproved assertion that the infimum exponent is attained.

## Literature and novelty boundary

Original sources for HKNS15, the 2023/2025 dynamic treewidth results, and the
2019 RSM work are stored in `sources/`. Crossref metadata for seven central
references is also stored there. The main 2019 RSM source explicitly already
uses dynamic intraprocedural updates and summary fixed points; the manuscript
does not claim invention of that machinery. The 2020 on-demand IFDS work is
acknowledged, and the present slower query bound is not represented as an
improvement on its static oracles.

Searches included dynamic IFDS + OMv, interprocedural reachability + dynamic
treewidth, and dynamic RSM summary propagation. A literature search does not
certify novelty. The simple OMv transfers and relation-circuit parameterization
require expert novelty/significance review before claiming a STOC contribution.
No independent human proof audit or external peer review has been performed.

## Current submission layout

The user superseded the initial anonymous sigconf instruction and supplied
all five authors. The current `4.tex` uses the official submission layout:
Letter paper, 11pt body, a single column, single spacing, 1-inch margins,
a separate title page with the supplied author names, affiliations and
emails, and references at the very end. Page numbering restarts after the
title page so the initial twelve body pages can be checked directly.

The class is `article` with explicit geometry. The paper was initially
developed from the supplied ACM template; `ACM-Reference-Format.bst` and the
same manuscript content are retained. The earlier sigconf source is stored
only as `research/4-sigconf-history.tex` and is not the final manuscript.

Source: https://acm-stoc.org/stoc2027/stoc2027-cfp.html
The retrieved page is saved as `sources/stoc2027-cfp.html`.

The official policy requires disclosure of substantive generative-AI use.
The manuscript includes an accurate disclosure, without claiming human
verification that has not occurred. Expert review and the missing empirical
study remain outstanding scientific requirements, separate from formatting.

## Reviewer revision v2

The total PDF now satisfies the user's stricter twelve-page cap: 10 pages,
including title and references. All figure, table, and caption text uses
normal 11pt; figures have no scaling operation.

The ancestor-incidence corollary is proved independently of the number of
call paths. Shared diamond chains provide a concrete non-unique-caller case.
It extends the former unique-occurrence fast regime without asserting a
new universal dynamic algorithm. The 2019 local-update primitives and global
summary iteration are explicitly credited.

The code/report gap is addressed by an embedded archive and per-comparison
raw records. They are actual executions and a clean extraction/replay was
performed; this is not an assertion of a human proof audit.

See `../REVIEW_RESPONSE.md` for the complete point-by-point response.
