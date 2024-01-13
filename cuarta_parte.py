import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    """
    Descarga los datos desde una URL y los guarda en un archivo CSV.

    :param url: URL del archivo a descargar.
    :param nombre_archivo: Nombre del archivo donde se guardarán los datos.
    """
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(respuesta.text)
        print(f"Archivo guardado: {nombre_archivo}")
    else:
        print("Error al descargar el archivo")

# Usar la función para descargar y guardar el archivo CSV
url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
nombre_archivo = 'heart_failure_clinical_records_dataset.csv'
descargar_y_guardar_csv(url, nombre_archivo)
