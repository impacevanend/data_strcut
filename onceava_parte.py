import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


df = pd.read_csv('sexta_parte_datos.csv') 


df = df.drop(columns=['categoria_edad'])


plt.figure(figsize=(6, 4))
df['DEATH_EVENT'].value_counts().plot(kind='bar', title='Distribución de Clases')
plt.show()


X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


decision_tree = DecisionTreeClassifier(random_state=42) 
decision_tree.fit(X_train, y_train)

y_pred = decision_tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy del árbol de decisión: {accuracy:.2f}')