This is a an end-to-end data engineering project that ingests ticker data from Yahoo Finance, cleans, enriches, and displays the data in a user-friendly dashboard.

This project uses Docker contrainers to deploy Airflow, which orchestrates the ELT pipeline, downloading data from the yf API to a delta lake bronze layer. It uses dbt and PySpark to build models across the silver and gold layers. The analytics are displayed in Streamlit.

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
[Gold Delta Table / Aggregates]
          │
          ▼
   Streamlit Dashboard / Analytics
```
