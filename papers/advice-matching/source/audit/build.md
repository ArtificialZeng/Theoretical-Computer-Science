# Fresh release build audit

Job: `advice-matching-release-01731cae3c13`. Verdict: **accept**.

Ran `sh manuscript/build.sh` in the foreground. It performs `latexmk -C` and
then pdfLaTeX/BibTeX with halt-on-error and recorder enabled. Exit status was
zero; the actual transcript is audit/release-build.log. Initial clean-build
passes naturally precede bibliography/cross-reference resolution; the bound
compiler log is the final `manuscript/main.log`, not an earlier pass. Read its
diagnostics and completion, the BibTeX log and latexmk's final success output.
The final TeX log has zero warnings, undefined citations/references, overfull
or underfull boxes, or errors. BibTeX processed six entries with zero warnings.

The PDF has 6 total US Letter pages, including its separate cover and final
bibliography, below the 12-page limit. Text extraction is nonempty. The official
acmart 2.20 class is byte-identical to template/acmart.cls; manuscript mode,
11pt text/caption/references, single spacing and nominal one-inch margins are
configured in main.tex. Caption size was checked through Poppler font data.
All used fonts are embedded. All five authors occur in the supplied order in
Info and XMP, with all supplied institutions and emails in XMP and the cover.
No publisher/journal type, fictitious DOI, review strip or manuscript job IDs
remain. AI disclosure precedes the final bibliography.

Fresh deterministic checks are in audit/release-validation.json, produced by
audit/release_validate.py. They verify frozen research/source integrity, current
manuscript/PDF bindings, official class, exact cited keys, source dependency
closure, source-archive equality, fonts and author metadata. The rebuilt text
is identical to the previously frozen PDF text. A clean rebuild changed the
PDF's byte digest; the real freeze-manuscript command was therefore rerun and
the new snapshot is in audit/manuscript-snapshot.json. No manuscript input or
mathematical evidence changed.

The standalone standard-library reproduction was rerun successfully in this
job; audit/release-reproduce.json records its exact finite coverage and ok=true.
These computational checks support the accepted proof and do not prove the
unbounded theorem by enumeration. The source ZIP still matches all current
inputs and excludes third-party fulltexts. This audit concerns a local artifact,
not author approval, external submission or venue acceptance.
