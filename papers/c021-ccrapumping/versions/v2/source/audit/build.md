Job: `c021-ccrapumping-release-e862e3a691c8`. Reviewed 2026-11-01 UTC / 2026-11-02 Asia/Shanghai.

Evidence snapshot: `c56f3440ebba4e41358a93f526e776e26091d3e07c234d06ecd41eb565a274b0`.
Manuscript snapshot: `89cdee1cc05804ee0c05f8fa38374b76576021cce0f05ea93b9a7cdc0edd9fc2`.
Current PDF: `a995aec21cc9daffd8f604e82c00be5cd08162aeafbc36af0feb17052d4076c1`.

# Fresh clean-build audit

**Verdict: accept.** After the PDF skill artifact marker succeeded once, this release context ran latexmk -C and latexmk -pdf main.tex from manuscript/. The build completed with exit code zero. Clean and command transcripts are in evidence/release-v2/clean.log and build-command.log. The binding compiler log is manuscript/build/main.log; the bibliography log manuscript/build/main.blg was also inspected.

Final TeX/BibTeX logs contain no compilation error, fatal diagnostic, undefined citation/reference, unresolved rerun, overfull box or underfull box. All seven bibliography entries were regenerated. Two harmless optional metadata warnings remain: acmart has no affiliation city, and C25 lacks a publisher address. The supplied institution/country and bibliographic data are retained rather than inventing information. These are not mathematical or layout failures. Intermediate first-pass unresolved references were resolved in the completed build.

The output has a valid PDF header, 11 pages, letter-size 612x792 point pages, selectable nonempty text and no encryption. It respects the user's 12-total-page cap. All 17 listed font instances are embedded with Unicode mappings. The PDF title matches the article. Its rendered author/contact and XMP creator are checked separately against authors.json; no external publication identifier or venue-acceptance statement is supplied. The PDFInfo Author field is not populated; this is not required by the current submission format, and the complete sole-author identification is plainly printed on page 1.

The manuscript sources, all frozen mathematical inputs and source.md remain byte-identical. The rebuild changes the PDF binary digest, as expected for a fresh compilation; freeze-manuscript was rerun successfully. The old/current extracted text and all eleven corresponding rendered-page PNG hashes are identical (evidence/release-v2/rebuild-comparison.json). Current final pages were then individually inspected. No proof, statement, bibliography or pagination was altered by the rebuild.

Complete dependency accounting is in evidence/release-v2/dependencies.json. The compiled local class and bibliography style and the remaining official input files all match the user-designated official distribution byte for byte. No source from another project was used. A preservation snippet initially used project-relative paths from manuscript/ and failed before copying; the clean build itself still ran, and preservation was corrected from the project root. evidence/release-v2/operations.md records that operational error honestly. It has no mathematical significance and no counter was reset.
