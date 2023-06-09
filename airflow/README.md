# Airflow

## Contents

- [Description](#description)
- [Airflow project structure](#airflow-project-structure)
- [DAGs structure](#dags-structure)
- [Local setup and run](#local-setup-and-run)
- [Troubleshooting](#troubleshooting)

## Description

## Airflow project structure

```
dags /                                  contains DAGs
dags / configs / transformation /       contains JSON files with data transform configuration 
                                          (renaming columns, dtypes for dataframes, etc.) used in DAGs
docker /                                contains Dockerfile and requirements.txt
variables_and_connections /             contains JSON files with variables and connections to import on airflow-init step
```

## DAGs structure

Three DAGs are presented in this project:

- `crime_pipeline_dag`:

  ![img.png](../docs/poc/airflow/airflow_crime_pipeline_dag_grid.png)
  ![img.png](../docs/poc/airflow/airflow_crime_pipeline_dag_graph.png)

- `datasets_to_gcs_dag`:

  ![img.png](../docs/poc/airflow/airflow_datasets_to_gcs_dag_grid.png)
  ![img.png](../docs/poc/airflow/airflow_datasets_to_gcs_dag_graph.png)

- `gcs_to_bigquery_dag`:

  ![img.png](../docs/poc/airflow/airflow_gcs_to_bigquery_dag_grid.png)
  ![img.png](../docs/poc/airflow/airflow_gcs_to_bigquery_dag_graph.png)

## Local setup and run

### Prerequisites

> **Warning**
>
> All requests should include an app token that identifies your application, and each application
> should have its own unique app token. A limited number of requests can be made without an app token, but they are
> subject to much lower throttling limits than request that do include one. With an app token, your application is
> guaranteed access to it's own pool of requests. If you don't have an app token yet, click the button to the right to
> sign up for one.
>
> Create App Token following the [instructions](/docs/PREREQUISITES.md#app-token-creation).

> **Warning**
>
> Before triggering DAGs your should create GCP infrastructure using [`terraform`](/terraform/README.md) and due to
> randomly generated bucket name set its value in variables manually following
> this [instructions](/docs/PREREQUISITES.md#set-gcs-bucket-variable).


> **Warning**
>
> You have to put `credentials.json` into `credentials` folder in project directory.
>
> Create Project and Service Account following the [instructions](/docs/PREREQUISITES.md#google-cloud-project).

> **Note**
>
> Due to `Tables should be partitioned and clustered in a way that makes sense for the upstream queries`
> You can see cluster and partition field in `gcs_to_bigquery.py`:
> ```python
> cluster_fields=[
>     'year',
>     'community_area',
>     'location',
>     'iucr',
> ] if dataset_name == 'crime' else None,
> time_partitioning={
>     'field': 'date',
>     'type': 'YEAR',
> } if dataset_name == 'crime' else None
> ```
> Clustering and partitioning makes sense only for `crime` table as it has millions of rows. The order of
> the `clustering_fields` is due to the specifics of the `aggregated` models (ordering and filtering data in reports
> based on dbt models).

1. Run in terminal in project root directory:

`./create_airflow_env_file.sh && docker-compose -f airflow/docker-compose.yaml up --build`

2. Open browser and go to `localhost:8080` and use `airflow` as username and password:

   ![img.png](../docs/poc/airflow/airflow_login.png)

3. Now you see dags:

   ![img.png](../docs/poc/airflow/airflow_home.png)

4. Unpause dags:

   ![img.png](../docs/poc/airflow/airflow_unpause_dags.png)

5. Due to schedule setting `@weekly` for `crime_pipeline_dag` you can trigger it manually:

   ![img.png](../docs/poc/airflow/airflow_trigger_root_dag.png)

6. Watch DAGs running:

   ![img.png](../docs/poc/airflow/airflow_crime_pipeline_dag_process.png)
   ![img.png](../docs/poc/airflow/airflow_datasets_to_gcs_dag_process.png)

7. After completion see the results and logs:

   ![img.png](../docs/poc/airflow/airflow_crime_pipeline_dag_success_home.png)
   ![img.png](../docs/poc/airflow/airflow_datasets_to_gcs_dag_success.png)
   ![img.png](../docs/poc/gcp/storage_crime_parquet_files.png)
   ![img.png](../docs/poc/airflow/airflow_gcs_to_bigquery_dag_success.png)
   ![img.png](../docs/poc/gcp/datasets_in_bigquery.png)

## Troubleshooting

### Error on downloading dataset from source:

Sometimes the error occurs when `download_dataset` task is running:
![img.png](../docs/poc/airflow/airflow_dataset_to_gcs_error.png)

This can happen for several reasons:

1. Wrong application token
2. Request limit too high

In such cases, you can reduce the limit, set the correct application token by replacing the appropriate values in
the "datasets_to_gcs" variable. If the task didn't crash immediately with an error, but after downloading a certain
amount of data, you can use the logs to see what the last offset value was, set this value in the "datasets_to_gcs"
variable for the desired dataset, and restart the task, clearing its state.

If you want to change the limit and offset values at the same time, you have to calculate appropriate values by
yourself. ¯\_(ツ)_/¯

By default, the offset value is 0, and the limit is 100000. Usually, you just need to change the offset value and
restart the task.

![img.png](../docs/poc/airflow/airflow_dataset_to_gcs_change_offset.png)
