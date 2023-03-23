from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 23),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_example',
    default_args=default_args,
    description='A simple Spark example DAG',
    schedule_interval=timedelta(days=1),
)

spark_job = SparkSubmitOperator(
    task_id='spark_job',
    application='/opt/airflow/dags/spark_jobs/my_spark_job.py',
    conn_id='spark_default',
    conf={
        'spark.executor.memory': '2g',
        'spark.executor.cores': '2',
        'spark.executor.instances': '2',
    },
    dag=dag,
)

spark_job