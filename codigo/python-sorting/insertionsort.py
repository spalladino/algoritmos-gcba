def sort(arreglo):
    for j in range(1, len(arreglo)):
        elem = arreglo[j]
        i = j - 1
        while (i >=0) and (arreglo[i] > elem):
            arreglo[i+1] = arreglo[i]
            i = i - 1
        arreglo[i+1] = elem
