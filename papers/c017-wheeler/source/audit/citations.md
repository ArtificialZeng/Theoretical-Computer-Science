# Verification report

Mode: Search, with frozen-proof and finite-record traceability for original
mathematical claims. Job: c017-wheeler-release-bce62e5f5c55. Date: 2026-11-01.
Document: manuscript/main.tex and its exact ten-page frozen PDF.
Verdict: accept at release scope.

The explicitly invoked $citation-check-skill was advisory. Pass 1 is the fixed
33-claim extraction in citation-extraction.md. Pass 2 below checks those IDs in
sequence; it does not add claims. The user's autonomous bounded release job
supersedes the skill's optional confirmation pause. All 33 extracted claim groups
are supported at the appropriate scope; numerical errors, undefined citations,
contradicted attributions, unsupported priority assertions and unresolved
bibliographic records: zero. Original-theorem checks here establish transcription
and scope fidelity to the actual accepted proof, rather than a new referee verdict
or formal mathematical certification. Source-level support is distinguished below.

## Complete dependency and bibliography scope

The six sources listed in publication.json were inspected: main.tex, references.bib,
main.bbl, official acmart.cls, official ACM-Reference-Format.bst, and README.md.
The class/style are byte-identical to the designated official distribution.
The recorder lists no additional local authored input, figure, custom style or
import. Its main.aux/main.out are reproducible generated cross-reference files;
BibTeX's .bib and .bst dependencies are explicitly listed. main.bbl is regenerated
byte-identically in the clean build. Six cited keys match exactly six database
records; none is unused or undefined. The extracted and rendered references on
page 10 have all six entries and all in-text numerical references resolve.
See release-integrity.json and release-rebuild.json.

literature/user_bibliography_check.md expressly confirms there is no designated
Excel list. No workbook was invented and no workbook-authority metadata basis is
claimed. All six references are relevant. The actual primary metadata and support
were accessible; no citation-access limitation is necessary. For BG00 the
first-order-query assertion is checked against its official abstract; the detailed
representative/projection facts are checked in the primary thesis Blum99. For
Becker23 only the precise language-recognition bound used in the prose is checked,
against its primary abstract. This does not purport to reverify that paper's proof.

## Fixed claim-by-claim pass 2

