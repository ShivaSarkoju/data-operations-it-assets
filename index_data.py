import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import os
 
# === CONFIGURATION ===
ES_ENDPOINT = "https://my-elasticsearch-project-fea0c1.es.asia-south1.gcp.elastic.cloud:443"
ES_API_KEY = "WmM4SVNKb0JYbnRkV3BzRFpJV0k6UHd0dXdfbklNWll6R3RpMHJBRzdPZw=="  # or use a hardcoded string for testing
INDEX_NAME = "mini_project"
CSV_FILE = "C:/Kaiser/it_asset_inventory_cleaned1111.csv"
 
# === CONNECT TO ELASTICSEARCH ===
es = Elasticsearch(
    ES_ENDPOINT,
    api_key=ES_API_KEY,
    verify_certs=True
)
 
if not es.ping():
    print("❌ Connection failed!")
    exit()
else:
    print("✅ Connected to Elasticsearch!")
 
# === READ CSV FILE ===
df = pd.read_csv(CSV_FILE, low_memory=False)
 
# === PREPARE DOCUMENTS ===
def generate_docs(df):
    for _, row in df.iterrows():
        yield {
            "_index": INDEX_NAME,
            "_id": str(row['hostname']),
            "_source": row.to_dict()
        }
 
# === BULK INDEX DOCUMENTS ===
try:
    bulk(es, generate_docs(df))
    print(f"✅ Successfully indexed {len(df)} documents into '{INDEX_NAME}'")
except Exception as e:
    print(f"❌ Error during indexing: {e}")