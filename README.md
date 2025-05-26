# Proyecto ETL - Contrataciones Públicas de Mendoza

Este proyecto implementa un pipeline ETL utilizando Apache Airflow para descargar, transformar y cargar datos abiertos de contrataciones públicas de la provincia de Mendoza (Argentina), conforme al estándar OCDS (Open Contracting Data Standard).

## 🛠️ Herramientas utilizadas

- **Apache Airflow**: Orquestación de tareas y ejecución programada del flujo ETL.
- **Python 3**: Desarrollo de scripts personalizados.
- **pandas**: Manipulación y transformación de datos.
- **SQLAlchemy + PyMySQL**: Conexión e inserción de datos en base de datos MySQL.
- **MySQL**: Base de datos relacional donde se almacenan los datos procesados.
- **OCDS**: Estándar para estructuración de datos de contrataciones públicas.

## 📁 Estructura del proyecto

airflow_etl_mendoza/
├── dags/
│ ├── etl_contrataciones_mendoza.py # DAG principal
│ └── scripts/
│ ├── guardar_csvs.py # Descarga y guarda los datos en CSV
│ ├── transformador.py # Limpieza y transformación
│ └── cargar_mysql.py # Inserta los datos en MySQL
├── data/ # Archivos CSV generados
├── requirements.txt
└── README.md


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

🧩 Estándar de Datos
Se utiliza el OCDS (Open Contracting Data Standard) como estructura base para los datos de procesos, adjudicaciones y contratos.
