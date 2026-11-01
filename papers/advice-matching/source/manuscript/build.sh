#!/bin/sh
set -eu
cd "$(dirname "$0")"
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -recorder main.tex
