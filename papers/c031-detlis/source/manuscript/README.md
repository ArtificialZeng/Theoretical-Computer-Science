# Deterministic two-dimensional Range-LIS reporting

This is the writing-stage source package for the accepted full-resolution
mathematical snapshot. Its actual internal STOC assessment is **working_paper**.
It is not an external peer-review decision, a final release audit, or an
authorization to submit or upload. The sole author is Zijian Zeng, UCSI
University, 1002266693@ucsiuniversity.edu.my.

## Build

From the package root run:

```sh
python3 manuscript/build.py
```

This clean-builds `manuscript/main.pdf` using installed `latexmk`, `pdflatex`
and `bibtex`, the included unmodified official `acmart.cls` (v2.20), and the
included `alphaurl.bst`. Standard TeX Live packages and fonts are required;
the script does not install anything or contact the network. It removes
only known generated `main.*` build files. The fixed public build timestamp
supports deterministic reproduction. `main.bbl` is included for convenience
and is regenerated from the authoritative source `references.bib`.

The document applies the current initial-submission layout in its own source:
single column, single spacing, 11pt body/references, Letter, 1in margins and
a distinct identified-author title page. The official class is unchanged.
Its `acmsmall` single-column base avoids the `manuscript` option's automatic
one-and-a-half spacing. The sigconf requirement in the official CFP concerns
accepted proceedings, not initial submissions. The project imposes a stricter
12-total-page cap. The writing-stage build has 9 total pages.

## Reproduce finite diagnostics

From an extracted package root run:

```sh
python3 manuscript/reproduce.py
```

Only Python 3 standard-library modules are required. The entry point copies
the scripts into an isolated temporary tree, preserving the original relative
`evidence/` and `intake/root-diagnostics/` dependency layout, runs them there,
and compares scientific counts with the included references. Frozen project
reports are not overwritten. The copied independent checker is byte-identical
to the separately written referee diagnostic; it imports no candidate code.
The job IDs embedded in copied diagnostic reports describe their original
provenance, not this reproduction run or a new referee decision.

Expected research counts: 24 local fixtures, 16,830 table states, 2,816 candidate
scores, 176 growth steps, 10,495 trace memberships, 14 merge nodes, and 10,542
invariant checks; 19 certified compressions, three uncertified and two all-dummy
fixtures. Seven exact uniform-parameter cases include large integers but do not
allocate the uniform production sampler.

Expected independent counts: 1,236 inputs, 35,318 subpath identities, 21,850
localized traces, 330,120 short-query/threshold cases, 88,758 stitching pivots,
2,160 rounded-table entries, 512 aggregate scores and 64 compression steps;
eight of sixteen manual compression fixtures have certified initial potentials.

The remaining fixtures assert only their documented algebraic identities.
These are finite diagnostics rather than a production implementation,
asymptotic benchmark, infinite proof, novelty certificate or venue assessment.
The self-contained manuscript supplies the mathematical argument. Substantial
Codex assistance is disclosed in the body and final methodology statement.

The release role must independently review citations/build/every page and
reproduce the **actual final delivered ZIP**. Passing a check of this checkout
does not waive that later requirement. No external submission is authorized.
