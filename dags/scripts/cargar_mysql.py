from sqlalchemy import create_engine, text
import pandas as pd
import json
import ast

def cargar_en_mysql():
    DB_USER = "airflow"
    DB_PASSWORD = "airflow"
    DB_NAME = "etl_mendoza"
    DB_HOST = "host.docker.internal"

    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
        connect_args={"max_allowed_packet": 67108864}
    )

    # Leer los CSV
    procesos = pd.read_csv("data/procesos.csv")
    adjudicaciones = pd.read_csv("data/adjudicaciones.csv")
    contratos = pd.read_csv("data/contratos.csv")

    def limpiar_json(valor):
        if pd.isna(valor):
            return None
        try:
            return json.dumps(ast.literal_eval(valor))
        except Exception:
            return valor

    # Limpiar campos tipo JSON
    columnas_json_procesos = ["parties", "tender_items", "awards", "contracts"]
    for col in columnas_json_procesos:
        if col in procesos.columns:
            procesos[col] = procesos[col].apply(limpiar_json)

    columnas_json_adjudicaciones = ["items", "suppliers"]
    for col in columnas_json_adjudicaciones:
        if col in adjudicaciones.columns:
            adjudicaciones[col] = adjudicaciones[col].apply(limpiar_json)

    columnas_json_contratos = ["items"]
    for col in columnas_json_contratos:
        if col in contratos.columns:
            contratos[col] = contratos[col].apply(limpiar_json)

    # Eliminar duplicados por clave primaria ('id')
    if 'id' in procesos.columns:
        procesos = procesos.drop_duplicates(subset=['id'], keep='first')
    if 'id' in adjudicaciones.columns:
        adjudicaciones = adjudicaciones.drop_duplicates(subset=['id'], keep='first')
    if 'id' in contratos.columns:
        contratos = contratos.drop_duplicates(subset=['id'], keep='first')

    # Verificar duplicados antes de insertar (debug)
    for df, name in [(procesos, "procesos"), (adjudicaciones, "adjudicaciones"), (contratos, "contratos")]:
        if 'id' in df.columns:
            duplicados = df['id'][df['id'].duplicated()]
            if not duplicados.empty:
                print(f"⚠️ IDs duplicados detectados en '{name}':")
                print(duplicados)

    # Cargar en MySQL
    with engine.begin() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))

        # Truncate en vez de DELETE para limpieza más segura y rápida
        conn.execute(text("TRUNCATE TABLE adjudicaciones;"))
        conn.execute(text("TRUNCATE TABLE contratos;"))
        conn.execute(text("TRUNCATE TABLE procesos;"))

        # Insertar datos
        procesos.to_sql("procesos", conn, if_exists="append", index=False)
        adjudicaciones.to_sql("adjudicaciones", conn, if_exists="append", index=False)
        contratos.to_sql("contratos", conn, if_exists="append", index=False)

        conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

    print("✅ Datos cargados en MySQL correctamente.")









