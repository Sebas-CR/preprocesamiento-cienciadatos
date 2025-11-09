import pandas as pd
import numpy as np

def cargar_datos(ruta_archivo):
    """Carga un dataset desde un archivo CSV."""
    print(f"Cargando datos desde: {ruta_archivo}")
    try:
        return pd.read_csv(ruta_archivo)
    except FileNotFoundError:
        print("Error: Archivo no encontrado. Devolviendo DataFrame de ejemplo.")
        return pd.DataFrame({'col1': [1, 2, np.nan, 4], 'col2': ['a', 'b', 'c', 'd']})

def limpiar_nulos(df, estrategia='media'):
    """Imputa valores nulos en columnas numéricas."""
    print(f"Limpiando nulos con estrategia: {estrategia}")
    if estrategia == 'media':
        return df.fillna(df.mean(numeric_only=True))
    elif estrategia == 'moda':
        return df.fillna(df.mode().iloc[0])
    return df

def normalizar_columna(df, columna):
    """Normaliza una columna numérica usando Min-Max Scaling."""
    print(f"Normalizando columna: {columna}")
    min_val = df[columna].min()
    max_val = df[columna].max()
    df[columna + '_norm'] = (df[columna] - min_val) / (max_val - min_val)
    return df

if __name__ == '__main__':
    # 1. Cargar Datos (usando un ejemplo si no hay archivo data.csv)
    df_ejemplo = cargar_datos("data/data.csv")

    # 2. Limpieza
    df_limpio = limpiar_nulos(df_ejemplo.copy(), estrategia='media')

    # 3. Transformación
    if 'col1' in df_limpio.columns:
         df_final = normalizar_columna(df_limpio, 'col1')
    else:
         df_final = df_limpio

    print("Resultados del Preprocesamiento")
    print("DataFrame Final:")
    print(df_final)