********** LABORATORIO: INGESTA Y PREPARACIÓN DE DATOS ***********
****************** Análisis de calidad del aire ******************

1. Carga los datos demográficos en una tabla utilizando pandas, utilizando el mismo CSV de demografía del ejemplo estudiado en clases: https://public.opendatasoft.com/explore/dataset/us-cities-demographics/table/?sort=total_population

Importa directamente usando esta url (https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B) con el siguiente código:

    '''url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')'''

2. Parsea los datos de calidad del aire para cada ciudad en la tabla demográfica obteniendo la información con la API https://api-ninjas.com/api/airquality. Crea una tabla de dimensiones utilizando pandas para almacenar estos datos.
    - Toma el elemento concentration de cada entrada por fila.

3. Limpia los datos demográficos realizando las siguientes acciones:
    - Elimina las columnas: Race, Count y Number of Veterans.
    - Elimina las filas duplicadas.

4. Crea una base de datos en SQLite, carga las dos tablas procesadas ahí

5. Aplica joins, y agregaciones para verificar si las ciudades más pobladas tienen la peor calidad del aire. (muestra las primeras 10 colúmnas y con eso responde la pregunta)

Crea un script para el ejercicio 3, luego en un archivo markdown escribe la query SQL que utilizaste para responder la pregunta y escribe una explicación detallada de tu interpretación de los resultados, este dos archivo súbelo aquí. (Adjunta también la base de datos sqlite).

Para los ejercicios 1 y 2 usa la siguiente plantilla:

    import pandas as pd
    from typing import Set


    def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
        pass

    def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
        pass

Y usa los siguientes tests:

    # Estos tests pueden fallar, sólo están aquí como referencia ya que debido a la actualización de valores por parte de la api, no se pueden mantener fijos para evaluar en todo momento al mismo valor.
    from hashlib import sha256
    from soluciones import (
        ej_1_cargar_datos_demograficos,
        ej_2_cargar_calidad_aire,
    )
    import pandas as pd


    def _hash(data):
        return sha256(str(data).encode("utf-8")).hexdigest()


    def test_sol_1():
        df = ej_1_cargar_datos_demograficos()
        idxs = [1995, 1360, 982, 2264, 2096, 1733, 1804, 2025, 2070, 507]
        
        selected_rows = df.loc[idxs].values
        assert _hash(selected_rows) == "567b67390efd8da8091f6f86da9f5e76b30d1b7dcb25bd7d9b87bcb757b2c571"
        
        
    def test_sol_2():
        df = ej_1_cargar_datos_demograficos()
        ej_2_cargar_calidad_aire(set(df["City"].tolist()))
        
        ciudades_df = pd.read_csv("ciudades.csv")
        
        actual = ciudades_df.loc[:9].to_dict()
        
        expected = {
            'CO': {0: 250.34, 1: 287.06, 2: 247.0, 3: 280.38, 4: 323.77, 5: 243.66, 6: 173.57, 7: 211.95, 8: 263.69, 9: 260.35},
            'NO2': {0: 3.43, 1: 0.76, 2: 0.56, 3: 1.06, 4: 1.67, 5: 0.91, 6: 0.23, 7: 0.84, 8: 0.8, 9: 1.71},
            'O3': {0: 167.37, 1: 103.0, 2: 41.13, 3: 98.71, 4: 86.55, 5: 100.14, 6: 94.41, 7: 105.86, 8: 100.14, 9: 130.18},
            'SO2': {0: 2.92, 1: 2.3, 2: 0.19, 3: 1.1, 4: 6.32, 5: 1.27, 6: 0.38, 7: 0.24, 8: 0.4, 9: 5.36},
            'PM2.5': {0: 17.78, 1: 6.06, 2: 1.79, 3: 4.08, 4: 2.64, 5: 5.43, 6: 12.62, 7: 1.67, 8: 4.49, 9: 6.21},
            'PM10': {0: 26.26, 1: 6.37, 2: 1.85, 3: 4.47, 4: 2.95, 5: 5.68, 6: 48.06, 7: 1.79, 8: 4.66, 9: 6.76},
            'overall_aqi': {0: 220, 1: 170, 2: 34, 3: 159, 4: 128, 5: 162, 6: 148, 7: 177, 8: 162, 9: 205},
            'city': {0: 'Perris', 1: 'Mount Vernon', 2: 'Mobile', 3: 'Dale City', 4: 'Maple Grove', 5: 'Muncie', 6: 'San Clemente', 7: 'Providence', 8: 'Norman', 9: 'Hoover'}
        }
        
        assert expected == actual

Debido a que este laboratorio tiene una solución más abierta que los demás, no existen tests para todos los pasos, es por eso que debes detallar tu solución en el markdown para faciliar la revisión a mano.


