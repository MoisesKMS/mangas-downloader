from Motor import Motor

print('Ingresa la URL de una serie')
url = input()
soup = Motor.navegar(url)

divPadre = soup.find('div', 'site-content')
print()

# Nombre
titulo = divPadre.find('div', 'post-title').text.strip()
print('Titulo: ', titulo)

# Imagen
imagen = divPadre.find('div', 'summary_image').find('img')['data-src']
print('Imagen: ', imagen)

## Obtenemos el contenedor para el Nombre original y Generos ##
contenedorInfo = divPadre.find('div', 'post-content')
contenedorInfo = contenedorInfo.find_all('div', 'summary-content')


# Nombre Original
# Obtenemos todos los heading de la info, y despues comprobamos que exista el texto 'Alternativa' para mostrar el titulo alternativo
# En caso de no existir, se asignara el titulo principal al Alternativo
divsHeading = divPadre.find_all('div', 'summary-heading')

if(divsHeading[2].text.strip() == 'Alternativa'):
    tituloOriginal = contenedorInfo[2].text.strip()
else:
    tituloOriginal = titulo

print('Titulo Original: ', tituloOriginal)
print()

# Descripcion
descripcion = divPadre.find('div', 'summary__content').text.strip()
print('Descripcion: ', descripcion)
print()

# Generos
divGeneros = divPadre.find('div', 'genres-content')
generos = divGeneros.find_all('a')

for genero in generos:
    nombreGenero = genero.text
    urlGenero = genero['href']
    print('Genero: ', nombreGenero)
    print('Enlace: ', urlGenero)

print()


## Obtenemos el estado y la fecha busando todos los divs que tenga la clase sumary-content para despues iterar sobre ellos ##
contenedorEstado = divPadre.find('div', 'post-status')
contenedorEstado = contenedorEstado.find_all('div',  'summary-content')

# Taratamos de obtner tanto el estado como la fecha de estreno, sino no hay fecha de estreno solo mostramos el estado
# En un caso exitoso contenedorEstado[0] tiene la fecha y contenedorEstado[1] el estado de emision
try:
    fecha = contenedorEstado[0].text.strip()
    estado = contenedorEstado[1].text.strip()
    print('Fecha: ', fecha)
    print('Estado: ', estado)
except:
    estado = contenedorEstado[0].text.strip()
    print('Estado: ', estado)

print()


# [Lista de Capitulos]
listaCapitulos = soup.find_all('li', 'wp-manga-chapter')
print('Capitulos Encontrados: ', len(listaCapitulos))
print()
for capitulo in listaCapitulos:
    # Nombre del Capitulo
    nombreCapitulo = str(capitulo.find('a'))
    nombreCapitulo = nombreCapitulo[nombreCapitulo.index(
        ';">') + 3: nombreCapitulo.index('<span')].strip()

    # Link de Capitulo
    urlCapitulo = capitulo.find('a')['href']

    print(nombreCapitulo)
    print(urlCapitulo)
    print()
