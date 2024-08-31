class nodo:  # El nodito
    def __init__(self, dato, siguiente=None):
        self.dato = dato  # Datos
        self.siguiente = siguiente  # apuntadores
        #self.anterior = anterior

class listita:  # La listita para las filas
    def __init__(self, inicio=None, fin=None, tamaño=0):  # El constructor de la lista
        self.inicio = inicio
        self.fin = fin
        self.tamaño = tamaño

    def agregar(self, dato):  # Función para agregar un nodo a la lista
        nuevo = nodo(dato)  # Creo el nodo con la información y el estado
        if self.tamaño == 0:  # si no hay nada, el inicio es igual al nuevo nodo
            self.inicio = nuevo
            self.fin = nuevo  # Igual que el final porque solo hay uno
            self.tamaño += 1  # Y el tamaño de la lista sería 1
            nuevo.siguiente=nuevo
            #nuevo.anterior=nuevo
        else:
            """aux = self.inicio #Lo comento porque antes lo había hecho como lista doblemente enlazada
            while (
                aux.siguiente != self.inicio
            ):  # Si el siguiente no está vacío, osea que no es el último
                aux = aux.siguiente  # Avanzo al siguiente
            aux.siguiente = nuevo  # Ya en el lugar, lo coloco en su posición de nuevo"""
            nuevo.siguiente = self.inicio
            self.fin.siguiente = nuevo
            self.fin = nuevo
            self.tamaño += 1  # aumento el tamaño

    def mostrando(self):  # La verdad no sirve para nada pero me gusta verlo :)
        aux = self.inicio
        """while aux != self.fin: #Todo lo comentado es por ese pasado oscuro del código :(
            print(aux.dato)
            aux = aux.siguiente"""
        while True:
            print(aux.dato)
            aux = aux.siguiente
            if aux==self.inicio:
                break

    def modificar(self, pos, dato):  # Para modificar un dato en una posición indicada
        aux = self.inicio
        cont = 0
        while cont < pos:  # Llegando a la posición indicada
            aux = aux.siguiente
            cont += 1
        aux.dato = dato

    def encontrar(self, pos):  # Función para encontrar un dato en una posición indicada
        aux = self.inicio
        cont = 0
        while cont < pos:  # Solo me regresa el nodo a partir de la posición indicada
            aux = aux.siguiente  # Aquí llego a la posición
            cont += 1
        return aux.dato  # Retorno el nodo que deseo
    
    def concatenarF(self): #Función para que la fila sea una sola línea
        aux = self.inicio
        cadena = ""
        while aux != self.fin:
            cadena += str(aux.dato) #proceso de concatenación por cada elemento de la fila
            aux = aux.siguiente
            if aux==self.inicio:
                break
        return cadena
    
    def eliminar(self, pos):
        if pos==0:
            self.inicio=self.inicio.siguiente #Solo inicio es igual a su siguiente (borrando el primero)
            self.fin.siguiente=self.inicio #Ahora el siguiente del final es el nuevo inicio
        else:
            aux = self.inicio
            cont = 0
            while cont < pos-1: #Ubico la posición con menos 1 porque necesito modificar el anterior al que quiero borrar
                aux = aux.siguiente
                cont += 1
            aux.siguiente = aux.siguiente.siguiente #Aquí hago que el anterior (-1) apunte al siguiente (+1) de la posición actual (0)
        self.tamaño -= 1

        """aux = self.inicio
        cont = 0
        while cont < pos: # Ubico donde quiero borrar el nodo
            aux = aux.siguiente
            cont += 1
        if aux == self.inicio:
            aux.siguiente.anterior = self.fin
            self.inicio=aux.siguiente #el inicio será el siguiente al actual
        elif aux == self.fin:
            aux.anterior.siguiente = self.inicio
            self.fin=aux.anterior
        else:
            aux.anterior.siguiente = aux.siguiente #el anterior tendrá como siguiente el siguiente al actual
            aux.siguiente.anterior = aux.anterior
        self.tamaño -= 1 #Reduzco el tamaño de la lista"""


class matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n  # cantidad de filas
        self.m = m  # cantidad de columnas
        self.filas = listita()  # lista de filas
        relleno = 2023  # Es para rellenar la matriz con algo que sea entero
        contadorn = 0
        while contadorn < n:
            contadorm = 0
            miami = listita() # lista de columnas
            while contadorm < m: 
                miami.agregar(relleno) # Aquí se rellena agrega una celda a la columna
                contadorm += 1 #Hasta que se tiene toda la columna de nodos
            self.filas.agregar(miami) # Aquí se rellena la fila con la columna
            contadorn += 1 # Hasta que termine de tener todas las filas deseadas :)

    def mostrar(self):  # Solo está hecha para ver si lo hice bien (no sirve para nada más)
        contadoro = 0
        while contadoro < self.n: 
            contadori = 0
            print("Fila: ", contadoro + 1)
            while contadori < self.m:
                print(self.filas.encontrar(contadoro).encontrar(contadori))
                contadori += 1
            contadoro += 1

    def encontrar(self, x, y): #Encuentra el dato en la posición indicada
        return self.filas.encontrar(x).encontrar(y) 

    def modificar(self, x, y, dato): #Modifica el dato en la posición indicada
        self.filas.encontrar(x).modificar(y, dato) 

    def encontrarF(self, x): #Encuentra la fila en la posición indicada
        return self.filas.encontrar(x) 
    
    def encontrarC(self, y): #Encuentra la columna en la posición indicada
        return self.columnas.encontrar(y) 

    def sumaModificaEliminaF(self,pos1, pos2): #Suma las filas pos1 y pos2 y lo coloca en la fila pos1
        contador=0

        while contador<self.m: #Recorre toda la fila y va sumando los elementos de las dos filas en las posiciones indicadas
            luis=self.encontrarF(pos1).encontrar(contador)
            fonsi=self.encontrarF(pos2).encontrar(contador)
            luisfonsi=luis+fonsi #guardando la suma de los dos valores
            self.encontrarF(pos1).modificar(contador,luisfonsi) #modificando la fila en la posición indicada---------------------------------------------------------------
            #self.modificar(x,contador,luisfonsi) #Es una opción alternativa que se quedará por cualquier coas :)
            contador+=1
        self.filas.eliminar(pos2) #Eliminando la fila que se sumó
        self.n-=1 #bajando la cantidad de filas



