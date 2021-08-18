from bs4 import BeautifulSoup
import motor

headers = motor.headers()

print('Ingresa la Url de una Serie')
url = input()

soup = motor.abrirEnlace(url)

def getCapitulos():
    contentListChapters = soup.find('div', class_='eplister')
    listChapters = contentListChapters.findAll('li')

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
        print()
        print('Titulo del Capitulo: ' + textTitle)
        print('Fecha de Subida: ' + chapterDate)
        print('Url del Capitulo: ' + urlChapter)



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
    process3 = process2.replace('<br/>', '\n')
    description = description + process3

print ('Descripcion: ')
print(description)



#get generes
contentGeneres = soup.find('div', class_="seriestugenre")
listGeneres =  contentGeneres.find_all('a')
generes = []
for genere in listGeneres:
    generes.append(str(genere.text))
print('Generos: ', generes)

# getCapitulos()

# print('Ultima vez actualizado: ', listChapters[0].find('span', class_="chapterdate").text)
# print('Capitulos:', len(listChapters))