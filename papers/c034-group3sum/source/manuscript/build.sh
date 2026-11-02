#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build
rm -f build/main.aux build/main.bbl build/main.blg build/main.log build/main.out build/main.pdf
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex > build/latex-pass1.log 2>&1
(cd build && BIBINPUTS=.. BSTINPUTS=.. bibtex main > bibtex-console.log 2>&1)
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex > build/latex-pass2.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex > build/latex-pass3.log 2>&1
cp build/main.pdf bounded-exponent-3sum-working_paper.pdf
