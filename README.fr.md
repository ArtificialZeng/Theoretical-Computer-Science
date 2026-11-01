# Theoretical Computer Science

[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)

Manuscrits de recherche, code reproductible et certificats exacts en informatique théorique. Cet instantané contient **10 ensembles de documents** : les cinq manuscrits initiaux et cinq résultats ultérieurs de la recherche continue. Chaque sujet dispose d’un résumé, d’un PDF, d’une archive source inchangée et de sources consultables directement.

**Bien lire la portée des résultats :** sept manuscrits sont enregistrés localement comme des résolutions complètes de leurs objectifs précis ; trois anciens manuscrits présentent des résultats partiels dont les questions générales restent ouvertes. Ces dossiers locaux ne constituent ni une évaluation externe par les pairs ni une acceptation à STOC. Les listes d’auteurs d’origine sont conservées ; les cinq manuscrits ultérieurs ont Zijian Zeng pour seul auteur.

## Index des manuscrits

| Sujet | Pages | Portée | Fichiers |
|---|---:|---|---|
| `coverage-sparse` | 8 | Objectif précis résolu | [PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md) |
| `privacy-interpolation` | 7 | Ancien résultat partiel | [PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md) |
| `robust-stopping` | 11 | Ancien résultat partiel | [PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md) |
| `curvature-noise` | 6 | Ancien résultat partiel | [PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md) |
| `advice-matching` | 6 | Objectif précis résolu | [PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md) |
| `c002-coverage` | 7 | Objectif précis résolu | [PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md) |
| `c009-cycle2` | 6 | Objectif précis résolu | [PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md) |
| `c012-upcycles` | 5 | Objectif précis résolu | [PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md) |
| `c015-imagebound` | 6 | Objectif précis résolu | [PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md) |
| `c017-wheeler` | 10 | Objectif précis résolu | [PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md) |

## Questions étudiées et résultats

### Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

**Résumé.** Quel effet ont des contraintes d’indépendance portant seulement sur certaines paires sur l’espérance optimale d’une fonction de couverture ? Pour les graphes k-coloriables et ceux de degré maximal au plus k−1, le manuscrit établit le rapport extrémal exact 1/[1−(1−1/k)^k]. Des cliques disjointes donnent les exemples limites, et une inégalité de collisions fournit des bornes finies avec erreurs. Il s’agit de suprema sur des classes de graphes.

[PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md)

### Mandatory Excursions in Privacy-Constrained Probability Paths

**Résumé.** Un chemin de probabilités soumis à une contrainte de confidentialité peut-il rester entre ses valeurs aux extrémités ? Pour des distributions à trois issues dont deux coordonnées sont échangées, le texte détermine le budget optimal et le pic minimal inévitable de la troisième coordonnée. Il étudie aussi le coût de la monotonie et fournit des certificats d’excursion. Cette ancienne note présente des résultats partiels ; le problème général reste ouvert.

[PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md)

### Certified Expected-Cost Optimization for Robust Ski Rental

**Résumé.** Comment exploiter une prévision rationnelle finie dans le problème de location de skis tout en respectant une borne du rapport compétitif moyen à chaque horizon ? Le manuscrit fournit une optimisation exacte avec certificats primaux et duaux, un support d’au plus b+1 jours d’achat et une frontière explicite pour la prévision uniforme. Le temps est polynomial en la valeur numérique de b et en la taille binaire de l’entrée. La question initiale plus générale reste ouverte.

[PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md)

### A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

**Résumé.** Quel est l’effet d’un bruit multiplicatif persistant de l’oracle sur la maximisation sous-modulaire à courbure connue ? Dans le régime k=⌊n^α⌋, 0<α<1/2 et εk→∞, une construction à ensemble caché fournit une borne asymptotique correspondant à la sélection selon les valeurs bruitées des singletons. Lorsque le bruit tend vers zéro, le facteur limite est 1−κ, contre 1−κ/e avec un oracle exact. Cette ancienne note ne résout que ce régime.

[PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md)

### Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

**Résumé.** Quel compromis entre cohérence et robustesse est possible pour le couplage biparti en ligne avec des conseils parfois erronés ? La frontière exacte est min{3/4, 3/2−c} pour les graphes non pondérés de degré maximal deux, et min{7/8, 7/4−c} pour les cycles. Un algorithme privilégiant les voisins hors ligne déjà exposés atteint les points extrêmes. L’adversaire est non adaptatif et les conseils peuvent contenir des arêtes absentes.

[PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md)

### A Size-Independent Discrepancy Bound for Sparse Coverage Functions

