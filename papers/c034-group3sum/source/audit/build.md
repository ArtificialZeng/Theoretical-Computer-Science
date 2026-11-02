# Clean build audit

Job: c034-group3sum-release-5f0540aba52c; 2026-11-02 UTC.
Verdict: accept for the current digest-bound working_paper artifact.

Ran sh manuscript/build.sh, clearing its named intermediate products and running
pdfLaTeX, BibTeX and two more pdfLaTeX passes. Read the real final log at
manuscript/build/main.log, console logs and main.blg. There is no fatal error,
undefined citation/reference, BibTeX warning, overfull or underfull box. Only the
natbib=false option forwarded to amsart and the intentionally omitted city give
benign warnings. The inferred city was removed; the existing Malaysia country
field remains. Earlier missing-country build failures are preserved in evidence;
they are operational events, not mathematical evidence. No class check was
disabled. A broad diagnostic initially matched the zero-valued BibTeX warning$
function counter; the actual warning-message check passes.

Official acmart v2.20 is byte-identical to the supplied distribution. It loads
amsart with 11pt: nominal body size is 10.95 TeX points, recorded as size 11 by
Poppler at zoom 1. Body and abstract are normal single-spaced type. The PDF has
eight 612x792-point Letter pages with a 468x648-point text area at one-inch
margins. Running heads, affiliation/contact and bibliography use the standard
class's smaller ancillary type; math subscripts are naturally smaller. All PDF
fonts are embedded. No Type 3 text is present.

pdfinfo confirms eight pages, no encryption or JavaScript, correct title and
actual acmart/TeX creator metadata. There is no separate Author metadata field;
visible title/contact information correctly names only Zijian Zeng, UCSI
University, 1002266693@ucsiuniversity.edu.my, with no conflicting metadata.
The distinct first page contains title, author/affiliation, abstract and contact;
main presentation follows. The eight-page PDF satisfies the 12 TOTAL page cap.
Both body and terminal AI statements disclose the actual model proof/code roles.
The current official STOC CFP was checked on 2026-11-02 UTC at
https://acm-stoc.org/stoc2027/stoc2027-cfp.html: nonanonymous submission,
single-column presentation and material-AI body/end disclosure are observed.
The actual internal assessment remains working_paper.

## Source ZIP reproduction

manuscript/bounded-exponent-3sum-sources-working_paper.zip contains publication.json
and every declared source. Unpacked it inside evidence/release-reproduction and
rebuilt from scratch successfully without network access. The recorder identifies
only declared local TeX/class/BBL inputs or generated aux/out files; the BibTeX
log confirms the declared database and style. Full extracted page text including
page breaks is identical, and the rebuilt BBL bytes are identical. PDF byte
identity is not claimed because TeX dates/trailer identifiers differ. Coverage,
hashes and recorder inputs are in evidence/release-reproduction.json. The audits
bind the reviewed original PDF and its actual log, not the reproduction output.
