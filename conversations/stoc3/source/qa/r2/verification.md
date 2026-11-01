# Revision 2 verification

Final document: 18 PDF pages = separate title page + 12 numbered main-text pages + appendices and references. The review-format source uses `article` at 11pt, Letter, normal single spacing, and 1.05-inch geometry margins. Alphanumeric bibliography contains 17 cited entries. The original 9-page anonymous ACM sigconf version is preserved in history.

PDF metadata and title-page text contain all five supplied author names, affiliations and emails in the requested order. Zijian Zeng is labeled corresponding author. XML extraction reports normal roman text size 11; content bounds are at least 74bp from the left edge and at most 539bp on the right, on a 612bp-wide page. The configured vertical margins are also 1.05 inches. Mathematical scripts and algorithm line numbers use their usual smaller sizes.

Title, main results, reduction and upper-bound diagrams, proof/algorithm pages, measured tables and plots, appendix provenance and references were rendered and visually inspected during revision. The arrow formula fits its box and floats no longer intervene inside the reachability proof. No overfull boxes, undefined references/citations, placeholder URLs or anonymous-author remnants remain in the final build.

The source ZIP was extracted into a fresh directory and rebuilt through the included build script. Its pdftotext output is identical to that of the delivered PDF; its build also has no overfull boxes or undefined references.

Executable evidence: 225 exhaustive OV cases, the same 225 arrow-only cases, 2,000 cyclic queries (including the splitter pipeline), 3,000 splitter/Moore graph comparisons, the exact 323-state cycle orbit, four frontend judgments and the tsc fixture. Seeds, measured data and phase timing observations are included in the artifact. Table sizes satisfy n=nv+ne, and every quotient visit count is below 2*qG*qH.

Public artifact release: https://github.com/ArtificialZeng/musub-artifact/releases/tag/musub-r2 . Commit: 87ad1b7f6e5c603a94bdbe2e1fb6a71cc70c8f2c. All 25 remote file blob hashes match the local published payload. Ordinary Git transport failed due a local dead proxy and an HTTP/2 connection error; the GitHub API publication and subsequent content verification succeeded.

These records document performed checks. They do not certify independent human proof review, originality, conference acceptance or completion of the required author video/submission declarations.
