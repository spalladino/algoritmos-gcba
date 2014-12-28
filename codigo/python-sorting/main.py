import random
from sortdemo import SortDemo

# Importo los archivos con las funciones a comparar
import insertionsort
import selectionsort
import bubblesort
import quicksort

# Cuantos elementos tiene cada arreglo?
cant_elementos = 30

# Cuanto puede valer a lo sumo a cada elemento del arreglo?
max_elemento = 100

# Creo el arreglo a ordenar
array = [random.randrange(1, max_elemento) for i in range(cant_elementos)]

# Creo la lista de algoritmos que quiero comparar
algoritmos = [
    (insertionsort.sort, "Insertion", array),
    (selectionsort.sort, "Selection", array),
    (bubblesort.sort,    "Bubble",    array),
    (quicksort.sort,     "Quicksort", array),
]

# Arranco la demo con la lista de algoritmos y los parametros:
# fps = frames per second, o cuantas acciones se hacen por segundo
# ancho = ancho en pixeles de la visualizacion de cada algoritmo
# alto = alto en pixeles de la visualizacion de cada algoritmo    
SortDemo(algoritmos, fps = 30, ancho = 280, alto = 400)
