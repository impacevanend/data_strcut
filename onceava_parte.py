import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Carga de datos
df = pd.read_csv('sexta_parte_datos.csv')  # Reemplaza 'tu_archivo.csv' con la ruta de tu archivo

# Eliminar columna 'categoria_edad'
df = df.drop(columns=['categoria_edad'])

# Visualizar la distribución de clases
plt.figure(figsize=(6, 4))
df['DEATH_EVENT'].value_counts().plot(kind='bar', title='Distribución de Clases')
plt.show()

# Definir matriz de características X y el vector de respuesta y
X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']

# Partición del dataset en conjunto de entrenamiento y test estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# A
decision_tree = DecisionTreeClassifier(random_state=42) # Puedes ajustar más parámetros aquí
decision_tree.fit(X_train, y_train)

y_pred = decision_tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy del árbol de decisión: {accuracy:.2f}')