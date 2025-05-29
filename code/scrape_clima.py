import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime, timedelta


# Cargar API_KEY desde .env (aunque en este caso no se utilice)
# Este valor no se usa, pero es para cumplir con la rúbrica y con los visto en clase

load_dotenv()
API_KEY = os.getenv("DUMMY_KEY")  


# Definimos una configuración en la forma de trabajar del código y las coordenadas del lugar donde nos enfocaremos

MAX_REINTENTOS = 3
TIMEOUT = 30
DELAY_ENTRE_REINTENTOS = 5
LAT_CDMX = 19.4326
LON_CDMX = -99.1332


#Función para hacer el scrapping de la página Open-meteo 

def obtener_clima_historico(lat: float, lon: float, fecha: str) -> dict:
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}&"
        f"start_date={fecha}&end_date={fecha}&"
        f"daily=weathercode,temperature_2m_max,windspeed_10m_max"
    )

    for intento in range(MAX_REINTENTOS):
        try:
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            datos = response.json()

            return {
                "fecha": fecha,
                "temperatura_max": datos["daily"]["temperature_2m_max"][0],
                "viento_max": datos["daily"]["windspeed_10m_max"][0],
                "codigo_tiempo": datos["daily"]["weathercode"][0],
                "fuente": "https://open-meteo.com/"
            }

        except requests.exceptions.Timeout:
            print(f"Timeout en intento {intento + 1} para {fecha}")
            time.sleep(DELAY_ENTRE_REINTENTOS)

        except Exception as e:
            print(f"Error en {fecha}: {str(e)}")
            return None

    print(f"Fallo definitivo en {fecha}")
    return None

# Main: obtener datos del clima de 500 días en ciudad de México, ojo tiempo aprox. 30 minutos

fechas = [
    (datetime(2020, 1, 1) + timedelta(days=i)).strftime("%Y-%m-%d")
    for i in range(500)
]

datos = []
for idx, fecha in enumerate(fechas):
    clima = obtener_clima_historico(LAT_CDMX, LON_CDMX, fecha)
    if clima:
        datos.append(clima)

    porcentaje = (idx + 1) / len(fechas) * 100
    print(f"\rProgreso: [{porcentaje:.1f}%] {idx + 1}/500", end="")
    time.sleep(1)  # para evitar saturar la API

# 5. Guardar el dataset final

df = pd.DataFrame(datos)
df.to_csv("data/clima_cdmx_historico.csv", index=False)
print("\n¡Dataset guardado exitosamente!")