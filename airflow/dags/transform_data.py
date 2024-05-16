from datetime import datetime, date
import pandas as pd
from airflow.operators.python import PythonOperator
from airflow import DAG

with DAG(
    'transform_data',
    default_args={
        'owner': 'airflow',
        'start_date': datetime(2024, 5, 1),
        'retries': 1
    },
    description='First DAG',
    schedule=None
) as dag:

    def transform_domains():
        df = pd.read_csv('/var/www/html/domains.csv')
        generic_type_df = df[df['Type'] == 'generic']
        generic_type_df['Date'] = date.today().strftime('%Y-%m-%d')
        generic_type_df.to_csv('/var/www/html/generic_domains.csv', index=False)

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_domains,
        dag=dag
    )
