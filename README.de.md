# Theoretical Computer Science

[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)

Forschungsmanuskripte, reproduzierbarer Code und exakte Zertifikate aus der theoretischen Informatik. Dieser Stand enthält **16 Manuskriptpakete**: elf aus dieser Forschungsreihe und fünf aus anderen Gesprächen; drei weitere Ordner enthalten nur Vorlagen. Zu jedem Thema gibt es eine Zusammenfassung, das PDF, ein unverändertes Quellarchiv und direkt einsehbaren Quellcode.

**Bitte den Geltungsbereich beachten:** Von den elf Manuskripten dieser Reihe werden acht lokal als vollständige Lösungen ihrer präzisen Ziele geführt; drei ältere Manuskripte enthalten Teilresultate, während die allgemeineren Ausgangsfragen offenbleiben. Dies sind lokale Forschungs- und Freigabeprotokolle, keine externe Begutachtung oder STOC-Annahme. Die ursprünglichen Autorenlisten bleiben erhalten; die sechs späteren Manuskripte nennen nur Zijian Zeng.

## Manuskriptübersicht

| Thema | Seiten | Geltungsbereich | Dateien |
|---|---:|---|---|
| `coverage-sparse` | 8 | Präzises Ziel vollständig gelöst | [PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md) |
| `privacy-interpolation` | 7 | Älteres Teilresultat | [PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md) |
| `robust-stopping` | 11 | Älteres Teilresultat | [PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md) |
| `curvature-noise` | 6 | Älteres Teilresultat | [PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md) |
| `advice-matching` | 6 | Präzises Ziel vollständig gelöst | [PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md) |
| `c002-coverage` | 7 | Präzises Ziel vollständig gelöst | [PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md) |
| `c009-cycle2` | 6 | Präzises Ziel vollständig gelöst | [PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md) |
| `c012-upcycles` | 5 | Präzises Ziel vollständig gelöst | [PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md) |
| `c015-imagebound` | 6 | Präzises Ziel vollständig gelöst | [PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md) |
| `c017-wheeler` | 10 | Präzises Ziel vollständig gelöst | [PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md) |
| `c021-ccrapumping` | 9 | Präzises Ziel vollständig gelöst | [PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md) |

## Fragestellungen und Ergebnisse

### Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

**Zusammenfassung.** Wie stark sinkt der beste erreichbare Erwartungswert einer Überdeckungsfunktion, wenn Unabhängigkeit nur für ausgewählte Paare verlangt wird? Für k-färbbare Graphen und Graphen mit Maximalgrad höchstens k−1 wird der genaue Worst-Case-Quotient 1/[1−(1−1/k)^k] bestimmt. Disjunkte Cliquen liefern scharfe Beispiele; eine Kollisionsungleichung liefert endliche Fehlergrenzen. Die Aussage betrifft Suprema über Graphklassen.

[PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md)

### Mandatory Excursions in Privacy-Constrained Probability Paths

**Zusammenfassung.** Kann ein durch Datenschutzbedingungen beschränkter Wahrscheinlichkeitsweg zwischen seinen Endpunktwerten bleiben? Für dreielementige Verteilungen mit vertauschten Koordinaten werden optimale Budgets und der kleinste unvermeidbare Spitzenwert der unveränderten Koordinate bestimmt. Hinzu kommen scharfe Kosten monotoner Wege und notwendige Auslenkungszertifikate. Dies ist eine ältere Teilresultat-Notiz; das ursprüngliche allgemeine Problem bleibt offen.

[PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md)

### Certified Expected-Cost Optimization for Robust Ski Rental

**Zusammenfassung.** Wie lässt sich eine endliche rationale Prognose beim Ski-Rental-Problem nutzen, während für jeden Zeithorizont eine Schranke des erwarteten Wettbewerbsfaktors gilt? Der Text bietet exakte Kostenoptimierung mit primalen und dualen Zertifikaten, eine Stützmenge von höchstens b+1 Kauftagen und eine explizite Grenze für Gleichverteilungsprognosen. Die Laufzeit ist polynomial im Zahlenwert von b und in der Eingabebitlänge. Die allgemeinere Ausgangsfrage bleibt offen.

[PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md)

### A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

