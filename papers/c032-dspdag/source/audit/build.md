Job: `c032-dspdag-release-5fe4e38b60c7`. Reviewed 2026-11-02T12:51:51.063385+00:00. Research snapshot: `df4def35c3d991745cbd37b3e8238b49c3edeedc07c6350a8a195b3092c3ad02`. Manuscript snapshot: `c2916fd05375010d302349b16227c74c3b9034412b631d619036c3087052fe3f`. PDF: `04e5cdc5235be2a9327b7f80616afcc3d5854ecbab67d4f9fe5c12c23aca20f2`. This is a local internal artifact audit, not external peer review or a venue decision.

# Clean-build audit

Verdict: accept. Ran python3 manuscript/build.py from the project root. It removed the prior work directory, copied four TeX inputs, ran pdflatex, BibTeX and two resolving pdflatex passes. The four console logs, final compiler log and final BibTeX log are preserved in evidence/release/. The final compiler and BibTeX logs contain no errors, undefined citations/references, overfull/underfull boxes or warnings. First-pass reference placeholders resolve in later passes. Nine cited keys match nine bibliography entries.

The compiled PDF is eight letter-size pages (612x792 points), below the twelve-total-page user cap. Text extraction is nonempty; no placeholder citation or broken cross-reference appeared in the extracted or rendered paper. Fonts are embedded as recorded in pdffonts.txt. PDF title metadata matches the manuscript; Creator identifies unmodified acmart v2.20 and pdfTeX. PDF author metadata is absent, while the displayed sole author and contact match authors.json; this does not obscure authorship. No encryption or JavaScript is present.

The official class and BST match the user-designated unmodified distribution byte for byte. The current official STOC CFP was re-opened (cfp.txt): named authors, title page, single column, single spacing, 11pt or larger ordinary text, letter paper and one-inch margins. Initial submission differs from proceedings sigconf. Poppler XML confirms ordinary abstract/contact/body/references are 11pt or larger; smaller running furniture and mathematical scripts are separate. Substantive AI use appears in the body and final methodology paragraph. This formatting check does not promote the actual working_paper assessment.

No mathematical or frozen evidence file was modified. Preserved entry PDF/source/snapshot show the limited font/prose changes. Rebuilt and re-froze the publication. Integrity record verifies all 21 frozen scientific files. PyMuPDF was unavailable, so Poppler supplied the successful font audit; an initially incomplete official-template path was corrected. These operational events are not mathematical evidence.

## Delivered-source archive reproduction

Built output/source/dspdag-working_paper-source.zip from 41 explicit files: all publication inputs, frozen scientific evidence, accepted mathematical/innovation/STOC records and relevant reproducibility checks. Extracted the actual archive into a clean project-local directory, invoked its build.py without network or installation, and compared results. Rebuilt PDF, bibliography and extracted text are identical; PDF equality is byte-for-byte. Archive listing and all digests are in evidence/release/zip-reproduction.json. The archive contains no credential or process-environment diagnostics.

Source archive SHA-256: `8747ef7056fa81e8a3523adfa454fb3dd4426e9a1f9ebe2366bb728e5d6b7d9f`. Reproduced PDF SHA-256: `04e5cdc5235be2a9327b7f80616afcc3d5854ecbab67d4f9fe5c12c23aca20f2`.
