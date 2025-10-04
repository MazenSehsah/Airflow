from airflow import DAG
import random
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
def random_number():
    print(random.randint(0,1000))
with DAG (
    dag_id = "Airflow_Depi",
    start_date = datetime(2025, 10, 4),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task3 = PythonOperator(
         task_id = "Random_Number",
         python_callable = random_number
    )
         
    
    
