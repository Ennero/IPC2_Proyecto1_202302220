class nodo:  # El nodito
    def __init__(self, nombre, estado, siguiente=None, anterior=None):
        self.nombre = nombre
        self.estado = estado
        self.siguiente = siguiente
        self.anterior = anterior


class listita:  # La listita para las filas
    def __init__(self, inicio=None, fin=None, tamaño=0):  # El constructor de la lista
        self.inicio = inicio
        self.fin = fin
        self.tamaño = tamaño

    def agregar(self, nombre, estado):  # Función para agregar un nodo a la lista
        nuevo = nodo(nombre, estado)  # Creo el nodo con la información y el estado
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
            print(aux.nombre)
            aux = aux.siguiente


# Aquí voy a probar si sirve lo que hice xd

estudiante = listita()


estudiante.agregar("Enner", "Activo")
estudiante.agregar("Luis", "Limones")
estudiante.agregar("Marian", "Saber")
estudiante.agregar("Mario", "Cloro")
estudiante.agregar("Berti", "machacar")
listita.mostrando(estudiante)  # Aquí debería mostrar los nombres de los estudiantes
