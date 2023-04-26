import json
from tempfile import NamedTemporaryFile

import pandas as pd
from google.cloud.storage import Bucket


def get_data_transformation_config(dataset_name: str):
    with open(f'dags/configs/transformation/{dataset_name}.json', 'r') as file:
        return json.loads(file.read())


def load(bucket: Bucket, filename: str, df: pd.DataFrame):
    with NamedTemporaryFile() as file:
        temp_file_name = f"{file.name}.parquet"

        df.to_parquet(
            path=temp_file_name,
            engine='fastparquet',
            index=False
        )

        bucket.blob(blob_name=filename).upload_from_filename(
            temp_file_name
        )
