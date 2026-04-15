# Datasource research

## Primary upstream sources

### Australian Parliamentary Debates (Hansard), APH website

- **Source**: Australian Parliament House (APH) Hansard pages and linked XML downloads.
- **What we ingest**: **Hansard XML** per sitting day (House; Senate potentially later).
- **Provenance note**: navigation and download links can change over time (the upstream project documents the path “as at July 2023”).

### Digitized database (1998–2022) by Katz et al

This project is built on (and extends) the digitized parliamentary debates corpus produced in the upstream `hansard-proj` project:

- **Upstream repository**: `https://github.com/lindsaykatz/hansard-proj`
- **Upstream dataset release**: the upstream README points to a “most recent version” on Zenodo at `https://zenodo.org/record/7336075`.
- **Coverage**: upstream describes **1998–2022**.
- **Method**: R-based pipeline (scrape XML → parse → fill member details → validate → add PartyFacts IDs → export daily files + combined corpus).

## What’s happening in our fork / adaptation

### Goal

Maintain a reproducible pipeline that can generate an exported Parquet corpus for analysis (and downstream loading to ClickHouse), while staying faithful to upstream definitions and data cleaning decisions.

Planned extensions:

- **Senate support**: write agents that extend the current implementation (which is House-only today) to ingest/process **Senate** Hansard as well.

### Current output in this repo

- **Corpus Parquet**: `data/raw/corpus_1998_to_latest.parquet`

### How `hansard-proj` works (local clone summary)

The cloned upstream repo contains:

- **R scripts**: the original “corpus v1” pipeline scripts (`scripts/corpus_v1/*`) and a newer “corpus v2” set (`scripts/corpus_v2/*`) plus an incremental corpus builder (`scripts/build_corpus_incremental.R`).
- **A Python orchestrator + scraper**: a single-command pipeline runner that scrapes the latest APH XMLs and then calls the R steps to produce daily Parquet and an updated corpus Parquet.
  - The orchestrator documentation explicitly states **scope is House of Representatives only** right now.
  - It is designed to be **idempotent**: existing XMLs and per-date artifacts are not regenerated; reruns resume.

## Attribution (required)

### Upstream project credit

This repository incorporates ideas, workflow structure, and data-processing logic from `hansard-proj`:

- **Repository**: `https://github.com/lindsaykatz/hansard-proj`
- **Primary author/maintainer (from git history)**: **Lindsay Katz**
- **Additional contributor (from git history)**: **Rohan Alexander**

If you publish analyses or derived datasets, you should also cite the upstream Zenodo release referenced by `hansard-proj` (see link above) and the Australian Parliament House Hansard source.

## Design principles for our pipeline

- **Idempotency**: never re-download/re-process historical days unless explicitly forced.
- **Incremental updates**: only ingest and process new sitting days, then rebuild/append the “latest” corpus.
- **Separation of concerns**: keep ingestion/ETL separate from analysis layers (notebooks → later API/frontend).
- **Traceability**: retain the per-day artifacts (XML / parsed CSV / filled CSV / daily Parquet) so the combined corpus can be audited.
- **Correctness checks**: verify Parquet outputs as part of the process (schema/column expectations, row counts, date coverage, and spot-check joins/flags) before treating a build as valid.
