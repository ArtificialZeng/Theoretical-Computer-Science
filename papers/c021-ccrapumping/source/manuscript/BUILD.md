# Local manuscript build

This is the local full-scope resolution manuscript accepted in the project's
frozen mathematical review. It has not been submitted or released.

From this directory, run:

```sh
latexmk -C -r latexmkrc main.tex
latexmk -r latexmkrc main.tex
```

The PDF is `build/main.pdf`. The captured clean-build transcript is
`build/build.log`; the final engine and bibliography logs are `build/main.log`
and `build/main.blg`. `latexmkrc` adds `vendor/` to the TeX and BibTeX style
search paths. It does not install packages or require shell escape. Required
installed tools are pdfLaTeX, BibTeX and latexmk with the standard acmart
package dependencies. The build used TeX Live 2026.

The official acmart v2.20 class and ACM-Reference-Format bibliography style,
plus the class's original source, installer and README, were copied unchanged
from the user-designated official ACM distribution. Hash comparisons are
recorded in `../evidence/write/preflight.json`. No official file was patched.
The source uses the single-column `acmlarge` layout at 11pt, with Letter
paper and 1-inch margins, to follow the current STOC 2027 submission geometry.
The default `manuscript` option selects one-and-a-half spacing and disallows
changing it, so the single-spaced class option is used instead. This is a
submission-format local PDF, not a proceedings article or venue acceptance.

The named sole author, affiliation and email are from `../authors.json`.
The class emits a nonfatal warning that no city was supplied; no author campus
is inferred. This does not affect the affiliation or the supplied email.

The bibliography includes the original STACS article, its full version, and
two directly relevant structural comparisons. No user Excel bibliography was
designated. The proof is self-contained; exact computational checks remain in
the project evidence and are not used as substitutes for universal arguments.
The AI methodology paragraph discloses substantive AI use throughout.
