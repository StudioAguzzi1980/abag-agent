#!/usr/bin/env python3
"""
LinkedIn Post Analyzer — ABAG Agent Tools
==========================================
Analizza i post LinkedIn esportati da LinkedIn (formato CSV).

Utilizzo:
    python linkedin_post_analyzer.py --input Share.csv [--output report.md] [--top-keywords 20]

Supporta il file "Share.csv" presente nell'export dati di LinkedIn
(Impostazioni → Privacy dei dati → Ottieni una copia dei tuoi dati → Posts).
"""

import argparse
import csv
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Costanti
# ---------------------------------------------------------------------------

# Stopwords comuni in italiano e inglese da escludere dall'analisi delle parole
STOPWORDS = {
    # Italiano
    "il", "la", "lo", "i", "gli", "le", "un", "una", "uno", "di", "del", "della",
    "dello", "dei", "degli", "delle", "a", "al", "alla", "allo", "ai", "agli",
    "alle", "da", "dal", "dalla", "dallo", "dai", "dagli", "dalle", "in", "nel",
    "nella", "nello", "nei", "negli", "nelle", "su", "sul", "sulla", "sullo",
    "sui", "sugli", "sulle", "per", "tra", "fra", "con", "e", "o", "ma", "se",
    "che", "chi", "cui", "non", "più", "come", "quando", "dove", "perché",
    "questo", "questa", "questi", "queste", "quello", "quella", "quelli", "quelle",
    "sono", "è", "era", "stato", "stati", "stata", "state", "ha", "hanno",
    "ho", "hai", "abbiamo", "avete", "ci", "ne", "si", "mi", "ti", "vi", "li",
    "anche", "già", "ancora", "molto", "bene", "sempre", "mai", "ogni",
    # Inglese
    "the", "a", "an", "and", "or", "but", "if", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "that", "this", "these", "those", "it", "its",
    "we", "you", "he", "she", "they", "i", "my", "your", "our", "their",
    "as", "not", "so", "all", "more", "also", "can", "about", "which",
    "than", "into", "up", "out", "some", "any", "what", "how", "when", "where",
}

# Colonne possibili nell'export LinkedIn (dipende dalla lingua dell'interfaccia)
POSSIBLE_DATE_COLUMNS = ["Date", "Data", "date", "data", "Timestamp"]
POSSIBLE_TEXT_COLUMNS = ["ShareCommentary", "Commentary", "Text", "Content",
                         "Testo", "Contenuto", "Message", "share_commentary"]


# ---------------------------------------------------------------------------
# Parsing del CSV
# ---------------------------------------------------------------------------

def detect_column(headers: list[str], candidates: list[str]) -> str | None:
    """Restituisce il primo nome colonna trovato tra i candidati."""
    for c in candidates:
        if c in headers:
            return c
    return None


def load_posts(filepath: Path) -> list[dict]:
    """Carica i post dal file CSV di export LinkedIn."""
    posts = []
    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        date_col = detect_column(headers, POSSIBLE_DATE_COLUMNS)
        text_col = detect_column(headers, POSSIBLE_TEXT_COLUMNS)

        if not text_col:
            print(f"[ERRORE] Colonna testo non trovata. Colonne disponibili: {headers}")
            print("  Specifica la colonna con --text-column <nome>")
            sys.exit(1)

        if not date_col:
            print(f"[AVVISO] Colonna data non trovata. L'analisi temporale sarà disabilitata.")

        for row in reader:
            text = row.get(text_col, "").strip()
            date_raw = row.get(date_col, "") if date_col else ""
            if text:
                posts.append({"text": text, "date_raw": date_raw, "raw": row})

    return posts


# ---------------------------------------------------------------------------
# Analisi
# ---------------------------------------------------------------------------

