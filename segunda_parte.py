import pandas as pd
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición de entrenamiento
data = dataset["train"]

# Convertir el objeto Dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el DataFrame en dos subconjuntos
fallecidos_df = df[df['is_dead'] == 1]
sobrevivientes_df = df[df['is_dead'] == 0]

# Calcular el promedio de edad para los fallecidos
promedio_edad_fallecidos = fallecidos_df['age'].mean()

# Calcular el promedio de edad para los sobrevivientes
promedio_edad_sobrevivientes = sobrevivientes_df['age'].mean()

# Imprimir los resultados
print(f"Promedio de edad de los fallecidos: {promedio_edad_fallecidos}")
print(f"Promedio de edad de los sobrevivientes: {promedio_edad_sobrevivientes}")
