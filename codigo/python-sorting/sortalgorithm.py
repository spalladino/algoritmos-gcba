import threading

# Clase para ejecutar un algoritmo dentro de un thread
class SortAlgorithm(threading.Thread):
    
    StatusNormal = 'normal'
    StatusWritten = 'write'
    StatusCmp = 'cmp'
    StatusSuccess = 'success'
    StatusFail = 'fail'
    
    # Notifies whenever set
    class NotifyingArray:

        # Notifies whenever compared
        class NotifyingItem(int):
            def __new__(cls, value, index, listener):
                obj = int.__new__(cls, value)
                obj.index = index
                obj.listener = listener
                return obj
                
            def __cmp__(self, other):
                self.listener.compared(self, other)
                return int.__cmp__(self, other)

        # Constructor
        def __init__(self, data, listener):
            self.data = [self.NotifyingItem(value, index, listener) for index,value in enumerate(data)]
            self.listener = listener

        # Overload []
        def __getitem__(self, index):
            return self.data[index]

        # Overload set []
        def __setitem__(self, key, item):
            item.index = key
            self.data[key] = item
            self.listener.item_set(key)

        # Return size to len()
        def __len__(self):
            return len(self.data)

        # String representation of data
        def __repr__(self):
            return repr(self.data)
            
    
    def __init__(self, algorithm, array, event, name="Algorithm"):
        threading.Thread.__init__(self)
        self.setDaemon(True)        

        self.algorithm = algorithm
        self.array = self.NotifyingArray(array, self)
        self.demo_event = event
        self.name = name
        
        self.event = threading.Event()
        self.clear_statuses()
        self.executing = False
        self.complete = False
        
        self.comparisons = 0
        self.assignments = 0

    # Ejecuta el algoritmo
    def run(self):
        self.executing = True
        self.algorithm(self.array)

        self.complete = True
        is_sorted = True
        for item1,item2 in zip(self.array[:-1], self.array[1:]):
            if item1 > item2:
                is_sorted = False
            
        self.statuses = [self.StatusSuccess if is_sorted else self.StatusFail for i in self.array]       
        self.event.set()
        print "Completado %s" % self.name
        
        
    # Marca ese item como escrito, frena el event y espera        
    def item_set(self, index):
        if not self.executing or self.complete: return
        self.statuses[index] = self.StatusWritten
        self.assignments += 1
        self.wait_for_draw()

        
    # Marca los dos items comparados
    def compared(self, one, two):
        if not self.executing or self.complete: return
        self.statuses[one.index] = self.StatusCmp
        self.statuses[two.index] = self.StatusCmp
        self.comparisons += 1
        self.wait_for_draw()

        
    # Limpia statuses anteriores
    def clear_statuses(self):
        self.statuses = [self.StatusNormal for i in self.array]
        
    
    # Metodo a llamar desde afuera, bloquea hasta q ejecute una iteracion
    def wait_for_execute_iteration(self):
        if not self.complete:
            self.event.wait()
            self.event.clear()
            
        
    # Bloquea hasta que el main loop haya dibujado
    def wait_for_draw(self):
        self.executing = False
        self.event.set()
        self.demo_event.clear()
        self.demo_event.wait()
        self.executing = True
        self.clear_statuses()

