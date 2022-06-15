# ALGORITMO DE BUSQUEDA DE ARCHIVOS EN UN SISTEMA DE DIRECOTRIOS, IMPLEMENTNADO NODOS
from operator import le
import pathlib
import os
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory
# Para archivos
from os.path import isfile, join, isdir

# La dirección completa del archivo .py - Proceso detemrinante
camino = pathlib.Path(__file__).parent.absolute()
ruta = str(camino) # Transformación del camino en una ruta legible para otros procesos

'''
VARIABLES GRLOBALES
-------------------
  arreglo_hero (lista): Arreglo el cual servira para crear el diccionario de lso nodos y nodoInvertidos
  comienzos (lista): Seria el nombre cabecilla del direcotrio y esta relacionado al espacio en la lista de objetivos
  objetivos (lista): Sera todo el contenido del nombre cabecilla añadido a la lista comienzos
'''
arreglo_hero = []
comienzos = []
objetivos = []

def elArchivo(url):
  '''
  Parametros
  ----------
    La URL o ruta estipulada para xomenzar con el rpoceso de analsiis de su contenido
  
  Retorna
  -------
    Devuelve una tupla, el primer elemento es todo lo que viene antes del elementos actual y en sgunda posición seria el componente de la ruta.
  '''
  return os.path.split(url)  # Metodo propio de la libreria os
  
def nuevaRuta(url, actual):
  '''
  Parametros
  ----------
    url (str): Esta ruta es la base para ua nueva ruta
    actual (str): Va despues de la ruta pasada por parametro

  Retorna
  -------
    La conversión entre la ruta y la psición actual, formando la ruta definitiva para proceder con la secuencia de procesos
  '''
  return  url + actual

def todoContenido(url):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os

  Retorna
  -------
    Devuelve una lista de todos los direcotrios y archivos contenidos dentro de la ruta especificada, sino se le pasa ese dato como parametro tomara como referencia la ruta actual
  '''
  return os.listdir(url)

def todoDirectorios(url, contenido):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os
    contenido (lista): Contendra todo los directorios y archivos contenidos en la ruta

  Retorna
  -------
    Un arreglo creado a partir de isdir(join())
      isdir() : Verifica que si la ruta especificada es un direcotrio existencia, devuelve True
      join() : Nos ayuda a concatenar compoenetes de direcotirios con un separador ('/')
      Observación:  Esto es necesario devido a que el contenido peude estar mezclado con archivos y directorios
  '''
  return [nombre for nombre in contenido if isdir(join(url, nombre))]

def todoArchivos(url, contenido):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os
    contenido (lista): Contendra todo los directorios y archivos contenidos en la ruta

  Retorna
  -------
    Un arreglo creado a partir de isdir(join())
      isdir() : Verifica que si la ruta especificada existen archivos que considerar, devuelve True
      join() : Nos ayuda a concatenar compoenetes de direcotirios con un separador ('/')
      Observación:  Esto es necesario devido a que el contenido peude estar mezclado con archivos y directorios
  '''
  return [nombre for nombre in contenido if isfile(join(url, nombre))]

def listado_archivos(url):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os

  Variable Interna
  ----------------
    arr (lista): Alamacena lo devuelto por allArchivo, que basicamente es donde se considera unicamente los archivos de esa ruta 
    cantidad (int): Por motivos de logica aplicables en un proceso se necesita pasar la cantidad de archivos contneidos en esa ruta
  Retorna
  -------
    Una lista que tiene como primera sentencia al arreglo de archivos y en segundo logar la cantidad de esos documentos
  '''
  arr = todoArchivos(url, todoContenido(url))
  cantidad = len(arr)
  return [arr, cantidad]

def listado_directorios(url):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os

  Variable Interna
  ----------------
    arr (lista): Alamacena lo devuelto por todoDirectorios, que basicamente es donde se considera unicamente a los directorios de esa ruta 
    cantidad (int): Por motivos de logica aplicables en un proceso se necesita pasar la cantidad de archivos contneidos en esa ruta
  Retorna
  -------
    Una lista que tiene como primera sentencia al arreglo de archivos y en segundo logar la cantidad de esos documentos
  '''
  arr = todoDirectorios(url, todoContenido(url))
  cantidad = len(arr)
  return [arr, cantidad]

def todoUrl(url):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os
  
  Varaibles internas
  ------------------
    listado (lista): Almacenara tanto los elementos de los direcotorios y archivos considerando las funciones de enlistado
    directorio (lista): Almacenara la lista en la cual se contempla a esos direcotrios ubicados dentro de la ruta establecida
    archivo (lista): Almacenara la lista en la cual se contempla a esos archivos ubicados dentro de la ruta establecida
    actual (tupla): Almacenara la tupka devuelta por la función elArchivo, esta evidenciara el contenido de esa ruta
  
  Desarrollo
  ----------
    Se aplica el llamado a funciones  la implementaicón de procesos ciclicos para ir registrando los datos
  
  Retorna
  -------
    Ina lista que contiene el listado de todos los elementos cotemplados en una ruta como primera posicón
    En segunda posición devuelve la lista de direcotrios existentes
    En la tercera posición devuelve la lista de los archivos 
    
  '''
  listado = []
  directorio = listado_directorios(url)
  archivo = listado_archivos(url)
  for dic in directorio[0]:
    listado.append(dic)
  for arc in archivo[0]:
    listado.append(arc)

  actual = elArchivo(url)
  return [listado, directorio[0], actual[1]]

