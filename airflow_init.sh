#!/bin/bash

mkdir ./airflow/dags ./logs ./airflow/plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
