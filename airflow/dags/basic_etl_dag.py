from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import pandas as pd
from airflow.operators.python import PythonOperator
from datetime import datetime, date

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 1),
    'retries': 1
}

with DAG(
    'basic_etl_dag',
    default_args=default_args,
    description='First DAG',
    schedule=None
) as dag:

    task_extract_domains_to_csv = BashOperator(
        task_id='task_extract_domains_to_csv',
        bash_command='wget -c https://r2.datahub.io/clt98mhbp000nl708qb1tppbw/master/raw/top-level-domain-names.csv \
        -O /var/www/html/domains.csv',
        dag=dag
    )

    def transform_domains():
        df = pd.read_csv('/var/www/html/domains.csv')
        generic_type_df = df[df['Type'] == 'generic']
        generic_type_df['Date'] = date.today().strftime('%Y-%m-%d')
        generic_type_df['SponsoringOrganization'] = generic_type_df['Sponsoring Organisation']
        generic_type_df.drop('Sponsoring Organisation', axis=1, inplace=True)
        generic_type_df.to_csv('/var/www/html/generic_domains.csv', index=False)

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_domains,
        dag=dag
    )

    load_task = BashOperator(
        task_id='loaddata',
        bash_command='python3 /var/www/html/airflow/dags/loaddata.py /var/www/html/generic_domains.csv /var/www/html/database.db',
        dag=dag
    )

    task_extract_domains_to_csv >> transform_task >> load_task
