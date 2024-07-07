"""
Este modulo permite el extraer datos relevantes de la url
"""

import bs4
import requests as rq



# url base, con format para obtener todas las url
url = ('https://books.toscrape.com/catalogue/page-{}.html')
libros_titulos = []
# Iteración para obtener todas las paginas disponibles
for n in range(1, 51):
    # cargamos pagina
    url_page = url.format(n)
    # obtener direccion
    aux = rq.get(url_page)
    # asignar objeto bs4
    page = bs4.BeautifulSoup(aux.text, 'lxml')
    # Obtenemos libro
    libros = page.select('.product_pod')

    for libro in libros:
        # Verificar que cumplan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            aux =libro.select('a')[1]['title']
            libros_titulos.append(aux)

for libro in libros_titulos:
    print(libro)



