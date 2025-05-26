import os
import requests
import json
import pandas as pd

URL_JSON = "https://datosabiertos-compras.mendoza.gov.ar/descargar-json/2020_20231021_v1_release.json"
TMP_DIR = "tmp"

def descargar_datos():
    os.makedirs(TMP_DIR, exist_ok=True)
    response = requests.get(URL_JSON)
    if response.status_code != 200:
        raise Exception("Error al descargar el archivo JSON")
    
    with open(os.path.join(TMP_DIR, "datos_raw.json"), "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print("✅ JSON descargado correctamente")

def procesar_datos():
    ruta = os.path.join(TMP_DIR, "datos_raw.json")
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "releases" not in data:
        raise ValueError("❌ El JSON no contiene la clave 'releases'.")

    releases = data["releases"]

    # Tender = procesos de compra
    procesos = pd.json_normalize(
        [r for r in releases if "tender" in r],
        sep="_",
        record_prefix="tender_",
        meta=["ocid", "id", "date"]
    )

    # Awards = adjudicaciones
    adjudicaciones = pd.json_normalize(
        [a for r in releases if "awards" in r for a in r["awards"]],
        sep="_",
        record_prefix="award_"
    )

    # Contracts = contratos
    contratos = pd.json_normalize(
        [c for r in releases if "contracts" in r for c in r["contracts"]],
        sep="_",
        record_prefix="contract_"
    )

    procesos.to_pickle(os.path.join(TMP_DIR, "procesos.pkl"))
    adjudicaciones.to_pickle(os.path.join(TMP_DIR, "adjudicaciones.pkl"))
    contratos.to_pickle(os.path.join(TMP_DIR, "contratos.pkl"))

    print("✅ Datos extraídos de OCDS y guardados como .pkl")

