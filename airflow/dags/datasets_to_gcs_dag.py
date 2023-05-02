import logging
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from airflow.decorators import task, dag
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.utils.task_group import TaskGroup
from sodapy import Socrata

from utils.etl import get_data_transformation_config
from utils.tasks import download_dataset_by_chunks, get_dataset_length
from utils.variables import VariablesGetter

variables = VariablesGetter(
    namespace='datasets_to_gcs',
    keys=[
        'gcp_conn_id',
        'datasets',
        'dataset_domain',
        'destination_bucket',
        'app_token',
    ]
)

download_config = VariablesGetter(
    namespace='datasets_download_config',
    keys=['datasets']
)


@task(retries=0, retry_delay=timedelta(seconds=15))
def download_dataset(dataset_name: str):
    dataset_config = variables['datasets'][dataset_name]
    dataset_identifier = dataset_config['dataset_identifier']
    client = Socrata(
        domain=variables['dataset_domain'],
        app_token=variables['app_token'],
    )
    # client.timeout = 60
    for chunk_number, partial_df in download_dataset_by_chunks(
        client=client,
        dataset_name=dataset_name,
        dataset_identifier=dataset_identifier,
        query_order=dataset_config.get('query_order'),
        query_offset=dataset_config.get('query_offset'),
        query_limit=dataset_config.get('query_limit'),
    ):
        filepath = Path(f'/tmp/csv/{dataset_name}/{chunk_number}.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        if filepath.exists():
            continue
        partial_df.to_csv(filepath, index=False)


@task
def transform_data(dataset_name: str):
    config = get_data_transformation_config(dataset_name=dataset_name)
    output_csv_dir = Path(f'/tmp/csv/{dataset_name}/')
    output_parquet_dir = Path(f'/tmp/parquet/{dataset_name}/')
    logging.info(f'Files found: {list(output_csv_dir.rglob("*.csv"))}')
    for filepath in output_csv_dir.rglob('*.csv'):
        logging.info(f'Current file: {str(filepath)}')
        df = pd.read_csv(filepath)
        df = df.reindex(sorted(df.columns), axis=1)
        if columns_to_drop := config.get('drop_columns'):
            df = df.drop(columns=columns_to_drop, errors='ignore')
        if columns_to_rename := config.get('rename_columns'):
            df = df.rename(columns=columns_to_rename, errors='ignore')
        if config.get('drop_duplicates'):
            df = df.drop_duplicates()
        if dtypes_specified := config.get('dtypes'):
            for column, dtype in dtypes_specified.items():
                df[column] = df[column].fillna(value=-1)
                df[column] = df[column].astype(dtype=dtype, errors='ignore')
        output_parquet = output_parquet_dir / filepath.name.replace('csv', 'parquet')
        output_parquet.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(output_parquet, index=False)


@task
def upload_data_to_gcs(dataset_name):
    bucket_name = variables['destination_bucket']
    filetype = 'parquet'
    filepaths = list(Path(f'/tmp/{filetype}/{dataset_name}/').rglob(f'*.{filetype}'))
    for number, filepath in zip(range(len(filepaths)), filepaths):
        gcs_hook = GCSHook(gcp_conn_id=variables['gcp_conn_id'])
        gcs_hook.upload(
            bucket_name=bucket_name,
            object_name=f'{filetype}/{dataset_name}/{number}.{filetype}',
            filename=str(filepath),
        )


@dag(
    dag_id='datasets_to_gcs_dag',
    start_date=datetime(2023, 4, 13),
    schedule_interval=None,
    catchup=False,
    default_args={
        'owner': 'serg.d',
    }
)
def additional_datasets_to_gcs_dag():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    datasets_list = [
        'crime',
        'community_area',
        'beat',
        'district',
        'iucr',
        'ward',
    ]
    tasks = []
    for dataset in datasets_list:
        with TaskGroup(group_id=f'{dataset}_group') as tg:
            download_dataset_task = download_dataset(
                dataset_name=dataset,
            )
            transform_data_task = transform_data(
                dataset_name=dataset,
            )
            upload_data_to_gcs_task = upload_data_to_gcs(
                dataset_name=dataset,
            )
            download_dataset_task >> transform_data_task >> upload_data_to_gcs_task
        tasks.append(tg)

    start >> tasks >> end


additional_datasets_to_gcs_dag()
