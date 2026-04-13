# 🧠 Aus Discourse Intelligence Engine

A data-driven system for analysing Australian parliamentary discourse using a hybrid approach of deterministic phrase statistics and semantic embeddings.

---

## 🎯 Objective

This project transforms parliamentary transcripts (e.g. Hansard from the Parliament of Australia) into structured, analysable data to enable:

- Tracking how political language evolves over time  
- Comparing discourse across parties, speakers, and chambers  
- Identifying emerging narratives and shifts in focus  
- Exploring both exact phrasing and semantic meaning  

> **Guiding principle:**  
> *Measure what is said, not what is believed.*

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

### Data
- Source: Australian Parliament Hansard transcripts  
- Format: HTML / XML  
- Metadata:
  - date
  - chamber
  - speaker
  - party
  - source URL

### Storage
- PostgreSQL (structured data)  
- OpenSearch (semantic search layer)

### Processing
- Python (pandas, spaCy)  
- Jupyter notebooks for exploration

---

## ⚙️ Core Pipeline

1. **Ingestion**
   - Load and parse transcripts
   - Store raw text + metadata

2. **Segmentation**
   - Split into speaker-level units

3. **Phrase Extraction**
   - Tokenise text
   - Generate n-grams
   - Filter noise (stopwords, low frequency)

4. **Statistical Analysis**
   - Compute:
     - raw counts
     - mentions per 1,000 words
     - speech counts
     - unique speaker counts

5. **Vectorisation**
   - Generate embeddings
   - Enable semantic querying

6. **Exploration**
   - Query phrases or concepts
   - View trends over time
   - Drill into source material

---

## 🔗 Source Linking

Every insight must link back to:
- original transcript segment
- matched phrase/context
- source URL

This ensures full transparency and verifiability.

---

## 📁 Project Structure

```
project/
notebooks/
01_ingestion.ipynb
02_phrase_extraction.ipynb
03_analysis.ipynb
04_embeddings.ipynb
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
- Basic ingestion pipeline  
- Speaker-level segmentation  
- N-gram extraction  
- Simple frequency analysis  

### Phase 2
- Improved phrase detection (noun phrases, collocations)  
- Normalized metrics  
- Time-series analysis  

### Phase 3
- Embeddings + semantic search (OpenSearch)  
- Clustering and topic exploration  

### Phase 4
- API + frontend exploration tool  

---

## 🧭 Vision

Inspired by Kevin Rudd’s analysis in *On Xi Jinping*, where he tracks the frequency of key terms in Chinese political discourse, this project explores how similar techniques can be applied — and automated — for Australian parliamentary speech.

The goal is to move from manual counting of political language to a scalable, data-driven system that continuously tracks and analyses discourse over time.
---

## 🛠️ Getting Started

```bash
# Clone repo
git clone https://github.com/your-username/discourse-intelligence-engine.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📌 Status

🚧 Early-stage (Jupyter-first development)
