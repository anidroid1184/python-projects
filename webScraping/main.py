"""
Este modulo es el principal para desarrollar
web scraping
url: https://escueladirecta-blog.blogspot.com/
"""

import bs4
import requests as rq

# Acceder a sitio web
web = rq.get("https://escueladirecta-blog.blogspot.com/")
# print(web.text)  # Código de la pagina web

# Crear un objeto con la web tipo beuhttps://www.escueladirecta.com/tifulsoup
escuela_directa = bs4.BeautifulSoup(web.text, 'lxml')

# enlaces para el archivo csv
enlaces = escuela_directa.select('.label-name')

# extraer imagenes
imagenes = escuela_directa.select('img')
srcs = []
for img in imagenes:
    srcs.append(img['src'])
print(srcs)

d_img =[]
for src in srcs:
    # Decodificar en binario
    try:
        aux = rq.get(src)
    except:
        continue
    else:
        d_img.append(aux)

files = []
i = 0
for img in d_img:
    # Descargar las imagenes que cumplan las condiciones
    aux = open(f'src{i}.jpg', 'wb')
    aux.write(img.content)
    aux.close()
    i += 1

