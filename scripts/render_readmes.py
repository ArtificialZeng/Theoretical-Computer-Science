#!/usr/bin/env python3
"""Generate the five language indexes from the public catalog and abstracts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT / "catalog.json").read_text())["papers"]
ABSTRACTS = json.loads((ROOT / "descriptions.json").read_text())
FILES = {"en": "README.md", "zh": "README.zh-CN.md", "de": "README.de.md", "fr": "README.fr.md", "ja": "README.ja.md"}
NAV = "[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)"

COPY = {
"en": {
"intro": "Research manuscripts, reproducible code and exact certificates in theoretical computer science. This repository contains **16 manuscript packages**: eleven from this continuous-research collection and five from other conversations. Three additional conversation folders contain templates only. Each topic below has an abstract, a PDF, an unchanged source archive, and browseable source code.",
"status": "**Read the scope labels:** Among the eleven packages in papers/, eight manuscripts are recorded as complete resolutions of their stated targets; three early manuscripts are partial-result notes whose broader original questions remain unresolved. These are local research/release records, not external peer review or STOC acceptance. The original author lists are preserved; the six later releases list Zijian Zeng as sole author.",
"overview": "Manuscript index", "topic": "Topic", "pages": "Pages", "scope": "Scope", "artifacts": "Files", "resolved": "Target resolution", "partial": "Legacy partial result", "abstract": "Abstract", "subjects": "What each project studies",
"notes_title": "Verified research notes: original questions still unresolved",
"notes": "Two additional dossiers document limitations of attempted proof methods. [The binary parity interface](notes/tp-parity-interface/) cannot combine the tested TP-graph colorings through one shared 72-entry table; the original three-coloring conjecture is not disproved. [The deletion-cycle lifting obstruction](notes/facet-cycle-lifting/) uses 200 maximal independent sets of P19 versus 189 base-cycle vertices to rule out a particular induction scheme; it is not a counterexample to facet-Hamiltonicity. Both include exact evidence and checking code.",
"repro": "Reproduce and build", "requirements": "The portable mathematical checks require **Python 3.10+ and its standard library**. Rebuilding PDFs additionally requires a LaTeX distribution, `latexmk`, and Poppler (`pdftotext`); official unmodified acmart inputs are included. Scripts work on temporary copies so the archived sources remain intact.",
"commands_note": "Run these commands from the repository root. Use `--paper ID` instead of `--all` for one topic. Finite computations check only their documented ranges; the general mathematical arguments are in the manuscripts. TeX timestamps may change rebuilt PDF bytes.",
"layout": "Repository layout", "layout_text": "`papers/ID/paper.pdf` is the released PDF; `source.zip` is the unchanged delivered source archive; `source/` exposes the same files for browsing. `catalog.json` records hashes and reproduction commands. `validation/` records the actual synchronization checks. Per-paper provenance retains citation limitations, including those of the ski-rental note.",
"assistance": "Authorship and assistance", "assistance_text": "Maintainer: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Research, code, proof development and manuscript preparation used substantial AI assistance, disclosed in the manuscripts. Existing third-party license notices are retained; see [RIGHTS.md](RIGHTS.md)."
},
"zh": {
"intro": "本仓库整理理论计算机科学研究稿件、可复现代码与精确证书。本仓库包含 **16 套稿件材料**：本持续研究对话的十一篇，以及其他对话的五篇；另有三个对话目录只有模板。下文逐项提供研究摘要、PDF、保持原样的源码归档及可直接浏览的源码。",
"status": "**请按范围标记阅读：**本对话的十一篇中，八篇稿件在本地记录中完整解决了各自明确的目标；三篇早期稿件属于部分结果，原始更广泛问题仍未解决。这些是本地研究与交付记录，不代表外部同行评审或 STOC 录用。原作者名单保持不变，后六篇稿件仅署名 Zijian Zeng。",
"overview": "稿件索引", "topic": "课题", "pages": "页数", "scope": "结果范围", "artifacts": "文件", "resolved": "明确目标的完整解答", "partial": "早期部分结果", "abstract": "摘要", "subjects": "各课题研究了什么",
"notes_title": "已验证研究笔记：原题仍未解决",
"notes": "另有两套材料记录证明方法的障碍。[二元奇偶接口](notes/tp-parity-interface/)证明一张共享的72项表无法合成受测 TP 图的三着色，但没有否定原始三着色猜想。[删点环提升障碍](notes/facet-cycle-lifting/)比较 P19 的200个极大独立集与基础环的189个顶点，排除一种特定归纳方案，但不是 facet-Hamiltonicity 的反例。两项均附精确证据与检查代码。",
"repro": "复现与编译", "requirements": "便携数学检查仅需 **Python 3.10+ 标准库**。重编译 PDF 还需 LaTeX 发行版、`latexmk` 与 Poppler（`pdftotext`），所需未修改的官方 acmart 文件已附带。脚本在临时副本上运行，保留归档源码原样。",
"commands_note": "在仓库根目录运行下列命令。单篇复现可将 `--all` 改成 `--paper ID`。有限计算只核验其注明的范围，一般性数学论证见稿件正文；TeX 时间戳可能导致重编译 PDF 的字节不同。",
"layout": "目录说明", "layout_text": "`papers/ID/paper.pdf` 为交付 PDF，`source.zip` 为保持原样的交付源码包，`source/` 提供相同文件供浏览。`catalog.json` 记录哈希与复现命令，`validation/` 记录本次实际检查。每篇 provenance 保留引用核查的适用范围，包括滑雪租赁稿件的文献访问限制。",
"assistance": "作者与研究辅助", "assistance_text": "维护者：**Zijian Zeng，UCSI University** · 1002266693@ucsiuniversity.edu.my。研究、代码、证明推导与写作使用了实质性 AI 辅助，稿件中已披露。所含第三方文件保留原许可说明，见 [RIGHTS.md](RIGHTS.md)。"
},
"de": {
"intro": "Forschungsmanuskripte, reproduzierbarer Code und exakte Zertifikate aus der theoretischen Informatik. Dieser Stand enthält **16 Manuskriptpakete**: elf aus dieser Forschungsreihe und fünf aus anderen Gesprächen; drei weitere Ordner enthalten nur Vorlagen. Zu jedem Thema gibt es eine Zusammenfassung, das PDF, ein unverändertes Quellarchiv und direkt einsehbaren Quellcode.",
"status": "**Bitte den Geltungsbereich beachten:** Von den elf Manuskripten dieser Reihe werden acht lokal als vollständige Lösungen ihrer präzisen Ziele geführt; drei ältere Manuskripte enthalten Teilresultate, während die allgemeineren Ausgangsfragen offenbleiben. Dies sind lokale Forschungs- und Freigabeprotokolle, keine externe Begutachtung oder STOC-Annahme. Die ursprünglichen Autorenlisten bleiben erhalten; die sechs späteren Manuskripte nennen nur Zijian Zeng.",
"overview": "Manuskriptübersicht", "topic": "Thema", "pages": "Seiten", "scope": "Geltungsbereich", "artifacts": "Dateien", "resolved": "Präzises Ziel vollständig gelöst", "partial": "Älteres Teilresultat", "abstract": "Zusammenfassung", "subjects": "Fragestellungen und Ergebnisse",
"notes_title": "Geprüfte Forschungsnotizen: Ausgangsfragen weiterhin offen",
"notes": "Zwei weitere Dossiers dokumentieren Hindernisse für Beweismethoden. Die [binäre Paritätsschnittstelle](notes/tp-parity-interface/) kann die untersuchten TP-Färbungen nicht durch eine gemeinsame Tabelle mit 72 Einträgen zusammensetzen; die ursprüngliche Dreifärbungsvermutung wird nicht widerlegt. Das [Hindernis für Zyklushebung nach Knotenlöschung](notes/facet-cycle-lifting/) vergleicht 200 maximale unabhängige Mengen von P19 mit 189 Basiszyklus-Knoten und schließt ein bestimmtes Induktionsverfahren aus. Beide Notizen enthalten exakte Daten und Prüfcode.",
"repro": "Reproduktion und PDF-Erstellung", "requirements": "Die portablen mathematischen Prüfungen benötigen nur **Python 3.10+ mit Standardbibliothek**. Für die PDFs werden zusätzlich eine LaTeX-Distribution, `latexmk` und Poppler (`pdftotext`) benötigt; die unveränderten offiziellen acmart-Dateien sind enthalten. Die Skripte arbeiten mit temporären Kopien.",
"commands_note": "Die folgenden Befehle werden im Wurzelverzeichnis ausgeführt. Für ein einzelnes Thema `--all` durch `--paper ID` ersetzen. Endliche Rechnungen prüfen nur den angegebenen Bereich; allgemeine Beweise stehen in den Manuskripten. TeX-Zeitstempel können die Bytes neu erstellter PDFs verändern.",
"layout": "Verzeichnisstruktur", "layout_text": "`papers/ID/paper.pdf` enthält das freigegebene PDF, `source.zip` das unveränderte ausgelieferte Archiv und `source/` dieselben Dateien zum Durchsehen. `catalog.json` enthält Hashwerte und Reproduktionsbefehle, `validation/` die tatsächlich ausgeführten Prüfungen. Die Provenienzdateien bewahren Einschränkungen der Literaturprüfung, insbesondere beim Ski-Rental-Manuskript.",
"assistance": "Autoren und Unterstützung", "assistance_text": "Verantwortlicher: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Forschung, Code, Beweisentwicklung und Manuskripte nutzten wesentliche KI-Unterstützung, die in den Texten offengelegt wird. Vorhandene Lizenzhinweise Dritter bleiben erhalten; siehe [RIGHTS.md](RIGHTS.md)."
},
"fr": {
"intro": "Manuscrits de recherche, code reproductible et certificats exacts en informatique théorique. Ce dépôt contient **16 ensembles de documents** : onze de cette recherche continue et cinq d’autres conversations ; trois autres dossiers contiennent seulement des modèles. Chaque sujet dispose d’un résumé, d’un PDF, d’une archive source inchangée et de sources consultables directement.",
"status": "**Bien lire la portée des résultats :** parmi les onze manuscrits de cette série, huit sont enregistrés localement comme des résolutions complètes de leurs objectifs précis ; trois anciens manuscrits présentent des résultats partiels dont les questions générales restent ouvertes. Ces dossiers locaux ne constituent ni une évaluation externe par les pairs ni une acceptation à STOC. Les listes d’auteurs d’origine sont conservées ; les six manuscrits ultérieurs ont Zijian Zeng pour seul auteur.",
"overview": "Index des manuscrits", "topic": "Sujet", "pages": "Pages", "scope": "Portée", "artifacts": "Fichiers", "resolved": "Objectif précis résolu", "partial": "Ancien résultat partiel", "abstract": "Résumé", "subjects": "Questions étudiées et résultats",
"notes_title": "Notes vérifiées : les questions initiales restent ouvertes",
"notes": "Deux dossiers décrivent des obstacles à certaines méthodes de preuve. L’[interface binaire de parité](notes/tp-parity-interface/) ne permet pas de combiner les colorations TP testées au moyen d’une table commune de 72 entrées ; elle ne réfute pas la conjecture initiale de 3-coloration. L’[obstruction au relèvement des cycles après suppression d’un sommet](notes/facet-cycle-lifting/) compare les 200 ensembles indépendants maximaux de P19 aux 189 sommets d’un cycle de base et exclut un schéma précis d’induction. Les données exactes et les vérificateurs sont inclus.",
"repro": "Reproduire et compiler", "requirements": "Les vérifications mathématiques portables utilisent uniquement **Python 3.10+ et sa bibliothèque standard**. La compilation des PDF nécessite aussi une distribution LaTeX, `latexmk` et Poppler (`pdftotext`) ; les fichiers officiels acmart non modifiés sont fournis. Les scripts travaillent sur des copies temporaires.",
"commands_note": "Exécuter les commandes suivantes à la racine du dépôt. Remplacer `--all` par `--paper ID` pour un seul sujet. Les calculs finis ne vérifient que les domaines indiqués ; les arguments généraux figurent dans les manuscrits. Les horodatages TeX peuvent modifier les octets des PDF recompilés.",
"layout": "Organisation du dépôt", "layout_text": "`papers/ID/paper.pdf` est le PDF livré ; `source.zip` est l’archive source d’origine inchangée ; `source/` expose les mêmes fichiers. `catalog.json` contient les empreintes et les commandes de reproduction, et `validation/` les vérifications réellement exécutées. Les dossiers de provenance conservent les limites de vérification bibliographique, notamment pour la location de skis.",
"assistance": "Auteurs et assistance", "assistance_text": "Responsable : **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. La recherche, le code, les preuves et la rédaction ont utilisé une assistance substantielle de l’IA, déclarée dans les manuscrits. Les mentions de licence existantes sont conservées ; voir [RIGHTS.md](RIGHTS.md)."
},
"ja": {
"intro": "理論計算機科学の研究稿、再現可能なコード、厳密な証明書をまとめたリポジトリ。本リポジトリには、この継続研究の十一編と他の会話の五編、計 **16 セットの論文資料**を収録する。他に三つの会話フォルダーはテンプレートのみである。各課題について、概要、PDF、変更していないソースアーカイブ、閲覧可能なコードを用意している。",
"status": "**結果の範囲に注意：**本研究系列の十一編のうち、研究記録上は八編が明示した研究目標の完全な解答に位置付けられている。初期の三編は部分結果であり、元のより一般的な問いは未解決である。これらはローカルの研究・公開確認記録で、外部査読や STOC 採択を意味しない。元の著者一覧を維持し、後の六編は Zijian Zeng の単著である。",
"overview": "論文原稿一覧", "topic": "課題", "pages": "ページ数", "scope": "結果の範囲", "artifacts": "ファイル", "resolved": "明示した目標の完全解答", "partial": "初期の部分結果", "abstract": "概要", "subjects": "各課題の研究内容",
"notes_title": "検証済み研究ノート：元の問いは未解決",
"notes": "二つの追加資料は、特定の証明方法の限界を示す。[二進パリティ・インターフェース](notes/tp-parity-interface/)では、共有72項目表によって対象の TP 彩色を合成できないが、元の三彩色予想を否定したわけではない。[頂点削除に沿うサイクル持ち上げの障害](notes/facet-cycle-lifting/)は、P19 の200個の極大独立集合と基礎サイクルの189頂点を比較し、ある帰納法を排除する。両資料に厳密なデータと検証コードがある。",
"repro": "再現とビルド", "requirements": "可搬な数学的チェックに必要なのは **Python 3.10 以降の標準ライブラリ**のみ。PDF の再ビルドには LaTeX、`latexmk`、Poppler（`pdftotext`） も必要で、未変更の公式 acmart ファイルを同梱している。スクリプトは一時コピーで動作し、アーカイブを変更しない。",
"commands_note": "以下はリポジトリのルートで実行する。個別の課題には `--all` の代わりに `--paper ID` を指定する。有限計算が検証するのは明記された範囲だけであり、一般的な証明は本文を参照。TeX の時刻情報により再ビルドした PDF のバイト列が変わることがある。",
"layout": "ディレクトリ構成", "layout_text": "`papers/ID/paper.pdf` は公開 PDF、`source.zip` は元の未変更ソース、`source/` は同じ内容を閲覧するための展開版。`catalog.json` はハッシュと再現コマンド、`validation/` は実際の確認結果を記録する。出典確認の範囲とアクセス制限は各 provenance に保存されている。",
"assistance": "著者と研究支援", "assistance_text": "管理者：**Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my。研究、コード、証明の検討、執筆には実質的な AI 支援を利用しており、論文原稿で開示している。同梱ファイルの既存ライセンス表示は維持する。[RIGHTS.md](RIGHTS.md) を参照。"
}}


def links(p):
    return f'[PDF]({p["pdf"]}) · [ZIP]({p["source_archive"]}) · [Code]({p["source_directory"]}/) · [Reproduce](papers/{p["id"]}/README.md)'


def main():
    for lang, filename in FILES.items():
        t = COPY[lang]
        lines = ["# Theoretical Computer Science", "", NAV, "", t["intro"], "", t["status"], "", f'## {t["overview"]}', "",
                 f'| {t["topic"]} | {t["pages"]} | {t["scope"]} | {t["artifacts"]} |', "|---|---:|---|---|"]
        for p in PAPERS:
            scope = t["resolved"] if p["kind"] == "resolution-paper" else t["partial"]
            lines.append(f'| `{p["id"]}` | {p["pages"]} | {scope} | {links(p)} |')
        lines += ["", f'## {t["subjects"]}', ""]
        for p in PAPERS:
            lines += [f'### {p["title"]}', "", f'**{t["abstract"]}.** {ABSTRACTS[p["id"]][lang]}', "", links(p), ""]
        lines += [f'## {t["notes_title"]}', "", t["notes"], "", f'## {t["repro"]}', "", t["requirements"], "", t["commands_note"], "",
                  "```sh", "git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git", "cd Theoretical-Computer-Science",
                  "python3 scripts/verify_artifacts.py", "python3 scripts/reproduce.py --all", "# Optional: rebuild every PDF", "python3 scripts/build_pdfs.py --all", "```", "",
                  f'## {t["layout"]}', "", t["layout_text"], "", f'## {t["assistance"]}', "", t["assistance_text"], ""]
        extra = {
            "en": ("Other conversation manuscripts", "Eight folders stoc1–stoc8 are indexed: five existing manuscripts and three template-only folders. These scoped manuscripts retain their originality limitations and do not count as new accepted continuous-research resolutions.", "Comparative ranking"),
            "zh": ("其他对话的稿件", "已整理 stoc1–stoc8 全部八个文件夹：五篇已有论文、三个纯模板目录。五篇稿件保留各自的范围与新颖性限制，不作为持续研究新通过的原题解答。", "综合排名"),
            "de": ("Manuskripte aus anderen Gesprächen", "Alle acht Ordner stoc1–stoc8 sind erfasst: fünf vorhandene Manuskripte und drei reine Vorlagenordner. Die Manuskripte behalten ihre Einschränkungen zur Neuheit und gelten nicht als neu akzeptierte vollständige Lösungen.", "Vergleichende Rangfolge"),
            "fr": ("Manuscrits des autres conversations", "Les huit dossiers stoc1–stoc8 sont recensés : cinq manuscrits existants et trois dossiers de modèles. Les limites de portée et de nouveauté sont conservées ; il ne s’agit pas de nouvelles résolutions validées par la recherche continue.", "Classement comparatif"),
            "ja": ("他の会話の論文原稿", "stoc1–stoc8 の全八フォルダーを整理した。既存の論文原稿は五編で、三フォルダーはテンプレートのみである。各原稿の独創性と結果の範囲に関する制限を保持し、継続研究で新たに承認された完全解答とは扱わない。", "比較順位")
        }[lang]
        lines += [f"## {extra[0]}", "", extra[1], "", "[stoc1–stoc8](conversations/README.md)", ""]
        for p in json.loads((ROOT / "conversation-catalog.json").read_text())["items"]:
            if p["kind"] != "existing-conversation-manuscript":
                continue
            lines += [f"### {p['title']}", "", f"**{t['abstract']}.** {ABSTRACTS[p['id']][lang]}", "", f"[PDF]({p['pdf']}) · [ZIP]({p['source_archive']}) · [Code]({p['source_directory']}/) · [Reproduce]({p['readme']})", ""]
        lines += [f"## {extra[2]}", "", "[中文：按 STOC 相对竞争力和新增解决问题大小排序](RANKING.zh-CN.md) · [English assessment](RANKING.md) · [Data](ranking.json)", "", "```sh", "python3 scripts/check_conversations.py --all", "```", ""]
        (ROOT / filename).write_text("\n".join(lines))
    for p in PAPERS:
        commands = "\n".join("python3 " + " ".join(c) for c in p["reproduction_commands"])
        text = f'''# {p['title']}

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

{ABSTRACTS[p['id']]['en']}

Scope: **{'resolution of the stated target' if p['kind']=='resolution-paper' else 'legacy partial result; original broader question unresolved'}**. {p['pages']} total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper {p['id']}
python3 scripts/build_pdfs.py --paper {p['id']}
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
{commands}
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
'''
        (ROOT / "papers" / p["id"] / "README.md").write_text(text)


if __name__ == "__main__":
    main()
