import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

def download_pubmed (keyword):
    """
    Funcion que entrada pide al usuario la keyword tipo str y en output guarda un archivo que contiene los resultados de la 
    busqueda en base a los titulos/resumen. 
    """ 
    Entrez.email = "slendy.alvarado@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term=keyword+"[Title/Abstract]",
                        retmax = 1000,
                        usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text",  
                       webenv=webenv,
                       query_key=query_key)
    out_handle = open("data/"+keyword, "w")
    data = handle.read()
    (id_list)
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list 

import re 
import csv 
import matplotlib.pyplot as plt
from collections import Counter

def science_plots(data):
    """
    Funcion que pide como entrada la data de la funcion download_pubmeds y como resultado muestra un grafico tipo pastel 
    indicando a los cinco paises que aparecieron mas veces  . 
    """ 
    with open("data/"+data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    ## expresion regular para la busqueda de la nacionalidad de los autores 
    pais = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    conteo=Counter(pais)
    resultado={}
    ## En este bucle agregamos los paises y la frecuencia que se repite 
    for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ordenar = (sorted(resultado.values()))## ordena de forma ascendente 
    ordenar.sort(reverse=True) ##ordena a los cinco primeros paises con mayor frecuencia
    import operator
    ## creamos dos listas que contendra a los paises y frecuencias 
    countries = [] 
    counter = []
    
    ## bucle que añade los valores pais y frecuencia a la listas vacias pais y contador 
    reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        countries.append(name[1][0])
        counter.append(resultado[name[1][0]])
    mas_pais = countries[0:5] ## seleccionamos los cinco primeros paises 
    mas_frec = counter[0:5] ## seleccionamos las cinco primero frecuencia respecto a los paises 
    fig = plt.figure(figsize =(10, 7))
    plt.pie(mas_frec, labels = mas_pais)
    (plt.savefig("img/"+data, dpi=120, bbox_inches='tight'))
    plt.show()
    


