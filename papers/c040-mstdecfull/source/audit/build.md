# Clean build audit

Job: c040-mstdecfull-release-2ca818aceb48. A real latexmk -C main.tex cleanup was followed by latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex in manuscript/. The command exited zero. Final manuscript/main.log and main.blg were inspected, with stdout retained in evidence/release-2ca818aceb48/build-output.txt.

The final log contains no fatal errors, unresolved citations/references or overfull/underfull boxes. The official class warns only that no affiliation city was supplied; the author supplied institution/country/email are intact. BibTeX warns about optional missing publisher addresses for the COLT and SODA entries. No city/address was invented. These are metadata completeness notices, not failed compilation or unresolved references. All 16 listed fonts are embedded Type 1 fonts. PDF header, readable text extraction, title, version1.7, nonencrypted/nonform state and US Letter612x792pt pages were checked. Visible sole author is Zijian Zeng, UCSI University, with the required email; the generic PDF Author field is absent rather than carrying another author.

There are 8 total pages, within the user's 12-total-page cap. The current official STOC CFP was checked: nonanonymous, separate title/abstract cover, single-column >=11pt single-spaced text and one-inch margins. The official acmart v2.20 class and bibliography style match the downloaded official files byte-for-byte. No official class/BST changes were made.

The complete source ZIP was freshly extracted inside the project and compiled successfully. Every extracted input equals the frozen source, including the regenerated bbl. Extracted text and all eight115dpi page render hashes match exactly. PDF byte hashes differ because compilation metadata varies; byte-identical PDF reproduction is not claimed. Details: evidence/release-2ca818aceb48/zip-reproduction.json. The archive is labelled working_paper and is build evidence; the supervisor owns final packaging/publication.

Final build log SHA-256: d17727b8f8ec473b052fe1689ca049ad0b1170f8730d269c4cac17b6e0f9d9e6.
Snapshot: 3a7133dbcc463bfba827578e6a5a4028802dc5a73d23c647e733201b0be99d76.
Manuscript: 203aa4452ff612d76a7e2cf95734dfb62d168580ad5fa1fe30831cf086035682.
PDF: f6bec7b5610084cfee824109f3245bd1fc875a19f4aa87d77f1ffecb2adb9660.
