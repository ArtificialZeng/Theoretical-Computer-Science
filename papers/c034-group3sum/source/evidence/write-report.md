# Writing report

Job: c034-group3sum-write-f534b28c23ae. Phase WRITE.

## Scope and gates

The actual check-math gate passed before manuscript authoring. Mathematical acceptance remains the fresh referee c034-group3sum-referee-f77368142a77 bound to snapshot 15a73043f23436b1592a376f95f678e39919b724da29d1fc7773757f6a82f52a. All frozen inputs, source.md and earlier review files remain unchanged. Research passes remain 1/3. No mathematical scope was strengthened or narrowed.

The manuscript proves the accepted all-M randomized bounded-time witness algorithm, including original-coset profiles, extremal divisor selection, all-order probabilities, support-product semantics, legal thin-product call, observable listing/scanning/random-generation caps, aggregate subinstance costs and fixed-input success. The accepted routine consequence for every fixed representable finite coordinate relation is given with direct attribution, finite quotient and witness-preserving translation.

## Artifact and format

PDF: manuscript/bounded-exponent-3sum-working_paper.pdf. Seven total pages, Letter, single column, nominal 11pt body and abstract, one-inch text margins. Sole author: Zijian Zeng, UCSI University, supplied email. Official acmart v2.20 is copied unchanged; its SHA256 matches the supplied official input. Alphanumeric references hyperlink to all three primary arXiv versions. Both body material-AI roles and an end methodology statement are present. No undocumented human verification is asserted.

Read PDF skill; its marker command succeeded exactly once before first authoring: node /Users/mac/.codex/plugins/cache/openai-primary-runtime/pdf/26.1017.22136/skills/pdf/container_tools/mark_artifact_operation_started.mjs --operation-kind create --expected-output-count 1 --output-format pdf.

Clean command: sh manuscript/build.sh. The script clears its named intermediate files, runs pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX, and copies the final PDF. Final logs: manuscript/build/main.log and manuscript/build/main.blg. Zero undefined citations/references, zero overfull/underfull boxes and zero BibTeX warnings. The only final LaTeX warning is unused-global-option reporting for natbib=false forwarded from acmart to amsart; acmart recognizes the option and the generated bibliography is correct.

The first build failed because manuscript mode uses one-and-a-half spacing and acmart rejects the attempted baseline change. Changed the document option to its naturally single-spaced acmsmall mode and kept the class unmodified; no integrity guard was disabled. This operational build issue is not mathematical evidence.

## Writer visual inspection

Rendered final PDF with pdftoppm at 110 dpi. Viewed every page individually (1 through 7); preserved evidence/write-rendered/final-page-1.png through final-page-7.png. Checked title/author block, theorem, original-coset lists, hash formulas, matrix memberships, inequality chains, finite-quotient proof, references and AI statement. No clipping, overlaps, missing glyphs or illegible equations observed. Page seven is a natural partial final page. This is the writer's inspection, not a fresh release audit.

Deterministic checks and PDF digest: evidence/write-final-checks.py and evidence/write-final-checks.json. PDF SHA256 791d00cdca2f62342a1ceb4348ec98071200f5b61a8506f28f589c2a33a8e1b5. Source manifest: publication.json; full frozen source/PDF mapping: audit/manuscript-snapshot.json. freeze-manuscript passed at 2026-11-02 16:49:34 UTC; no listed source/PDF has changed since.

## Classification and remaining work

Retain actual working_paper assessment: technical_depth remains uncertain in audit/stoc-assessment.json. No automatic promotion, numerical acceptance estimate or external submission. The source bibliography applicability check is literature/user_bibliography_check.md: no user Excel list was designated, and none was invented. Primary metadata refresh succeeded for the three cited records.

Next test: a fresh RELEASE worker must inspect citations against actual source statements, reproduce a clean build/ZIP, inspect all seven pages and run the required release gates while retaining working_paper. No release or fresh citation/visual acceptance is asserted by this WRITE job.
