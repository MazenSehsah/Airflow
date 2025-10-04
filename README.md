# Airflow Task With DEPI
This repository contains three distinct workflows built with Apache Airflow.
# Dag1
This time-based DAG executes a Bash task every 60 seconds that outputs the current time to the logs.
Code : 

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/dag1/Code_1.png" height =1080 width = 720 >

Final Output :

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/dag1/Dag1.png" height =1080 width = 720 >

# Dag2
This DAG uses a PythonOperator to execute a function that displays a message every 1 minute.
Code : 

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/dag2/code_2.png" height =1080 width = 720 >

Final Output : 

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/dag2/dag2.png" height =1080 width = 720 >

# Dag3
This time-scheduled DAG leverages a PythonOperator to generate and log a random number every minute, providing continuous randomized output for testing or demonstration purposes.
Code :

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/Dag3/code_3.png" height =1080 width = 720 >

Final Output :

<img src= "https://github.com/MazenSehsah/Airflow/blob/master/result/Dag3/dag3.png" height =1080 width = 720 >
