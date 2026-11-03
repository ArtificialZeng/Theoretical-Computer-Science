# Reproducing the supplied code

Run from the extracted source-package root with Python 3. The following
self-contained finite checkers use the Python standard library:

```sh
python3 evidence/check_compiled_poisson.py
python3 evidence/check_compiled_oracle_integration.py
python3 evidence/check_rounded_oracle.py
python3 evidence/check_offline_composition.py
python3 evidence/check_bounded_exponential.py
```

The first four use exact rational arithmetic for their specified finite
fixtures. The last uses exact rational operations under test and 130-digit
Decimal exp/log comparisons as numerical smoke tests; those comparisons are
not certified intervals. The paper's universal bounds are analytic proofs.
These scripts do not execute or benchmark the full algorithm at its prescribed
large clock parameter, and finite success does not establish an infinite
theorem. Their output JSON files state the actual coverage.

The archive also includes the original fresh-review code
`audit/referee-checks.py`. Its complete main routine additionally rehashes
every file in `audit/snapshot.json`, including three cached primary-paper
PDFs. Third-party full texts are not redistributed in this source archive.
To rerun that full routine, retrieve these exact primary inputs into the
indicated paths and check their SHA-256 values against the snapshot:

- `intake/primary/2610.18337.pdf`: https://arxiv.org/pdf/2610.18337v2
- `intake/primary/2502.10348.pdf`: https://arxiv.org/pdf/2502.10348v1
- `intake/primary/2410.17179.pdf`: https://arxiv.org/pdf/2410.17179v1

Then run `python3 audit/referee-checks.py`. Its finite synchronous-reference
checks and the integrity assertions are separate operations. Do not remove
an integrity check and describe the modified run as a reproduction of the
original review. The five commands above require no third-party paper files.

For the manuscript build, follow the package README/build script. Official
unmodified acmart class/BibTeX files and their original dtx/ins/README source
companions are included. A TeX distribution and the indicated installed
packages/fonts are required; Poppler is used only for PDF inspection/rendering.

The actual internal venue classification is `working_paper`. Reproduction,
compilation and internal review are not external peer review or a STOC decision.
