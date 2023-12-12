import pandas as pd
import requests
from typing import Set
import sqlite3

def separador(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("==============================================\n==============================================")
        return result
    return wrapper


@separador
def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    return data


@separador
def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    datos_demograficos = ej_1_cargar_datos_demograficos()
    calidad_aire_data = {'city': [], 'CO': [], 'NO2': [], 'O3': [], 'SO2': [], 'PM2.5': [], 'PM10': [], 'overall_aqi': [] }

    for ciudad in ciudades:
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        response = requests.get(api_url, headers={'X-Api-Key': 'BxVi4qFBRJH8qaxUZyRjjA==anRqHFCtQQAD310w'})

        try:
            response.raise_for_status()  
            data = response.json()
            
            CO = data.get('CO', 'No data')
            NO2 = data.get('NO2', 'No data')
            O3  = data.get('O3', 'No data')
            SO2 = data.get('SO2', 'No data')
            PM2_5 = data.get('PM2.5', 'No data')
            PM10 = data.get('PM10', 'No data')
            overall_aqi = data.get('overall_aqi', 'No data')
            
            calidad_aire_data['city'].append(ciudad)
            calidad_aire_data['CO'].append(CO)
            calidad_aire_data['NO2'].append(NO2)
            calidad_aire_data['O3'].append(O3)
            calidad_aire_data['SO2'].append(SO2)
            calidad_aire_data['PM2.5'].append(PM2_5)
            calidad_aire_data['PM10'].append(PM10)
            calidad_aire_data['overall_aqi'].append(overall_aqi)
            
        except requests.exceptions.RequestException as e:
            print(f"Error for {ciudad}: {str(e)}")

    df_calidad_aire = pd.DataFrame(calidad_aire_data)
    df_calidad_aire.to_csv('ciudades_calidad_aire.csv', index=False)


@separador
def ej_3_limpiar_datos(datos_demograficos: pd.DataFrame) -> pd.DataFrame:
    limpieza_datos = datos_demograficos.drop(['Race', 'Count', 'Number of Veterans'], axis=1)
    limpieza_datos = limpieza_datos.drop_duplicates()
    return limpieza_datos


@separador
def ej_4_crear_base_datos(US_Cities_Demographics: pd.DataFrame, Edited_US_Cities_Demographics: pd.DataFrame) -> None:
    with sqlite3.connect('datos_ciudades.db') as conn:
        US_Cities_Demographics.to_sql('US_Cities_Demographics', conn, index=False, if_exists='replace')
        Edited_US_Cities_Demographics.to_sql('Edited_US_Cities_Demographics', conn, index=False, if_exists='replace')


@separador
def ej_5_analizar_calidad_aire_vs_poblacion() -> None:
    with sqlite3.connect('datos_ciudades.db') as conn:
        datos_demograficos = pd.read_sql_query('SELECT * FROM Edited_US_Cities_Demographics', conn)
    
    calidad_aire_data = pd.read_csv('ciudades_calidad_aire.csv')

    datos_demograficos['City'] = datos_demograficos['City'].str.lower()
    calidad_aire_data['city'] = calidad_aire_data['city'].str.lower()
    calidad_aire_primeras_10 = calidad_aire_data.head(10)

    datos_demograficos['City'] = datos_demograficos['City'].str.lower()
    calidad_aire_primeras_10['city'] = calidad_aire_primeras_10['city'].str.lower()

    result = pd.merge(datos_demograficos, calidad_aire_primeras_10, left_on='City', right_on='city', how='inner')

    result = result[['City', 'State', 'Total Population', 'overall_aqi']]
    print(result)

if __name__ == "__main__":
    
    dataframe_demografico = ej_1_cargar_datos_demograficos()
    ciudades_demograficas = set(dataframe_demografico['City'])
    
    print("--- PRIMERA FUNCIÓN: Cargar Datos Demográficos ---")
    print(dataframe_demografico)

    print("--- SEGUNDA FUNCIÓN: Cargar Calidad de Aire ---")
    ej_2_cargar_calidad_aire(ciudades_demograficas)
    print("--- CSV 'ciudades_claidad_aire.csv' LISTO ---")

    print("--- TERCERA FUNCIÓN: Limpiar Datos ---")
    limpiar_datos = ej_3_limpiar_datos(dataframe_demografico)
    print(limpiar_datos)

    print("--- CUARTA FUNCIÓN: Crear Base de Datos ---")
    ej_4_crear_base_datos(dataframe_demografico, limpiar_datos)
    print("--- DATABASE 'datos_ciudades.db' HA SIDO CREADA ---")

    print("--- QUINTA FUNCIÓN: Analizar Calidad de Aire vs. Población ---")
    ej_5_analizar_calidad_aire_vs_poblacion()


###################"""
