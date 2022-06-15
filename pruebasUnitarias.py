import unittest
import busquedaArchivo
import pathlib
import os
from test import support

# Procesos complementarios para funciones que si valen probar
def procedimentales():
    # La dirección completa del archivo .py
    camino = pathlib.Path(__file__).parent.absolute()
    ruta = str(camino)
    return ruta

class TestMyModule(unittest.TestCase):
    '''
    Constara de 4 test
    ------------------
        test_todoDirectorio():
            Verificara el resultado al aplicar las funciones todoContenido y todoDirectorio
        
        test_listaArchivo():
            Verificara el resultado al aplicar las funciones listado_archivos
        
        test_todoUrl():
            Verificara el resultado al aplicar las funciones todoUrl
        
        test_arregloMaestro():
            Verificara el resultado al aplicar la función recursiva arreglo_maestro en las variables globales
        
    '''

    # Esta función es aplicable para los archivos, solo es cuestión de cambiar el metodo de enlistado
    def test_allDirectorio(self):
        ruta = procedimentales()
        contenido = busquedaArchivo.todoContenido(ruta)
        directorios = busquedaArchivo.todoDirectorios(ruta, contenido)
        self.assertEqual(type(directorios), type([])) # Se verifica que el tipo de respuesta sea igual a una lista
    
    # Esta función es aplicable para los directorios, solo es cuestión de cambiar el metodo de enlistado
    def test_listadoArchivo(self):
        ruta = procedimentales()
        contenido = busquedaArchivo.listado_archivos(ruta)
        self.assertEqual(len(contenido), 2) # Se verifica que el largo de la lista con respecto al contenido sea igual a 2

    def test_todoUrl(self):
        ruta = procedimentales()
        contenido = busquedaArchivo.todoUrl(ruta)
        self.assertEqual(len(contenido), 3) # Se asegura que el largo del conteido sea igual a 3

    def test_arregloMaestro(self):
        # VARIABLES GLOBALES
        ruta = procedimentales()
        arreglo_hero = busquedaArchivo.arreglo_hero
        busquedaArchivo.arreglo_maestro(ruta)
        result = True if len(arreglo_hero) > 0 else False
        self.assertIs(bool(result), True) # Verifica que el resultado sea verdadero para decir que la lista principal no esta vacia

if __name__ == "__main__":
    unittest.main()