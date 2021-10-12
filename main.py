from Motor import Motor

soup = Motor.navegar("https://yugenmangas.com/")

contenedorSeries = soup.find_all('div', 'card series')

for serie in contenedorSeries:
    # url
    url = serie.find('a')['href'].split('/')
    url = f'{url[0]}//{url[2]}/{url[3]}/{url[4]}/'

    # nombre
    titulo = serie.find('a')['href'].split(
        '/')[4].replace('-', ' ').capitalize().strip()

    # si el nombre de la serie regresa numeros accedemos a la url de la serie para obtener el titulo
    if(str.isdigit(titulo)):
        soup = Motor.navegar(url)
        divPadre = soup.find('div', 'site-content')
        titulo = divPadre.find('div', 'post-title').text.strip()

    # numero ultimo capitulo
    numeroCapitulo = serie.find(
        'span', 'badge badge-md text-uppercase bg-darker-overlay').text.strip()

    # imagen
    imagenUrl = serie.find('img')['src']

    print(titulo)
    print(numeroCapitulo)
    print(imagenUrl)
    print(url)
    print()
