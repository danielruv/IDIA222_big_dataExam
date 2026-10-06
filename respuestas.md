# Examen práctico — Manejo Masivo de Datos

## Nombre: Daniel Ruvalcaba Juarez

## Grupo: IDIA 222

## Fecha: 05/10/2026

# 5. Las 5 V aplicadas al proyecto

| V | Relación con el sistema de sensores | Ejemplo concreto | ¿Aparece en el CSV actual o es futura ampliación? |
|---|---|---|---|
| **Volumen** | El sistema almacena una gran cantidad de mediciones generadas por los sensores. Actualmente se tienen 100,000 registros. | 100,000 mediciones de temperatura y vibración. | **Actual:** aparece en el CSV. |
| **Velocidad** | Los sensores generan mediciones continuamente y en el futuro podrían enviarlas cada segundo, aumentando la rapidez con la que llegan los datos. | Recibir una lectura de temperatura cada segundo y detectar rápidamente una temperatura mayor a 85 °C. | **Futura ampliación:** el CSV actual contiene mediciones almacenadas. |
| **Variedad** | El sistema puede manejar diferentes tipos de información además de los datos tabulares de los sensores. | CSV con mediciones, fotografías de máquinas y reportes de mantenimiento. | **CSV actual:** datos estructurados. **Futura ampliación:** fotografías y reportes. |
| **Veracidad** | Es necesario comprobar que las mediciones sean confiables para tomar decisiones correctas. | Revisar si una temperatura extremadamente alta es una medición válida o un error del sensor. | **Futura aplicación:** el CSV contiene mediciones, pero no proporciona información adicional para comprobar su veracidad. |
| **Valor** | Los datos pueden utilizarse para detectar situaciones anormales y apoyar decisiones de mantenimiento. | Detectar las lecturas superiores a 85 °C para identificar alertas de temperatura. | **Actual:** el análisis del CSV utiliza este criterio. |

> **Nota:** Las fotografías y los reportes de mantenimiento corresponden a la ampliación futura descrita en el examen y no deben considerarse parte del CSV actual.


# 6. Tipos de datos y procesamiento tradicional

## Clasificación de los datos

| Elemento | Tipo de dato | Justificación |
|---|---|---|
| CSV de sensores | **Estructurado** | Tiene columnas y filas definidas, como identificador, fecha, sensor, planta, temperatura y vibración. |
| Mensaje JSON enviado por un sensor | **Semiestructurado** | Tiene una estructura basada en claves y valores, pero permite diferentes campos y estructuras. |
| Fotografía de una máquina | **No estructurado** | Es información visual que no está organizada naturalmente en filas y columnas. |
| Texto libre de un reporte de mantenimiento | **No estructurado** | Contiene texto libre que no sigue una estructura tabular fija. |

## ¿Por qué 100,000 registros no convierten automáticamente al archivo en Big Data?

Tener 100,000 registros por sí solo no significa que los datos sean Big Data. Big Data depende de factores como el volumen, la velocidad, la variedad y las necesidades de procesamiento.

En este proyecto, el archivo tiene 100,000 registros y puede ser procesado de manera relativamente sencilla con Python y pandas en una computadora convencional.

Al aumentar la escala podrían aparecer problemas como:

- Millones o miles de millones de registros.
- Datos llegando continuamente y a gran velocidad.
- Mayor consumo de memoria y almacenamiento.
- Necesidad de procesar los datos en tiempo real.
- Mayor cantidad y variedad de fuentes de datos.
- Necesidad de utilizar procesamiento distribuido.
- Mayor dificultad para almacenar y analizar toda la información en una sola computadora.


# 7. Batch y Streaming

## Procesamiento realizado

El programa desarrollado utiliza **procesamiento Batch**, porque analiza un archivo CSV que ya está almacenado.

Primero se carga el archivo completo y posteriormente se realizan operaciones sobre los datos, como calcular promedios, encontrar la temperatura máxima y contar las alertas.

## Alerta en pocos segundos

Para emitir una alerta pocos segundos después de recibir una lectura mayor a 85 °C utilizaría **procesamiento Streaming**.

Cada nueva medición podría ser procesada conforme llega. Si la temperatura supera los 85 °C, el sistema podría generar inmediatamente una alerta.

Esto sería adecuado porque la empresa necesita obtener el resultado prácticamente en tiempo real.

## Resumen al terminar el día

Para generar un resumen al terminar el día utilizaría **procesamiento Batch**.

Al finalizar el día se podrían tomar todas las mediciones almacenadas y calcular:

- Temperatura promedio.
- Temperatura máxima.
- Cantidad de alertas.
- Alertas por planta.
- Sensores con mayor cantidad de alertas.

La elección depende del tiempo requerido para obtener el resultado:

- **Segundos:** Streaming.
- **Al finalizar el día:** Batch.


# 8. Lambda y Kappa

## Escenario A — Arquitectura Lambda

Para el escenario A utilizaría una **arquitectura Lambda**, porque se necesita combinar una ruta de procesamiento por lotes con otra ruta para procesar los datos recientes rápidamente.

La arquitectura Lambda permite tener una capa Batch para recalcular el historial y una capa Speed para procesar los datos recientes.

### Diagrama

```text
                    Mediciones de sensores
                            |
                            v
                     +-------------+
                     | Almacenamiento|
                     |   de datos   |
                     +-------------+
                       /           \
                      /             \
                     v               v
             +-------------+   +-------------+
             | Capa Batch  |   | Capa Speed  |
             | Historial   |   | Tiempo real |
             +-------------+   +-------------+
                      \             /
                       \           /
                        v         v
                     +-------------+
                     |    Vista    |
                     |   final     |
                     +-------------+