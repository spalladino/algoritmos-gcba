def sort(arreglo):
    for i in range(0,len(arreglo)):
	    for j in range(len(arreglo)-1,i,-1):
		    if arreglo[j] < arreglo[j-1]:
			    arreglo[j], arreglo[j-1] = arreglo[j-1], arreglo[j]

