# ALGORITMO DE BUSQUEDA DE ARCHIVOS EN UN SISTEMA DE DIRECOTRIOS, IMPLEMENTNADO NODOS
import pathlib
import os
camino = pathlib.Path(__file__).parent.absolute()
print(camino.name) # Obtiene el nombre de su directorio
print(camino.parent)

for base, dirs, files in os.walk(camino):
  print(dirs)

