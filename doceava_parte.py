from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('sexta_parte_datos.csv')
X = df.drop(columns=['DEATH_EVENT'])
y = df['DEATH_EVENT']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

random_forest = RandomForestClassifier(random_state=42)  
random_forest.fit(X_train, y_train)

y_pred_rf = random_forest.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_pred_rf)
print('Matriz de confusión:')
print(conf_matrix)

f1 = f1_score(y_test, y_pred_rf)
print(f'F1-Score: {f1:.2f}')

accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Accuracy del random forest: {accuracy_rf:.2f}')
print(f'Comparación -> F1-Score: {f1:.2f}, Accuracy: {accuracy_rf:.2f}')

random_forest_tuned = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
random_forest_tuned.fit(X_train, y_train)
y_pred_rf_tuned = random_forest_tuned.predict(X_test)
f1_tuned = f1_score(y_test, y_pred_rf_tuned)
print(f'F1-Score después del ajuste de parámetros: {f1_tuned:.2f}')
