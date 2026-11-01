# OctaFine: revised manuscript and complete finite-check artifact

`5.pdf` is the revised full manuscript. `5_source.zip` includes the editable manuscript, the complete finite-check artifact, raw fixtures, logs and the pinned ELINA scalar-kernel source subset. No external submission or public repository was created. `response_to_reviewers.md` maps every review point to the revision, and distinguishes completed corrections from remaining originality assessment and whole-analyzer experiments.

## Manuscript build

```sh
make -f Makefile.octafine pdf
```

Requires a modern TeX distribution, latexmk, BibTeX, TikZ, and the supplied acmart dependencies. The local unmodified acmart v2.20 is retained. The revised source uses 11pt manuscript mode, one column, single spacing, Letter paper and one-inch margins, following the user's superseding official-CFP instruction. The source explicitly adjusts acmart's manuscript 1.5-spacing default and its baseline guard to satisfy the single-spacing requirement. The five author names, order, institutions and emails are user-supplied. `alphaurl.bst` provides alphabetic labels and linked source URLs. `5.bbl` is included for a direct pdflatex build.

All tables and figures occur between complete source paragraphs with `[H]` placement. A complete width theorem/proof appears within the first twelve body pages. The second figure now visualizes the incremental construction instead of duplicating the operation table.

## Reproduce the recorded inputs without randomness

```sh
make -f Makefile.octafine replay
```

This builds the original ELINA scalar kernel, loads every archived input, reruns its mathematical assertions, and compares complete outputs and SHA-256 digests with the recorded outputs. It invokes no random generator. The result is 7,250 reference cases plus 1,000 separate ELINA cases comparing 389,512 entries. `artifact/logs/archive-replay.log` is the actual recorded replay output.

The kernel build script chooses `-dynamiclib`/`.dylib` on macOS and `-shared`/`.so` on Linux. It uses `CC` if set, otherwise clang on macOS and cc elsewhere. GMP and MPFR development headers must be installed; `/opt/homebrew/include` and `/usr/local/include` are searched when present. A nonstandard include directory can be added to `artifact/build_elina.py`. The archived run used macOS arm64 and Apple clang; Linux portability is encoded in the build script but has not been tested on a Linux machine here.

## Regenerate the same seeded streams

```sh
python3 artifact/validate.py --verify-fixtures artifact/reference_cases.jsonl.gz
python3 artifact/elina_compare.py --verify-fixtures artifact/elina_cases.jsonl.gz
python3 artifact/make_parameter_table.py
```

The seeds are 20271031 (reference suites) and 20271032 (ELINA). These commands rerun the generators and assert byte-identical fixture streams on the recorded Python generation behavior. The randomness-free replay above is the reproducibility path when random-library behavior differs between interpreter versions.

The original five suites remain 5,000 parity/model cases, 600 bounded enumeration cases, 400 product encodings, 250 incremental product encodings checked at every prefix, and 500 elimination cases: 6,750 in total. A new sixth suite adds 500 direct graph embeddings to validate the strengthened exponent-preserving reduction. The separate 1,000 ELINA cases retain the original matrix-entry total.

## Raw records and parameter distributions

- `artifact/reference_cases.jsonl.gz`: all 7,250 generated inputs, size/edge parameters, rational/integer feasibility labels, full checked outputs, output digests, and per-case pass records.
- `artifact/elina_cases.jsonl.gz`: all 1,000 ELINA inputs and both full reference and kernel output matrices, plus dimensions, edge counts, potentials and digests.
- `artifact/results.json`, `artifact/elina_results.json`: source hashes, actual elapsed times, platform, seed, and run summaries.
- `artifact/coverage.json`: recomputed totals and complete ELINA dimension-frequency distribution.
- `artifact/parameter_table.tex`: the manuscript table generated from these records, with feasible/infeasible counts and observed edge-count ranges.
- `artifact/logs/`: actual reference, ELINA, kernel-build and archive-replay stdout.
- `artifact/MANIFEST.json`: SHA-256 checksums for source, fixtures, results, logs and vendor kernel files.

The number `m` in the coverage table counts distinct weighted records after coherent completion and before minimum coalescing of parallel bounds, except that elimination and direct-embedding cases use the original unsigned graph's edges. A case count is not an individual entry comparison count. Original and newly added suites are distinguished in `coverage.json`.

## Pinned ELINA subset

The revision is `f524156d292ac3a6f3cd676e2d2e7db6629e2b6f`. The archive includes its unmodified `elina_oct/opt_oct_closure_dense_scalar.c`, the required header subset, `REVISION`, and the upstream LGPL-3.0 license. Kernel SHA-256 is recorded in the results and manifest. No GitHub access is required to rebuild the comparison. No modifications were made to the kernel algorithm. The adapter covers feasible rational strong closure only; it does not invoke integer ELINA closure or a complete analyzer.

Upstream source: https://github.com/eth-sri/ELINA/tree/f524156d292ac3a6f3cd676e2d2e7db6629e2b6f

## Revised scientific scope

The traditional cubic APSP-hypothesis lower-bound narrative has been removed. A now gives exponent-preserving reductions and equality of the optimal dense exponents, C gives an unconditional exponent transfer, and D gives compact/dense bounds plus a general-graph combination and a width-to-product transfer. October 2026 preprints are dated and attributed; the n^(2.9945+o(1)) bound is inherited from Majdoddin's reported guarantee.

B is explicitly a classical criterion plus modern SSSP composition. No new SSSP or flow algorithm, independent validation of every argument in the new preprints, or established STOC-level originality is asserted. No experimental number is estimated. Complete SV-COMP/APRON/Crab studies remain unperformed; the current evidence is proof-oriented and kernel-level. Named human authors remain responsible for independent proof and originality verification before submission.
