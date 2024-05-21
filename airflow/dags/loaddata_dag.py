from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='loaddata_dag',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False
) as dag:
    load_task = BashOperator(
        task_id='loaddata',
        bash_command='python3 /var/www/html/airflow/dags/loaddata.py /var/www/html/generic_domains.csv /var/www/html/database.db',
        dag=dag
    )

    load_task
