from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("🚀 Hello from Airflow!")

with DAG(
    dag_id="example_hello_world",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    hello = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )
