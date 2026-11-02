# Operational build observations

Job c029-vftfast-write-7567570a6950. The initial pdflatex build exited 1 because manuscript mode defaults to one-and-a-half spacing and the class rejected a subsequent singlespacing command: `Class acmart Error: An attempt to redefine baselinestretch detected.` The raw initial log was overwritten during later builds; this record preserves the observed failure without claiming the original raw log remains. Native acmsmall mode supplies single spacing without changing class enforcement. The official class is unchanged.

An initial running-header override before the author declaration caused the author name to appear twice. Every-page visual inspection caught this; removal of the premature override fixed the rendered header. The final PDF has one listed author and one running author. These operational corrections are not mathematical evidence and do not change research-pass counters or the accepted mathematical snapshot.

The writer validation initially tried to decode the TeX log as UTF-8 and encountered a non-UTF-8 font byte. Reading the same existing log as Latin-1 completed the check; no mathematical input, manuscript or PDF changed. This diagnostic decoding error has no mathematical significance.
