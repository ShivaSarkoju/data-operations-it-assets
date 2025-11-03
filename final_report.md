# Final Report – Data Operations IT Assets

## Overview

This mini project focuses on building a data pipeline for IT asset inventory management. It includes data cleaning, indexing, transformation, visualization, and version control.

---

## Phase 1: Excel Data Cleaning

- Cleaned raw IT asset data using Excel.
- Removed unnecessary rows and columns.
- Standardized date formats to `yyyy-mm-dd`.

---

## Phase 2: Indexing Data to Elasticsearch

- Connected to Elasticsearch using Python.
- Indexed cleaned data using custom scripts.
- Verified data ingestion using Elasticsearch queries.

---

## Phase 3: Data Transformation

- Created `transform_data.py` to enrich and reshape data.
- Used Elasticsearch queries to retrieve and validate transformed data.

---

## Phase 4: Visualization in Kibana

- Created dashboards and visualizations:
  - **Bar Chart**: Top 5 countries vs. unique hostnames.
  - **Pie Chart**: Hostname count by top 5 countries.
  - **Heat Map**: Median performance score by country and hostname.
  - **Table**: Performance scores split by country and hostnames.

---

## Phase 5: GitHub Submission

- All project files, scripts, and documentation were uploaded to GitHub for version control and collaboration.

---

## Conclusion

This project demonstrates a complete data lifecycle using modern tools and practices. It showcases skills in data cleaning, Python scripting, Elasticsearch indexing, and dashboard creation in Kibana.