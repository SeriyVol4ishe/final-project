import logging
import math

import pandas as pd
from sodapy import Socrata


def get_dataset_length(
    client: Socrata,
    dataset_identifier: str,
    query_filter: str = None,
) -> int:
    return int(client.get(
        dataset_identifier,
        select='count(*) as count',
        where=query_filter,
    )[0]['count'])


def download_dataset(
    client: Socrata,
    dataset_name: str,
    dataset_identifier: str,
    query_filter: str = None,
    query_order: str = None,
    query_limit: int = 100000,
) -> pd.DataFrame:
    results_df = pd.DataFrame()
    total_rows = get_dataset_length(
        client=client,
        dataset_identifier=dataset_identifier,
        query_filter=query_filter,
    )
    logging.info(f'Total rows count for dataset {dataset_name}: {total_rows}')
    for x in range(math.ceil(total_rows / query_limit)):
        logging.info(f'Load data with offset={x * query_limit} and limit {query_limit}')
        batch = client.get(
            dataset_identifier,
            select='*',
            where=query_filter,
            order=query_order,
            offset=x * query_limit,
            limit=query_limit,
        )
        partial_df = pd.DataFrame.from_records(batch)
        results_df = pd.concat([results_df, partial_df], axis=0, ignore_index=True)
    return results_df


def download_dataset_by_chunks(
    client: Socrata,
    dataset_name: str,
    dataset_identifier: str,
    query_filter: str = None,
    query_order: str = None,
    query_offset: int = None,
    query_limit: int = None,
):
    query_offset = query_offset or 0
    query_limit = query_limit or 100000
    total_rows = get_dataset_length(
        client=client,
        dataset_identifier=dataset_identifier,
        query_filter=query_filter,
    )
    logging.info(f'Total rows count for dataset {dataset_name}: {total_rows}')
    for x in range(math.floor(query_offset / query_limit), math.ceil(total_rows / query_limit)):
        logging.info(f'Load data with offset={x * query_limit} and limit {query_limit}')
        batch = client.get(
            dataset_identifier,
            select='*',
            where=query_filter,
            order=query_order,
            offset=x * query_limit,
            limit=query_limit,
        )
        partial_df = pd.DataFrame.from_records(batch)
        yield x, partial_df
