# Clean build audit

Job: c029-vftfast-release-bdd37c945f4e. Checked 2026-11-02 UTC.

Mathematical snapshot: b1495a4cbeb794181b64a2bc9a00b637d90f0a7a7fdf654844a24036b4029e66.
Manuscript snapshot: 8013342c36141de01d96e75509498833a97008d1df48c6153524aefa6caa4daa.
PDF SHA-256: 8f61902bb7427aec09254cd8ac7566c87a76748f4dc9eb4d9bbed9828af7a7a8.

Verdict: accept. A source ZIP containing exactly the listed publication inputs plus publication.json was extracted under tmp/pdfs/release-reproduce/. Generated bbl, aux, out, log and PDF were absent before the first build. The supplied sh manuscript/build.sh completed with LaTeX/BibTeX. The final clean compiler log is audit/release-clean-build.log; console history is tmp/pdfs/release-reproduce-console.log. The isolated output PDF and bbl are byte-identical to the current final outputs. Details, archive digest and official-template comparisons are in audit/release-reproduction.json.

Final compiler/BibTeX checks: zero compilation errors, undefined citations/references, overfull boxes or missing bibliography fields. Two nonfatal diagnostics are retained: acmart reports no city for the affiliation, because the user supplied no city; one bibliography underfull hbox has badness 1158. The final rendered references are readable and the warning causes no clipping or overlap.

PDF validation: genuine PDF 1.7, seven letter-size pages, no encryption or JavaScript, nonempty text extraction, all listed fonts embedded. Metadata title matches the manuscript; the Author metadata field is empty, while title page and contact footnote correctly name the sole author Zijian Zeng, UCSI University, with the supplied email. No conflicting author metadata exists. The unmodified official class and bibliography style match the designated distribution byte for byte. The 12-total-page cap is met.

Current STOC CFP was refreshed at https://acm-stoc.org/stoc2027/stoc2027-cfp.html on 2026-11-02: named title page, at least 11pt, single column/single spacing, letter paper and one-inch margins are the submission guidelines. Numerical reference labels are permitted though alphanumeric labels are recommended; the user-designated ACM style is retained. Substantial AI roles are disclosed in body and endmatter, with references last. Formatting does not upgrade the actual working_paper assessment. No external submission is authorized or performed.

An official-template path lookup failed only while assembling the reproduction record; it was repaired using the actual distribution/acmart location. The builds had succeeded, and their hashes were verified separately. This operational detail is recorded in audit/release-operational.md, without changing mathematical evidence or counters.
