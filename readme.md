# Data Operations IT Assets – Mini Project

This project demonstrates a complete data pipeline for IT asset management, from data cleaning to visualization, using tools like Excel, Python, Elasticsearch, and Kibana.

## 📌 Project Phases

### ✅ Phase 1: Excel Data Cleaning
- Cleaned real-world messy data using Excel functions.
- Trimmed unnecessary rows and columns.
- Standardized date format from `dd-mm-yyyy` to `yyyy-mm-dd`.

### ✅ Phase 2: Indexing Data to Elasticsearch Using Python
- Connected to Elasticsearch.
- Wrote Python scripts to index and enrich data.
- Indexed cleaned data into Elasticsearch.

### ✅ Phase 3: Data Transformation & Enrichment
- Used Git for version control.
- Created `transform_data.py` for data transformation.
- Queried data using Elasticsearch console (`GET mini-project/_search`).

### ✅ Phase 4: Visualization and Insights
- Built dashboards in Kibana for IT asset insights.
- Created visualizations:
  - **Bar Chart**: Top 5 countries vs. unique hostnames.
  - **Pie Chart**: Hostname count by top 5 countries.
  - **Heat Map**: Median performance score by country and hostname.
  - **Table**: Performance scores split by country and hostnames.

### ✅ Phase 5: GitHub Submission
- Project files and documentation uploaded to GitHub.

## 📁 Project Structure