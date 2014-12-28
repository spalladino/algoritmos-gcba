# Introduccion a python
# ---------------------
#
# Descomentar los distintos ejemplos al final de este archivo para ver la salida
# Ejecutar usando "python intro.py"

# Permite usar las funciones definidas en el archivo lineal.py
import lineal

# Testea la funcion busqueda lineal del archivo lineal.py,
# notar que se la debe invocar como lineal.busquedaLineal, 
# es decir, usando el nombre del archivo en la invocacion
def testBusquedaLineal():
    arreglo = ['A','B','C','D','E']

    print "Arreglo:", arreglo
    print "Buscando D:", lineal.busquedaLineal('D', arreglo)
    print "Buscando F:", lineal.busquedaLineal('F', arreglo)


# Ejemplo avanzado de listas por comprension
# No es necesario manejarlo, está aquí solo como curiosidad
def comprension():
    lista = range(10)
    print "Lista original:", lista
    print "Dobles:", [x*2 for x in lista]
    print "Pares:", [x for x in lista if x % 2 == 0]
    print "Dobles de mayores a 7:", [x*2 for x in lista if x > 7]    


# Distintas maneras de iterar una lista
def iterando():
    lista = ['A', 'B', 'C', 'D', 'E']

    print "Usando for each"
    for letra in lista:
        print letra

    print "Usando for sobre range"
    size = len(lista)
    for indice in range(size):
        print indice, lista[indice]
    
    print "Usando enumerate"    
    for indice, letra in enumerate(lista):
        print indice, letra

    print "Usando while con indice"        
    indice = 0
    while indice < len(lista):
        print indice, lista[indice]
        indice += 1
        

# Manipulacion de listas
def listas():
    lista = ['A', 'B', 'C', 'D', 'E']
    print "Lista:", lista
    print "Size:", len(lista)
    print "Segundo elemento:", lista[1]
    print "Ultimo elemento:", lista[-1]
 
    lista.append('F')
    print "Appendeado F:", lista
    
    lista.insert(1, 'AB')
    print "Insertado AB en 1:", lista


# Como usar la estructura de control if
def condicionales():
    print "Test condicionales: "
    valor = 10
    if valor > 10:
        print "Mayor"
    elif valor < 10:
        print "Menor"
    else:
        print "Igual"
        

# Descomentar las siguientes funciones para ver los distintos ejemplos:

#listas()
#condicionales()
#iterando()
#comprension()
