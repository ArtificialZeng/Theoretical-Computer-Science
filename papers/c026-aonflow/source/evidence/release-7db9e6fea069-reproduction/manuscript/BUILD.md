# Local build

Run `make all` from this directory with an installed TeX Live distribution,
`latexmk`, `pdflatex` and `bibtex`. No system packages are installed by this
project. The target is `build/aonflow-working_paper.pdf`.

`make clean` removes this target's generated build files. A complete clean
build is `make clean && make all`. The official `acmart.cls` v2.20 and
`ACM-Reference-Format.bst` are unmodified copies of the user-specified
download. Their accompanying source and README are included locally.

The document is a single-column 11pt letter-paper submission-format draft,
with one-inch margins and a separate title/abstract page. It has seven total
pages. The project cap is twelve total pages, including references.
The retained internal classification is `working_paper`. Mathematical
acceptance does not promote that label or replace the separate release gate.
