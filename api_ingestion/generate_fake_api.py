# generate_fake_api.py

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

OUTPUT_DIR = Path("../data/local_raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "shipments.json"

CARRIERS = ["FedEx", "UPS", "DHL", "USPS"]
REGIONS = ["West", "East", "North", "South"]
PRODUCTS = ["Electronics", "Food", "Furniture", "Clothing"]


def generate_shipment(i):
    ship_date = datetime.now() - timedelta(days=random.randint(1, 10))
    delivery_date = ship_date + timedelta(days=random.randint(1, 5))
    delay_days = max(0, (delivery_date - ship_date).days - 3)

    return {
        "shipment_id": f"SHP{i:05}",
        "carrier": random.choice(CARRIERS),
        "region": random.choice(REGIONS),
        "product_type": random.choice(PRODUCTS),
        "ship_date": ship_date.isoformat(),
        "expected_delivery_date": (ship_date + timedelta(days=3)).isoformat(),
        "actual_delivery_date": delivery_date.isoformat(),
        "delay_days": delay_days,
        "cost_usd": round(random.uniform(50, 500), 2),
        "spoilage": random.choice([True, False]) if delay_days > 1 else False
    }


def main():
    print("🔧 Generating fake shipment data...")
    fake_data = [generate_shipment(i) for i in range(1, 51)]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(fake_data, f, indent=4)

    print(f"✅ File written to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
