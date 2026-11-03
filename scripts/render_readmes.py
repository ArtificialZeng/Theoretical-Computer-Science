#!/usr/bin/env python3
"""Render one unified index in five languages, with two collapsed groups."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {'en': 'README.md', 'zh': 'README.zh-CN.md', 'de': 'README.de.md', 'fr': 'README.fr.md', 'ja': 'README.ja.md'}
NAV = ' · '.join(f'[{label}]({FILES[key]})' for key, label in [('en','English'),('zh','中文'),('de','Deutsch'),('fr','Français'),('ja','日本語')])
TEXT = {
 'en': {
  'intro': 'Research in theoretical computer science: algorithms, complexity, combinatorics, automata, optimization and program analysis. Each topic includes an abstract, manuscript PDFs, original source archives and browseable code. **{total} topics: {ready} submission_ready, {working} working_paper.**',
  'policy': 'All topics share the same two categories, regardless of where the work originated. submission_ready requires a fresh, strong assessment of importance, novelty, technical depth, breadth and verifiability, as well as the artifact checks. working_paper includes results below that threshold and existing drafts with unresolved scope or missing assessments. Labels are internal judgments, not conference decisions; mathematical scope is stated for each topic. See the [quality standard](QUALITY_STANDARD.md).',
  'ready': 'STOC-level · submission_ready', 'working': 'Working papers · working_paper',
  'click': 'Click either group to expand its complete index and abstracts.',
  'empty': 'No manuscript currently satisfies the shared submission_ready standard.',
  'topic': 'Topic', 'pages': 'Pages', 'files': 'Files', 'abstract': 'Abstract', 'code': 'Code', 'reproduce': 'Reproduce',
  'partial': 'The broader original question remains unresolved. This existing partial draft is preserved as working_paper, not counted as a new complete resolution.',
  'extra': 'Additional expanded version', 'prior': 'Earlier version',
  'extra_note': 'Same topic; retained original authors and source bytes. This version has not passed the shared fresh STOC-level assessment.',
  'repro_title': 'Code and reproducibility',
  'repro': 'Run the commands below from the repository root. For a single topic, replace --all with --paper ID. Python 3.10+ is required; some artifacts additionally need Rust, Node.js, scientific Python packages or project-specific tools. PDF builds require LaTeX, latexmk and Poppler. Per-topic instructions and original dependency notes are linked above. Finite checks cover their documented cases and do not replace general proofs.',
  'layout': 'catalog.json is the unified machine-readable index; readiness.json contains the two categories. Existing file URLs remain valid. PDF filenames carry the current label while original PDFs and ZIPs are preserved. Historical comparisons remain available in [English](RANKING.md) and [Chinese](RANKING.zh-CN.md); they cover an older snapshot and do not set current readiness.',
  'notes': 'Additional method diagnostics and exact checkers: [parity interface](notes/tp-parity-interface/) · [cycle lifting](notes/facet-cycle-lifting/). These are research notes, not additional manuscript categories.',
  'author': 'Maintainer: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Original manuscript author lists are preserved. Substantial AI assistance is disclosed in the manuscripts; local model reviews are not external peer review. Third-party notices remain in place: [RIGHTS.md](RIGHTS.md).',
 },
 'zh': {
  'intro': '理论计算机科学研究：算法、复杂性、组合数学、自动机、优化及程序分析。每个课题提供摘要、论文 PDF、原始源码包及可浏览代码。**共{total}个课题：{ready}个 submission_ready，{working}个 working_paper。**',
  'policy': '全部课题统一按以下两类展示，不再按工作来源分组。submission_ready 需要新的审核对重要性、新颖性、技术深度、影响范围及可核验性均给出有充分依据的强评价，并通过文件交付检查；working_paper 收录未达到该标准的结果，以及范围仍有限或缺少相应审核的已有稿件。分类属于内部判断，不是会议录用结论；各课题的实际数学范围分别说明。详见[质量标准](QUALITY_STANDARD.md)。',
  'ready': 'STOC 级别 · submission_ready', 'working': '工作论文 · working_paper',
  'click': '点击下方任一分组，展开完整目录与各课题摘要。',
  'empty': '目前没有稿件达到统一的 submission_ready 标准。',
  'topic': '课题', 'pages': '页数', 'files': '文件', 'abstract': '摘要', 'code': '代码', 'reproduce': '复现说明',
  'partial': '原始更广泛问题仍未解决。这份已有部分结果稿作为 working_paper 保留，不计为新通过的完整原题解答。',
  'extra': '另附扩展版本', 'prior': '早期版本',
  'extra_note': '属于同一课题，保留原作者及源文件字节；该版本尚未通过统一标准下新的 STOC 级别审核。',
  'repro_title': '代码与可复现性',
  'repro': '在仓库根目录运行下列命令。单个课题可将 --all 替换为 --paper ID。需要 Python 3.10+；部分材料另需 Rust、Node.js、科学计算 Python 包或课题专用工具。PDF 编译需要 LaTeX、latexmk 和 Poppler。具体步骤与原始依赖说明见各课题入口。有限检查只覆盖注明的实例，不能替代一般性证明。',
  'layout': 'catalog.json 是统一的机器可读目录，readiness.json 记录两类状态。原有文件链接继续有效；当前 PDF 文件名带状态标记，原 PDF 与 ZIP 均保留。此前的[英文](RANKING.md)及[中文](RANKING.zh-CN.md)比较评价仍可查阅，但只针对旧快照，不决定当前就绪状态。',
  'notes': '额外的方法诊断与精确检查代码：[奇偶接口](notes/tp-parity-interface/) · [环提升](notes/facet-cycle-lifting/)。它们属于研究笔记，不构成第三类论文分组。',
  'author': '维护者：**Zijian Zeng，UCSI University** · 1002266693@ucsiuniversity.edu.my。保留原稿作者名单。论文披露了实质性 AI 辅助；本地模型审核不是外部同行评审。第三方许可说明保留，见 [RIGHTS.md](RIGHTS.md)。',
 },
 'de': {
  'intro': 'Forschung in theoretischer Informatik: Algorithmen, Komplexität, Kombinatorik, Automaten, Optimierung und Programmanalyse. Jedes Thema bietet eine Zusammenfassung, Manuskript-PDFs, originale Quellarchive und einsehbaren Code. **{total} Themen: {ready} submission_ready, {working} working_paper.**',
  'policy': 'Alle Themen verwenden dieselben zwei Kategorien, unabhängig von ihrer Herkunft. submission_ready erfordert eine neue, begründete starke Bewertung von Bedeutung, Neuheit, technischer Tiefe, Reichweite und Überprüfbarkeit sowie bestandene Artefaktprüfungen. working_paper umfasst Ergebnisse unterhalb dieser Schwelle und vorhandene Entwürfe mit offenen Fragen oder fehlender Bewertung. Die Einordnung ist ein internes Urteil, keine Konferenzentscheidung; der mathematische Geltungsbereich steht beim jeweiligen Thema. Siehe [Qualitätsstandard](QUALITY_STANDARD.md).',
  'ready': 'STOC-Niveau · submission_ready', 'working': 'Arbeitspapiere · working_paper',
  'click': 'Eine Gruppe anklicken, um das gesamte Verzeichnis und die Zusammenfassungen aufzuklappen.',
  'empty': 'Derzeit erfüllt kein Manuskript den gemeinsamen submission_ready-Standard.',
  'topic': 'Thema', 'pages': 'Seiten', 'files': 'Dateien', 'abstract': 'Zusammenfassung', 'code': 'Code', 'reproduce': 'Reproduktion',
  'partial': 'Die allgemeinere Ausgangsfrage bleibt offen. Dieser vorhandene Teilresultat-Entwurf bleibt working_paper und zählt nicht als neue vollständige Lösung.',
  'extra': 'Zusätzliche erweiterte Fassung', 'prior': 'Frühere Fassung',
  'extra_note': 'Dasselbe Thema; ursprüngliche Autoren und Quelldateien bleiben erhalten. Diese Fassung hat die gemeinsame neue STOC-Bewertung nicht bestanden.',
  'repro_title': 'Code und Reproduzierbarkeit',
  'repro': 'Die folgenden Befehle im Wurzelverzeichnis ausführen. Für ein Thema --all durch --paper ID ersetzen. Erforderlich ist Python 3.10+; einige Artefakte brauchen zusätzlich Rust, Node.js, wissenschaftliche Python-Pakete oder themenspezifische Werkzeuge. PDF-Erstellung benötigt LaTeX, latexmk und Poppler. Die verlinkten Themenhinweise nennen Schritte und Abhängigkeiten. Endliche Tests decken nur ihre angegebenen Fälle ab und ersetzen keine allgemeinen Beweise.',
  'layout': 'catalog.json ist das einheitliche maschinenlesbare Verzeichnis; readiness.json enthält die beiden Kategorien. Bisherige Datei-URLs bleiben gültig. Aktuelle PDF-Namen tragen die Einordnung, originale PDFs und ZIPs bleiben erhalten. Ältere Vergleiche sind auf [Englisch](RANKING.md) und [Chinesisch](RANKING.zh-CN.md) verfügbar; sie bewerten einen früheren Stand und bestimmen nicht die aktuelle Einordnung.',
  'notes': 'Weitere Methodendiagnosen und exakte Prüfer: [Paritätsschnittstelle](notes/tp-parity-interface/) · [Zyklushebung](notes/facet-cycle-lifting/). Dies sind Forschungsnotizen, keine zusätzliche Manuskriptkategorie.',
  'author': 'Verantwortlicher: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Die ursprünglichen Autorenlisten bleiben erhalten. Wesentliche KI-Unterstützung ist in den Manuskripten offengelegt; lokale Modellprüfungen sind kein externes Peer-Review. Hinweise Dritter: [RIGHTS.md](RIGHTS.md).',
 },
 'fr': {
  'intro': 'Recherche en informatique théorique : algorithmes, complexité, combinatoire, automates, optimisation et analyse de programmes. Chaque sujet propose un résumé, des PDF, les archives sources originales et du code consultable. **{total} sujets : {ready} submission_ready, {working} working_paper.**',
  'policy': 'Tous les sujets partagent ces deux catégories, indépendamment de leur origine. submission_ready exige une nouvelle appréciation forte et étayée de l’importance, de la nouveauté, de la profondeur technique, de la portée et de la vérifiabilité, ainsi que les contrôles des fichiers. working_paper regroupe les résultats sous ce seuil et les textes existants dont la portée reste ouverte ou l’évaluation manque. Ces catégories sont des jugements internes, pas des décisions de conférence ; la portée mathématique est précisée par sujet. Voir le [standard de qualité](QUALITY_STANDARD.md).',
  'ready': 'Niveau STOC · submission_ready', 'working': 'Documents de travail · working_paper',
  'click': 'Cliquer sur une catégorie pour déplier son index complet et les résumés.',
  'empty': 'Aucun manuscrit ne satisfait actuellement au standard commun submission_ready.',
  'topic': 'Sujet', 'pages': 'Pages', 'files': 'Fichiers', 'abstract': 'Résumé', 'code': 'Code', 'reproduce': 'Reproduction',
  'partial': 'La question initiale générale reste ouverte. Ce texte partiel existant est conservé comme working_paper et ne compte pas comme nouvelle résolution complète.',
  'extra': 'Version étendue supplémentaire', 'prior': 'Version antérieure',
  'extra_note': 'Même sujet ; auteurs et sources d’origine conservés. Cette version n’a pas reçu de validation selon le nouveau standard STOC commun.',
  'repro_title': 'Code et reproductibilité',
  'repro': 'Exécuter les commandes ci-dessous à la racine. Pour un sujet, remplacer --all par --paper ID. Python 3.10+ est nécessaire ; certains fichiers demandent aussi Rust, Node.js, des bibliothèques Python scientifiques ou des outils spécifiques. Compiler les PDF exige LaTeX, latexmk et Poppler. Les instructions par sujet précisent étapes et dépendances. Les tests finis ne couvrent que leurs cas documentés et ne remplacent pas les preuves générales.',
  'layout': 'catalog.json constitue l’index unifié lisible par machine ; readiness.json contient les deux catégories. Les anciennes URL restent valables. Les noms des PDF actuels portent la catégorie, tandis que les PDF et ZIP d’origine sont conservés. Les comparaisons antérieures restent disponibles en [anglais](RANKING.md) et en [chinois](RANKING.zh-CN.md) ; elles portent sur un ancien état et ne déterminent pas les catégories actuelles.',
  'notes': 'Autres diagnostics de méthodes et vérificateurs exacts : [interface de parité](notes/tp-parity-interface/) · [relèvement de cycles](notes/facet-cycle-lifting/). Ce sont des notes de recherche, pas une troisième catégorie de manuscrits.',
  'author': 'Responsable : **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Les listes d’auteurs originales sont conservées. L’assistance substantielle de l’IA est déclarée dans les manuscrits ; les contrôles locaux par modèles ne constituent pas une évaluation externe par les pairs. Mentions tierces : [RIGHTS.md](RIGHTS.md).',
 },
 'ja': {
  'intro': '理論計算機科学の研究：アルゴリズム、計算量、組合せ論、オートマトン、最適化、プログラム解析。各課題に概要、論文PDF、元のソースアーカイブ、閲覧可能なコードを添える。**全{total}課題：submission_ready {ready}件、working_paper {working}件。**',
  'policy': '出所にかかわらず、全課題を同じ二分類で示す。submission_ready には重要性、新規性、技術的深さ、波及範囲、検証可能性のすべてについて根拠のある強い新規評価と、成果物検査の通過が必要である。working_paper はその水準に届かない結果や、未解決範囲・未評価部分が残る既存稿を含む。分類は内部判断であり、会議の採否ではない。数学的範囲は課題ごとに記す。[品質基準](QUALITY_STANDARD.md)も参照。',
  'ready': 'STOC 水準 · submission_ready', 'working': 'ワーキングペーパー · working_paper',
  'click': '各分類をクリックすると、全目次と各課題の概要が展開される。',
  'empty': '共通の submission_ready 基準を満たす論文は現在ない。',
  'topic': '課題', 'pages': 'ページ', 'files': 'ファイル', 'abstract': '概要', 'code': 'コード', 'reproduce': '再現手順',
  'partial': '元の一般問題は未解決である。この既存の部分結果稿は working_paper として保存し、新しい完全解決には数えない。',
  'extra': '追加の拡張版', 'prior': '以前の版',
  'extra_note': '同じ課題の別版で、元の著者とソースを保存する。共通基準による新たな STOC 水準の認定は受けていない。',
  'repro_title': 'コードと再現性',
  'repro': '以下をリポジトリのルートで実行する。一課題だけなら --all を --paper ID に置き換える。Python 3.10+ が必要で、一部には Rust、Node.js、科学計算用Pythonパッケージ、専用ツールも必要である。PDF構築には LaTeX、latexmk、Poppler を使う。各課題のリンク先に手順と依存関係がある。有限検査は明示された事例のみを覆い、一般証明の代わりではない。',
  'layout': 'catalog.json が統一機械可読目次、readiness.json が二分類の記録である。既存URLを維持し、現行PDF名に分類を付け、元のPDFとZIPを保存する。以前の比較は[英語](RANKING.md)と[中国語](RANKING.zh-CN.md)で参照できるが、旧時点を対象とし現行分類を決定しない。',
  'notes': '追加の手法診断と正確な検査コード：[パリティ接口](notes/tp-parity-interface/) · [サイクルの持ち上げ](notes/facet-cycle-lifting/)。これらは研究ノートであり、第三の論文分類ではない。',
  'author': '管理者：**Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my。元の論文の著者一覧を保存する。実質的なAI支援は各稿で開示している。ローカルのモデル検査は外部査読ではない。第三者の権利表示：[RIGHTS.md](RIGHTS.md)。',
 }
}


RECORD_NOTICE = {
 'en': '**c049 remains unresolved in these records.** [Four-pass research dossier](notes/c049-dualpreserve/README.md) · [Code](notes/c049-dualpreserve/source/code/) · [Source ZIP](notes/c049-dualpreserve/source.zip). A sparse construction is proved for one shared-selector family; the original general-graph target is unresolved. This is an archived research record with no manuscript PDF.',
 'zh': '**c049 在这些记录中仍未解决。** [四轮研究记录](notes/c049-dualpreserve/README.zh-CN.md) · [代码](notes/c049-dualpreserve/source/code/) · [源码 ZIP](notes/c049-dualpreserve/source.zip)。已证明一个共享选择器图族的稀疏构造，原始任意图问题仍未解决；按研究记录归档，没有论文 PDF。',
 'de': '**c049 bleibt in diesen Aufzeichnungen ungelöst.** [Forschungsdossier aus vier Durchläufen](notes/c049-dualpreserve/README.de.md) · [Code](notes/c049-dualpreserve/source/code/) · [Quellarchiv](notes/c049-dualpreserve/source.zip). Eine dünne Konstruktion ist für eine Familie geteilter Selektoren bewiesen; das ursprüngliche Problem für allgemeine Graphen bleibt offen. Dies sind archivierte Forschungsaufzeichnungen ohne Manuskript-PDF.',
 'fr': '**c049 reste non résolu dans ce dossier.** [Dossier de quatre sessions](notes/c049-dualpreserve/README.fr.md) · [Code](notes/c049-dualpreserve/source/code/) · [Archive source](notes/c049-dualpreserve/source.zip). Une construction parcimonieuse est démontrée pour une famille de sélecteurs partagés ; le problème initial sur les graphes généraux reste ouvert. Ces archives de recherche ne comprennent aucun manuscrit PDF.',
 'ja': '**本記録で c049 は未解決である。** [四回の研究記録](notes/c049-dualpreserve/README.ja.md) · [コード](notes/c049-dualpreserve/source/code/) · [ソースZIP](notes/c049-dualpreserve/source.zip)。共有セレクターの特定の族では疎な構成を証明したが、一般グラフ上の元問題は未解決である。論文PDFを伴わない研究記録として保存する。'
}
RECORD_REPRO = {
 'en': 'To reproduce the separate c049 research record, use Python 3.10+ and a C++17 compiler:',
 'zh': 'c049 研究记录单独复现，需要 Python 3.10+ 和 C++17 编译器：',
 'de': 'Für die gesonderten c049-Aufzeichnungen sind Python 3.10+ und ein C++17-Compiler erforderlich:',
 'fr': 'Pour reproduire séparément le dossier c049, utiliser Python 3.10+ et un compilateur C++17 :',
 'ja': 'c049 の研究記録は別途再現する。Python 3.10+ と C++17 コンパイラが必要：'
}


def links(p, lang='en'):
    t = TEXT[lang]
    return f"[PDF]({p['pdf']}) · [ZIP]({p['source_archive']}) · [{t['code']}]({p['source_directory']}/) · [{t['reproduce']}]({p['readme']})"


def main():
    papers = json.loads((ROOT / 'catalog.json').read_text())['papers']
    abstracts = json.loads((ROOT / 'descriptions.json').read_text())
    counts = {key: sum(p['readiness_label'] == key for p in papers) for key in ['submission_ready', 'working_paper']}
    for lang, filename in FILES.items():
        t = TEXT[lang]
        lines = ['# Theoretical Computer Science', '', NAV, '',
                 t['intro'].format(total=len(papers), ready=counts['submission_ready'], working=counts['working_paper']),
                 '', t['policy'], '', t['click'], '']
        if (ROOT/'research-records.json').is_file():
            lines += [RECORD_NOTICE[lang], '']
        for label, heading in [('submission_ready', 'ready'), ('working_paper', 'working')]:
            selected = [p for p in papers if p['readiness_label'] == label]
            lines += ['<details>', f"<summary><strong>{t[heading]} ({len(selected)})</strong></summary>", '']
            if not selected:
                lines += [t['empty'], '']
            else:
                lines += [f"| {t['topic']} | {t['pages']} | {t['files']} |", '|---|---:|---|']
                for p in selected:
                    lines.append(f"| {p['title']} (`{p['id']}`) | {p['pages']} | {links(p, lang)} |")
                lines.append('')
                for p in selected:
                    lines += [f"### {p['title']}", '', f"**{t['abstract']}.** {abstracts[p['id']][lang]}", '']
                    if p.get('scope_warning') == 'original_unresolved':
                        lines += [t['partial'], '']
                    lines += [links(p, lang), '']
                    for version in p.get('additional_versions', []):
                        lines += [f"**{t['extra']} ({version['pages']} {t['pages']}):** [PDF]({version['pdf']}) · [ZIP]({version['source_archive']}) · [{t['code']}]({version['source_directory']}/). {t['extra_note']}", '']
                    if p.get('earlier_version'):
                        v=p['earlier_version']
                        lines += [f"{t['prior']} ({v['pages']} {t['pages']}): [PDF]({v['pdf']}) · [ZIP]({v['source_archive']}).", '']
            lines += ['</details>', '']
        lines += [f"## {t['repro_title']}", '', t['repro'], '', '```sh',
                  'git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git',
                  'cd Theoretical-Computer-Science', 'python3 scripts/verify_artifacts.py',
                  'python3 scripts/reproduce.py --all', 'python3 scripts/build_pdfs.py --all', '```', '',
                  RECORD_REPRO[lang], '', '```sh',
                  'python3 -B notes/c049-dualpreserve/source/reproduce.py', '```', '',
                  t['layout'], '', t['notes'], '', t['author'], '']
        (ROOT / filename).write_text('\n'.join(lines))
    for p in papers:
        directory=(ROOT/p['readme']).parent
        original=directory/'README.md'
        if original.exists() and not (directory/'README.previous.md').exists():
            original.rename(directory/'README.previous.md')
        text = ['# '+p['title'], '', '**'+p['readiness_label']+'** · '+str(p['pages'])+' total pages.', '',
                f"[PDF]({Path(p['pdf']).relative_to(Path(p['readme']).parent).as_posix()}) · [Unified index](../../README.md)", '',
                abstracts[p['id']]['en'], '', 'Classification basis: '+p['assessment_basis'], '',
                'Mathematical scope: '+p['mathematical_status'], '', 'From the repository root:', '',
                '```sh', f"python3 scripts/reproduce.py --paper {p['id']}", f"python3 scripts/build_pdfs.py --paper {p['id']}", '```', '',
                'The original archive and expanded source are linked in the unified index. Checks run on disposable copies. '
                'Finite checks are not a full proof, formal verification, new novelty review or external peer review. '
                'Original author lists and archived files remain unchanged.', '']
        for v in p.get('additional_versions', []):
            prefix=Path(p['readme']).parent
            text += [f"Additional version ({v['pages']} pages, working_paper): "
                     f"[PDF]({Path(v['pdf']).relative_to(prefix)}) · [ZIP]({Path(v['source_archive']).relative_to(prefix)}) · "
                     f"[Source]({Path(v['source_directory']).relative_to(prefix)}/). {v['assessment_basis']}", '']
        original.write_text('\n'.join(text))


if __name__ == '__main__':
    main()
