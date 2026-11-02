# Local working paper

Title: Arena-Independent Memory for Pure Subgame-Perfect Equilibria in Reachability Games

Sole author: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my.

Build from the project root with `sh manuscript/build.sh`. The build runs
pdfLaTeX, BibTeX, and two further pdfLaTeX passes. It writes
`output/pdf/spe-memory-working_paper.pdf`. TeX Live 2026 and its installed
standard packages are required. No package installation or network access
is part of the build. The class and its documented source are unmodified
files from the user-designated official ACM distribution. `alpha.bst` is
the unmodified installed standard BibTeX style. The generated main.bbl is
included as an additional auditable bibliography input.

The article contains the complete accepted arbitrary-arena payoff-preserving
compression, credited old-existence corollary, and constrained binomial lower
bound. Its proofs do not rely on finite enumeration. Separate exact-checker
records remain in the project's code/, evidence/ and audit/ directories.

The current STOC2027 submission CFP requests named authors, a separate
title page, single-column text in at least 11pt, letter paper and one-inch
margins. Those settings are applied through normal class/package options.
The proceedings sigconf setting is different and is not used here.
The user's twelve-total-page cap applies to this local draft.

The fresh internal venue assessment is working_paper. This package does not
upgrade that assessment, establish external peer review, or authorize any
external submission, upload, video or contact. Substantial AI use is disclosed
in the article; no unobserved human verification is asserted. Separate fresh
citation/build/every-page review and the script release gates remain pending.
