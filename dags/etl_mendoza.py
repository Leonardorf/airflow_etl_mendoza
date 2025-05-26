from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

from scripts.transformador import descargar_datos, procesar_datos
from scripts.guardar_csvs import guardar_csvs
from scripts.cargar_mysql import cargar_en_mysql

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    'etl_contrataciones_mendoza',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='ETL de contrataciones públicas de Mendoza',
) as dag:

    t1 = PythonOperator(
        task_id='descargar_datos',
        python_callable=descargar_datos,
    )

    t2 = PythonOperator(
        task_id='procesar_datos',
        python_callable=procesar_datos,
    )

    t3 = PythonOperator(
        task_id='guardar_csvs',
        python_callable=guardar_csvs,
    )

    t4 = PythonOperator(
        task_id='cargar_en_mysql',
        python_callable=cargar_en_mysql,
    )

    t1 >> t2 >> t3 >> t4
