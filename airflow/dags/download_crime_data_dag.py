import logging
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from airflow.decorators import task, dag
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from sodapy import Socrata

from utils.tasks import download_dataset, get_dataset_length
from utils.variables import VariablesGetter

variables = VariablesGetter(
    namespace='download_crime_dataset',
    keys=[
        'app_token',
        'gcp_conn_id',
        'dataset_domain',
        'dataset_identifier',
        'destination_bucket',
    ]
)


@task
def get_years():
    client = Socrata(
        domain=variables['dataset_domain'],
        app_token=variables['app_token'],
    )
    years = pd.DataFrame.from_records(client.get(
        dataset_identifier=variables['dataset_identifier'],
        select='distinct year as year'
    )).year.to_list()

    return years


@task(retries=2, retry_delay=timedelta(seconds=15))
def download_crime_data_by_year(year):
    local_filepath = Path(f'/tmp/csv/crime/crime_{year}.csv')
    if local_filepath.exists():
        return str(local_filepath)
    client = Socrata(
        domain=variables['dataset_domain'],
        app_token=variables['app_token'],
    )
    rows_count = get_dataset_length(
        client=client,
        dataset_identifier=variables['dataset_identifier'],
        query_filter=f"year = '{year}'",
    )
    logging.info(f'Total rows count for year {year}: {rows_count}')
    results_df = download_dataset(
        client=client,
        dataset_name='crime',
        dataset_identifier=variables['dataset_identifier'],
        query_filter=f"year = '{year}'",
    )
    results_df.to_csv(local_filepath, index=False)
    return str(local_filepath)


@task
def upload_data_to_gcs(filepath: str):
    bucket_name = variables['destination_bucket']
    df = pd.read_csv(filepath)
    year = df.year[0]
    gcs_hook = GCSHook(gcp_conn_id=variables['gcp_conn_id'])
    gcs_hook.upload(
        bucket_name=bucket_name,
        object_name=f'crime/crime_raw_data_{year}.csv',
        data=df.to_csv(index=False),
        gzip=True,
    )


@dag(
    dag_id='download_crime_data_dag',
    start_date=datetime(2023, 4, 10),
    schedule_interval="0 9 * * *",
    catchup=False,
    default_args={
        'owner': 'serg.d',
    }
)
def crime_dataset_to_gcs_dag():
    upload_data_to_gcs.expand(filepath=download_crime_data_by_year.expand(year=get_years()))


crime_dataset_to_gcs_dag()