**Résumé.** Peut-on équilibrer des fonctions de couverture creuses avec une erreur indépendante du nombre d’objets ? Si chaque objet appartient à au plus t occurrences de caractéristiques dans toute la famille, un algorithme déterministe en temps polynomial partitionne les objets en k≥2 classes et garantit une discrépance entre classes d’au plus 4kt(kt−1)². Des témoins de Hall équilibrent les grandes caractéristiques, puis un arrondi de Beck–Fiala à choix multiples traite les interactions restantes.

[PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md)

### A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

**Résumé.** Les cycles orientés alternés dont chaque arête est subdivisée une fois satisfont-ils la propriété locale de Sidorenko pour les tournois, à toute longueur ? Pour Hℓ issu d’un cycle alterné de longueur 2ℓ, le manuscrit établit une densité d’homomorphismes d’au moins 2^(−4ℓ). Une inégalité matricielle antisymétrique donne aussi une estimation quantitative de rigidité et le cas d’égalité. L’exposant 4ℓ est optimal.

[PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md)

### A Universal Partial Cycle with Three Wildcards per Window

**Résumé.** Existe-t-il un cycle partiel universel non trivial comportant plusieurs jokers par fenêtre ? Un cycle binaire explicite de longueur 512 possède des fenêtres de longueur 12 contenant exactement trois jokers. Elles partitionnent les 4096 mots binaires de longueur 12 en groupes de huit complétions. Le cycle entier est donné par 128 chiffres octaux et vérifié par un court programme Python sans solveur, ce qui constitue une preuve finie d’existence.

[PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md)

### Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

**Résumé.** La borne supérieure connue sur la longueur des mots mortels des automates non déterministes à images bornées par k est-elle optimale ? Pour chaque k≥2 fixé, le maximum de la longueur du plus court mot mortel vaut Θk(n^(k+1)). La borne inférieure reste valable pour tout n assez grand, même avec un alphabet binaire et une forte connexité. Une construction à file et horloges cycliques fournit le délai tout en préservant un invariant global d’image.

[PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md)

### Deciding Membership and Realizability for Wheeler Transducers

**Résumé.** Peut-on décider l’appartenance à la classe de Wheeler lorsque le nombre de morceaux monotones de sortie n’est pas fixé ? Le manuscrit donne un algorithme polynomial pour les transducteurs sous-séquentiels déterministes finis émondés, avec transitions partielles et sorties effaçantes ; une borne binaire prudente est O(S^13). Les composantes fortement connexes ramifiées et les cycles simples exigent des critères distincts. La réalisabilité équivalente est aussi décidable et constructive, sans garantie polynomiale ni de minimalité pour cette construction.

[PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md)

## Notes vérifiées : les questions initiales restent ouvertes

Deux dossiers décrivent des obstacles à certaines méthodes de preuve. L’[interface binaire de parité](notes/tp-parity-interface/) ne permet pas de combiner les colorations TP testées au moyen d’une table commune de 72 entrées ; elle ne réfute pas la conjecture initiale de 3-coloration. L’[obstruction au relèvement des cycles après suppression d’un sommet](notes/facet-cycle-lifting/) compare les 200 ensembles indépendants maximaux de P19 aux 189 sommets d’un cycle de base et exclut un schéma précis d’induction. Les données exactes et les vérificateurs sont inclus.

## Reproduire et compiler

Les vérifications mathématiques portables utilisent uniquement **Python 3.10+ et sa bibliothèque standard**. La compilation des PDF nécessite aussi une distribution LaTeX, `latexmk` et Poppler (`pdftotext`) ; les fichiers officiels acmart non modifiés sont fournis. Les scripts travaillent sur des copies temporaires.

Exécuter les commandes suivantes à la racine du dépôt. Remplacer `--all` par `--paper ID` pour un seul sujet. Les calculs finis ne vérifient que les domaines indiqués ; les arguments généraux figurent dans les manuscrits. Les horodatages TeX peuvent modifier les octets des PDF recompilés.

```sh
git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git
cd Theoretical-Computer-Science
python3 scripts/verify_artifacts.py
python3 scripts/reproduce.py --all
# Optional: rebuild every PDF
python3 scripts/build_pdfs.py --all
```

## Organisation du dépôt

`papers/ID/paper.pdf` est le PDF livré ; `source.zip` est l’archive source d’origine inchangée ; `source/` expose les mêmes fichiers. `catalog.json` contient les empreintes et les commandes de reproduction, et `validation/` les vérifications réellement exécutées. Les dossiers de provenance conservent les limites de vérification bibliographique, notamment pour la location de skis.

## Auteurs et assistance

Responsable : **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. La recherche, le code, les preuves et la rédaction ont utilisé une assistance substantielle de l’IA, déclarée dans les manuscrits. Les mentions de licence existantes sont conservées ; voir [RIGHTS.md](RIGHTS.md).
