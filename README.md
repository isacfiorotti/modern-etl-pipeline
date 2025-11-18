# Lakehouse ETL with Delta, PySpark, and dbt

### Gold Price ETL Pipeline
This is a an end-to-end data engineering project that ingests gold prices from Yahoo Finance, cleans and enriches the data, and produces enriched analytics-ready data using Delta Lake, dbt and PySpark.

I was inspired to do this given the recent price surge on gold, initially driven up by international central banks increasing their supply of gold following a move away from of the dollar, while the dollar remains the world's global currency, this is a clear desire to decrease reliance on the global reserve currency as a store of value.

### NOTE: 
1. For this portfolio project, I have chosen to build the pipeline inside a notebook so I can comment on my design decisions.

2. This project will *not* use an orchestrator due to its scope, typically you would add materialisation checks at each stage and kick off the next step following data validation checks, common choices for this are Airflow, Prefect and Dagster.

## Get Started

1. In your ***.venv*** run the following: 
```
pip install poetry
```
```
poetry install
```

## Architecture Diagram
```
[Raw Data / Bronze Parquet]
          │
          ▼
   PySpark Transformations
          │
          ▼
[Silver Delta Table] -- (Incremental / ACID)
          │
          ▼
         dbt Models
          │
          ▼
[Gold Delta Table / Aggregates]
          │
          ▼
   Streamlit Dashboard / Analytics
```
