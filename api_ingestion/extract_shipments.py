# api_ingestion/extract_shipments.py

import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

# Load the input file path from .env
INPUT_FILE = os.getenv("LOCAL_SHIPMENT_FILE")

def fetch_data_with_retry(file_path, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            print(f"📦 Attempt {attempt}: Reading shipment data...")
            with open(file_path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading file: {e}")
            if attempt < retries:
                print(f"🔁 Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise

def save_raw_json(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved raw data to {output_path}")

def main():
    print("🚚 Starting shipment data extraction...")

    data = fetch_data_with_retry(INPUT_FILE)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_path = f"data/local_raw/shipments_bronze.json"
    save_raw_json(data, output_path)

if __name__ == "__main__":
    main()
