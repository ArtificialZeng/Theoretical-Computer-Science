# Local source and build

Run `sh build.sh` from this directory, or `sh manuscript/build.sh` from the project root. Requires an installed TeX distribution providing pdfLaTeX, BibTeX, latexmk, and standard acmart dependencies. The official `acmart.cls` and `ACM-Reference-Format.bst` are included without modification. No package installation or network access is needed for compilation in the checked environment.

The output is `msthalf_working_paper.pdf`. This filename retains the actual fresh internal assessment `working_paper`; it is not a venue decision. The article uses the current STOC submission layout (named author, 11pt single-column single-spaced text, US Letter, one-inch margins), with the official class's single-column `acmlarge` base and document-level geometry options. This is not the separate sigconf proceedings layout. The user additionally requires at most 12 total pages including title and references.

Substantive AI assistance is disclosed in the article. The complete mathematical proof is in the article; no code execution is necessary to establish its theorem. Code and finite-check evidence remain in the project evidence packet, and are not substitutes for the proof.

This is a writing-phase draft. Separate citation/build/visual release review and the script release gate remain required. No external submission, upload, contact, or email has been authorized.
