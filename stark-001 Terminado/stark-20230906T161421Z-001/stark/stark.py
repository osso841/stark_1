from funciones import *
from data_stark import lista_personajes
from copy import deepcopy

lista_personaje_normalizado = deepcopy(lista_personajes)
normalizar_lista(lista_personaje_normalizado)

comenzar_consulta_stark(lista_personaje_normalizado)