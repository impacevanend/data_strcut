import pandas as pd

def eliminar_valores_atipicos(df, columnas):
    """
    Elimina valores atípicos de un DataFrame en las columnas especificadas.

    :param df: DataFrame con los datos.
    :param columnas: Lista de columnas para verificar valores atípicos.
    :return: DataFrame sin valores atípicos.
    """
    for columna in columnas:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        filtro = (df[columna] >= Q1 - 1.5 * IQR) & (df[columna] <= Q3 + 1.5 * IQR)
        df = df.loc[filtro]
    
    return df

def preparar_y_guardar_datos(df, archivo_salida):
   
    if df.isnull().values.any():
        df = df.dropna()

  
    df = df.drop_duplicates()

  
    columnas_numericas = df.select_dtypes(include=['number']).columns
    df = eliminar_valores_atipicos(df, columnas_numericas)

   
    condiciones = [
        (df['age'] <= 12),
        (df['age'] <= 19),
        (df['age'] <= 39),
        (df['age'] <= 59),
        (df['age'] > 59)
    ]
    categorias = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['categoria_edad'] = pd.cut(df['age'], bins=[0, 12, 19, 39, 59, float('inf')], labels=categorias, right=False)

 
    df.to_csv(archivo_salida, index=False)
    print(f"Datos guardados en {archivo_salida}")


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
preparar_y_guardar_datos(df, 'datos_limpios.csv')
