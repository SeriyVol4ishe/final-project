import logging
from datetime import datetime

from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.operators.gcs import GCSListObjectsOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.task_group import TaskGroup

from utils.variables import VariablesGetter

variables = VariablesGetter(
    namespace='gcs_to_bigquery',
    keys=[
        'gcp_conn_id',
        'source_bucket',
    ]
)


@task
def print_files_task(list_files: list[str]):
    logging.info(list_files)


@dag(
    dag_id='gcs_to_bigquery_dag',
    start_date=datetime(2023, 4, 14),
    schedule_interval=None,
    catchup=False,
    default_args={
        'owner': 'serg.d',
    }
)
def gcs_to_bigquery_dag():
    source_bucket = variables['source_bucket']

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    create_dataset_task = BigQueryCreateEmptyDatasetOperator(
        task_id='create_dataset_task',
        dataset_id='crime_final_dataset',
        gcp_conn_id=variables['gcp_conn_id']
    )

    datasets_list = [
        'crime',
        'community_area',
        'beat',
        'district',
        'iucr',
        'ward',
    ]
    tasks = []
    filetype = 'parquet'
    for dataset_name in datasets_list:
        with TaskGroup(group_id=f'{dataset_name}_group') as tg:
            get_parquet_files_links_task = GCSListObjectsOperator(
                task_id=f'get_parquet_files_list_{dataset_name}',
                bucket=source_bucket,
                prefix=f'{filetype}/{dataset_name}/',
                delimiter=f'.{filetype}',
                gcp_conn_id=variables['gcp_conn_id']
            )
            gcs_to_bq_operator = GCSToBigQueryOperator(
                task_id=f'gcs_to_bq_task_{dataset_name}',
                gcp_conn_id=variables['gcp_conn_id'],
                bucket=source_bucket,
                source_objects=get_parquet_files_links_task.output,
                autodetect=True,
                write_disposition="WRITE_TRUNCATE",
                destination_project_dataset_table=f'crime_final_dataset.{dataset_name}',
                source_format=filetype.upper(),
            )
            get_parquet_files_links_task >> gcs_to_bq_operator
        tasks.append(tg)

    start >> create_dataset_task >> tasks >> end


gcs_to_bigquery_dag()
