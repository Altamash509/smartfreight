import requests
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

API_URL = "https://smartfreight-api.onrender.com/shipments"
LOCAL_FALLBACK_FILE = Path("data/local_raw/shipments_bronze.json")
OUTPUT_FILE = Path("data/local_raw/shipments_extracted.json")

def fetch_from_api():
    logging.info("🚚 Starting shipment data extraction from API...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        logging.info(f"✅ Fetched {len(data)} records from API.")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error fetching data: {e}")
        return None

def load_local_file():
    logging.info(f"📂 Loading local fallback data from {LOCAL_FALLBACK_FILE}")
    if LOCAL_FALLBACK_FILE.exists():
        with open(LOCAL_FALLBACK_FILE, 'r') as f:
            data = json.load(f)
        logging.info(f"✅ Loaded {len(data)} records from local file.")
        return data
    else:
        logging.warning("⚠️ Local fallback file not found.")
        return None

def save_data(data):
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    logging.info(f"💾 Saved extracted data to {OUTPUT_FILE}")

def main():
    data = fetch_from_api()
    if data is None:
        data = load_local_file()
    if data:
        save_data(data)
    else:
        logging.warning("⚠️ No data to save.")

if __name__ == "__main__":
    main()

# existing imports
import logging
import boto3
from pathlib import Path

# your existing extraction code here...

# after you save the extracted JSON file locally, add this:

def upload_to_s3():
    s3 = boto3.client('s3')
    bucket_name = "smartfreight-bronze-bucket-2025"  # replace with your bucket
    s3_key = "shipments/shipments_extracted.json"
    local_file_path = Path("data/local_raw/shipments_extracted.json")

    try:
        logging.info(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_key}")
        s3.upload_file(str(local_file_path), bucket_name, s3_key)
        logging.info("Upload successful.")
    except Exception as e:
        logging.error(f"Failed to upload file to S3: {e}")

# call this upload function at the end of your script
upload_to_s3()
