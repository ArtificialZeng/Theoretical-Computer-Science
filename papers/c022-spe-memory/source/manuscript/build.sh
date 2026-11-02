#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build ../output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory=build main.tex > build/pass-1.txt 2>&1
bibtex build/main > build/bibtex.txt 2>&1
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory=build main.tex > build/pass-2.txt 2>&1
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory=build main.tex > build/pass-3.txt 2>&1
cp build/main.pdf ../output/pdf/spe-memory-working_paper.pdf
