import requests
from bs4 import BeautifulSoup
import pandas as pd

# Lista de URLs de productos específicos
urls_productos = [
    "https://www.blippo.com/collections/toys/products/kuromi-baby-bear-diaper-plushie-mini",
    "https://www.blippo.com/collections/toys/products/mochi-mochi-panda-x-kuromi-copycat-plushie-medium",
    "https://www.blippo.com/collections/toys/products/chiikawa-atsumete-2-sticker-set-with-gum",
    "https://www.blippo.com/collections/bags/products/kawaii-school-accessories-4pc-bundle",
    "https://www.blippo.com/collections/toys/products/pompompurin-perler-beads-craft-kit",
    "https://www.blippo.com/collections/candy/products/hello-kitty-4d-gummy-apple-vinegar-soda",
    "https://www.blippo.com/collections/toys/products/hello-kitty-daisuki-neko-neko-plushie-medium"
]

datos_productos = []

# Función para obtener datos de una página de producto
def obtener_datos(url):
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()
        
        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ajustar el selector según la estructura de la página web
        nombre_elemento = soup.find('h1', class_='product-detail__title small-title')
        precio_elemento = soup.find('span', class_='theme-money large-title')
        disponibilidad_elemento = soup.find('span', class_='product-inventory__status')

        # Comprobar que los elementos existen antes de acceder a su texto
        nombre = nombre_elemento.text.strip() if nombre_elemento else 'N/A'
        precio = precio_elemento.text.strip() if precio_elemento else 'N/A'
        disponibilidad = disponibilidad_elemento.text.strip() if disponibilidad_elemento else 'Full Stock'

        print(f"Producto encontrado: Nombre={nombre}, Precio={precio}, Disponibilidad={disponibilidad}")

        # Añadir los datos del producto a la lista
        datos_productos.append({
            'nombre': nombre,
            'precio': precio,
            'disponibilidad': disponibilidad
        })
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud HTTP: {e}")
    except Exception as e:
        print(f"Error al procesar la página: {e}")

# Recorrer las URLs y obtener los datos
for url in urls_productos:
    print(f"Procesando URL: {url}")
    obtener_datos(url)

# Crear el DataFrame con los datos de los productos
df_productos = pd.DataFrame(datos_productos)

# Guardar el DataFrame en un archivo CSV
df_productos.to_csv('datos_productos.csv', index=False)
print("Datos guardados en datos_productos.csv")

# Y listo :)