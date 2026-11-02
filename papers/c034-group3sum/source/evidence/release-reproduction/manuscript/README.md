# Rebuilding the working paper

Run `sh build.sh` from this directory (or invoke the script by its path).
Requirements: an installed TeX Live with pdfLaTeX, BibTeX, and the dependencies
of official acmart v2.20. No package installation or network access is needed
by the build. The script clears only its named intermediate TeX products,
runs pdfLaTeX, BibTeX, and two further pdfLaTeX passes, then copies the PDF to
`bounded-exponent-3sum-working_paper.pdf`.

`acmart.cls` is a byte-identical copy of the supplied official ACM distribution.
`alpha.bst` is an unmodified TeX Live standard bibliography style. The document
uses the class's single-column acmsmall mode, 11pt, with Letter and one-inch
text margins configured in the preamble. The class remains unmodified. The
abstract explicitly uses the normal body size. The final compiler warnings are the harmless amsart forwarding report for
the recognized `natbib=false` acmart option and a missing affiliation city. The inferred city is omitted. There are no undefined citations/references or overfull boxes.

The PDF has eight total pages, including a separate title page, bibliography and end AI
methodology statement. The current internal venue assessment is working_paper;
its uncertainty about STOC technical depth has not been upgraded by writing or
successful compilation. No submission or public posting has been performed.

Mathematical evidence and the accepted internal review live in the parent
project's research/ and audit/ directories. A fresh release phase must audit
citations, clean-build/ZIP reproduction and rendered pages before local release.
