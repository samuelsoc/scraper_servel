"""
autor: samuelrg

Recolección votaciones 2da vuelta.
Datos preliminares sitio web del Servel.
Por defecto, al entrar al sitio, entra a la info de la 2da vuelta
"""


import time
from time import sleep
import random
import pandas as pd
from datetime import datetime
import re
import sys
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')

# sin navegador
#web = webdriver.Firefox(firefox_options=options)

# para ver con navegador
web = webdriver.Firefox()
web.get("https://www.servelelecciones.cl/")

time.sleep(2)
#
# seleccionar Elecciones Gobernadores 2da vuelta
gobernadores = web.find_element_by_css_selector('li.hidden-xs:nth-child(1) > a:nth-child(1)')
gobernadores.click()
time.sleep(1.5)
# click en regiones
region = web.find_element_by_css_selector('#selRegion')
region.click()
# seleccionar opciones del elemento menu "region"
nom_reg = Select(region)
time.sleep(1.5)
# Seleccionar Region para extraer info
RM = nom_reg.select_by_visible_text('METROPOLITANA DE SANTIAGO')
time.sleep(1.5)

# Entrar a menu Comunas
comuna = web.find_element_by_css_selector('#selComunas')
comuna.click()
time.sleep(1)
comuna1 = Select(comuna)
comuna2 = comuna1.options

# crear lista con los nombres de comunas que contiene el menu
comunas = []
for i in comuna2:
    comunas.append(i.text)

# items de la lista para ser omitidos
del_comunas = {'Comunas...'}
# eliminar elementos
comunas = [ele for ele in comunas if ele not in del_comunas]

# recorrer lista de comunas

data = []

for comuna in comunas:
    # entrar a cada comuna
    comuna1.select_by_visible_text(comuna)
    time.sleep(1.5)
    tabla = web.find_element_by_css_selector('.table')

    lista_pacto = []
    partido = []
    votos = []
    porcentaje = []
    electo = []
    time.sleep(1.5)

    # valores columna pactos
    lista1 = tabla.find_elements_by_css_selector('td:nth-of-type(1) span')
    for i in lista1:
        lista_pacto.append(i.text)
    # valores columna partidos
    lista1b = tabla.find_elements_by_css_selector('td.aligLeft:nth-of-type(2)')
    for i in lista1b:
        partido.append(i.text)

    # valores columna votos
    lista2 = tabla.find_elements_by_css_selector('td:nth-of-type(3) span')
    for i in lista2:
        votos.append(i.text)

    # valores columna porcentaje
    lista3 = tabla.find_elements_by_css_selector('td:nth-of-type(4) span')
    for i in lista3:
        porcentaje.append(i.text)

    # valores columna electos
    lista5 = tabla.find_elements_by_css_selector('td:nth-of-type(6) span')
    for i in lista5:
        electo.append(i.text)
    # crear dataframe con lista recolectadas

    df = pd.DataFrame({'Pacto/Lista': lista_pacto,
                       'Partido':partido,
                       'Votos':votos,
                       'Porcentaje':porcentaje,
                       'Electos':electo,
                       'Comuna':comuna})

    data.append(df)

    print(f'Comuna: {comuna} recolectada.')
    print(df)

df2 = pd.concat(data)
df2.to_csv(f'votos_gobernadores_RM_v2.csv')

############################################

print(f'Fin de la recolección a las {time.ctime()}')

#### CLOSE ####
web.quit()