def parse_date(date_str: str) -> datetime | None:
    """Prova a parsare la data in vari formati."""
    formats = [
        "%Y-%m-%d %H:%M:%S UTC",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None


def extract_keywords(text: str) -> list[str]:
    """Estrae le parole chiave da un testo (minuscolo, senza punteggiatura, senza stopwords)."""
    words = re.findall(r"[a-zA-ZÀ-ÿ]{3,}", text.lower())
    return [w for w in words if w not in STOPWORDS]


def extract_hashtags(text: str) -> list[str]:
    """Estrae gli hashtag da un testo."""
    return [tag.lower() for tag in re.findall(r"#\w+", text)]


def analyze_posts(posts: list[dict], top_n: int = 20) -> dict:
    """Esegue l'analisi completa dei post."""
    all_keywords: list[str] = []
    all_hashtags: list[str] = []
    lengths: list[int] = []
    dates: list[datetime] = []
    monthly_counts: Counter = Counter()

    for post in posts:
        text = post["text"]
        lengths.append(len(text))
        all_keywords.extend(extract_keywords(text))
        all_hashtags.extend(extract_hashtags(text))

        dt = parse_date(post["date_raw"])
        if dt:
            dates.append(dt)
            monthly_counts[dt.strftime("%Y-%m")] += 1

    keyword_freq = Counter(all_keywords)
    hashtag_freq = Counter(all_hashtags)

    return {
        "total_posts": len(posts),
        "avg_length": sum(lengths) / len(lengths) if lengths else 0,
        "max_length": max(lengths) if lengths else 0,
        "min_length": min(lengths) if lengths else 0,
        "top_keywords": keyword_freq.most_common(top_n),
        "top_hashtags": hashtag_freq.most_common(top_n),
        "monthly_counts": sorted(monthly_counts.items()),
        "date_range": (min(dates), max(dates)) if dates else None,
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def build_markdown_report(posts: list[dict], analysis: dict, source_file: str) -> str:
    """Genera un report in formato Markdown."""
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines += [
        "# Report Analisi Post LinkedIn",
        "",
        f"**File sorgente:** `{source_file}`  ",
        f"**Generato il:** {now}  ",
        "",
        "---",
        "",
        "## Statistiche Generali",
        "",
        f"| Metrica | Valore |",
        f"|---------|--------|",
        f"| Totale post analizzati | **{analysis['total_posts']}** |",
        f"| Lunghezza media (caratteri) | {analysis['avg_length']:.0f} |",
        f"| Post più lungo (caratteri) | {analysis['max_length']} |",
        f"| Post più corto (caratteri) | {analysis['min_length']} |",
    ]

    if analysis["date_range"]:
        start, end = analysis["date_range"]
        lines.append(f"| Periodo | {start.strftime('%d %b %Y')} → {end.strftime('%d %b %Y')} |")

    lines += ["", "---", "", "## Parole Chiave più Frequenti", ""]
    lines.append("| # | Parola | Occorrenze |")
    lines.append("|---|--------|-----------|")
    for rank, (word, count) in enumerate(analysis["top_keywords"], 1):
        lines.append(f"| {rank} | `{word}` | {count} |")

    if analysis["top_hashtags"]:
        lines += ["", "---", "", "## Hashtag più Utilizzati", ""]
        lines.append("| # | Hashtag | Occorrenze |")
        lines.append("|---|---------|-----------|")
        for rank, (tag, count) in enumerate(analysis["top_hashtags"], 1):
            lines.append(f"| {rank} | `{tag}` | {count} |")

    if analysis["monthly_counts"]:
        lines += ["", "---", "", "## Distribuzione Mensile dei Post", ""]
        lines.append("| Mese | Post |")
        lines.append("|------|------|")
        for month, count in analysis["monthly_counts"]:
            bar = "█" * count
            lines.append(f"| {month} | {count} {bar} |")

    lines += ["", "---", "", "## Testi dei Post", ""]
    for i, post in enumerate(posts, 1):
        date_str = post["date_raw"] if post["date_raw"] else "data sconosciuta"
        text_preview = post["text"].replace("\n", " ")
        lines.append(f"### Post {i} — {date_str}")
        lines.append("")
        lines.append(text_preview)
        lines.append("")

    return "\n".join(lines)


def build_csv_report(analysis: dict) -> str:
    """Genera un report sintetico in formato CSV."""
    lines = ["tipo,chiave,valore"]
    lines.append(f"statistiche,totale_post,{analysis['total_posts']}")
    lines.append(f"statistiche,lunghezza_media,{analysis['avg_length']:.0f}")
    for word, count in analysis["top_keywords"]:
        lines.append(f"keyword,{word},{count}")
    for tag, count in analysis["top_hashtags"]:
        lines.append(f"hashtag,{tag},{count}")
    for month, count in analysis["monthly_counts"]:
        lines.append(f"mensile,{month},{count}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analizza i post LinkedIn esportati da LinkedIn (CSV).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Percorso del file CSV esportato da LinkedIn (es. Share.csv)"
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="File di output (es. report.md o report.csv). Default: stampa a schermo"
    )
    parser.add_argument(
        "--format", "-f", choices=["markdown", "csv"], default="markdown",
        help="Formato del report (default: markdown)"
    )
    parser.add_argument(
        "--top-keywords", "-k", type=int, default=20,
        help="Numero di parole chiave da mostrare (default: 20)"
    )
    parser.add_argument(
        "--text-column", default=None,
        help="Nome della colonna testo nel CSV (se non rilevata automaticamente)"
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERRORE] File non trovato: {input_path}")
        sys.exit(1)

    print(f"[INFO] Caricamento post da: {input_path}")
    posts = load_posts(input_path)
    print(f"[INFO] Post caricati: {len(posts)}")

    if not posts:
        print("[ERRORE] Nessun post trovato nel file.")
        sys.exit(1)

    print("[INFO] Analisi in corso...")
    analysis = analyze_posts(posts, top_n=args.top_keywords)

    if args.format == "csv":
        report = build_csv_report(analysis)
    else:
        report = build_markdown_report(posts, analysis, str(input_path))

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding="utf-8")
        print(f"[INFO] Report salvato in: {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
