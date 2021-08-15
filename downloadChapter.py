import json
import os
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
}

chapterId = "https://yugenmangas.com/no-quise-seducir-al-protagonista-masculino-capitulo-0/"

url = chapterId;


response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='lxml')

contentListImg = soup.find('div', class_="readingnav rnavbot")
scriptContainer = soup.find_all('script')
# print(scriptContainer)
stringContainer = scriptContainer[29].contents[0]
convjson_process1 = stringContainer.replace('ts_reader.run(', '')
convjson_process2 = convjson_process1.replace(');', '')
imgContainer = convjson_process2.replace('\\', '')


#get chapter script container
print(imgContainer)




### Donwload Images ###

# path = "C:\\Users\ScarKMS\\Desktop\\imgdownloaded\\"
path = "./Downloads/"
images = ["https://i1.wp.com/i.ibb.co/qRsL2bR/0-No-Quise-Seducir-Al-protagonista.jpg","https://i0.wp.com/i.ibb.co/qyGskmP/page001.jpg","https://i0.wp.com/i.ibb.co/fF6fQqr/page002.jpg","https://i0.wp.com/i.ibb.co/YkgF6K7/page003.jpg","https://i0.wp.com/i.ibb.co/bbF82N9/page004.jpg"]
numberCount = -1

def download(url, pathname, imageNumber):
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    
    # get the file name
    filename = os.path.join(pathname + str(imageNumber) + ".jpg")
    
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


for image in images:
    numberCount = numberCount + 1
    download(image, path, numberCount)