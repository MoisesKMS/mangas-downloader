import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

serieId = "no-quise-seducir-al-protagonista-masculino-capitulo-0/"

url = "https://yugenmangas.com/manga/" + serieId;


response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='lxml')

contentListChapters = soup.find('div', class_='eplister')
listChapters = contentListChapters.findAll('li');

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


print('Capitulos:', len(listChapters) )