from datetime import datetime

from airflow.models import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

DAG_ID = "example_spark_operator"

with DAG(
    dag_id=DAG_ID,
    schedule=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    submit_job = SparkSubmitOperator(
        conn_id='spark_default',
        application="dags/spark_job.py",
        num_executors=2,
        task_id="submit_job",
    )
