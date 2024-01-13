import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px


df = pd.read_csv('sexta_parte_datos.csv')  


X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values


y = df['DEATH_EVENT'].values


X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)


df_tsne = pd.DataFrame(X_embedded, columns=['Componente 1', 'Componente 2', 'Componente 3'])
df_tsne['DEATH_EVENT'] = y


fig = px.scatter_3d(df_tsne, x='Componente 1', y='Componente 2', z='Componente 3',
                    color='DEATH_EVENT', title='Visualización t-SNE de Datos de Fallo Cardíaco')

fig.show()
