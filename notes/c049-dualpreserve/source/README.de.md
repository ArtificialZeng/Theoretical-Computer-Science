# Ungelöste Forschungsaufzeichnungen: Erreichbarkeit bei zwei Ausfällen

[en](README.md) · [zh](README.zh-CN.md) · [de](README.de.md) · [fr](README.fr.md) · [ja](README.ja.md)

**UNRESOLVED — RESEARCH RECORDS, NO PAPER/PDF**

Nach vier begrenzten Forschungsdurchläufen, einschließlich des ausdrücklich zusätzlich genehmigten Durchlaufs, bleibt das ursprüngliche Problem ungelöst. Dieses Verzeichnis enthält Markdown-Argumente, exakte endliche Prüfungen und Quellcode. Es ist kein Manuskript, kein vollständiger Beweis oder Gegenbeweis der Ausgangsfrage und kein submission_ready-Ergebnis.

Gesucht ist ein Polynomialzeitalgorithmus für einen Teilgraphen aus Originalkanten mit O-tilde(n+n sqrt(p)) Kanten, der die gerichtete Erreichbarkeit aller p vorgegebenen Paare nach beliebigen höchstens zwei gemischten Knoten- oder Kantenausfällen erhält. Die geprüften Primärquellen liefern weiterhin die obere Schranke O(n^(4/3) p^(1/3)) und die untere Schranke Omega(n sqrt(p)).

Mehrere stärkere Hilfsaussagen sind widerlegt. Eine Reduktion mit zufällig ausgewählten Rückkanten und eine Abdeckung für drei kantendisjunkte Pfade behandeln einige kritische Kanten. Die globale Kantenzahl bleibt offen. Die folgende Dichteaussage ist nur eine hinreichende Bedingung; ihre Notwendigkeit ist nicht bewiesen.

- [Frozen original / 原始完整问题](ORIGINAL_PROBLEM.md)
- [Pass 1: flow/cut coverage and its limits](proofs/research-67929c1f9552-math.md)
- [Pass 2: the high-beta core counterexample](proofs/research-c6b2b0ea3f71-math.md)
- [Pass 3: orientation energy and the remaining gap](proofs/research-2396269cbd5d-math.md)
- [Code](code/) · [Original finite results](results/) · [Provenance](manifest.json)

Remaining sufficient inequality (unproved): for every edge-critical (G,P) and nonempty U,

`|E(G[U])|^2 <= C n(p+1)|U| log(n+2)^c`.

Here n counts the entire original graph, including all selector vertices.

Run all declared finite checks on disposable copies with Python 3.10+ (standard library only):

```sh
python3 -B reproduce.py
```

These finite checks do not prove an asymptotic bound. The directory excludes raw model transcripts, credentials and third-party full-text caches. Its mathematical arguments have not passed a fresh acceptance review. Substantial research and code assistance used OpenAI Codex; internal model checks are not external peer review.

Researcher: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. Local preparation only; publication requires the user's revised finalization decision.


Der vierte Durchlauf beweist für eine genau definierte vollständig geteilte Selektorfamilie ein Zertifikat mit höchstens 8t+p Kanten und klassifiziert deren kritische Kernkanten. Das allgemeine Problem und die globale Dichteschranke bleiben offen.

[Fourth-pass proof and exact finite coverage](proofs/research-960416a85f25-math.md). Earlier pass notes preserve their historical budgets and decisions. Reproduction additionally requires a C++17 compiler (`c++`, `clang++` or `g++`). Only original source files are included; compiled binaries and third-party text caches are excluded.

Nur in der temporären Reproduktionskopie wird eine abgelaufene absolute Forschungsfrist-Prüfung entfernt. Alle mathematischen Prüfungen und endlichen Fallbereiche bleiben erhalten. Originalquellen und das erste fehlgeschlagene Paket werden bewahrt; dies ist kein neuer Forschungsdurchlauf.
