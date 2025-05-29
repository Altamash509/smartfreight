from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json
import os

def simulate_api_data():
    # Simulated API response
    data = {
        "shipment_id": "SHP123",
        "carrier": "DHL",
        "region": "US-East",
        "expected_delivery": "2024-06-01",
        "actual_delivery": "2024-06-02"
    }

    # Save to a local file (later this will go to S3)
    os.makedirs("/opt/airflow/data", exist_ok=True)
    with open("/opt/airflow/data/shipment_data.json", "w") as f:
        json.dump(data, f)

    print(" Simulated API data saved to /opt/airflow/data/shipment_data.json")

with DAG(
    dag_id="simulate_api_to_local_file",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example", "api", "file"]
) as dag:
    
    extract_task = PythonOperator(
        task_id="extract_from_api",
        python_callable=simulate_api_data
    )

    extract_task
