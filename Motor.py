import requests
from bs4 import BeautifulSoup


class Motor:
    def __init__(self) -> None:
        pass

    def navegar(direccion):
        # definimos las cabeceras para realizar la solicitud
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36"
        }

        url = direccion
        # hacemos que la solicitud vaya con nuestro user agent
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'

        # guardamos la respuesta de la solicitud en 'soup'
        soup = BeautifulSoup(response.text, features='lxml')
        return soup

    def caracteresEspeciales(cadena):
        # definimos los caracterres especiales que no queremos
        lista = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '¿']
        cadenaFinal = ''

        for letra in cadena:
            caracterIgual = False

            for caracter in lista:
                if(letra == caracter):
                    caracterIgual = True

            if(caracterIgual == False):
                cadenaFinal += letra

        return cadenaFinal
