# Operational notes

Job: c021-ccrapumping-triage-d79f905080dc, 2026-11-01.

* Direct DOI opening failed in the web tool; the publisher's entity page,
  official PDF, and current arXiv records were accessible.
* Web screenshots of the official PDF failed with a cache-miss response.
  Local pdftoppm rendered the supplied official PDF instead. Both rendered
  pages were visually inspected. These are source inputs, not authored PDFs.
* sympy and fitz were unavailable in the default Python interpreter.
  Exact baseline/rank checks use Python's Fraction; no package was installed.
* An initial apply_patch attempt was rejected because it combined delete/add
  for the same path. It did not change files. A subsequent write saved
  problem.md and checkpoint.md. The immutable source was never written.
* No process/environment diagnostics, credentials, agents, external contacts,
  background workers, or edits outside the assigned project were used.

These are operational facts, not mathematical evidence. Research-pass and
revision counts remain 0; state.json is owned by the runner and was not edited.
