import requests
from bs4 import BeautifulSoup
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

url = "https://yugenmangas.com/"

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, features='lxml')


divPadre = soup.find('div', 'col-md-8 col-sm-12 col-xs-12')
divSeries = divPadre.findAll('div', 'd-flex justify-content-center')
contenedorSeries = divSeries[1]
listaSeries = contenedorSeries.findAll(
    'div', 'col-6 col-sm-6 col-md-6 col-xl-3')


for serie in listaSeries:
    # Obtener Imagen Serie
    contenedorImagen = BeautifulSoup(
        str(serie.find('img', class_='series-image')), 'html.parser').img
    urlImagen = contenedorImagen['src']

    print("Url de la Imagen: " + urlImagen)

    # obtener Nombre y Url de la serie
    contenedorPadre = serie.find('div', 'series-content')
    contenedorEnlace = BeautifulSoup(str(serie.find('a')), 'html.parser').a
    enlace = contenedorEnlace['href']

    contenedorTitulo = BeautifulSoup(
        str(contenedorPadre.find('h5')), 'html.parser').h5.text

    urlSerie = enlace.split('/')
    urlSerie = "https://yugenmangas.com/series/" + urlSerie[4]

    print("Url del ultimo capitulo: " + enlace)
    print("Url de la Serie: " + urlSerie)
    # print(enlace[:enlace.index('/{3}?')])
    print("Titulo de la Serie: " + contenedorTitulo)
    print()
