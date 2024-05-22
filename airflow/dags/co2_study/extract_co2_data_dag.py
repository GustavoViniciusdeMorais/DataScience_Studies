# extract_co2_data_dag
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
    'extract_co2_data_dag',
    default_args=default_args,
    description='Extract CO2 data',
    schedule=None
) as dag:

    extract_co2_data = BashOperator(
        task_id='extract_co2_data',
        bash_command='wget -c http://cdiac.ess-dive.lbl.gov/ftp/ndp030/CSV-FILES/global.1751_2014.csv \
        -O /var/www/html/co2.csv',
        dag=dag
    )

