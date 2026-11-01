.PHONY: all check clean
all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
check:
	python3 -B reproduce.py
clean:
	latexmk -c main.tex
