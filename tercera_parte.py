import pandas as pd
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
df = pd.DataFrame(data)

print("Tipos de datos en el DataFrame:")
print(df.dtypes)

cantidad_hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
cantidad_mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print(f"Cantidad de hombres fumadores: {cantidad_hombres_fumadores}")
print(f"Cantidad de mujeres fumadoras: {cantidad_mujeres_fumadoras}")
