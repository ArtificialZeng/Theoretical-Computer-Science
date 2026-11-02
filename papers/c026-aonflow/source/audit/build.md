# Fresh clean-build audit

Job: c026-aonflow-release-7db9e6fea069. Checked 2026-11-02T01:01:23.276353+00:00.
Verdict: accept. Bindings are in audit/build.json.

Ran make clean then make all in manuscript/ after the purely editorial release edits. Actual transcript: evidence/release-7db9e6fea069-build.log. The final compiler log is manuscript/build/aonflow-working_paper.log; the corresponding .blg was inspected. The final log has no warning/error, undefined citation/reference, overfull/underfull box or missing-character diagnostic. Any first-pass unresolved references in the multi-pass transcript are resolved by latexmk; the bound final compiler log is clean.

The PDF header is valid; pdfinfo reports seven letter-size pages, no encryption/forms/JavaScript, and the correct title. Full pdftotext extraction is nonempty and agrees with the manuscript. All 14 listed font subsets are embedded with Unicode mappings. Exactly one author/contact matches authors.json; references and symbols are resolved. The five official ACM input copies were independently compared byte for byte with the user-designated official distribution (evidence/release-7db9e6fea069-template-check.json).

Source dependency checks, frozen-mathematics integrity and retained classification are in evidence/release-7db9e6fea069-preflight.json. The 14 frozen mathematical files and all previous referee/innovation/STOC verdicts are unchanged. The unnecessary constant-factor encoding sentence was replaced by polynomially bounded growth, as required by the supervisor handoff; this corrects excess prose without changing the accepted algorithm or proof requirements. The body now also identifies substantive Codex assistance. Original writer bytes and prior manuscript snapshot were archived before editing. The rebuilt manuscript was refrozen with the existing accepted mathematical snapshot.

Portable ZIP: evidence/release-7db9e6fea069-working_paper-source.zip. It contains all source_files, official ancillary inputs, exact original scope, accepted proof proposal, author record, retained venue assessment, and the advertised standalone finite checker. Extracted archive inputs were hash checked, a clean build succeeded, the regenerated bibliography bytes and entire extracted PDF text agree, and all seven rendered page PNGs agree exactly at 105 dpi. The extracted checker passed. PDF container bytes differ because build metadata/trailer identifiers differ; byte reproducibility is not asserted. See evidence/release-7db9e6fea069-zip-reproduction.json and its build/checker records. These finite checks do not implement the full algorithm or replace mathematical review.

The retained label is working_paper. No submission, publication activation, upload, email or contact was performed.
