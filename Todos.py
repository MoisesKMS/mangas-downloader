import os
from tqdm import tqdm
import requests
from Motor import Motor


def descargar(url, pathname, imageNumber):
    # Si la ruta no existe, la creamos
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    # Descargar el cuerpo de la respuesta por partes, no imediatamente
    response = requests.get(url, stream=True)

    # Obtener el tamaño total del imagen
    file_size = int(response.headers.get("Content-Length", 0))

    # Asignamos el nombre a la imagen
    filename = os.path.join(pathname + str(imageNumber) + ".jpg")

    # barra de progreso, cambiando la unidad a bytes (predeterminado por tqdm)
    progress = tqdm(response.iter_content(
        1024), f"Descargando {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # escribir datos leídos en el archivo
            f.write(data)
            # actualizar la barra de progreso manualmente
            progress.update(len(data))


print('Ingresa la URL de una serie')
url = input()
soup = Motor.navegar(url)

divPadre = soup.find('div', 'site-content')

# Nombre
titulo = divPadre.find('div', 'post-title').text.strip()
print('Titulo: ', titulo)

# [Lista de Capitulos]
listaCapitulos = soup.find_all('li', 'wp-manga-chapter')
print('Capitulos Encontrados: ', len(listaCapitulos))
print()
for capitulo in reversed(listaCapitulos):
    # Nombre del Capitulo
    nombreCapitulo = str(capitulo.find('a'))
    nombreCapitulo = nombreCapitulo[nombreCapitulo.index(
        ';">') + 3: nombreCapitulo.index('<span')].strip()

    # Link de Capitulo
    urlCapitulo = capitulo.find('a')['href']

    soup = Motor.navegar(urlCapitulo)

    divPadre = soup.find('div', 'reading-content')
    listaImagenes = divPadre.find_all('img')

    print('Descargando: ', titulo, nombreCapitulo)

    numberCount = 0
    ruta = str("./descargas/" + titulo + "/" + nombreCapitulo.lower() + "/")

    for imagen in listaImagenes:
        urlImagen = imagen['data-src'].strip()
        numberCount = numberCount + 1
        descargar(urlImagen, ruta, numberCount)

    print()
