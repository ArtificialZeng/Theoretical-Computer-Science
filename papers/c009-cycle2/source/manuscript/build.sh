#!/bin/sh
set -eu
cd -- "$(dirname -- "$0")"
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
