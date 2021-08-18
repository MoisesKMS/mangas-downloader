import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

print('Ingresa la Url de una Serie')
url = input()

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='lxml')

contentListChapters = soup.find('div', class_='eplister')
listChapters = contentListChapters.findAll('li');

#obtener Imagen Cover
contentImg = soup.find('div', class_="thumb")
labelImg = BeautifulSoup(str(contentImg), 'html.parser').img
urlImg = str(labelImg['data-src']).strip()
print('Url Imagen: ', urlImg)

#Obtener Descripcion
contentDescription = soup.find('div', class_="entry-content entry-content-single")
contentParagraphs = contentDescription.find_all('p')
description = ''

for paragraph in contentParagraphs:
    process1 = str(paragraph).replace('<p>', '')
    process2 = process1.replace('</p>', '\n')
    description = description + process2

print ('Descripcion: ', description)

for chapter in listChapters:
    #get chapter titele
    title = chapter.find('span', class_="chapternum")
    textTitle = title.text.strip()
    
    #get upload date from chapter
    date = chapter.find('span', class_="chapterdate")
    chapterDate = date.text.strip()

    #get url chapter
    contentChapterUrl = chapter.find('a')
    contentUrl = BeautifulSoup(str(contentChapterUrl), 'html.parser').a
    urlChapter = contentUrl['href']
    
    print('Titulo del Capitulo: ' + textTitle)
    print('Fecha de Subida: ' + chapterDate)
    print('Url del Capitulo: ' + urlChapter)
    print()


#get generes
contentGeneres = soup.find('div', class_="seriestugenre")
listGeneres =  contentGeneres.find_all('a')
generes = []
for genere in listGeneres:
    generes.append(str(genere.text))
print('Generos: ', generes)


print('Ultima vez actualizado: ', listChapters[0].find('span', class_="chapterdate").text)
print('Capitulos:', len(listChapters))