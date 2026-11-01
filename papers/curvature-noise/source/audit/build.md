# Fresh final-build audit

Job: `curvature-noise-release-132a90b124b3`. Date: 2026-10-31.
**Verdict: accept.** This is a fresh audit of the existing clean final
compilation, not a claim to have recompiled or edited the frozen PDF in this job.

I inspected the real final `manuscript/main.log`, its geometry/font settings,
diagnostics and successful output summary. Its byte-identical stable copy is
`audit/release-build.log` (SHA-256
`b4ac62345e6d4f5dcf62d3d347765819b07df2f88eebde1b4afd05763b8fc495`).
The log identifies pdfTeX/TeX Live 2026 and official acmart 2.20, and ends with
`Output written on main.pdf (6 pages, 394903 bytes)`. The existing current PDF
has that size, six pages, a valid PDF header and nonempty text extraction.
The presentation revision's multi-pass build transcript was also inspected;
its initial unresolved references were resolved by subsequent passes. The
bound final compiler log has no undefined references/citations, errors,
missing-character diagnostics, overfull boxes or pending rerun warnings.

One underfull vertical box, badness 3646, occurs on body page 3 (physical page
4). I inspected that page; all equations and paragraphs are legible, contained
and orderly. It is a harmless spacing warning, not a failed build.

`publication.json` documents the latexmk/pdfLaTeX/BibTeX command. The recorder
and bibliography dependencies agree with the declared source closure; see the
citation report and `audit/release-checks.json`. The portable source archive
digest matches the publication record and every packaged source matches its
frozen file. The existing writer/package build evidence remains available;
it is not represented as a new compilation by this reviewer.

Fresh execution of `python3 manuscript/reproduce.py` exited zero and reproduced
all exact checks in `audit/release-reproduction.json`, including every reported
finite fraction. It uses the standard library, writes only stdout, and did not
change frozen evidence. This is a reproducibility check, not new mathematical
certification.

`pdfinfo` confirms US Letter (612 by 792 PDF points), six total pages including
cover and references, correct title and ordered five-author Info metadata.
The extracted XMP has the same ordered authors, all five emails and all five
institutions. All fonts reported by `pdffonts` are embedded Type 1 fonts; none
is Type 3. Files: `audit/release-pdfinfo.txt`, `audit/release-xmp.xml`,
`audit/release-fonts.txt`, `audit/release-pdf-text.txt`.

The class matches `template/acmart.cls` exactly. The final compiler geometry
reports 72.26999 TeX-point margins on all four nominal text sides; the source
uses single-column manuscript mode, 11pt text/captions/references, single
spacing and the separate title/abstract/contact cover. The final
`onehalfspacing` guard runs after `clearpage`, after all content is shipped.
No printed page uses that restored class spacing. There are no line numbers,
fake article DOI, submission ID, acceptance claim or copyright strip.

All frozen mathematical/source/PDF hashes remain unchanged. No repair or
manuscript refreeze was necessary. Current bindings and the actual build-log
digest are in `audit/build.json`.
