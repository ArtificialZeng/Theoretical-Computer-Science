# Clean-build and source-reproduction audit

Job: c042-strongrsp-release-8a7cb8c2de68. Verdict: accept.

Ran latexmk -C main.tex inside manuscript, then the declared build.sh using
pdfLaTeX/BibTeX from TeX Live 2026. evidence/release/build-clean.log records the
whole clean multipass build. evidence/release/compiler-final.log is the complete
final-pass compiler log copied from manuscript/main.log and bound by SHA-256 in
build.json. Temporary first-pass cross-reference warnings resolved on rerun.
The final pass has no errors, undefined citations/references, missing glyphs,
overfull or underfull boxes, or remaining rerun request. The only class warning
is the unspecified affiliation city; the authorized institution and email are
printed correctly and no city was invented.

The final PDF is readable, unencrypted, nine US Letter pages, with nonempty text
extraction and all listed fonts embedded. Its XMP dc:creator contains Zijian Zeng;
the title metadata matches the manuscript (Poppler's basic info summary omits an
Author field). Exactly one human author is printed. The source uses the unmodified
official acmart class and ACM bibliography style; byte comparison is recorded in
evidence/release/template-check.json.

The [current official STOC CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html)
was checked on 2026-11-03 UTC. The separate cover, named author, single-column
single-spacing, 11pt prose including abstract/references, letter paper and nominal
one-inch geometry are present. Nine TOTAL pages meet the user's stricter cap of
twelve. Subscripts and contact-note typography use normal smaller auxiliary
sizes. Microtype optical glyph protrusion does not alter the geometry. Body and
end AI disclosures describe actual substantive roles, without claiming human
verification. Local format compliance does not establish venue competitiveness.

evidence/release/source-package-working_paper.zip contains exactly the declared
publication sources plus publication.json. reproduce.py extracted it into an
isolated project subdirectory and ran a clean source build. reproduction.json
records identical extracted text, the same nine pages, and byte-identical PNG
renders for every page. Binary PDF equality is separately recorded; timestamp
differences are not concealed. The package is local audit evidence, not a public
upload or active release. The supervisor alone calls publish.

An initial rendering attempt lacked its destination directory; an initial
reproduction comparison expected two-digit names although nine-page Poppler
output used one digit. Both operational failures are preserved in their logs,
repaired, and rerun successfully. Neither was mathematical evidence. A template
comparison initially used the parent directory; the successful comparison uses
the actual distribution/acmart subdirectory.

