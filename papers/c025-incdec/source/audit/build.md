# Clean build and source-archive reproduction audit

Job: c025-incdec-release-4b3b2544efe9. Audit date: 2026-11-02 UTC.

Mathematical snapshot: 2b34def4196da89c592b17665c39fbf7b0b04e44c40aeac720bf40cd52fb35b4.
Manuscript snapshot: d4717112b7a2b8ec108123ef8efb3e63f3f6ed5f1f6caf1810a2969f35593c6a.
PDF SHA-256: 407ec869e3c74ed3fea9001fc3e1afb187d4b3175fabfd78c52d40408afeb186.

Verdict: accept.

Ran python3 manuscript/build.py using a new temporary directory with no preexisting auxiliary files: pdflatex, bibtex, pdflatex, pdflatex. Every compiler invocation succeeded. The final compiler log is manuscript/main.log; its digest is bound in build.json. The complete build console and BibTeX log were also inspected. No fatal/compiler error, undefined citation/reference, overfull or underfull box, missing-glyph, font-substitution or BibTeX warning remains. The first compilation's expected unresolved auxiliaries are resolved by the final passes, as required for a normal clean BibTeX build.

Two harmless official-class warnings remain: unused global option natbib=false (the class uses the working direct BibTeX bibliography) and no supplied affiliation city. Neither creates unresolved references or changes the actual author/institution/country. No city was invented. Final output is six readable USLetter pages, 373519 bytes. pdfinfo confirms a valid unencrypted PDF 1.7 with text extraction, no JavaScript, correct title, and the official acmart v2.20 creator. All 15 listed font resources are embedded, subsetted and have Unicode maps; no Type 3 bitmap font appears. Body, abstract and bibliography use the public 11pt setup; running furniture and mathematical scripts use normal subordinate sizes. Class and matching dtx are byte-identical to the user's existing official ACM download.

After the sole approximate-bound wording qualification, freeze-manuscript was rerun successfully; no accepted mathematics changed. The entire 24-file mathematical snapshot still matches, including immutable source.md. The fresh main.bbl also agrees with the frozen publication dependency. No research-pass or scheduling counter was changed.

Created evidence/release/optimal-incdec-working_paper-source.zip from the exact eleven declared archive members listed in source-archive-manifest.json: all eight source files, publication.json, the final PDF, and the unchanged actual venue assessment. Extracted this exact archive inside evidence/release/reproduction and ran its bundled manuscript/build.py. This independent clean directory rebuilt the PDF and bibliography byte-for-byte identically. Every archived member still matches its manifest after the build. See evidence/release/zip-reproduction.json and zip-build-result.json for actual hashes and command. The archive is a local source package, and does not activate release/main.pdf or authorize upload. The supervisor still owns publish.
