# ALGORITMO DE BUSQUEDA DE ARCHIVOS EN UN SISTEMA DE DIRECOTRIOS, IMPLEMENTNADO NODOS
from operator import le
import pathlib
import os
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory
# Para archivos
from os.path import isfile, join, isdir

# La dirección completa del archivo .py
camino = pathlib.Path(__file__).parent.absolute()

# def camino():
#   return pathlib.Path(__file__).parent.absolute()
ruta = str(camino)

def isArchive(url):
  return os.path.split(url)
  
def isRuta(url, actual):
  return  url + actual

# FUnción para saber si se trata de un directorio o un archivo
# True: Directorio
# False: archivo
def isDirectorio(dato):
  res = dato.find('.')
  if res == -1:
    return True
  return False

def allContenido(url):
  return os.listdir(url)

def allDirectorios(url, contenido):
  return [nombre for nombre in contenido if isdir(join(url, nombre))]

def allArchivos(url, contenido):
  return [nombre for nombre in contenido if isfile(join(url, nombre))]

def listado_archivos(url):
  arr = allArchivos(url, allContenido(url))
  cantidad = len(arr)
  return [arr, cantidad]

def listado_directorios(url):
  arr = allDirectorios(url, allContenido(url))
  cantidad = len(arr)
  return [arr, cantidad]

# print(type(ruta))
# result = listado_directorios(ruta+'\casi')
# result = listado_archivos(ruta+'\casi')
# print(result)

def all(url):
  print('Entraste')
  listado = []
  contados = 0
  directorio = listado_directorios(url)
  archivo = listado_archivos(url)
  for dic in directorio[0]:
    listado.append(dic)
  for arc in archivo[0]:
    listado.append(arc)
  
  contados = directorio[1] + archivo[1]

  return [listado, directorio[0], directorio[1] , contados]

arreglo_hero = []

def arreglo_maestro(url):
  # lista_maestra = []
  todo = all(url)

  for parte in todo[0]:
    arreglo_hero.append(parte)

  index = 0
  print(todo[1])
  for par in todo[1]:
    if(index == 0):
      url = isRuta(url, f'\{par}')
      arreglo_maestro(url)
      # listado = all(url)
      # for li in listado[0]:
      #   arreglo_hero.append(li)
    else:
      new = isArchive(url)
      url = new[0]
      url = isRuta(url, f'\{par}')
      arreglo_maestro(url)
      # listado = all(url)
      # for li in listado[0]:
      #   arreglo_hero.append(li)
    index = index + 1
  


arreglo_maestro(ruta)

print(arreglo_hero)

nodoInicial = camino.name 
num = 0
nodos = {num: nodoInicial}
for nodo in arreglo_hero:
  num = num + 1
  nodos[num]= nodo
print(nodos)


