# Proyecto Final - Minería de Datos con API

Este proyecto fue realizado para el taller de **Econometría II**. Se busca construir un código que pueda sustraer datos desde una API. En este caso se construyo un código que sea reproducible para recolectar datos climáticos usando una API pública como lo es la API de clima histórico de Open-Meteo, procesarlos y generar un conjunto de datos listo para análisis econométrico.

La API de Open Meteo es pública y tiene su propios respositorio de github: 
🌤 Open-Meteo Weather API: 
Open-Meteo is an open-source weather API and offers free access for non-commercial use. No API key is required. You can use it immediately! https://github.com/open-meteo/open-meteo


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

## 🔐 Uso de variables de entorno con .env
Este proyecto incluye el uso de un archivo .env para demostrar las buenas prácticas de seguridad al manejar claves o variables confidenciales, como claves de API.

Aunque la API de Open-Meteo no requiere autenticación, se simula el uso de una variable de entorno para cumplir con la rúbrica y mostrar cómo se configuraría en un entorno real.

🛠️ ¿Cómo configurarlo?
Crea un archivo llamado .env en la raíz de tu proyecto.

Agrega una línea como esta:DUMMY_KEY=12345

Lo anterior demostraría cómo se accede a variables seguras dentro de un script en Python usando la librería python-dotenv.



## 🧠 Detalles técnicos: uso de time.sleep(1) y duración del scraping
Para evitar saturar el servidor de la API (Open-Meteo) y respetar sus límites de uso, el script incluye la instrucción: time.sleep(1)

Así hacemos que el programa espere 1 segundo entre cada petición a la API
Esto asegura que el script sea respetuoso con el servidor y menos propenso a errores de tipo 429 (Too Many Requests).

Como resultado, el scraping de 500 días aproximadamente 30 minutos pero se estan estudiando posibles mejoras en la eficiencia del tiempo.

Si se desea mayor velocidad, este valor puede ajustarse a time.sleep(0.5) (bajo riesgo) o eliminarse completamente (alto riesgo de bloqueo).

## 🌎 Ubicación del análisis

Este proyecto utiliza datos climáticos históricos de la **Ciudad de México (CDMX)**.  
Las coordenadas utilizadas en el script son:

- **Latitud:** `19.4326`
- **Longitud:** `-99.1332`

Estas coordenadas se encuentran definidas al inicio del archivo `scrape_clima.py` como:

LAT_CDMX = 19.4326
LON_CDMX = -99.1332 

🔁 Si quieres cambiar de Ciudad...
Solo reemplaza esos valores por las coordenadas deseadas. Aquí algunos ejemplos:

| Ciudad      | Latitud | Longitud  |
| ----------- | ------- | --------- |
| Monterrey   | 25.6866 | -100.3161 |
| Guadalajara | 20.6597 | -103.3496 |
| Madrid      | 40.4168 | -3.7038   |


## 📊 Descripción del dataset generado

El script `scrape_clima.py`, ubicado en la carpeta `code/`, recolecta datos históricos del clima utilizando la API de Open-Meteo. El resultado de esta recolección es un archivo llamado clima_cdmx_historico.csv. 

Este dataset contiene **500 observaciones diarias** correspondientes al clima en la Ciudad de México desde el 1 de enero de 2020 hasta el 14 de mayo de 2021. 

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