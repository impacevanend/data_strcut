from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Cargar los datos
df = pd.read_csv('sexta_parte_datos.csv')  # Reemplaza 'tu_archivo.csv' con la ruta de tu archivo

# Preparar la matriz X eliminando las columnas 'DEATH_EVENT', 'age' y 'categoria_edad'
X = df.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'])

# Preparar el vector y con los valores de la columna 'age'
y = df['age']

# Crear una instancia del modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo
model.fit(X, y)

# Predecir las edades
y_pred = model.predict(X)

# Calcular el error cuadrático medio
mse = mean_squared_error(y, y_pred)
print(f"El error cuadrático medio (MSE) de las edades predichas es: {mse}")
