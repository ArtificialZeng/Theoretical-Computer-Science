# Dossier de recherche non résolu : accessibilité sous deux pannes

[en](README.md) · [zh](README.zh-CN.md) · [de](README.de.md) · [fr](README.fr.md) · [ja](README.ja.md)

**UNRESOLVED — RESEARCH RECORDS, NO PAPER/PDF**

Après quatre sessions de recherche bornées, dont la session supplémentaire explicitement autorisée, le problème initial reste non résolu. Ce dossier contient des arguments Markdown, des vérifications exactes finies et du code source. Ce n'est ni un manuscrit, ni une preuve ou réfutation complète du problème initial, ni un résultat submission_ready.

L'objectif est un algorithme polynomial produisant un sous-graphe composé d'arêtes originales, de taille O-tilde(n+n sqrt(p)), qui préserve l'accessibilité des p paires dirigées après toute combinaison d'au plus deux pannes de sommets ou d'arêtes. Les sources primaires vérifiées donnent encore la borne supérieure O(n^(4/3) p^(1/3)) et la borne inférieure Omega(n sqrt(p)).

Plusieurs lemmes auxiliaires plus forts sont réfutés. Une réduction utilisant des arêtes de retour échantillonnées et une couverture pour trois chemins disjoints en arêtes traitent certaines arêtes critiques. La borne globale reste à prouver. L'inégalité de densité ci-dessous est seulement suffisante ; sa nécessité pour le problème initial n'est pas établie.

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


La quatrième session démontre un certificat d'au plus 8t+p arêtes pour une famille précisément définie de sélecteurs entièrement partagés et caractérise ses arêtes critiques centrales. Le problème général et la borne globale de densité restent ouverts.

[Fourth-pass proof and exact finite coverage](proofs/research-960416a85f25-math.md). Earlier pass notes preserve their historical budgets and decisions. Reproduction additionally requires a C++17 compiler (`c++`, `clang++` or `g++`). Only original source files are included; compiled binaries and third-party text caches are excluded.

Dans la copie temporaire de reproduction, seule une assertion de délai absolu de recherche expiré est retirée. Les assertions mathématiques et les domaines finis restent inchangés. Les sources originales et le premier paquet en échec sont conservés ; il ne s'agit pas d'une nouvelle session de recherche.
