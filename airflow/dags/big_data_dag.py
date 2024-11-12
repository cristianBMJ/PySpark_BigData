# /home/cris/workaplace/Big_data_pyspark/airflow/dags
# V7
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.fetch_data import fetch_data
from scripts.process_data import process_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 2 ),
    'retries': 1
}

dag = DAG('big_data_pipeline', default_args=default_args, schedule_interval='@daily')

t1 = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag
)

t2 = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag
)

t1 >> t2  # Task dependency (fetch data first, then process it)