def arreglo_maestro(url):
  '''
  Parametros
  ----------
    url (str): es la ruta actual donde se ejecutara uno de los metodos propiso de os
  
  Varaibles internas
  ------------------
    todo (lista): Almacenara en una lista todos los elementos retornados por la función todoUrl() 
    comienzos (lista): Aplica desestructuración para lograr capturar el como fueron apareciendo los directorios
    objetivos (lista): Aplica desestructuración para lograr capturar el como fueron apareciendo los archivos
  
  Desarrollo
  ----------
    Se aplica un ciclo para contemplar un registro de todo el listado contmeplado en primera instancia de la variable todo
    Inicializar un contador 'index'
    Comenzar estructura ciclica evaluando lso direcotrios y avanzar segun condicional para una nueva ruta y nuevo llamado a recursividad
    De caso contrario se optiene el nuevo posiconamiento para evalizar una nueva ruta y vovler aplicar la recursividad
    Estos llamados se temrinan al contemplar todos los direcotrios padres por así decirlo 
  '''
  todo = todoUrl(url)
  comienzos.append(todo[2])
  objetivos.append(todo[0])

  for parte in todo[0]:
    arreglo_hero.append(parte)

  index = 0
  for par in todo[1]:
    if(index == 0):
      url = nuevaRuta(url, f'\{par}')
      arreglo_maestro(url)
    else:
      new = elArchivo(url)
      url = new[0]
      url = nuevaRuta(url, f'\{par}')
      arreglo_maestro(url)
    index = index + 1