**Zusammenfassung.** Wie beeinflusst dauerhaftes multiplikatives Orakelrauschen die Maximierung submodularer Funktionen bei bekannter Krümmung? Im Bereich k=⌊n^α⌋ mit 0<α<1/2 und εk→∞ liefert eine versteckte Menge eine asymptotische untere Schranke, die zur Auswahl nach verrauschten Einzelwerten passt. Bei verschwindendem Rauschen ist der Grenzfaktor 1−κ statt 1−κ/e beim exakten Orakel. Die ältere Notiz löst diesen Bereich, nicht das uneingeschränkte Ausgangsproblem.

[PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md)

### Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

**Zusammenfassung.** Welche Konsistenz-Robustheits-Grenze ist beim Online-Matching mit möglicherweise falschen Ratschlägen erreichbar? Für ungewichtete bipartite Graphen mit Maximalgrad zwei ist sie min{3/4, 3/2−c}, für Zyklen min{7/8, 7/4−c}. Ein Algorithmus mit Vorrang für bereits exponierte Offline-Nachbarn erreicht die Endpunkte; kleine ununterscheidbare Eingaben liefern passende obere Schranken. Der Gegner ist nichtadaptiv, und Ratschläge dürfen nicht vorhandene Kanten enthalten.

[PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md)

### A Size-Independent Discrepancy Bound for Sparse Coverage Functions

**Zusammenfassung.** Lassen sich dünn besetzte Überdeckungsfunktionen unabhängig von der Anzahl der Elemente ausgleichen? Wenn jedes Element in höchstens t Merkmalsvorkommen der gesamten Familie liegt, liefert eine deterministische Polynomialzeiteinteilung in k≥2 Klassen eine paarweise Diskrepanz von höchstens 4kt(kt−1)². Hall-Zeugen gleichen große Merkmale aus; eine Mehrfachwahlvariante der Beck–Fiala-Rundung behandelt die übrigen Wechselwirkungen. Die Schranke hängt nur von t und k ab.

[PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md)

### A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

**Zusammenfassung.** Erfüllen alternierende gerichtete Zyklen nach einmaliger Unterteilung jeder Kante die lokale Tournament-Sidorenko-Eigenschaft für alle Längen? Für den so aus einem alternierenden 2ℓ-Zyklus entstehenden Graphen Hℓ wird eine Homomorphismendichte von mindestens 2^(−4ℓ) bewiesen. Eine Ungleichung für schiefsymmetrische Matrizen liefert die gesamte Familie, eine quantitative Starrheitsaussage und den Gleichheitsfall. Der Exponent 4ℓ ist optimal.

[PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md)

### A Universal Partial Cycle with Three Wildcards per Window

**Zusammenfassung.** Existiert ein nichttrivialer universeller partieller Zyklus mit mehreren Platzhaltern pro Fenster? Ein expliziter binärer Zyklus der Länge 512 besitzt Fenster der Länge 12 mit genau drei Platzhaltern. Die Fenster zerlegen alle 4096 binären 12-Wörter in Gruppen von je acht Vervollständigungen. Der gesamte Zyklus wird durch 128 Oktalziffern beschrieben und mit einem kurzen solverfreien Python-Programm vollständig geprüft: ein endlicher Existenzbeweis.

[PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md)

### Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

**Zusammenfassung.** Ist die bekannte obere Schranke für Mortalität bei k-bildbeschränkten nichtdeterministischen Automaten scharf? Für jedes feste k≥2 wird die maximale Länge eines kürzesten tödlichen Wortes als Θk(n^(k+1)) bestimmt. Die untere Schranke gilt für alle hinreichend großen n auch bei binärem Alphabet und stark zusammenhängenden Automaten. Eine Warteschlange mit zyklischen Uhren erzeugt die Verzögerung; eine globale Bildinvariante erhält die Beschränkung für jedes Wort.

[PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md)

### Deciding Membership and Realizability for Wheeler Transducers

**Zusammenfassung.** Ist Wheeler-Zugehörigkeit entscheidbar, wenn die Anzahl monotoner Ausgabestücke nicht vorgegeben ist? Für endliche getrimmte deterministische subsequenzielle Transduktoren mit partiellen Übergängen und löschenden Ausgaben wird ein Polynomialzeitalgorithmus mit konservativer Bitschranke O(S^13) angegeben. Verzweigte starke Zusammenhangskomponenten und einfache Zyklen benötigen unterschiedliche Kriterien. Auch äquivalente Wheeler-Realisierbarkeit ist entscheidbar und konstruktiv; für diese Konstruktion wird keine polynomiale Laufzeit oder Minimalität behauptet.

[PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md)

### Uniform Pumping Does Not Characterize Copyless Cost Register Automata

**Zusammenfassung.** Charakterisiert die uniforme Pumping-Bedingung die von copyless polynomialen Kostenregisterautomaten berechneten Funktionen? Das Manuskript widerlegt dies selbst für rationale, durch gewichtete Automaten erkennbare Funktionen: Die Summe der Positionen aller Einsen eines Binärworts erfüllt die Bedingung mit einem einzigen Exponenten und einem endlich erzeugten Unterhalbring, ist aber durch keinen solchen endlichen Kostenregisterautomaten berechenbar. Eine Retraktion auf ein minimales Bild und eine polynomiale Spektralprojektion liefern ein Kommutationshindernis; Rückkehrwörter behandeln endliche Steuerung. Enthalten ist die freigegebene neunseitige Trennung, nicht die spätere Erweiterung.

[PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md)

## Geprüfte Forschungsnotizen: Ausgangsfragen weiterhin offen

Zwei weitere Dossiers dokumentieren Hindernisse für Beweismethoden. Die [binäre Paritätsschnittstelle](notes/tp-parity-interface/) kann die untersuchten TP-Färbungen nicht durch eine gemeinsame Tabelle mit 72 Einträgen zusammensetzen; die ursprüngliche Dreifärbungsvermutung wird nicht widerlegt. Das [Hindernis für Zyklushebung nach Knotenlöschung](notes/facet-cycle-lifting/) vergleicht 200 maximale unabhängige Mengen von P19 mit 189 Basiszyklus-Knoten und schließt ein bestimmtes Induktionsverfahren aus. Beide Notizen enthalten exakte Daten und Prüfcode.

## Reproduktion und PDF-Erstellung

Die portablen mathematischen Prüfungen benötigen nur **Python 3.10+ mit Standardbibliothek**. Für die PDFs werden zusätzlich eine LaTeX-Distribution, `latexmk` und Poppler (`pdftotext`) benötigt; die unveränderten offiziellen acmart-Dateien sind enthalten. Die Skripte arbeiten mit temporären Kopien.

Die folgenden Befehle werden im Wurzelverzeichnis ausgeführt. Für ein einzelnes Thema `--all` durch `--paper ID` ersetzen. Endliche Rechnungen prüfen nur den angegebenen Bereich; allgemeine Beweise stehen in den Manuskripten. TeX-Zeitstempel können die Bytes neu erstellter PDFs verändern.

```sh
git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git
cd Theoretical-Computer-Science
python3 scripts/verify_artifacts.py
python3 scripts/reproduce.py --all
# Optional: rebuild every PDF
python3 scripts/build_pdfs.py --all
```

## Verzeichnisstruktur

`papers/ID/paper.pdf` enthält das freigegebene PDF, `source.zip` das unveränderte ausgelieferte Archiv und `source/` dieselben Dateien zum Durchsehen. `catalog.json` enthält Hashwerte und Reproduktionsbefehle, `validation/` die tatsächlich ausgeführten Prüfungen. Die Provenienzdateien bewahren Einschränkungen der Literaturprüfung, insbesondere beim Ski-Rental-Manuskript.

## Autoren und Unterstützung

Verantwortlicher: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Forschung, Code, Beweisentwicklung und Manuskripte nutzten wesentliche KI-Unterstützung, die in den Texten offengelegt wird. Vorhandene Lizenzhinweise Dritter bleiben erhalten; siehe [RIGHTS.md](RIGHTS.md).

## Manuskripte aus anderen Gesprächen

Alle acht Ordner stoc1–stoc8 sind erfasst: fünf vorhandene Manuskripte und drei reine Vorlagenordner. Die Manuskripte behalten ihre Einschränkungen zur Neuheit und gelten nicht als neu akzeptierte vollständige Lösungen.

[stoc1–stoc8](conversations/README.md)

### Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds

**Zusammenfassung.** Untersucht die Online-Vervollständigung von Tokens unter Grammatikbedingungen mit getrennten Parametern für Grammatik, Wortschatz und Stromlänge. Der Text liefert OMv-basierte Schranken und Stack-Indizes mit explizitem exponentiellem Kompilierungsaufwand. Eine allgemeine LR(1)-Beschleunigung und ausreichende eigenständige Neuheit für STOC sind nicht nachgewiesen.

