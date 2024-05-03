from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the function that will write the message to a text file
def write_message_to_file():
    message = "Hello, this is a message written to a text file."
    with open("/path/to/your/file/message.txt", "w") as file:
        file.write(message)

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 1),
    'retries': 1
}

# Define the DAG object
dag = DAG(
    'write_message_to_file',
    default_args=default_args,
    description='A simple DAG that writes a message to a text file',
    schedule_interval=None,  # You can define the schedule interval here
    catchup=False  # Set to False if you don't want historical runs to be processed
)

# Define the task that calls the function to write the message to a file
write_message_task = PythonOperator(
    task_id='write_message_task',
    python_callable=write_message_to_file,
    dag=dag
)

# Set task dependencies
write_message_task
