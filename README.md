# IDIA222_big_dataExam
# Análisis de sensores industriales

## Objetivo

Analizar 100,000 mediciones simuladas de sensores
industriales utilizando Python y pandas.

## Datos

El archivo contiene mediciones de sensores instalados
en cuatro plantas industriales.

Los datos son simulados y se utilizan únicamente con
fines académicos.

## Instalación

Crear el entorno virtual:

python -m venv venv

Activarlo en Windows:

venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

## Ejecución

python analisis.py

## Resultados

El programa calcula:

- Cantidad de registros.
- Sensores distintos.
- Temperatura promedio por planta.
- Temperatura máxima.
- Sensor y fecha de la temperatura máxima.
- Lecturas mayores a 85 °C.
- Planta con más alertas.

También genera:

resultados/alertas.csv