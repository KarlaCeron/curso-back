import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

try:
    # Cargar el archivo Excel
    df = pd.read_excel('precio_oro_1900_2025.xlsx')

    # Mostrar las primeras filas
    print("Primeras 5 filas del archivo:")
    print(df.head())

    # Mostrar nombres de las columnas
    print("\nNombres de las columnas:")
    print(df.columns)

    # Definir las columnas a analizar (ajusta estos nombres según tu archivo)
    selected_columns = ['Año', 'Precio_Oro_USD', 'PIB_Per_Capita_USD']

    # Verificar si las columnas existen
    missing_cols = [col for col in selected_columns if col not in df.columns]
    if missing_cols:
        print(f"\nAdvertencia: Las siguientes columnas no se encontraron en el archivo: {missing_cols}")
        print("Por favor, verifica los nombres de las columnas.")
    else:
        print(f"\nEstadísticas descriptivas para las columnas {selected_columns}:")
        print(df[selected_columns].describe())

    # Mostrar una imagen usando matplotlib
    try:
        img = mpimg.imread('oro_portada.jpg')  # Cambia al nombre de tu imagen
        plt.imshow(img)
        plt.axis('off')  # Ocultar ejes
        plt.title("Imagen relacionada con el análisis del precio del oro")
        plt.show()
        print("\nImagen mostrada correctamente con matplotlib.")
    except FileNotFoundError:
        print("\nAdvertencia: La imagen 'oro_portada.jpg' no fue encontrada.")
        print("Asegúrate de que el archivo está en la ruta correcta.")

except FileNotFoundError:
    print("Error: El archivo 'precio_oro_1900_2025.xlsx' no fue encontrado.")
    print("Asegúrate de que el archivo está en la ruta correcta o proporciona la ruta completa.")
except Exception as e:
    print(f"Ocurrió un error al leer o procesar el archivo: {e}")
