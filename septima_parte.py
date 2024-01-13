import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('sexta_parte_datos.csv') 


plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=range(0, 100, 10), color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.show()


categorias = ['has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']
labels = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']
colors = ['blue', 'red']
gender = ['Hombres', 'Mujeres']
bar_width = 0.35  


plt.figure(figsize=(12, 7))


conteos = [[df[df['is_male'] == i][cat].sum() for cat in categorias] for i in [1, 0]]

#
