from Motor import Motor
from bs4 import BeautifulSoup, NavigableString


print('Ingresa la URL de una serie')
url = input()
soup = Motor.navegar(url)

divPadre = soup.find('div', 'site-content')

# Nombre
titulo = divPadre.find('div', 'post-title').text.strip()
print('Titulo: ', titulo)

# Imagen
imagen = divPadre.find('div', 'summary_image').find('img')['data-src']
print('Imagen: ', imagen)

# Descripcion
descripcion = divPadre.find('div', 'summary__content').text.strip()
print('Descripcion: ', descripcion)


## Obtenemos el contenedor para el Nombre original y Generos ##
contenedorInfo = divPadre.find('div', 'post-content')
contenedorInfo = contenedorInfo.find_all('div', 'summary-content')


# Nombre Original
tituloOriginal = contenedorInfo[2].text.strip()
print('Titulo Original: ', tituloOriginal)

print()
# Generos
divGeneros = contenedorInfo[3].find('div', 'genres-content')
generos = divGeneros.find_all('a')
for genero in generos:
    nombreGenero = genero.text
    urlGenero = genero['href']
    print('Genero: ', nombreGenero)
    print('Enlace: ', urlGenero)


print()
## Obtenemos el estado y la fecha ##
contenedorEstado = divPadre.find('div', 'post-status')
contenedorEstado = contenedorEstado.find_all('div',  'summary-content')
# Estado
fecha = contenedorEstado[0].text.strip()
estado = contenedorEstado[1].text.strip()
print('Fecha: ', fecha)
print('Estado: ', estado)

print()
# [Lista de Capitulos]
listaCapitulos = soup.find_all('li', 'wp-manga-chapter')
print('Capitulos Encontrados: ', len(listaCapitulos))
for capitulo in listaCapitulos:
    # Nombre del Capitulo
    nombreCapitulo = capitulo.find('a').text.strip()

    # Link de Capitulo
    urlCapitulo = capitulo.find('a')['href']

    print(nombreCapitulo)
    print(urlCapitulo)
    print()
