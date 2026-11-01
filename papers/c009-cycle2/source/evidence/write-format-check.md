# Submission format checked before build

Job: `c009-cycle2-write-9354f37401a8`. Checked 2026-11-01 against the live official primary CFP:
https://acm-stoc.org/stoc2027/stoc2027-cfp.html

The root-retrieved input at `research/continuous/batches/20261101-009/official-cfp.html` was also read. The actual current submission rules are: named, nonanonymous title page with affiliations and abstract; single-column, single-spaced text; at least 11-point main type; letter paper; one-inch margins. The initial twelve pages following the title page should explain importance, prior work and ideas; the CFP imposes no total submission page limit. The project's stricter twelve-TOTAL-page ceiling remains in force here. The separate twelve-page sigconf rule is explicitly for accepted proceedings versions, not the current submission format.

The manuscript uses the unmodified official acmart class from the user-designated downloaded distribution. The acmsmall/nonacm/11pt options supply a single-column, single-spaced base, with document-level letter-paper/one-inch geometry settings. The manuscript option was initially tried, but acmart enforces one-and-a-half spacing in that option and rejects a document-level change; that actual failed build is preserved in `evidence/write-build-attempt1.log`. Switching to the existing acmsmall option meets the submission rules without modifying the class or disabling its checks. A separate title page includes the sole designated author, institution and email. References use alphanumeric labels. Substantive Codex assistance is disclosed factually at the end, without claiming human verification or external review.

This is local manuscript preparation only. No submission, upload, contact or email is performed; no venue suitability or acceptance claim follows from formatting.
