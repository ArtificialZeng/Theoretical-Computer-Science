LATEXMK ?= latexmk

.PHONY: all clean
all:
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build -jobname=aonflow-working_paper main.tex

clean:
	$(LATEXMK) -C -outdir=build -jobname=aonflow-working_paper main.tex
