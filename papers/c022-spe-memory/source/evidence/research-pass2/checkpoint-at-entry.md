# Checkpoint

## Write complete — c022-spe-memory-write-ec7adf27a885

**Decision:** ready for a separate fresh release review; kind
**resolution-paper**, original status **proved** under the actual accepted
internal mathematical review. The venue classification remains
**working_paper**, exactly as assessed by the fresh referee. This phase does
not claim external peer review, release, submission readiness, or submission.

**Accepted scope:** every given pure SPE in any set-sized, no-dead-end
n-player Boolean reachability arena has an exact-payoff-equivalent pure SPE
using at most n*3^n VERTEX-update states per player. This includes arbitrary
infinite arenas/branching, every legal history, prefix targets, and every
required winner subset with extra winners allowed. No original quantifier
was narrowed. No unconditional infinite-arena existence, optimality, or new
FPT decision bound is claimed.

**Gates and integrity:** release_gate.py check-math passed before authoring.
The accepted mathematical snapshot is
`584a7fb098fe85033ce2ffdf4ed2efe808d7dde6097b69a23cab1d6c9f6df4e9`,
reviewed by `c022-spe-memory-referee-4a3aae04fe17` in `audit/math.json`,
`audit/math.md`, and `audit/innovation.json`. Its separate
`audit/stoc-assessment.json` is working_paper. All twelve frozen files still
match their hashes. Immutable source.md remains SHA-256
`9dd4ff19af8a2996db2a11e18b2a4caa65426f62647822995c446c31dd0899fe`.
No frozen mathematical packet or earlier verdict was edited.

**New artifacts:** `manuscript/main.tex` contains the complete accepted proof,
precise prior-work comparison, limitations, finite-check coverage, and
substantial Codex-use disclosure. It has exactly the prescribed author,
Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. The official
ACM acmart v2.20 class/source are unmodified. Current STOC 2027 CFP was
checked: named authors, separate title page, single column, at least 11pt,
letter paper, and one-inch margins. The seven-total-page PDF
`output/pdf/spe-memory-working_paper.pdf` is below the user's 12-page cap.
No workbook was designated; no irrelevant citation was inserted. Relevant
primary records were refreshed; precise version/theorem support is in
`evidence/write/citation-basis.md`.

**Build and freeze:** clean `sh manuscript/build.sh` succeeds with installed
pdflatex/BibTeX. Five references resolve, all fonts are embedded, and there
are no overfull/underfull boxes or undefined cross-references. Two harmless
official-class notices are disclosed in `evidence/write/build-check.json`.
Every final page was rendered and visually inspected; records/images are in
`evidence/write/visual-check.json` and `evidence/write/pages/`.
release_gate.py freeze-manuscript succeeded:
manuscript digest `bf2ff6975b073ab30ef9ab28bef780cd700d4fcc4421e6a5d3d8b5c934446313`,
PDF digest `c6f0eef23829878b3d7b75daa7093c6e90063748459b352dbf74dc2737371b31`.
The frozen input list is `publication.json`; binding is
`audit/manuscript-snapshot.json`. Optional bounding-box text extraction
crashed; normal text extraction and page rendering succeeded. This operational
failure has no mathematical implication and is recorded separately.

**History preserved:** research_passes=1 was the previously observed runner
count; this writer did not edit counters, usage, scheduling, or state.json.
The incomplete triage timeout and recovery remain recorded. Owner-free reset,
rank-free selection, and noncredible-NE threat failures remain in
`evidence/research-pass1-adversarial.md`; none disproves the original question.
The prior checkpoint is preserved at `evidence/write/checkpoint-at-entry.md`,
and the research-entry checkpoint remains in its earlier evidence location.
No agents, other Codex processes, background workers, or external contacts
were used in this write job.

**One next test:** the assigned fresh RELEASE worker should verify citations,
reproduce the clean build from the frozen complete source list, inspect every
page, perform required ZIP reproduction/release gates, and retain the actual
working_paper label. This writer creates no release acceptance metadata.
