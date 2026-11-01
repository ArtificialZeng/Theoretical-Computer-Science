# Fresh clean-build audit

Verdict: accept. Job `coverage-sparse-release-baf234409c0d`.

Executed the publication build command from manuscript/:

    latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex

It completed successfully using installed TeX Live 2026 pdfLaTeX/BibTeX. The
actual final compiler log is copied unchanged to
`evidence/release/baf234409c0d/main.log`; build.json binds its SHA-256.
The full driver output is build.stdout.log in that directory. No package was
installed. The PDF-skill edit marker completed successfully before source edits.

The final log contains no TeX error, fatal diagnostic, undefined reference or
citation, rerun request, overfull box or underfull box. The sole warning is
the official class's unused-global `natbib=false` option; bibliography processing
is successful and all seven alpha citation labels resolve. This benign warning
does not affect layout, citations or the output. All 18 fonts are embedded.

PDF inspection confirms eight total 612×792-point Letter pages: separate cover,
six body pages and final references. Official acmart manuscript mode selects
11pt; single spacing and one-inch nominal text geometry are configured explicitly.
No sigconf layout or review line numbers are used. The class is byte-identical
to its official dtx/ins regeneration, SHA-256
784c4f2fb07a70d8a797ee9d1c63f441c10fbd2f915c9c615d28cda35c0b742a.
The permitted CTAN origin and original publisher endpoint failures are recorded
accurately in the unchanged template/download-provenance.json.

Title and five ordered authors agree in TeX, PDF Info, XMP, publication.json and
the final response/handoff. All five user-supplied emails are visible. No old
default identity, fabricated DOI/acceptance/copyright strip or invented author
declaration appears in the article. The current official CFP was also checked.

The compiler recorder found no missing local dependency in publication.json.
The standalone source ZIP's 22 members match current sources; its read-only
exact launcher passes, and a clean build from the extracted ZIP succeeds. All
eight package-build renders exactly match the individually viewed final renders.
See source-archive.json, archive-reproduction.json, archive-build.stdout.log and
archive-build-comparison.json in the release evidence directory.

All 23 frozen mathematical inputs and immutable source.md remain byte-identical
to the accepted snapshot. Only title/float/prose and current handoff metadata
were changed. The manuscript was refrozen after these changes. The gate checks
process bindings and is not itself proof or external review.

During audit automation, Poppler bbox control characters required sanitizing
the extracted XML for parsing, and a table parser initially included its header
and TeX escaped spaces. These checker issues were corrected and exact cell
comparisons rerun; they were not document or mathematical defects.
