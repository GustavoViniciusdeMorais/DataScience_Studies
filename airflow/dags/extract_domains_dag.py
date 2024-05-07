from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 1),
    'retries': 1
}

with DAG(
    'extract_domains_dag',
    default_args=default_args,
    description='First DAG',
    schedule=None
) as dag:

    task1 = BashOperator(
        task_id='task_extract_domains_to_csv',
        bash_command='wget -c https://r2.datahub.io/clt98mhbp000nl708qb1tppbw/master/raw/top-level-domain-names.csv \
        -O ./domains.csv',
        dag=dag
    )

