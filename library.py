import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

url = "https://yugenmangas.com/manga/?order=update";

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='lxml')

contentSerie = soup.find('div', class_="listupd")
listSerie = contentSerie('div', class_="bs")

for serie in listSerie:
    #get titele
    title = serie.find('div', class_="tt")
    textTitle = title.text.strip()

    #get type
    selectType = serie.find('span', class_='type')
    contentType = BeautifulSoup(str(selectType), 'html.parser')
    typeSerie = contentType.span['class'][1].strip()

    #get img
    contentImg = serie.find('img', class_='ts-post-image')
    coverImg = BeautifulSoup(str(contentImg), 'html.parser').img
    deleteSizeImg = str(coverImg['data-src']).strip()
    urlImg = deleteSizeImg[:deleteSizeImg.index('?')]
    
    #get url
    contentTitleUrl = serie.find('a')
    contentUrl = BeautifulSoup(str(contentTitleUrl), 'html.parser').a
    urlSerie = contentUrl['href']


    
    print('Titulo: ' + textTitle)
    print('Tipo: ' + typeSerie)
    print('Cover Img: ' + urlImg)
    print('Url: ' + urlSerie)
    print()