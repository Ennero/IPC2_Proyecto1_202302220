class nodo:  # El nodito
    def __init__(self, dato, siguiente=None, anterior=None):
        self.dato = dato #Datos
        self.siguiente = siguiente #apuntadores
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

    def mostrando(self):  # La verdad ni creo que sirva pero meh xd
        aux = self.inicio
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def modificar(self, pos, dato): #Para modificar un dato en una posición indicada
        aux = self.inicio
        cont = 0
        while cont < pos:
            aux = aux.siguiente
            cont += 1
        aux.dato = dato

    def encontrar(self, pos): #Función para encontrar un dato en una posición indicada	
        aux=self.inicio
        cont=0
        while cont<pos:
            aux=aux.siguiente
            cont+=1
        return aux.dato

class matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n #cantidad de filas
        self.m = m #cantidad de columnas
        self.filas = listita()
        self.columnas = listita()
        relleno="papayo" #El espacio en blanco para darle tamaño a la matriz
        contadorn=0
        while contadorn<n:
            contadorm=0
            miami=listita()
            while contadorm<m:
                miami.agregar(relleno)
                contadorm+=1
            self.filas.agregar(miami)
            contadorn+=1
        
    def mostrar(self): #Muestra los datos de la matriz fija creada
        contadoro=0
        while contadoro<self.n:
            contadori=0
            print("Fila: ", contadoro+1)
            while contadori<self.m:
                print(self.filas.encontrar(contadoro).encontrar(contadori))
                contadori+=1
            contadoro+=1

    
    def modificar(self, x, y, dato):
        self.filas.encontrar(x-1).modificar(y-1,dato)




luisfonsi=matriz("LuisFonsi", 3, 3)


luisfonsi.modificar(1, 1, "Despacito")
luisfonsi.modificar(1, 2, "Daddy Yanky")
luisfonsi.modificar(2, 2, "Mario Lopez")
luisfonsi.mostrar()







# Aquí voy a probar si sirve lo que hice xd



