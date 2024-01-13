import matplotlib.pyplot as plt
import pandas as pd

# Suponiendo que 'df' es tu DataFrame luego de realizar el proceso de ETL
df = pd.read_csv('sexta_parte_datos.csv') # Descomenta y reemplaza con el nombre de tu archivo CSV

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=range(0, 100, 10), color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()

# Graficar histogramas agrupados por género
categorias = ['has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']
labels = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']
colors = ['blue', 'red']
gender = ['Hombres', 'Mujeres']
bar_width = 0.35  # Ancho de las barras

# Crear las figuras para los histogramas agrupados
plt.figure(figsize=(12, 7))

# Obtener los conteos para cada categoría y género
conteos = [[df[df['is_male'] == i][cat].sum() for cat in categorias] for i in [1, 0]]

#
