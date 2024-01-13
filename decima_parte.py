from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


df = pd.read_csv('sexta_parte_datos.csv')  


X = df.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'])


y = df['age']

model = LinearRegression()


model.fit(X, y)


y_pred = model.predict(X)


mse = mean_squared_error(y, y_pred)
print(f"El error cuadrático medio (MSE) de las edades predichas es: {mse}")
