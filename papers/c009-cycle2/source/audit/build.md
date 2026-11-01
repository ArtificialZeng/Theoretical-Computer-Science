# Fresh clean-build audit

Job: c009-cycle2-release-70b6b8b76475. Date:2026-11-01. Verdict: ACCEPT.

After reading the PDF skill, its edit operation marker was run successfully exactly once before the fresh PDF build; evidence/release-artifact-marker.log records completion. The existing authorized build command sh manuscript/build.sh ran latexmk -C then latexmk -pdf with halt-on-error and file-line-error. It exited0. Console: evidence/release-build-console.log. Current actual compiler log: manuscript/build/main.log. The build audit binds the SHA-256 of that nonempty log.

I inspected the real final compiler log and BibTeX log. There are zero compiler errors, warnings, undefined references/citations, missing characters, overfull boxes or underfull boxes. BibTeX used all five database entries and emitted no warning; its empty$ and missing$ lines are built-in-function counters, not missing-data diagnostics. The build regenerated the bibliography from the listed database/style and stabilized all cross-references. The six-page PDF has a valid PDF header and nonempty pdftotext extraction. No image-only manuscript or placeholder citation is present.

pdfinfo reports six letter-size pages,612x792 points, PDF1.7, no encryption and no JavaScript. All16 listed font instances are embedded/subset with Unicode maps and no Type3 font. Title metadata is correct; XMP dc:creator lists exactly Zijian Zeng, and contact email matches authors.json. The class is the unmodified official acmart input (SHA-256784c4f2fb07a70d8a797ee9d1c63f441c10fbd2f915c9c615d28cda35c0b742a).

The live official STOC2027 CFP, https://acm-stoc.org/stoc2027/stoc2027-cfp.html, was read on2026-11-01. It requires a named title page, single column, single spacing, at least11pt main text, letter paper and one-inch margins. These are supplied by current document options and geometry. It has no overall submission page limit; this project additionally imposes12 total pages and the actual count6 satisfies it. The later proceedings sigconf format is distinct. Page1 names only Zijian Zeng, UCSI University; substantive Codex use is disclosed at the end. No submission or venue-quality inference was made.

The fresh clean build changes PDF timestamp/ID bytes, so freeze-manuscript was actually rerun. evidence/release-freeze.json records that pass. The accepted evidence and mathematical scope were unchanged; the newly generated bbl has the same source hash. All release audits use this refreshed PDF digest and current source/evidence digests. No inherited success flag is used.
