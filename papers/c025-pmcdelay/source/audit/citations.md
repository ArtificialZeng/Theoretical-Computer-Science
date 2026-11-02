# Verification Report

Mode: search verification with accepted-proof fidelity review. Job: c025-pmcdelay-release-dfedec0715d6. Checked 2026-11-01 UTC. The advisory citation-check-skill was explicitly invoked and read. Pass 1 is the fixed extraction in evidence/release-citation-extraction.md; external verification followed it. The user's authorized autonomous release job supersedes the advisory request for another extraction-confirmation turn. No Excel workbook or authoritative user bibliography was designated; literature/user_bibliography_check.md was inspected.

Overall verdict: **accept_with_citation_limitations**. All 34 extracted claims were reviewed. No contradicted attribution, numerical discrepancy, undefined key, unsupported novelty strengthening or out-of-scope theorem was found. The historical BBC99 chapter's complete text was not obtained; its existence and metadata were verified. The exact theorem-level primitive is available in inspected BLS Lemma 1. No unavailable chapter text is represented as inspected. This is a disclosed text-access limitation, not a mathematical or artifact veto.

## Claim-to-source verification, in extraction order

| ID | Finding and exact support |
|---|---|
| C01 | Matches claim.json and research/streaming_proof.md Sections 1, 5–6, accepted by the existing referee. Theorem 1.1 retains every original input, output, initial/final-delay and storage quantifier. This release review does not create a second mathematical acceptance. |
| C02 | Verified: BLS v3 Theorem 1 (printed p.6) states O(n^4 m K); Section 1.4 (p.8) explicitly leaves polynomial delay open. |
| C03 | Accepted-proof fidelity: total cost alone does not bound individual waits; the manuscript supplies separate rank/termination bounds. |
| C04 | Verified: local IPEC primary Theorem 32, printed 21:15, is restricted to triconnected plane graphs. |
| C05 | Verified: local Kenig v1 Theorem 1.1 gives 2^{O(k^3)} n^4 log n and required/excluded vertices, including both endpoints. Its n>=2 boundary convention does not strengthen the cited asymptotic comparison. |
| C06 | Verified: BCLPR v1 Lemma 4 states O(n^9 m^2 K^4) time and O(n^3) space; manuscript uses only output-polynomial/polyspace. |
| C07 | Fidelity passed: accepted streaming proof Sections 2–4 contains the actual helper emissions, exact child suspension and additive simultaneous induction. No claim that these known structural ingredients are newly invented. |
| C08 | Verified: IPEC Proposition 29, printed 21:14, uses a minimal triangulation with S made a clique and an extending maximal clique. The manuscript acknowledges an antecedent rather than attributing the general helper theorem to that restricted proposition. |
| C09 | Verified: CS23 primary abstract, Introduction and Section 3.1 describe the folklore exponential-space queue conversion; CS26 publisher abstract also states amortized-to-delay transformations. Conversion is explicitly credited as standard. |
| C10 | Verified: BLS v3 Theorem 4 and Lemma 7, p.15. The nonadjacent-pair/component formulation is also explicit in BCLPR Theorem 2.1. |
| C11 | Verified: BLS Lemma 11 (p.17) gives existence; BCLPR Proposition 1 gives exactly one of K and K+{a}. |
| C12 | Verified: BLS Lemma 12, p.17, gives the child/separator alternatives for parent PMCs containing a. |
| C13 | Verified via available primary text: BLS Lemma 1, p.12, explicitly gives polynomial delay from BBC. BBC publisher abstract gives O(n^3) per separator. Direct inspection of the entire historical chapter remains unavailable. |
| C14 | Verified: actual local BBHP04 Theorem 4.4, p.294, gives minimal triangulation and minimal elimination ordering; primary Fig.4, p.291, gives the fixed-input weighted path tests. |
| C15 | Accepted primitive fidelity passed: research/polynomial_primitives.md states the same queue scheme, trie and emission-before-expansion rule. Official igraph generation loops corroborate the recipe; full historical BBC completeness proof was not obtained. BLS Lemma 1 supplies the precise primitive theorem used by the accepted proof. |
| C16 | Fidelity passed: primitive dossier's naive polynomial path implementation and clique candidates match the manuscript; BBHP Fig.4 uses original input G and simultaneous weight updates. |
| C17 | Fidelity passed: bit vectors, depth-n tries, linked queues and polynomial bit-length addresses are specified in the accepted streaming proof; no polynomial-space claim appears. |
| C18 | Fidelity passed: accepted proof Section 2 gives the polynomial map and outside component, hence fibers at most n. |
| C19 | Fidelity passed: the manuscript retains the glued-block chordality and forced-saturation minimality argument. |
| C20 | Fidelity passed: the manuscript includes its tree-subtree Helly argument rather than an unsupported source attribution. |
| C21 | Fidelity passed: actual helper outputs with at-most-n fibers yield the stated prefix charge; earlier discoveries count once. |
| C22 | Verified: BLS Definition 16 p.16, Lemma 10 p.16, Theorem 8 p.32, Theorem 9 p.37, Theorem 10 pp.40–42 and its proof. The witness form, lost-vertex adjacency and component decrease are present. Manuscript explains the sandwich consequence and does not silently assume the inconsistent endpoint wording. |
| C23 | Verified: BLS Definition 12 p.14 assumes X\{a} separates a,b; Definition 20 p.29 selects both endpoints from the source PMC. The manuscript explicitly defines and proves the guarded searches it actually uses. |
| C24 | Fidelity passed: component-query guard, S subset N(A), and n(n-1) candidate pairs match the accepted executable neighborhood. |
| C25 | Fidelity passed: the accepted transfer proof retains exactly the witness arcs and strict component-decrease reachability, without single-arbitrary-seed connectivity. |
| C26 | Fidelity passed: accepted generator Section 3 uses recognized insertions, a trie, all non-a-nice seeds and one queue expansion per discovered PMC; distinct child outputs have distinct lifts. |
| C27 | Fidelity passed: fixed nondecreasing polynomial p and additive Q recurrence match accepted proof Section 4. |
| C28 | Fidelity passed: all three phase inequalities and the separate child termination invariant match the accepted proof; no aggregate-only delay inference. |
| C29 | Fidelity passed: the self-contained FIFO argument uses both E(j)<=qj and T<=qK, including finalization, matching accepted Section 5 and credited standard conversion. |
| C30 | Fidelity passed: accepted Section 6 proves the connected-component partition and handles zero vertices, isolates and complete inputs. |
| C31 | Exact numeric check: parsed frozen pass1-targeted-streaming.json: 29 records, maximum order 10, sum of serialized output counts 471. These remain diagnostics only. |
| C32 | Exact record check: audit/referee-verification.json reports 1100 graphs and 29 serialized cases; 1100 also equals sum_{n=0}^5 2^{n(n-1)/2}. The manuscript calls this an automated finite check, not an asymptotic proof. |
| C33 | Fidelity passed: scope limitations are explicit in accepted claim/proof and retained working_paper assessment. No improved space, constrained oracle, treewidth exponent, priority certificate or venue acceptance is asserted. |
| C34 | Bibliographic metadata checked against the primary records below and actual local primary title pages. All eight records exist; all printed DOI/version/year/author/title/volume/page fields agree. BCLPR's IWOCA venue is confirmed in the publisher's IWOCA 2024 contents. The only full-text limitation is BBC99. |

