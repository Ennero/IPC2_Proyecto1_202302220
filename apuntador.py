class nodo:  # El nodito
    def __init__(self, dato, siguiente=None, anterior=None):
        self.dato = dato  # Datos
        self.siguiente = siguiente  # apuntadores
        self.anterior = anterior


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
        else:
            aux = self.inicio
            while (
                aux.siguiente != None
            ):  # Si el siguiente no está vacío, osea que no es el último
                aux = aux.siguiente  # Avanzo al siguiente
            aux.siguiente = nuevo  # Ya en el lugar, lo coloco en su posición de nuevo
            nuevo.anterior = aux  # Coloco el apuntador al anterior
            self.fin = nuevo
            self.tamaño += 1  # aumento el tamaño

    def mostrando(self):  # La verdad no sirve para nada pero me gusta verlo :)
        aux = self.inicio
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

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


class matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n  # cantidad de filas
        self.m = m  # cantidad de columnas
        self.filas = listita()
        self.columnas = listita()
        relleno = 66  # Es para rellenar la matriz con algo que sea entero
        contadorn = 0
        while contadorn < n:
            contadorm = 0
            miami = listita()
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

    def encontrar(self, x, y):
        return self.filas.encontrar(x - 1).encontrar(y - 1)

    def modificar(self, x, y, dato):
        self.filas.encontrar(x - 1).modificar(y - 1, dato)


luisfonsi = matriz("LuisFonsi", 3, 3)


luisfonsi.modificar(1, 1, "Despacito")
luisfonsi.modificar(1, 2, "Daddy Yanky")
luisfonsi.modificar(2, 2, "Mario Lopez")
luisfonsi.mostrar()


# Aquí voy a probar si sirve lo que hice xd
