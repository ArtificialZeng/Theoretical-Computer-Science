# Current official STOC 2027 formatting check

Job: c021-ccrapumping-write-e0235d117feb. Checked 2026-11-01 UTC
(2026-11-02 Asia/Shanghai), using the official current CFP:
[STOC 2027 Call for Papers](https://acm-stoc.org/stoc2027/stoc2027-cfp.html).
The initially guessed `/cfp.html` address was inaccessible; following the
conference link identified the actual page above. Third-party summaries
were discovery leads, not the basis for the choices below.

The official submission rules specify a title page with names, affiliations
and abstract, single-column 11-point or larger text, single spacing, Letter
paper and 1-inch margins. Submissions are not anonymous. No submission page
limit is imposed by that CFP, but the user's stricter 12 TOTAL page cap is
binding here. The official proceedings instructions separately require
`sigconf` and 12 pages; that is not the initial submission format.

The prepared PDF uses the user's unmodified official acmart v2.20 inputs
in a single-column class option with 11pt body, abstract and bibliography,
Letter stock and 1-inch margins. It has a separate named title page and
nine total pages. A substantial AI methodology statement describes the
actual use of Codex in proof work, diagnostics, literature and writing.
The original `manuscript` option's hard-coded one-and-a-half spacing
caused a class error when single spacing was requested. That failed build
is retained in build-attempt1.log; the final source uses `acmlarge` with
no line-spacing override and no modification to the class itself.

Current CFP public-posting, author responsibility and video requirements
concern a future external submission. This job prepared local files only;
no submission, public posting, upload, contact or email was performed.
No claim of STOC quality, selection or acceptance follows from formatting.
