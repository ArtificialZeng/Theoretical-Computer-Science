#!/bin/sh
set -eu
cd "$(dirname "$0")"
# Fix only TeX's timestamp inputs so identical sources can reproduce PDF bytes.
export SOURCE_DATE_EPOCH=1793598960
export FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error -jobname=vftfast-working_paper main.tex
bibtex vftfast-working_paper
pdflatex -interaction=nonstopmode -halt-on-error -jobname=vftfast-working_paper main.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=vftfast-working_paper main.tex
