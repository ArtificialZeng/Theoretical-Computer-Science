# Fresh clean-build audit

Job: c021-ccrapumping-release-92d7dacdae19.

Evidence snapshot: fb196911906a12d3f006a58d590694062481bf6aa44e05c6691883c3e220d3cf.
Manuscript snapshot: 99eb0bd7c1fdc78cfa6c6d2b1e58391d7bde1db59600709934d6a48a747cdfff.
PDF SHA-256: a9c5a9244838f61a7c8fcd01a8ef0902229b629de8e3ba55d917e0c639c5f27b.

Verdict: accept. Both latexmk -C -r latexmkrc main.tex and latexmk -r latexmkrc main.tex were independently run in manuscript/ and exited zero. Command records and full transcripts are evidence/release/build-commands.json, clean.log and build.log. Current copied transcript is manuscript/build/build.log; authoritative final engine log is manuscript/build/main.log, with digest in build.json. BibTeX processed all four records with zero warning calls. First-pass unresolved-reference messages in the multi-pass transcript were resolved by later passes; the final engine log contains none.

The final log has no compiler error, undefined citation/reference, missing glyph, overfull or underfull box. The sole nonfatal acmart warning is absent author city; the supplied affiliation/email are preserved without inventing a campus. pdfinfo confirms nine total Letter pages, PDF 1.7, no encryption or JavaScript, correct title and acmart v2.20 creator. pdffonts reports all fonts embedded with Unicode mappings; no Type 3 font. Text extraction is nonempty. The body, abstract and bibliography are normal 11pt; mathematical scripts and running-head/contact furniture use normal class sizes. Font inspection is evidence/release/font-check.json. The unmodified class, style and original source files independently match the user-designated official ACM distribution by SHA-256; comparison paths and hashes are in dependency-check.json.

Current official STOC 2027 CFP (https://acm-stoc.org/stoc2027/stoc2027-cfp.html), checked this release date, requires a named title page, single-column/single-spaced text at least 11pt, Letter paper and 1-inch margins, and disclosure of substantive AI use. These are present; the stricter user cap of 12 total pages is met. The AI paragraph identifies Codex and all materially affected sections, with research role described. Formatting and local checks do not imply STOC acceptance, submission or mathematical certification. No external action was performed.

The PDF skill was read and its required edit marker ran successfully before authoring in this context. A read-only comparison initially guessed a nonexisting parent path, then was corrected to actual nested distribution files; operations.md preserves the failure. This did not affect the clean build or mathematics. Frozen evidence/source.md remain unchanged; freeze-manuscript succeeded after the editorial-only rebuild.
