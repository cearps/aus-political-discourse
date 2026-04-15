# 🧠 Aus political discourse (analysis + display)

This repository is the **analysis and display** layer for Australian parliamentary discourse: notebooks and Python utilities that operate over **pre-built Parquet exports** of Hansard-derived data.

For datasource provenance and required attribution, see `docs/datasource.md`.

---

## 🎯 Objective

This project transforms parliamentary transcripts (e.g. Hansard from the Parliament of Australia) into structured, analysable data to enable:

- Tracking how political language evolves over time
- Comparing discourse across parties, speakers, and chambers
- Identifying emerging narratives and shifts in focus
- Exploring both exact phrasing and semantic meaning

> **Guiding principle:**  
> _Measure what is said, not what is believed._

---

## 🧪 Approach

The system combines two complementary layers:

### 1. Deterministic Layer (Statistical)

- Tokenisation (spaCy)
- N-gram extraction (unigrams, bigrams, trigrams)
- Frequency and normalized metrics
- Aggregation by:
  - date
  - speaker
  - party
  - chamber

### 2. Semantic Layer (Vector-Based)

- Embeddings per speech segment
- Semantic search (e.g. “housing affordability”)
- Clustering of discourse themes
- Discovery of related language beyond exact keywords

---

## 🏗️ Architecture (Early Stage)

### Data inputs

- **Now**: you manually place Parquet exports into `data/raw/` (kept out of git).
- **Later**: this repo will optionally read from a **ClickHouse** instance produced/maintained in another repo (once stood up).

### Processing

- Python (pandas, spaCy)
- Jupyter notebooks for exploration

---

## ⚙️ What this repo does (scope)

- **Analyse**: phrase stats, aggregations, embeddings, semantic search prototypes.
- **Display**: notebooks now; later an API/frontend that queries ClickHouse (and/or local Parquet).

This repo is **not** responsible for scraping Hansard, parsing XML, or producing the canonical corpus export (that ingestion/ETL lives elsewhere).

---

## 🔗 Source Linking

Every insight must link back to:

- original transcript segment
- matched phrase/context
- source URL

This ensures full transparency and verifiability.

---

## 📁 Project Structure

```text
docs/
  datasource.md
notebooks/
  01_ingestion.ipynb
src/
  ingest.py
  segment.py
  phrases.py
  stats.py
  embed.py
```

---

## 📊 Example Outputs

- “Mentions of ‘housing supply’ increased 180% over 12 months”
- “Opposition speakers used ‘cost of living’ 3x more than government this quarter”
- “New phrase ‘rent crisis’ emerged and rapidly increased in usage”
- “Semantically similar speeches reveal growing focus on affordability constraints”

---

## ⚠️ Constraints

- No interpretation of intent or belief
- Avoid misleading aggregation
- Ensure accurate speaker attribution
- Maintain strict linkage to source material

---

## 🚀 Roadmap

### Phase 1 (MVP)

- Load and validate provided Parquet exports
- Speaker-level segmentation utilities (where needed for analysis)
- Simple frequency analysis in notebooks

### Phase 2

- Improved phrase detection (noun phrases, collocations)
- Normalized metrics
- Time-series analysis

### Phase 3

- Embeddings + semantic search prototypes
- Clustering and topic exploration

### Phase 4

- API + frontend exploration tool (backed by ClickHouse, with Parquet fallback)

---

## 🧭 Vision

Inspired by Kevin Rudd’s analysis in _On Xi Jinping_, where he tracks the frequency of key terms in Chinese political discourse, this project explores how similar techniques can be applied — and automated — for Australian parliamentary speech.

**The goal** is to move from manual counting of political language to a scalable, data-driven system that continuously tracks and analyses discourse over time.

## 🛠️ Getting Started

```bash
# Clone repo
git clone <this-repo>

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📌 Status

🚧 Early-stage (Jupyter-first development)
