# Proyecto Final - Minería de Datos con API

Este proyecto fue realizado para el taller de **Econometría II**. Se busca construir un código que pueda sustraer datos desde una API. En este caso se construyo un código que sea reproducible para recolectar datos climáticos usando una API pública como lo es la API de clima histórico de Open-Meteo, procesarlos y generar un conjunto de datos listo para análisis econométrico.


## Estructura del repositorio

ProyectoFinal/
├── README.md
├── .gitignore
├── requirements.txt
├── code/
│ └── scrape_clima.py
└── data/
   └── clima_cdmx_historico.csv

## ⚙️ Cómo usar este proyecto 


### 1. Clona este repositorio:

git clone https://github.com/DaniEspinosaOl/ProyectoFinal.git
cd ProyectoFinal

### 2. Instala Dependencia

pip install -r requirements.txt

### 3. Ejecuta el scraper

python code/scrape_clima.py
'''

## 🧠 Detalles técnicos: uso de time.sleep(1) y duración del scraping
Para evitar saturar el servidor de la API (Open-Meteo) y respetar sus límites de uso, el script incluye la instrucción: time.sleep(1)

Esto hace que el programa espere 1 segundo entre cada petición a la API
Esto asegura que el script sea respetuoso con el servidor y menos propenso a errores de tipo 429 (Too Many Requests).

Como resultado, el scraping de 500 días toma más de 8 minutos.

Si se desea mayor velocidad, este valor puede ajustarse a time.sleep(0.5) (bajo riesgo) o eliminarse completamente (alto riesgo de bloqueo).

## 🌎 Ubicación del análisis

Este proyecto utiliza datos climáticos históricos de la **Ciudad de México (CDMX)**.  
Las coordenadas utilizadas en el script son:

- **Latitud:** `19.4326`
- **Longitud:** `-99.1332`

Estas coordenadas se encuentran definidas al inicio del archivo `scrape_clima.py` como:

LAT_CDMX = 19.4326
LON_CDMX = -99.1332 

🔁 ¿Quieres cambiar de ciudad?
Solo reemplaza esos valores por las coordenadas deseadas. Aquí algunos ejemplos:

| Ciudad      | Latitud | Longitud  |
| ----------- | ------- | --------- |
| Monterrey   | 25.6866 | -100.3161 |
| Guadalajara | 20.6597 | -103.3496 |
| Madrid      | 40.4168 | -3.7038   |


## 📊 Descripción del dataset generado

El script `scrape_clima.py`, ubicado en la carpeta `code/`, recolecta datos históricos del clima utilizando la API de Open-Meteo. El resultado de esta recolección es un archivo llamado clima_cdmx_historico.csv. 

Este dataset contiene **500 observaciones diarias** correspondientes al clima en la Ciudad de México desde el 1 de enero de 2020 en adelante.

### 🔠 Columnas del dataset:

| Columna           | Descripción                                               |
|-------------------|-----------------------------------------------------------|
| `fecha`           | Fecha del registro climático (formato `YYYY-MM-DD`)       |
| `temperatura_max` | Temperatura máxima del día en grados Celsius              |
| `viento_max`      | Velocidad máxima del viento (en m/s)                      |
| `codigo_tiempo`   | Código numérico del tipo de clima (según Open-Meteo)      |
| `fuente`          | Fuente geográfica de los datos, en este caso: `"CDMX"`    |

### 📁 Ubicación del archivo

El archivo CSV es guardado automáticamente en la carpeta `data/` después de ejecutar el script.  
Puedes abrirlo con Excel, Google Sheets o directamente en Python con `pandas`.

## 👩‍💻 Autor
Laura Daniela Espinosa Olvera
CU: 192346
Repositorio para entrega final taller de Econometría II