# Version iterativa de la funcion busqueda binaria
# TAREA: Hacer la version recursiva
def busquedaBinaria(buscado, arreglo):
    desde = 0
    hasta = len(arreglo)-1
    while desde < hasta:
        medio = (desde + hasta) / 2
        if arreglo[medio] > buscado:
            hasta = medio -1
        elif arreglo[medio] < buscado:
            desde = medio+1
        else:
            return medio
    
    if arreglo[desde] == buscado:
        return desde
    else:
        return -1

# Esta linea hace que se ejecute el codigo solamente si se lo llama como python binaria.py
# y evita que se ejecute si se hace un import de este archivo
if __name__ == '__main__':
    arreglo = ['A','B','C','D','E']

    print "Arreglo:", arreglo
    print "Buscando D:", busquedaBinaria('D', arreglo)
    print "Buscando F:", busquedaBinaria('F', arreglo)