| ID | Status and confidence | Evidence and scope |
|---|---|---|
| C01 | Supported, interpretation | Theorem 1.1 and Sections 2–3 reproduce the accepted membership proof, including the explicit O(S^13) bound, partial transitions and erasure; source.md and research-1-resolution.md have the same full input scope. |
| C02 | Supported, interpretation | Theorem 1.2/Section 5 reproduce research-2-realizability-proof.md. No polynomial or minimality assertion was added. |
| C03 | Verified, paraphrase | DP26 Definitions 4–5 and Section 2.1; DP26short Definition 3.1. The literal reaching-language convention is expressly stated; terminal output is not substituted. |
| C04 | Verified, paraphrase | DP26 Section 4, printed p. 16, and DP26short Section 4, printed p. 69 both pose the two decision questions. |
| C05 | Verified, exact numerical bound | Becker23 primary abstract states O(mn) for n-state, m-transition DFA language recognition; prose distinguishes accumulated output. |
| C06 | Verified, paraphrase | BC00 abstract/introduction, printed pp. 503–504: prefix normalization precedes sequential minimization, including empty-labeled cycles. |
| C07 | Verified, paraphrase | Blum99 Theorem 3.4, Definition 3.9/Proposition 3.10, printed pp. 11, 13–14; BG00 official first-order-query abstract. Synchronous finite-word operations match the hypotheses. |
| C08 | Verified, paraphrase | DP26 Remark 3 explicitly factors the statewise continuation LCP from accumulated output. The paper credits this identity as prior. |
| C09 | Supported, interpretation | Section 2 retains regular reaching-language comparison and the accepted convexity argument. |
| C10 | Supported, interpretation | Lemma 2.1 retains the ordered disjoint blocks, uniqueness of last transitions, common-suffix cancellation and convexity. |
| C11 | Supported, interpretation | Lemma 2.2 retains mismatch, proper-prefix and equality cases from frozen Section 2; output ranges are independent only across already ordered blocks. |
| C12 | Supported, interpretation | Lemma 2.3 retains both forward propagation and the decreasing-length converse. |
| C13 | Supported, interpretation | Accepted finite sorted-witness argument and distinct-boundary argument are transcribed, without converting nested turns into nonmembership. |
| C14 | Supported, interpretation | Lemma 3.1 states the accepted every-state SCC equivalence; its necessity retains common-loop replication. |
| C15 | Supported, interpretation | Noncommuting loops, finite-power mismatch and the fixed interval direction are retained in Equation 2. |
| C16 | Supported, interpretation | Equations 3–4 preserve external entering blocks, left/right order, and the length proof excluding a remainder. |
| C17 | Supported, interpretation | Lemma 3.2 keeps independently oriented sides, empty-side cases, shifted adjacent-level tests and transitivity; the two-piece assertion is only at the selected cycle state. |
| C18 | Supported, exact example | The four transitions, erasing outputs and peaks agree with the frozen nested-turn control and its all-n argument. |
| C19 | Supported, interpretation | Topological acyclic inheritance completes all states; no branching-prefix subclass replaces the original. |
| C20 | Supported, exact bound transcription | The accepted resource derivation is present, including O(S^2) comparisons, conservative O(S^13) bit operations and membership-only qualification. |
| C21 | Supported, interpretation | Corollary 4.1 retains both interval directions, common pump and total computable B(T), with no witness-runtime inference. |
| C22 | Supported, interpretation | Fixed-certificate argument retains residue/orbit decomposition, constant moduli and explicit empty-block exception; no actual PA-solver claim is made. |
| C23 | Supported, interpretation | Section 5.1 matches accepted LCP inclusion and normalized-residual refinement, including partial domains/coaccessibility. |
| C24 | Supported, interpretation | Distinct initial state and nonempty-return handling preserve the accepted epsilon exception and H identity. |
| C25 | Supported, interpretation | Section 5.2 explicitly handles all-padding tails for longer quantified witnesses and regular shortlex representatives; accepted construction unchanged. |
| C26 | Supported, interpretation | Productive-cycle finiteness and convex successor invariance are retained, with no guessed cutoff. |
| C27 | Supported, interpretation | The split construction and necessity from any Wheeler realization match the accepted proof; no minimization conclusion is added. |
| C28 | Verified against finite record, exact | membership-check.json records 16+528=544 exhaustive tables at lengths 7 and 600 seeded tables at length 8 with the stated alphabets/state counts. All-final scope is preserved. |
| C29 | Verified against finite record, exact | research-2-realizability-check.json has 13 controls, 20 finite domains, and exactly 1475/1318/8171/1315 checks in the stated categories. |
| C30 | Verified against finite record, paraphrase | Named controls include partial terminals, erasure, epsilon only, parity, initial LCP/cycles and finite-component output rejection; the cited JSON and proof retain coverage limits. |
| C31 | Verified as workflow record, paraphrase | Actual distinct referee role, math.md and job-specific check report document the separate context; paper explicitly disclaims external peer review and formal verification. |
| C32 | Supported, bounded interpretation | Current exact/equivalent searches and primary comparison in citation-search.md found no equivalent inspected SCC theorem; prose makes only a bounded comparison, not universal priority. |
| C33 | Verified, exact metadata | All six bibliography records match the primary title/author/version/year/venue/pages inspected; see mapping below. |

## Bibliographic record and nearby-claim mapping

- DP26: D'Agostino and Paradiso, arXiv:2606.29405v3, 13 August 2026, displayed
  title and authors match. Definitions 4–5 support the class; Remark 3 supports
  the residual-prefix attribution; Section 4 supports the stated prior question.
- DP26short: same authors/title, ICTCS 2026, CEUR-WS 4269, pp. 66–70, editors
  Luca Geatti and Carla Piazza, Udine; primary volume and PDF agree. The newer
  version retains both decision questions. No earlier single-piece definition
  is substituted.
- BC00: Marie-Pierre Béal and Olivier Carton, RAIRO TIA 34(6), 503–514 (2000).
  The journal record and original abstract support the normalization attribution.
- Blum99: Achim Blumensath, Automatic Structures, diploma thesis, RWTH Aachen,
  October 1999. Original front matter and relevant constructions were read;
  regular representative selection and first-order closure are standard tools.
- BG00: Achim Blumensath and Erich Grädel, LICS 2000, 51–62, IEEE Computer
  Society Press. The official LICS record supplies exact metadata and supports
  effective first-order queries; no separate new quotient result is claimed.
- Becker23: six displayed authors agree with the primary arXiv record,
  arXiv:2306.04737v2, 18 December 2023. Its abstract supports precisely O(mn)
  DFA-language recognition. The manuscript does not attribute the output test to it.

All primary URLs and actual query strings are retained in citation-search.md.
No reference or novelty strengthening required repair. Mathematical acceptance
remains the actual frozen referee decision, not this citation report.
