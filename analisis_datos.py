import pandas as pd
import time

# Función para medir el tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
        return resultado
    return wrapper

# Decorador para análisis de precio medio
@medir_tiempo
def analisis_precio_medio(df):
    return df['precio'].mean()

# Leer el DataFrame desde el archivo CSV
df_productos = pd.read_csv('datos_productos.csv')

# Limpiar y transformar datos 
df_productos['precio'] = pd.to_numeric(df_productos['precio'], errors='coerce')

# Función para el análisis
precio_medio = analisis_precio_medio(df_productos)
print(f"El precio medio de los productos es: ${precio_medio:.2f}")
