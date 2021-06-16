# Scraper Basico Servel

Este código se basa en otro mas profundo que desarrolle en mi trabajo, para extraer los votos de cada mesa en la RM. Si bien éste es mucho mas breve, puede ser adaptado y usado como referente.

### Requisitos

En mi caso, el SO es Debian 10, tengo un enviroment con las librerias necesarias, para este código serían:

- Python 3.8
- Selenium
- Geckodriver
- Pandas

También corre en Windows.

Recomiendo guardar el driver en la misma carpeta que dejen el código, y la última versión de Firefox.

### Descripción

Con este script es posible recolectar, desde el sitio web del SERVEL, los resultados preliminares de las votaciones, por comuna, en la segunda vuelta de Gobernadores año 2021.

El resultado es un archivo csv que contiene las mismas columnas visibles en el portal, más una columna que indica la comuna correspondiente.

El código puede ser adaptado para otras regiones, desde el mismo código o agregando un parámetro.
