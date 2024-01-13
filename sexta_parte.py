import pandas as pd
import requests
import argparse
from io import StringIO

def descargar_datos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return pd.read_csv(StringIO(respuesta.text))
    else:
        raise Exception(f"Error al descargar los datos desde {url}")

def limpiar_y_categorizar_datos(df):
    # Verificar y tratar valores faltantes
    if df.isnull().values.any():
        df = df.dropna()

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Eliminar valores atípicos
    columnas_numericas = df.select_dtypes(include=['number']).columns
    for columna in columnas_numericas:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        filtro = (df[columna] >= Q1 - 1.5 * IQR) & (df[columna] <= Q3 + 1.5 * IQR)
        df = df.loc[filtro]

    # Categorizar por edades
    condiciones = [
        (df['age'] <= 12),
        (df['age'] <= 19),
        (df['age'] <= 39),
        (df['age'] <= 59),
        (df['age'] > 59)
    ]
    categorias = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=[0, 12, 19, 39, 59, float('inf')], labels=categorias, right=False)

    return df

def main(url, archivo_salida):
    df = descargar_datos(url)
    df = limpiar_y_categorizar_datos(df)
    df.to_csv(archivo_salida, index=False)
    print(f"Datos procesados y guardados en {archivo_salida}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar y limpiar datos de insuficiencia cardíaca.")
    parser.add_argument("url", help="URL del archivo CSV con los datos")
    parser.add_argument("archivo_salida", help="Nombre del archivo CSV para guardar los datos procesados")
    args = parser.parse_args()
    main(args.url, args.archivo_salida)
