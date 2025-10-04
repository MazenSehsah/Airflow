from airflow import DAG
import random
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
def say_welcome():
    print("Hello airflow, Iam Mazen Hesham")
def random_number():
    print(random.randint(0,1000))
with DAG (
    dag_id = "Airflow_Depi",
    start_date = datetime(2025, 10, 4),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task1 = BashOperator(
        task_id = "print_time",
        bash_command = "date"
    ) 
    task2 = PythonOperator(
        task_id = "Say_Welcome",
        python_callable = say_welcome
    )
    task3 = PythonOperator(
         task_id = "Random_Number",
         python_callable = random_number
    )
         
    
    
