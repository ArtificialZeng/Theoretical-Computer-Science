# Marked-mirror language edit distance

This directory uses the supplied ACM template, with the exact class line
`\documentclass[sigconf,screen]{acmart}`. The manuscript and metadata are anonymous.

## Deliverables

- `2.pdf`: nine-page paper, including references.
- `2.tex`, `references.bib`: editable manuscript and verified references.
- `research/code/k_repair.py`: deterministic, suffix-indexed threshold algorithm with a repaired-string witness.
- `research/code/verify.py`: independent finite-language and interval oracles, exhaustive thresholds, random corruption checks, and the guarded reduction.
- `research/code/check_indexed.py`: indexed algorithm and witness verification.
- `research/results/`: actual check counts, bibliography metadata, and build evidence.
- `estimated_values.md`: records that no estimated experimental numbers were used.
- `research/audit.md`: mathematical scope, limitations, and handoff notes.

## Build and reproduce

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error 2.tex
python3 research/code/verify.py
python3 research/code/check_indexed.py
python3 research/code/k_repair.py 'aaabbb#aaabbb' 5
```

Python scripts need only the standard library. The theoretical linear preprocessing bound uses a standard linear-time LCE index; the provided comparison-sort implementation has the separately stated `O(n log²(n+2) + (k+1)²)` time bound. The scan verifier is not an implementation of linear-time LCE preprocessing.

## Readiness

The typeset artifact is complete and contains no fabricated benchmark data. It is a restricted research manuscript, not a certification that the original general-LR(1) STOC objective has been met. General-LR parameterized upper bounds, the unrestricted binary-grammar lower bound, general distinct-string parameter-only delay, real compiler integration, human-fix agreement experiments, and publication-level novelty remain unresolved. The paper states these limitations.

The source bundle omits downloaded third-party source PDFs and local audit files. No submission has been uploaded or sent anywhere.
