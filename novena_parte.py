import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

# Cargar los datos
df = pd.read_csv('sexta_parte_datos.csv')  # Reemplaza 'tu_archivo.csv' con la ruta de tu archivo

# Preparar la matriz con solo los valores de los atributos
X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values

# Preparar el array unidimensional de la columna objetivo
y = df['DEATH_EVENT'].values

# Ejecutar t-SNE
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear un DataFrame para el gráfico
df_tsne = pd.DataFrame(X_embedded, columns=['Componente 1', 'Componente 2', 'Componente 3'])
df_tsne['DEATH_EVENT'] = y

# Realizar un gráfico de dispersión 3D
fig = px.scatter_3d(df_tsne, x='Componente 1', y='Componente 2', z='Componente 3',
                    color='DEATH_EVENT', title='Visualización t-SNE de Datos de Fallo Cardíaco')

fig.show()
