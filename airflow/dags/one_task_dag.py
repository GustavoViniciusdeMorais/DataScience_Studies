from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 1),
    'retries': 1
}

with DAG(
    'one_task_dag',
    default_args=default_args,
    description='First DAG',
    schedule_interval=None
) as dag:

    task1 = BashOperator(
        task_id='write_message_to_file',
        bash_command='echo "First DAG." >> /var/www/html/dags/message.txt',
        dag=dag
    )

