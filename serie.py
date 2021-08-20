from bs4 import BeautifulSoup
import motor
import json

headers = motor.headers()
url = input()
soup = motor.abrirEnlace(url)

def getCapitulos():

    contentListChapters = soup.find('div', class_='eplister')
    listChapters = contentListChapters.findAll('li')
    
    jsonChapters = {}
    jsonChapters['capitulos'] = []

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
        
        jsonChapters['capitulos'].append({
            'tiutlo': str(textTitle),
            'fecha': str(chapterDate),
            'url': str(urlChapter)})

    return jsonChapters

def getImagen():
    #obtener Imagen Cover
    contentImg = soup.find('div', class_="thumb")
    labelImg = BeautifulSoup(str(contentImg), 'html.parser').img
    urlImg = str(labelImg['data-src']).strip()
    return urlImg

def getDescripcion():
    contentDescription = soup.find('div', class_="entry-content entry-content-single")
    contentParagraphs = contentDescription.find_all('p')
    description = ''

    for paragraph in contentParagraphs:
        process1 = str(paragraph).replace('<p>', '')
        process2 = process1.replace('</p>', '\n')
        process3 = process2.replace('<br/>', '\n')
        description = description + process3

    return description

def getGeneros():
    contentGenres = soup.find('div', class_="seriestugenre")
    listGenres =  contentGenres.find_all('a')
    genres = []
    for gender in listGenres:
        genres.append(str(gender.text))
    return genres



# jsonCapitulos = getCapitulos()

# getCapitulos()

# print('Ultima vez actualizado: ', listChapters[0].find('span', class_="chapterdate").text)
# print('Capitulos:', len(listChapters))