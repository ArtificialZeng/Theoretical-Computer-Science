#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build artifact/records
python3 artifact/validate.py
python3 artifact/audit_records.py
python3 artifact/make_table.py
python3 artifact/pack_artifact.py
cp artifact/treeflow-artifact-v2.zip treeflow-artifact-v2.zip
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build 4.tex
cp build/4.pdf 4.pdf
pdftotext -layout 4.pdf build/4.txt
python3 artifact/check_submission.py
