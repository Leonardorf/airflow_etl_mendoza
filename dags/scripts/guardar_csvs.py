import pandas as pd
import os

def guardar_csvs():
    os.makedirs("data", exist_ok=True)

    procesos = pd.read_pickle("tmp/procesos.pkl")
    adjudicaciones = pd.read_pickle("tmp/adjudicaciones.pkl")
    contratos = pd.read_pickle("tmp/contratos.pkl")

    procesos.to_csv("data/procesos.csv", index=False)
    adjudicaciones.to_csv("data/adjudicaciones.csv", index=False)
    contratos.to_csv("data/contratos.csv", index=False)

    print("Archivos CSV guardados correctamente.")
