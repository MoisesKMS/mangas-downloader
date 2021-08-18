import requests
from bs4 import BeautifulSoup

def headers():
    #definimos el user agent para simular un navegador web
    cabeceras = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
    }
    return cabeceras

def abrirEnlace(url):
    heads = headers()
    response = requests.get(url, headers=heads)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    return soup