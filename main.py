import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

url = "https://yugenmangas.com/"

# hacemos que la solicitud vaya con nuestro user agent
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# guardamos la respuesta de la solicitud en 'soup'
soup = BeautifulSoup(response.text, features='lxml')

contenedorSeries = soup.find_all('div', 'card series')

for serie in contenedorSeries:
    # nombre
    titulo = serie.find('a')['href'].split(
        '/')[4].replace('-', ' ').capitalize().strip()
    # if(str.isdigit(tiutlo) != True):

    # numero ultimo capitulo
    numeroCapitulo = serie.find(
        'span', 'badge badge-md text-uppercase bg-darker-overlay').text.strip()

    # imagen
    imagenUrl = serie.find('img')['src']

    # url
    url = serie.find('a')['href'].split(
        '/')

    url = f'{url[0]}//{url[2]}/{url[3]}/{url[4]}/'

    print(titulo)
    print(numeroCapitulo)
    print(imagenUrl)
    print(url)
    print()
