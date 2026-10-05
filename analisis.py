from pathlib import Path
import pandas as pd

# Ajusta estos nombres a los del CSV
COL_ID = "id_registro"
COL_FECHA = "fecha_hora"
COL_SENSOR = "id_sensor"
COL_PLANTA = "planta"
COL_TEMP = "temperatura_c"
UMBRAL = 85

base = Path(__file__).parent
df = pd.read_csv(base / "data" / "sensores_industriales.csv")

# 1. Registros y sensores distintos
print("Registros:", len(df))
print("Sensores distintos:", df[COL_SENSOR].nunique())

# 2. Temperatura promedio por planta
print("\nTemperatura promedio por planta:")
print(df.groupby(COL_PLANTA)[COL_TEMP].mean())

# 3. Temperatura máxima (muestra empates)
tmax = df[COL_TEMP].max()
print(f"\nTemperatura máxima: {tmax}")
print(df[df[COL_TEMP] == tmax][[COL_SENSOR, COL_FECHA, COL_TEMP]])

# 4. Lecturas con alerta
alertas = df[df[COL_TEMP] > UMBRAL]
print(f"\nLecturas con alerta (> {UMBRAL} °C): {len(alertas)}")

# 5. Planta con más alertas (muestra empates)
conteo = alertas[COL_PLANTA].value_counts()
print("\nPlanta(s) con más alertas:")
print(conteo[conteo == conteo.max()])

# 6. Exportar alertas con las columnas originales
salida = base / "resultados"
salida.mkdir(exist_ok=True)
alertas.to_csv(salida / "alertas.csv", index=False)
print("\nExportado a resultados/alertas.csv")