## Primary records consulted

- BLS: https://arxiv.org/abs/2610.19850v3 ; local frozen PDF/text, exact version 20 October 2026. The live record still identifies v3. Source title, three authors, Theorem 1 and the open delay statement match.
- Kenig: https://arxiv.org/abs/2610.24856v1 ; local frozen primary PDF/text, 17 October 2026, Theorem 1.1.
- GKTZ: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.IPEC.2025.21 ; local frozen PDF/text Theorem 32/Proposition 29. Official metadata gives volume 358, 21:1–21:17, four named authors, 2025.
- BCLPR: https://arxiv.org/abs/2402.18265v1 and https://arxiv.org/html/2402.18265v1 ; Proposition 1 and Lemma 4 inspected. Publisher contents https://link.springer.com/book/10.1007/978-3-031-63021-7?page=2 confirm IWOCA 2024 and all five authors.
- BBC99: https://link.springer.com/chapter/10.1007/3-540-46784-X_17 ; verified authors/title/WG 1999/LNCS 1665/167–172/DOI and abstract. Complete chapter not obtained. Known queue recipe additionally compared with the official implementation https://raw.githubusercontent.com/igraph/igraph/main/src/connectivity/separators.c ; code is corroboration, not the completeness theorem.
- BBHP04: https://link.springer.com/article/10.1007/s00453-004-1084-3 ; actual local primary Theorem 4.4 and Fig.4 inspected. Official metadata agrees with all four authors, Algorithmica 39, 287–298, 2004 and DOI.
- CS23: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2023.18 and its official PDF; abstract and queue-conversion discussion checked. Volume 254, 18:1–18:22, 2023 and DOI match.
- CS26: https://link.springer.com/article/10.1007/s00037-026-00287-w ; official abstract and metadata give Computational Complexity 35, article 6, 20 July 2026 and both authors. The source is credited for the general amortization context; the explicit FIFO detail is independently present in CS23.

For every cited work the applicable citation-check templates were run: first author/year/first title words; full title with arXiv/Semantic Scholar restriction; first author/year/venue; DOI where present; arXiv ID where present. Results used for verification are the primary records above, not secondary aggregations. Additional exact-title and general-graph/incremental/polynomial-delay searches found no equivalent all-size general-graph theorem among the inspected primary results. This is a bounded current-literature comparison, not proof of exhaustive priority; the paper already makes that limit explicit.

## Dependency and rendered-reference scope

Reviewed every source listed in publication.json, the main text's imports/citations, the generated bibliography and extracted/rendered references on page 9. The recorder reproduction reads local main.tex, acmart.cls and main.bbl; BibTeX reads references.bib and alpha.bst. Other packages/fonts are system TeX dependencies. README/build.py/template provenance and unmodified official .dtx/.ins are included in the declared sources. No local figure, unlisted TeX import, external bibliography, experimental reference archive or dynamically generated mathematical input is needed. All eight citation keys resolve and are used. No unnecessary unrelated reference was inserted.

The manuscript's original theorem is within the accepted full original scope. It accurately credits inherited recognition, lifts, structural preimages, separator extension and buffering. It contains the required sole author and candid substantial AI disclosure. The live STOC 2027 CFP was reopened: identified authors, title page, single column, single spacing, >=11pt, Letter and 1in margins are consistent with this 12pt nine-total-page artifact and the user's stricter 12-total-page cap. This is format review, not an upgrade of working_paper.