[PDF](conversations/stoc1/paper.pdf) · [ZIP](conversations/stoc1/source.zip) · [Code](conversations/stoc1/source/) · [Reproduce](conversations/stoc1/README.md)

### Syntax Repair in Near-Linear Time: Exact Bounds for Marked-Palindrome Grammars

**Zusammenfassung.** Exakte Sprach-Editierdistanz für feste markierte Palindromgrammatiken: theoretisch O(n+k²) mit Reparaturzeugnis, eine SETH-Schranke mit Schutzsymbolen und Aufzählungsresultate. Die Implementierung benötigt O(n log²(n+2)+(k+1)²). Die allgemeine LR(1)-Frage bleibt offen; das anonyme zweispaltige PDF muss vor einer STOC-Einreichung umformatiert werden.

[PDF](conversations/stoc2/paper.pdf) · [ZIP](conversations/stoc2/source.zip) · [Code](conversations/stoc2/source/) · [Reproduce](conversations/stoc2/README.md)

### Is Quadratic Subtyping Optimal? Conditional Hardness on Shared Acyclic Type Graphs

**Zusammenfassung.** Überträgt bekannte OV-Härte für Automaten-Schnitt auf strukturelles Subtyping gemeinsam genutzter azyklischer Typgraphen. Selbst drei feste Record-Felder oder reine Pfeiltypen haben eine bedingte quadratische Schranke; Gleichheit bleibt fast linear. Quotienten- und Zugriffsschranken ergänzen das Bild. Die Eigenständigkeit des semantischen Transfers ist die zentrale Neuheitsfrage. Das PDF umfasst 18 Seiten.

[PDF](conversations/stoc3/paper.pdf) · [ZIP](conversations/stoc3/source.zip) · [Code](conversations/stoc3/source/) · [Reproduce](conversations/stoc3/README.md)

### Fully Dynamic Interprocedural Dataflow Analysis: OMv Barriers and Summary-Local TreeFlow Updates

**Zusammenfassung.** Voll dynamischer interprozeduraler Datenfluss mit expliziten Kosten globaler Abhängigkeiten. OMv-Schranken gelten selbst für Pfadprozeduren und flache azyklische Aufrufe. Ein Relationsschaltkreis liefert Schranken über betroffene Gatter und Aufrufinzidenzen bei festen Zerlegungen. Die allgemeine Ausgangsfrage und produktive Integration bleiben offen; die Neuheit gegenüber RSM-Verfahren ist zu prüfen.

[PDF](conversations/stoc4/paper.pdf) · [ZIP](conversations/stoc4/source.zip) · [Code](conversations/stoc4/source/) · [Reproduce](conversations/stoc4/README.md)

### Octagons Are APSP-Complete: Fine-Grained Complexity of Weakly Relational Abstract Domains

**Zusammenfassung.** Ordnet Octagon- und Zonenoperationen durch exponentenerhaltende APSP-Reduktionen, inkrementelle Min-Plus-Abwägungen, Zulässigkeit und breitenabhängige Rekonstruktion ein. Die APSP-Schranken vom Oktober 2026 sind übernommene berichtete Resultate, kein neuer Kürzeste-Wege-Algorithmus. Ein festgelegter ELINA-Kern ist reproduzierbar enthalten. Neuheitsprüfung und vollständige Analysatorstudien fehlen; das PDF hat 19 Seiten.

[PDF](conversations/stoc5/paper.pdf) · [ZIP](conversations/stoc5/source.zip) · [Code](conversations/stoc5/source/) · [Reproduce](conversations/stoc5/README.md)

## Vergleichende Rangfolge

Die verlinkte Rangfolge bezieht sich auf den früheren Stand mit fünfzehn Manuskripten. Das neu ergänzte CCRA-v1-Paket ist darin noch nicht bewertet; die erweiterte Fassung wartet auf die abschließende Freigabeprüfung.

[中文：按 STOC 相对竞争力和新增解决问题大小排序](RANKING.zh-CN.md) · [English assessment](RANKING.md) · [Data](ranking.json)

```sh
python3 scripts/check_conversations.py --all
```
