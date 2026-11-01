# Local manuscript build

Build from this directory with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The local `acmart.cls` is an unchanged copy from the user-designated official
ACM distribution. The submission layout uses acmsmall/nonacm, 11pt, letter paper,
single spacing and document-level one-inch geometry. It is not the two-column
camera-ready sigconf layout. No submission has been made.

Run `python3 verify.py` without optimization. The complete code is included
verbatim in the paper through `lstinputlisting` and uses only the standard library.
The body states the exact scope and substantial AI assistance. The draft remains
subject to the separate citation/build/visual release review.
