# Busqueda secuencial de un elemento en un arreglo
def busquedaLineal(buscado, arreglo):
    for i, elemento in enumerate(arreglo):
        if elemento == buscado:
            return i
    return -1
        
