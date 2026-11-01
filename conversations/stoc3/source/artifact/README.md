# muSub artifact — revision 2

Reproducibility artifact for **Is Quadratic Subtyping Optimal? Conditional Hardness on Shared Acyclic Type Graphs**, by Zijian Zeng, Jiayin Cao, Weinan Dai, Rui Wang, and Fei Ding.

Release: `musub-r2` (software version 0.2.0). This repository contains the graph checkers, validation scripts, measured synthetic runs, and coverage-qualified corpus summaries. The manuscript is distributed separately. OpenAI Codex materially assisted with implementation and preparation; executable checks and mathematical proofs are separate evidence.

## Reproduce the checks

Recorded environment: Node.js v25.5.0, Apple M3 Pro (arm64); TypeScript syntax API 5.9.3. Install the exact dependency lockfile, then run:

```sh
npm ci
npm test
node bench.mjs
```

`npm test` runs:

```sh
node validate.mjs
node validate-splitter.mjs
node extra-validation.mjs
node frontend-validation.mjs
node node_modules/typescript/bin/tsc --noEmit --strict --skipLibCheck example.ts
```

- `core.mjs`: normalized KPS-style subtyping product, independently decomposed descending fixed-point oracle, union-find equality, Moore reference quotient, and the OV generator.
- `splitter.mjs`: sparse smaller-half partition refinement. Incoming predecessors are snapshotted before the splitter is mutated; pending splitters retain both children, while consumed splitters schedule only the smaller child. Work counters expose graph operations. Map/Set costs are those of the JavaScript runtime.
- `pipeline.mjs`: revised `runMuSub` pipeline using the splitter, with separately timed equality, minimization, search, and wall-clock total. `core.mjs` retains its Moore-based `musub` as a reference.
- `validate.mjs`: all 225 nonempty subset-pairs of two-dimensional OV and 2,000 seeded cyclic queries, seed 1701; both quotient pipelines are checked against direct/vector or fixed-point decisions. Equality is checked independently by synchronous exploration.
- `validate-splitter.mjs`: 3,000 seeded graph comparisons with Moore and successor-stability checks, seed 20271031.
- `extra-validation.mjs`: 225 arrow-only OV cases and a 17/19 cycle product with exactly 323 states.
- `frontend-validation.mjs`: four projected directional queries, plus a TypeScript fixture checked by tsc in the test command.

These are bounded executable validations. They do not establish theorem originality or replace mathematical proofs.

## Raw synthetic data and size convention

`bench-results.json` contains all seven measured repetitions after two warmups for each size, plus medians. Generation is excluded. Equality, both graph minimizations, and quotient-product search are included in the optimized total. The total is timed over the full pipeline; separate phase medians need not add to its median.

Every row reports:

- `nv`: total vertices, `ne`: total edges, and `n = nv + ne` (the theoretical convention).
- `baselinePairs`: expanded states on original graphs.
- `quotientPairs`: expanded states on quotient graphs.
- `quotient`: the two quotient vertex counts; `quotientProductBound = 2*qG*qH`.
- `equalityMs`, `minimizationMs`, `searchMs`, `totalMs`, and `baselineMs`.
- Per-run smaller-half work counters.

The synthetic family is intentionally compressible: `a_i = (bin(i), 0^L, 1)` and `b_j = (0^L, bin(j), 1)`. Its timings illustrate state reduction, not OVH or end-to-end compiler acceleration. The previous manuscript's Moore timings are not reused as if they were splitter measurements.

## Corpus scan and coverage

Pinned DefinitelyTyped commit: `72e15dbdd8088284d3f0387a05539e7c2e6c743b`.

```sh
curl -L --fail https://codeload.github.com/DefinitelyTyped/DefinitelyTyped/tar.gz/72e15dbdd8088284d3f0387a05539e7c2e6c743b -o DefinitelyTyped.tar.gz
tar -xzf DefinitelyTyped.tar.gz
node corpus.mjs DefinitelyTyped-72e15dbdd8088284d3f0387a05539e7c2e6c743b/types
```

The ordered relative-path/content digest is `a2e28632e9fd2a9d838ac94f0c7afaee8bbd3acd2249cb77978390a85e0b4ce4`. The scan covers 23,098 `.d.ts` files, 59,949 file-top-level candidates, and 4,072 accepted roots (6.79%). DFS back-edge counts are 4,069 roots with zero and three with one. Quotient bins are 4,007 roots at 1–4 states, 64 at 5–16, and one at 17–64.

The projection accepts required fields, primitive leaves, unary functions, unknown/never, and local nongeneric references. It rejects inheritance, merged declarations, imports, nested declarations, generics, optional members, unions, and unsupported dependencies. Fields become immutable and primitive names become distinct atomic leaves. This changes some tsc assignability rules, including those for empty records and void. Coverage is reported against top-level candidates, not every nested declaration.

The Scala-like parser accepts explicit equation interchange syntax with val fields, unary arrows, Any, and Nothing. It is not a Scala compiler frontend. `example.scala-subset` intentionally identifies that scope.

`corpus-summary.json` contains coverage, digest, bins, and single-pass query percentiles; `corpus-roots.json` contains every accepted root's path, name, vertex/edge counts, DFS count, and quotient size; `corpus-queries.json` records artificial adjacent-root queries. These queries are not tsc traces. The corpus remains on the validated Moore reference for quotient statistics, yielding the same mathematical quotient; no corpus re-timing is claimed in this revision.

## Provenance

`SHA256SUMS` records the released source/data contents. DefinitelyTyped source is downloaded by the pinned command and is not vendored. Generated dependency directories, credentials, personal workspace paths, and manuscript/reviewer files are excluded from the public artifact.
