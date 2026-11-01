# Fresh primary-source check

Job: `robust-stopping-referee-e7c6798337e7`.

The official [PMLR record](https://proceedings.mlr.press/v306/kim26l.html)
was reopened read-only. It identifies Kim and Fan, ICML 2026, volume 306,
pages 57411--57444, and links the repository
<https://github.com/JihwanKim4689/distributional-ski-rental> as Software.
The repository landing page lists both frozen Python filenames.

I extracted the complete frozen proceedings PDF afresh with `pdftotext
-layout`. Its 560062 bytes have SHA-256
`5c5842ff3d0d2df8b802bc9968d520410ade6a059f83b3ca9fb1ac6a8f53ec4c`;
all 34 pages extract and the extraction matches the frozen source extraction.
The fresh extraction is `referee-e7c6798337e7-published-extract.txt`.
Printed page 7 supplies the relevant cost, pointwise robustness and expected
objective; pages 29--30 supply D.2. The precise erroneous inference is present
on printed page 30. No equality of all versions or all results is inferred.

The [arXiv v1 primary HTML](https://arxiv.org/html/2603.29233v1)
was also reopened at C.4 Theorem C.1(ii) and D.2--D.4. The one-hot capped
geometric structure and the original support-level inference are present.
The correction is confined to the latter inference.

The [commit-pinned Table2 raw source](https://raw.githubusercontent.com/JihwanKim4689/distributional-ski-rental/0a86125f31e9e1b1abbba5bd4fde32a332860124/Table2_Consistency_Comparison_under_Fixed_Robustness.py)
was available in the web reader. The matching Figure1 endpoint and GitHub
commit/tree/blob endpoints returned cache misses; shell URL access returned
DNS errors. These failures are recorded in
`referee-e7c6798337e7-source-refresh.json`. I do not represent those failed
refreshes as external authentication of both complete file hashes. The
full hashes and archived commit association are supplied in the frozen
`revision/published-extension-provenance.json`; I independently checked the
actual frozen bytes and executed both unchanged classes. Thus the observations
are reproducibly bound to those exact bytes and the supplied pinned-source
provenance. They do not depend on a claim about the current repository head.

For nearby-model comparison I reopened the primary statements in
[Li--Christianson--Li v1](https://arxiv.org/html/2510.14887v1),
[DKT et al.](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf),
and [Cui--Dinitz v1](https://arxiv.org/html/2602.21104v1).
The claim must retain the acknowledged one-hot overlap and bounded novelty
language. This report is not a comprehensive historical-priority certificate
or a final manuscript bibliography audit.

All accesses were read-only. No submission, message, upload or account action
occurred, and no third-party source or frozen input was edited.
