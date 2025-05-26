# Proyecto ETL - Contrataciones Públicas de Mendoza

Este proyecto implementa un pipeline ETL utilizando Apache Airflow para descargar, transformar y cargar datos abiertos de contrataciones públicas de la provincia de Mendoza (Argentina), conforme al estándar OCDS (Open Contracting Data Standard).
📊 Dataset
Los datos provienen de fuentes públicas del Gobierno de Mendoza y están estructurados bajo el estándar OCDS.

✅ Resultado
Este pipeline permite mantener una base de datos actualizada y limpia con información clave sobre procesos de licitación, adjudicaciones y contratos.

## 🛠️ Herramientas utilizadas

- **Apache Airflow**: Orquestación de tareas y ejecución programada del flujo ETL.
- **Python 3**: Desarrollo de scripts personalizados.
- **pandas**: Manipulación y transformación de datos.
- **SQLAlchemy + PyMySQL**: Conexión e inserción de datos en base de datos MySQL.
- **MySQL**: Base de datos relacional donde se almacenan los datos procesados.
- **OCDS**: Estándar para estructuración de datos de contrataciones públicas.

## 📁 Estructura del proyecto

```text
airflow_etl_mendoza/
+-- dags/
¦   +-- etl_mendoza.py              # DAG principal
¦   +-- scripts/
¦       +-- cargar_mysql.py
¦       +-- guardar_csvs.py
¦       +-- transformador.py
+-- data/
¦   +-- procesos.csv
¦   +-- adjudicaciones.csv
¦   +-- contratos.csv
+-- tmp/                            # Archivos temporales .pkl
+-- requirements.txt
+-- docker-compose.yml              
+-- .gitignore
+-- README.md
```




## 📊 Tablas principales en la base de datos

- `procesos`: Contiene metadatos generales del proceso de contratación.
- `adjudicaciones`: Información sobre adjudicaciones realizadas.
- `contratos`: Detalles de contratos firmados.

## 🚀 Cómo ejecutar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
2. Configurar la conexión a MySQL en cargar_mysql.py

3. Ejecutar Airflow:

airflow db init
airflow webserver
airflow scheduler

4. Habilitar y lanzar el DAG etl_contrataciones_mendoza desde la interfaz web.

   🚀 Ejecución
Este proyecto se ejecuta desde el DAG etl_contrataciones_mendoza en el entorno de Airflow. Las tareas incluyen:

Descarga de datos (guardar_csvs)

Transformación (transformador)

Carga en MySQL (cargar_mysql)
![Imagen de ejemplo](airflow_dags.png)



## 📌 Licencia
MIT
