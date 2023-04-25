from datetime import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


@dag(
    dag_id='crime_pipeline_dag',
    start_date=datetime(2023, 4, 25),
    schedule_interval="@weekly",
    catchup=False,
    default_args={
        'owner': 'serg.d',
    }
)
def crime_pipeline_dag():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    trigger_upload_datasets_to_gcs = TriggerDagRunOperator(
        task_id="trigger_upload_datasets_to_gcs",
        trigger_dag_id="datasets_to_gcs_dag",
        wait_for_completion=True,
    )
    trigger_upload_data_from_gcs_to_bigquery = TriggerDagRunOperator(
        task_id="trigger_upload_data_from_gcs_to_bigquery",
        trigger_dag_id="gcs_to_bigquery_dag",
        wait_for_completion=True,
    )

    start >> trigger_upload_datasets_to_gcs >> trigger_upload_data_from_gcs_to_bigquery >> end


crime_pipeline_dag()
