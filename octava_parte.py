import pandas as pd
import matplotlib.pyplot as plt

# Asumiendo que df es tu DataFrame después de la limpieza y categorización de datos
df = pd.read_csv('sexta_parte_datos.csv')  # Reemplaza 'tu_archivo.csv' con la ruta de tu archivo

# Parte 7: Histogramas agrupados por género
# Preparar los datos
categorias = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
hombres = df[df['sex'] == 1]
mujeres = df[df['sex'] == 0]

# Configurar las propiedades del gráfico
bar_width = 0.35
index = pd.np.arange(len(categorias))
opacity = 0.8

# Crear el gráfico
plt.figure(figsize=(10, 5))

# Barras para hombres
barras_hombres = plt.bar(index, hombres[categorias].sum(), bar_width, alpha=opacity, color='b', label='Hombres')

# Barras para mujeres
barras_mujeres = plt.bar(index + bar_width, mujeres[categorias].sum(), bar_width, alpha=opacity, color='r', label='Mujeres')

plt.xlabel('Categorías')
plt.ylabel('Cantidad')
plt.title('Histograma Agrupado por Sexo')
plt.xticks(index + bar_width / 2, categorias)
plt.legend()

plt.tight_layout()
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(10, 10))


distribuciones = {
    'Anémicos': df['anaemia'].value_counts(),
    'Diabéticos': df['diabetes'].value_counts(),
    'Fumadores': df['smoking'].value_counts(),
    'Muertos': df['DEATH_EVENT'].value_counts()
}



for ax, (label, data) in zip(axs.flatten(), distribuciones.items()):
    ax.pie(data, labels=['No ' + label, label], autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Distribución de {label}')
    ax.axis('equal')  
plt.show()

