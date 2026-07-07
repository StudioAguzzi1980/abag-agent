# LinkedIn Post Analyzer — Guida all'uso

Strumento Python per analizzare i post LinkedIn esportati come file CSV.  
**Non richiede API key né accesso a internet** — funziona interamente offline sul tuo file export.

---

## Prerequisiti

- Python 3.11 o superiore
- Nessuna libreria esterna richiesta (usa solo la standard library)

---

## Passo 1 — Esporta i tuoi dati da LinkedIn

1. Accedi a [linkedin.com](https://www.linkedin.com)
2. Vai su **Impostazioni → Privacy dei dati → Ottieni una copia dei tuoi dati**
3. Seleziona **"Posts"** (o "Tutto" per un export completo)
4. Clicca **Richiedi archivio** — LinkedIn ti invierà un'email entro qualche minuto/ora
5. Scarica il file ZIP dall'email e decomprimi
6. Trova il file **`Share.csv`** nella cartella decompressa

---

## Passo 2 — Esegui l'analisi

```bash
# Report Markdown a schermo
python tools/linkedin_post_analyzer.py --input /percorso/Share.csv

# Salva il report in un file Markdown
python tools/linkedin_post_analyzer.py --input /percorso/Share.csv --output report.md

# Report in formato CSV
python tools/linkedin_post_analyzer.py --input /percorso/Share.csv --output report.csv --format csv

# Mostra le 30 parole chiave più frequenti (default: 20)
python tools/linkedin_post_analyzer.py --input /percorso/Share.csv --top-keywords 30
```

---

## Opzioni disponibili

| Opzione | Descrizione | Default |
|---------|-------------|---------|
| `--input` / `-i` | Percorso del file CSV LinkedIn (**obbligatorio**) | — |
| `--output` / `-o` | File di output (es. `report.md`) | Stampa a schermo |
| `--format` / `-f` | Formato output: `markdown` o `csv` | `markdown` |
| `--top-keywords` / `-k` | Numero di parole chiave da mostrare | `20` |
| `--text-column` | Nome colonna testo (se non rilevata automaticamente) | auto |

---

## Cosa contiene il report

Il report generato include:

- **Statistiche generali** — numero di post, lunghezza media/min/max, periodo coperto
- **Parole chiave più frequenti** — le parole più usate nei post (escluse le stopwords in italiano e inglese)
- **Hashtag più utilizzati** — gli hashtag più frequenti
- **Distribuzione mensile** — quanti post sono stati pubblicati ogni mese
- **Elenco completo dei post** — tutti i testi con data di pubblicazione

---

## Struttura del file CSV di LinkedIn

LinkedIn esporta i post in un file `Share.csv` con colonne simili a:

| Colonna | Descrizione |
|---------|-------------|
| `Date` | Data e ora di pubblicazione (UTC) |
| `ShareCommentary` | Testo del post |
| `ShareMediaCategory` | Tipo di media allegato (NONE, IMAGE, ARTICLE, ecc.) |
| `PostLink` | URL diretto al post |

---

## Esempio di output

```
# Report Analisi Post LinkedIn

**File sorgente:** `Share.csv`
**Generato il:** 2026-07-07 17:00

## Statistiche Generali

| Metrica | Valore |
|---------|--------|
| Totale post analizzati | 47 |
| Lunghezza media (caratteri) | 312 |
| Periodo | 01 Jan 2023 → 07 Jul 2026 |

## Parole Chiave più Frequenti

| # | Parola | Occorrenze |
|---|--------|-----------|
| 1 | `business` | 34 |
| 2 | `italy` | 28 |
...
```

---

## Risoluzione problemi

**"Colonna testo non trovata"**  
Apri il file CSV con un editor di testo o Excel e verifica il nome esatto della colonna con il testo dei post. Poi usa:
```bash
python tools/linkedin_post_analyzer.py --input Share.csv --text-column "NomeColonna"
```

**"File non trovato"**  
Controlla il percorso del file. Su Windows usa i backslash o il percorso assoluto:
```bash
python tools/linkedin_post_analyzer.py --input "C:\Users\TuoNome\Downloads\Basic_LinkedInDataExport\Share.csv"
```

---

*Strumento sviluppato per il progetto ABAG Agent. Tutti i dati rimangono locali — nessuna informazione viene inviata a server esterni.*
