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
dags /                      contains DAGs
dags / configs /            contains JSON files with some configuration stuff used in DAGs
docker /                    contains Dockerfile and requirements.txt
variables_and_connections / contains JSON files with variables and connections to import on airflow-init step
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
   ![img.png](../docs/poc/airflow/airflow_gcs_to_bigquery_dag_success.png)

## Troubleshooting
    !TODO: add this section