class Grafo:
    """
    Una clase que representa a un grafo.

    ...
    
    Argumentos
    ----------
    num_nodos: entero
        Es usado para determinar el número de nodos.
    dirigido: booleano
        Determina si el nodo es dirigido. Valor por defecto "Verdadero".

    Atributos
    ---------
    matriz_num_nodos : entero
        Número de nodos en el grafo.
    matriz_nodos : entero
        Clave del nodo generado.
    matriz_dirigido : booleano
        Determina si el nodo es dirigido.
    matriz_lista_adyacencia: diccionario
        Almacena los nodos como  un conjunto no ordenado de pares clave-valor.

    Métodos
    -------
    agregar_arista(self, nodo1, nodo2, peso=1):
        Agrega una arista o arco entre dos nodos a la representación del grafo.

    imprimir_lista_adyacencia(self):
        Imprime la lista de adyacencia como representación del grafo.

    bpp(self, nodo_inicial):
        Imprime el recorrido del algoritmo de búsqueda por profunidad desde un nodo dado hasta un nodo objetivo.
    """
    # Se establece el constructor de la clase
    def __init__(self, num_nodos, dirigido=True):
        """
        Contructor con todos los atributos necesarios para la clase grafo.

        Parámetros
        ----------
        matriz_num_nodos : entero
            Número de nodos en el grafo.
        matriz_nodos : entero
            Clave del nodo generado.
        matriz_dirigido : booleano
            Determina si el nodo es dirigido.
        matriz_lista_adyacencia: diccionario
            Almacena los nodos como  un conjunto no ordenado de pares clave-valor.
        """
        # Se inicializan los atributos de la clase
        # Atributo: número de nodos
        self.matriz_num_nodos = num_nodos
        # Se establece que el nodo debe estar en el rango permitido
        self.matriz_nodos = range(self.matriz_num_nodos)
        # Atributo: dirigido. Por defecto "Verdadero"
        self.matriz_dirigido = dirigido
        #Representación gráfica con una lista de adyacencia
        #Se genera un diccionario y se settea todos los nodos con un ciclo repetitivo "para"
        self.matriz_lista_adyacencia = {nodo: set() for nodo in self.matriz_nodos}    
         
    #  Función que agrega una arista o arco entre dos nodos a la representación del grafo
    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega una arista o arco entre dos nodos a la representación del grafo.

        El último argumento, peso, tiene como valor asignado 1.

        Parámetros
        ----------
        nodo1 : entero
            Almacena el valor para el primer nodo.
        nodo2 : entero
            Almacena el valor para el segundo nodo.
        nodo1 : entero
            Almacena el peso de los arcos, línea que une los nodos. Valor por defecto 1. 

        Retorna
        -------
        A un index del diccionario establecido, matriz_lista_adyacencio[clave], se le 
        añadirá su nodo adyacente, nodo# y el peso. 
        """
        # Añade una arista del nodo 1 al 2 con peso por defecto 1
        self.matriz_lista_adyacencia[nodo1].add((nodo2, peso))
        # Si la matriz no es dirigida, añade una arista del nodo 2 al 1 con peso por defecto 1
        if not self.matriz_dirigido:
            self.matriz_lista_adyacencia[nodo2].add((nodo1, peso))
   
    # Función que imprime la lista de adyacencia
    def imprimir_lista_adyacencia(self):
        """
        Imprime la lista de adyacencia como representación del grafo.

        Parámetros
        ----------
        Ninguno

        Retorna
        -------
        Una cadena de texto con la matriz de adyacencia generada.
        """
        for key in self.matriz_lista_adyacencia.keys():
            print("node", key, ": ", self.matriz_lista_adyacencia[key])
 
    # Función que imprime el recorrido de la busqueda por anchura de un vértice fuente dado.
    def bpp(self, nodo_inicial, nodo_objetivo, camino = [], visitado = set()):
        """
        Imprime el recorrido del algoritmo de búsqueda por profunidad desde un nodo dado hasta un nodo objetivo.

        Parámetros
        ----------
        nodo_inicial : entero
            Representa al nodo raíz del grafo generado.
        nodo_objetivo : entero
            Representa al nodo objetivo a encontrar en grafo generado.
        camino : lista
            Almacena el camino requerido para llegar al objetivo en caso de existir.
        visitado : colección
            Almacena los nodos que han sido visitados.

        Retorna
        -------
        Una lista del camino generado desde un nodo origen hasta el nodo objetivo.
        """
        # Se inicializa la lista añdiendo el nodo inicial al camino
        camino.append(nodo_inicial)
        # Se marca como visitado al nodo inicial
        visitado.add(nodo_inicial)
        # Si el nodo inicial es igual que le nodo objetivo retorna el camino como respuesta
        if nodo_inicial == nodo_objetivo:
            return camino
        # Recorrer cada nodo vecino, con su peso, presentes en la lista de adyacencia con la clave nodo incial 
        for(vecino, peso) in self.matriz_lista_adyacencia[nodo_inicial]:
            # Si el nodo adyacente encontrado no ha sido visitado
            if vecino not in visitado:
                # Se genera la recursividad del algoritmo bpp
                # con el nuevo nodo descubierto 
                resultado = self.bpp(vecino, nodo_objetivo, camino, visitado)
                # Si el nodo adyacente del nodo descubierto no existe retorna el camino y continúa con la otra rama del grafo.
                if resultado is not None:
                    return resultado
        # Retorna el último elemento de la pila y la presenta
        camino.pop()
        # No retorna nada
        return None

# PARA LA EJECUCIÓN
if __name__ == "__main__": 

  # Ejecución del arreglo_maestro
  arreglo_maestro(ruta)


  # Inicio del proceso: Creación de lso diccionarios compuesots por lso nodos
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
  
  # Fin del proceso: Creación de lso diccionarios compuesots por lso nodos
  
  # Instanciar un grafo con una cantidad de nodos de forma automatica
  cantidad = len(nodos.keys())
  grafo = Grafo(cantidad, dirigido=True
  )
  count = 0
  # Proceso para la agregación de todos los nodos en el grafo
  for directo in comienzos:
    prin = nodosInvertidos.get(directo)
    # print(prin)
    arr_obj = objetivos[count]
    for puerto in arr_obj:
      sec = nodosInvertidos.get(puerto)
      # print(sec)
      grafo.agregar_arista(prin, sec)
    count = count + 1

  # Imprimir el grafo para una mejor perspectiva 
  grafo.imprimir_lista_adyacencia()

  ruta = []
  print('GRAFO 1')
  buscar = input('Ingrese su archivo o docuemnto a buscar: ')
  objetivo = nodosInvertidos.get(buscar)
  # print(objetivo)
  ruta = grafo.bpp(0, objetivo)

  if ruta != None:  
    print(f" La ruta transversal del nodo 0 al nodo 3 es {ruta}")
    new_ruta = []
    for plox in ruta:
      new_ruta.append(nodos.get(plox))
    print(f" La ruta transversal del nodo 0 al nodo 3 es {new_ruta}")
  else:
    print(f"El nombre del archivo no coincide en este sistema de directorio")


