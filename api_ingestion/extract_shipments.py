import json
import random
import time
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path("data/local_raw/shipments_bronze.json")

def generate_shipment():
    carriers = ["FedEx", "UPS", "DHL", "USPS"]
    statuses = ["In Transit", "Delivered", "Delayed", "Lost"]
    regions = ["North", "South", "East", "West"]

    shipment = {
        "shipment_id": f"SHP{random.randint(1000, 9999)}",
        "carrier": random.choice(carriers),
        "status": random.choice(statuses),
        "origin_region": random.choice(regions),
        "destination_region": random.choice(regions),
        "weight_kg": round(random.uniform(0.5, 50.0), 2),
        "cost_usd": round(random.uniform(10.0, 500.0), 2),
        "shipment_date": datetime.now().isoformat()
    }
    return shipment

def fetch_shipments(num_shipments=10):
    shipments = []
    for _ in range(num_shipments):
        shipment = generate_shipment()
        shipments.append(shipment)
    return shipments

def save_shipments(shipments, filepath=OUTPUT_FILE):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(shipments, f, indent=4)
    print(f"Saved {len(shipments)} shipments to {filepath}")

if __name__ == "__main__":
    shipments = fetch_shipments()
    save_shipments(shipments)

