# Fresh build and metadata audit

Job: c017-wheeler-release-bce62e5f5c55. Date: 2026-11-01. Verdict: accept.

The bound build log is manuscript/main.log, the real successful compiler log for
the frozen manuscript/main.pdf. It is nonempty and records a 10-page, 408699-byte
output. There are no fatal diagnostics, undefined references/citations, BibTeX
warnings, missing glyph messages, or overfull boxes. BibTeX used all six entries
and warning$ ran zero times. One underfull vertical box, badness 2409 on page 6,
was assessed on the rendered page and is harmless vertical whitespace.

A fresh clean build was also executed in tmp/pdfs/release-build-bce62e5f5c55 from
byte-identical copies of the complete six declared inputs, without preexisting
.aux/.out/.log/.pdf files. The PDF-skill create marker succeeded once immediately
before this audit's first PDF-authoring command. latexmk -pdf -interaction=nonstopmode
-halt-on-error -file-line-error main.tex completed with exit code 0 and ran the
necessary pdflatex/BibTeX passes. Regenerated main.bbl and every copied input remain
byte-identical. Both the final compiler log and complete latexmk transcript were
inspected. The clean copy has the same lone underfull box and no unresolved
citation, reference, font or overfull diagnostics.

The clean PDF has identical extracted text and all ten 110-dpi PNGs are
byte-identical to the directly inspected frozen PDF's page images. Their PDF
byte digests differ because they are separate builds; no byte-identical PDF
reproducibility is claimed. release-rebuild.json records both digests, every
page comparison and the clean build-log digest. The frozen manuscript/PDF was
not modified and no acceptance was refreshed or manufactured.

pdfinfo reports an unencrypted 10-page US-Letter PDF, 612 by 792 points, rotation
0, PDF 1.7, with the correct title and normal pdfTeX/acmart producer metadata.
It has no JavaScript or forms and is not image-only. No Author field is exposed
by pdfinfo, but the title page and contact information correctly identify the
sole author, Zijian Zeng, UCSI University, with the supplied email; this optional
metadata omission is nonblocking. pdffonts shows all 15 listed fonts embedded
and subset; no Type 3 font is present. pdftotext yields complete nonempty text,
including mathematical statements and all six references.

The official class and bibliography style match the designated official files
byte-for-byte. The dependency recorder, BibTeX log and manual source inspection
show complete local dependency coverage; system TeX packages are not local
sources. The 11pt single-column nonacm layout uses US Letter and one-inch margins.
The actual STOC 2027 CFP was opened today and confirms named submissions,
11-point-or-larger single-column/single-space layout, and substantive-AI disclosure.
The user's stricter 12-total-page cap is met by all 10 pages including title and
references. The explicit substantial Codex disclosure is on page 9. No conference
acceptance, quality guarantee, external upload or submission follows from this
format check. The structural gate remains a separate last step.
