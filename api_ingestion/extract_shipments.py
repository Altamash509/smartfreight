# extract_shipments.py

import json
import time
from pathlib import Path

INPUT_FILE = Path("../data/local_raw/shipments.json")
OUTPUT_FILE = Path("../data/local_raw/shipments_bronze.json")


def fetch_data_with_retry(file_path, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            print(f"📦 Attempt {attempt}: Reading shipment data...")
            with open(file_path, "r") as f:
                data = json.load(f)
            print("✅ Data loaded successfully.")
            return data
        except Exception as e:
            print(f"⚠️ Error reading file: {e}")
            if attempt < retries:
                print(f"🔁 Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise


def save_extracted_data(data, output_path):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Extracted data saved to: {output_path.resolve()}")


def main():
    print("🚚 Starting shipment data extraction...")
    data = fetch_data_with_retry(INPUT_FILE)
    save_extracted_data(data, OUTPUT_FILE)


if __name__ == "__main__":
    main()
