from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator 
def say_hello():
    print("Hello Airflow !")
def show_time():
    print("Current time is:", datetime.now())

with DAG (
    dag_id = "dag1",
    start_date = datetime(2025, 9, 29),
    schedule_interval = timedelta(minutes= 1),
    catchup = False
) as dag :
    task_say = PythonOperator(
        task_id = "say_hello",
        python_callable = say_hello
    )
    task2 = PythonOperator(
        task_id = "time_task",
        python_callable = show_time
    )
    
    