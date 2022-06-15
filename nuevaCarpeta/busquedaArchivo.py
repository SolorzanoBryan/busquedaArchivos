# ALGORITMO DE BUSQUEDA DE ARCHIVOS EN UN SISTEMA DE DIRECOTRIOS, IMPLEMENTNADO NODOS
from operator import le
import pathlib
import os
# from tkinter import Tk, Tcl
# from tkinter.filedialog import askdirectory
# Para archivos
from os.path import isfile, join, isdir

# La dirección completa del archivo .py
camino = pathlib.Path(__file__).parent.absolute()

# def camino():
#   return pathlib.Path(__file__).parent.absolute()
ruta = str(camino)

def elArchivo(url):
  return os.path.split(url) # Devuelve una tupla, el primer elemento es todo lo que viene antes del elementos actual y en sgunda posición seria el componente de la ruta. 
  
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

def todoUrl(url):
  listado = []
  directorio = listado_directorios(url)
  archivo = listado_archivos(url)
  for dic in directorio[0]:
    listado.append(dic)
  for arc in archivo[0]:
    listado.append(arc)

  actual = elArchivo(url)
  return [listado, directorio[0], directorio[1] , archivo[1], actual[1]]

arreglo_hero = []
arreglo_dic = []
arreglo_arc = []
comienzos = []
objetivos = []

def arreglo_maestro(url):
  todo = todoUrl(url)
  comienzos.append(todo[4])
  objetivos.append(todo[0])
  arreglo_dic.append([todo[2]])
  arreglo_arc.append([todo[3]])

  for parte in todo[0]:
    arreglo_hero.append(parte)

  index = 0
  # print(todo[1])
  for par in todo[1]:
    if(index == 0):
      url = isRuta(url, f'\{par}')
      arreglo_maestro(url)
    else:
      new = elArchivo(url)
      url = new[0]
      url = isRuta(url, f'\{par}')
      arreglo_maestro(url)
    index = index + 1

arreglo_maestro(ruta)

# print(arreglo_hero)



nodoInicial = camino.name 
num = 0
nodos = {num: nodoInicial}
for nodo in arreglo_hero:
  num = num + 1
  nodos[num]= nodo

num = 0
nodosInvertidos = {nodoInicial: num}
for nodo in arreglo_hero:
  num = num + 1
  nodosInvertidos[nodo]= num

# print('NODOS', nodos)
# print('NODOS INVERTIDOS',nodosInvertidos)

# print('Comienzos', comienzos)
# print('objetivos', objetivos)
# print('.................')
# print(arreglo_dic)
# print(arreglo_arc)

class Grafo:

  def __init__(self, numero_nodos, dirigido=True):
    # Atributos
    self.g_numeros_nodos = numero_nodos 
    self.g_nodos = range(self.g_numeros_nodos) 
    self.g_dirigido = dirigido 
    self.g_adjuntar_lista = {nodo: set() for nodo in self.g_nodos} 
  
  def agregar_borde(self, nodo1, nodo2, peso=1):
    self.g_adjuntar_lista[nodo1].add((nodo2, peso)) 
    if not self.g_dirigido: 
      self.g_adjuntar_lista[nodo2].add((nodo1, peso)) 
    
  # Imprimir lista de nodos
  def imprimir_adjuntar_lista(self): 
    for clave in self.g_adjuntar_lista.keys(): # 
      print(f'nodo{clave}: {self.g_adjuntar_lista[clave]}') 

  def busqueda_profundidad(self, inicio, objetivo, camino = [], visitado = set()):
    camino.append(inicio) # Añade el nodo a la lista
    visitado.add(inicio) # Seta el nodo como visitado
    # print(visitado)
    # print(camino)
        # print(camino)
    if inicio == objetivo: # D eser verdadero no hay para que hacer la busqueda 
        return camino
    for (puerto, peso) in self.g_adjuntar_lista[inicio]:
        if puerto not in visitado:
            resultado = self.busqueda_profundidad(puerto, objetivo, camino, visitado) # Recursividad
            if resultado is not None:
                return resultado
    camino.pop()
    return None  

if __name__ == "__main__": 
  cantidad = len(nodos.keys())
  grafo = Grafo(cantidad, dirigido=True)
  count = 0
  for directo in comienzos:
    prin = nodosInvertidos.get(directo)
    # print(prin)
    arr_obj = objetivos[count]
    for puerto in arr_obj:
      sec = nodosInvertidos.get(puerto)
      # print(sec)
      grafo.agregar_borde(prin, sec)
    count = count + 1

  grafo.imprimir_adjuntar_lista()

  ruta = []
  buscar = input('Ingrese su archivo o docuemnto a buscar: ')
  objetivo = nodosInvertidos.get(buscar)
  ruta = grafo.busqueda_profundidad(0, objetivo)
  print(f" La ruta transversal del nodo 0 al nodo 3 es {ruta}")

  new_ruta = []
  for plox in ruta:
    new_ruta.append(nodos.get(plox))
  print(f" La ruta transversal del nodo 0 al nodo 3 es {new_ruta}")


