# Aquí solo meteré el menu y probablemente
# Algunas funciones que se necesiten para el menu o todo el programa
# Pretendiéndo que sea como mi Main
import xml.etree.ElementTree as ET
import apuntador as ap
import copy
from graphviz import Digraph

matrices=ap.listita() #aquí las matrices se guardarán :)
matrix=ap.listita() #aquí las matrices de acceso se crearán :)
matrixR=ap.listita() #aquí las matrices de acceso reducidas se guardarán :)
matrix2=ap.listita() #aquí las matrices de acceso copiadas se guardarán :)
repeticiones=ap.listita() #aquí las repeticiones se guardarán [son 3 puntos para acceder a cada una de las parejas]
orden=0 #este entero dictaminará el orden de los archivos

def cargarArchivo():  # Función para cargar el archivo
    global orden
    if orden==0: #Si es la primera vez que se carga un archivo
        global matrices
        ruta = input("Ingrese la ruta del archivo: ") # Ingresando la ruta del archivo
        print("-----------------------")
        try:
            print("Cargando Archivo...")  # Mensaje de carga
            arbol = ET.parse(ruta)  # parseando la ruta del archivo
            ramas = arbol.getroot()  # Obteniendo la raíz del archivo
            for i in ramas.iter("matriz"):
                nombre = str(i.get("nombre"))
                n = int(i.get("n"))
                m = int(i.get("m"))
                nombre = ap.matriz(nombre, n, m)  # creación de la matriz con los datos respectivos
                for j in i.iter("dato"):
                    x = int(j.get("x"))
                    y = int(j.get("y"))
                    text = int(j.text)
                    nombre.modificar(x-1, y-1, text)  # modificando cada dato de la matriz en su lugar (no sé por qué solo me funciona así :<)
                matrices.agregar(nombre)  # Agregando la matriz a la lista de la matrices
                matrix.agregar(copy.deepcopy(nombre)) #Agregando la matriz a la lista de matrices de acceso
                matrixR.agregar(copy.deepcopy(nombre)) #Agregando la matriz a la lista de matrices de acceso reducidas
            print("Archivo", ruta, "cargado exitosamente") #Depurado así que no sé que efectivamente está todo bien hasta aquí

            # Ciclo para ver si lo hice bien :)
            """contodini = 0
            while contodini < matrices.tamaño:
                matrices.encontrar(contodini).mostrar()
                contodini += 1"""
            #......................................................................

        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
        orden=1 #Ya se cargó un archivo
    else: #Si ya se cargó un archivo
        print("Ya se cargó un archivo, procese el archivo actual")


def procesarArchivo():  # Función para procesar el archivo
    global orden, repeticiones
    if orden==1: #Si ya se cargó el archivo 
        print("Calculando las matrices binarias...")
        print("-----------------------")
        contando=0
        while contando<matrix.tamaño: #Moviendo en la lista en donde están la matrices
            contodono=0
            print("Matriz binaria",contando+1,"creada exitosamente...")
            while contodono<matrix.encontrar(contando).n: #Recorriendo las filas de la matriz
                contodororo=0
                while contodororo<matrix.encontrar(contando).m: #Recorriendo las columnas de la matriz
                    if (matrix.encontrar(contando).encontrar(contodono, contodororo)<=0): #Si tiene una entrada, lo vuelve 1
                        matrix.encontrar(contando).modificar(contodono,contodororo,0)
                    else:
                        matrix.encontrar(contando).modificar(contodono,contodororo,1) #Si no tiene entrada, lo vuelve 0
                    contodororo+=1
                contodono+=1 #Los contadorinis xd
            contando+=1

        #Aquí tambien solo ando viendo que se haya realizado correctamente
        """contodini=0
        while contodini<matrix.tamaño:
            matrix.encontrar(contodini).mostrar()
            contodini+=1
        contodini = 0
        while contodini < matrices.tamaño:
            matrices.encontrar(contodini).mostrar()
            contodini += 1"""
        #......................................................................
        print("-----------------------")
        print("Matrices binarias creadas exitosamente")
        print("-----------------------")
        print("Realizando suma de tuplas...")

        matrix2=copy.deepcopy(matrix) #Copiando las matrices de acceso
        contuno=0
        while contuno<matrix2.tamaño: #moviendo en el arreglo de las matrices
            contdos=0
            borde=matrix2.encontrar(contuno).n
            

            grupo=ap.listita() #lista del grupo de las parejas
            g=1
            banderita=False
            while contdos<borde: #recorriendo las filas de la matriz
                jala=0
                fila=matrix2.encontrar(contuno).encontrarF(contdos).concatenarF() #obteniendo la fila que evaluaré
                conttres=0
                f=1 #contador de la frecuencia
                while conttres<borde: #recorriendo las filas de la matriz que se analizarán
                    fila2=matrix2.encontrar(contuno).encontrarF(conttres).concatenarF() #obteniendo la fila que compararé
                    if fila==fila2: #verificando
                        jala+=1
                    if(jala>=2):
                        matrixR.encontrar(contuno).sumaModificaEliminaF(contdos, conttres) #Suma, modifica y elimina la fila
                        matrix2.encontrar(contuno).filas.eliminar(conttres) #Elimina la fila 
                        matrix2.encontrar(contuno).n-=1 #Disminuye el tamaño de la matriz
                        if(contdos==conttres-1): #Para el siguiente sumaré 1 al contador de las posición del grupo
                            banderita=True
                        f+=1 #Aumenta la frecuencia
                        borde-=1 #Disminuye el borde
                        jala=1 #Reinicia el contador de las filas iguales
                    conttres+=1
                contdos=contdos+1
                pareja=ap.listita() #lista de las parejas
                pareja.agregar(g) #Agrega el número de la pareja
                pareja.agregar(f) #Agrega la frecuencia
                grupo.agregar(pareja) #Agrega las parejas al grupo
                g+=1
                if(banderita==True): #Si se eliminó una fila, se debe sumar uno porque la siguiente fila será la que estaba en la posición anterior
                    banderita=False
                    g+=1
            repeticiones.agregar(grupo) #Agrega los grupos y las frecuencias a la lista de repeticiones
            contuno=contuno+1

        print("Suma de tuplas realizada exitosamente")
        print("-----------------------")
        print("Archivo procesado correctamente")
        orden=2 #Ya se procesó el archivo

        #Aquí tambien solo ando viendo que se haya realizado correctamente
        """contodini=0
        while contodini<matrixR.tamaño:
            matrixR.encontrar(contodini).mostrar()
            contodini+=1
        contodini = 0
        while contodini < matrix2.tamaño:
            matrix2.encontrar(contodini).mostrar()
            contodini += 1
        contodini = 0
        print("Repeticiones:")
        while contodini < repeticiones.tamaño: #Recorriendo la lista de las repeticiones
            contodoro=0
            print("Grupo:", contodini+1, "----------")
            while contodoro<repeticiones.encontrar(contodini).tamaño: #Recorriendo el grupo de las repeticiones (las bolitas)
                contoinodoro=0
                print("Pareja:" ,contodoro+1)
                while contoinodoro<repeticiones.encontrar(contodini).encontrar(contodoro).tamaño: #Recorriendo las parejas
                    print(repeticiones.encontrar(contodini).encontrar(contodoro).encontrar(contoinodoro))
                    contoinodoro+=1
                contodoro+=1
            contodini += 1"""
        #......................................................................
        
    else:
        if(orden==2):
            print("Ya se procesó un archivo, escriba el archivo de salida")
        else:
            print("No se ha cargado un archivo, cargue un archivo .xml primero")


def indent(elem, level=0, hor='\t', ver='\n'): # Función para indentar el archivo (solo lo copié y lo pegué xd)
    i = ver + level * hor
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + hor
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1, hor, ver)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def escribirArchivo():  # Función para escribir el archivo de salida
    global orden
    if orden==2:
        try:
            ruta=input("Ingrese la ruta del archivo de salida: ")
            ruta=ruta+".xml"
            print("Escribiendo Archivo de salida...")
            raiz=ET.Element("matrices") #Creando la raíz del archivo .xml
            contador=0
            while contador<matrixR.tamaño: #Recorriendo las matrices
                #Aquí estoy dentro de la matriz
                contadorini=0
                nombreM=matrixR.encontrar(contador).nombre
                nn=str(matrixR.encontrar(contador).n)
                mm=str(matrixR.encontrar(contador).m)
                gg=str(repeticiones.encontrar(contador).tamaño)
                rama=ET.SubElement(raiz, "matriz",nombre=nombreM,n=nn,m=mm,g=gg) #Creando la rama de las matrices
                while contadorini<matrixR.encontrar(contador).n: #Recorriendo las filas
                    #Aquí estoy dentro de la fila
                    contadororo=0
                    while contadororo<matrixR.encontrar(contador).m: #Recorriendo las columnas
                        #Aquí estoy dentro de la columna (el cuadrito o celda pues)
                        ET.SubElement(rama, "dato", x=str(contadorini+1), y=str(contadororo+1)).text=str(matrixR.encontrar(contador).encontrar(contadorini, contadororo)) #Agregando los datos a la rama
                        contadororo+=1
                    contadorini+=1
                #Aquí ya que se colocaron los valores de la matriz, se procede a colocar las frecuencias
                contando=0
                while contando<repeticiones.encontrar(contador).tamaño:
                    gegege=str(repeticiones.encontrar(contador).encontrar(contando).encontrar(0))
                    fefefe=str(repeticiones.encontrar(contador).encontrar(contando).encontrar(1))
                    ET.SubElement(rama, "frecuencia", g=gegege).text=fefefe
                    contando+=1
                contador+=1
            #Aquí escribo el archivo con lo que acabo de generar
            salida=ET.ElementTree(raiz)
            ET.dump(raiz) #La verdad no entiendo nada de esta parte xd
            indent(raiz)
            salida.write(ruta)
            print("-----------------------")
            print("Archivo de salida en la ruta", ruta, "escrito exitosamente")
        except Exception as e:
            print(f"Error al escribir el archivo de salida: {e}")
    else:
        print("No se ha procesado un archivo, procese un archivo primero")


def generarGrafica():  # Función para generar la gráfica
    global orden
    if orden>0:
        nombre=input("Ingrese el nombre de la matriz que desea que sea graficada: ")
        contador=0
        pos=-1
        while contador<matrixR.tamaño: #Busca la matriz que se desea graficar a partir del nombre
            if(nombre==matrixR.encontrar(contador).nombre): #Si los nombres coinciden:
                pos=contador
                print("Matriz", nombre, "encontrada en la posición", pos+1)
            contador+=1
        if(pos!=-1):
            print("-----------------------")
            print("Generando gráfica...")
            grafo=Digraph(comment="Grafica de la matriz "+nombre) #Creando el grafo de la matriz seleccionada
            grafo.node("Matrices", "Matrices")
            #Creación de la matriz original -----------------------------------------------------
            grafo.node("Matriz", nombre) #Creando el nodo de la matriz
            n=matrices.encontrar(pos).n
            m=matrices.encontrar(pos).m
            grafo.node("n", "n="+str(n), color="blue") #Creando los nodos de las dimensines de la matriz
            grafo.node("m", "m="+str(m), color="blue")
            grafo.edge("Matrices", "Matriz") #Creando la arista de la gráfica
            grafo.edge("Matriz", "n") #Creando las aristas de las dimensiones de la matriz
            grafo.edge("Matriz", "m")
            contador=0
            while contador<m: #Recorriendo las columnas de la matriz
                contadororo=0
                luis="Matriz" #Creando el identificador del nodo de la matriz para unir los nodos de sus valores
                while contadororo<n: #Recorriendo las filas de columan (de arriba hacia abajo)
                    name=str(contador*1000)+str(contadororo) #Creando el nombre del nodo
                    grafo.node(name, str(matrices.encontrar(pos).encontrar(contadororo,contador))) #Creando el nodo
                    grafo.edge(luis, name) #Creando la arista que lo conecta con el nodo anterior (el de arribita)
                    luis=name #El nodo anterior ahora es el nodo actual
                    contadororo+=1
                contador+=1
            #Creación de la matriz reducida -----------------------------------------------------
            if(orden>1): #Si ya se ha procesado el archivo
                print("-----------------------")
                print("Generando gráfica reducida...")
                grafoR=Digraph(comment="Grafica de la matriz reducida "+nombre) #Creando el grafoR de la matriz seleccionada
                grafoR.node("Matrices", "Matrices")

                #Creación de la matriz reducida -----------------------------------------------------
                grafoR.node("MatrizReducida", nombre) #Creando el nodo de la matriz
                nn=matrixR.encontrar(pos).n
                mm=matrixR.encontrar(pos).m
                gg=repeticiones.encontrar(pos).tamaño
                grafoR.node("nn", "n="+str(nn), color="blue") #Creando los nodos de las dimensines de la matriz
                grafoR.node("mm", "m="+str(mm), color="blue")
                grafoR.node("gg", "g="+str(gg), color="blue")
                grafoR.edge("Matrices", "MatrizReducida") #Creando la arista de la gráfica
                grafoR.edge("MatrizReducida", "nn") #Creando las aristas de las dimensiones de la matriz
                grafoR.edge("MatrizReducida", "mm")
                grafoR.edge("MatrizReducida", "gg")

                contador=0
                while contador<mm: #Recorriendo las columnas de la MatrizReducida
                    contadororo=0
                    luisito="MatrizReducida" #Creando el identificador del nodo de la MatrizReducida para unir los nodos de sus valores
                    while contadororo<nn: #Recorriendo las filas de columan (de arriba hacia abajo)
                        name=str(contador*1000)+str(contadororo) #Creando el nombre del nodo
                        grafoR.node(name, str(matrixR.encontrar(pos).encontrar(contadororo,contador))) #Creando el nodo
                        grafoR.edge(luisito, name) #Creando la arista que lo conecta con el nodo anterior (el de arribita)
                        luisito=name #El nodo anterior ahora es el nodo actual
                        contadororo+=1
                    contador+=1
                contadoriño=0
                #verificando estoooooooooooooosfdadsfsdnagndhfm jdnk afhamsdnfk lsdfhnks
                while contadoriño<gg: #Recorriendo los grupos de las repeticiones
                    g="g="+str(repeticiones.encontrar(pos).encontrar(contadoriño).encontrar(0))
                    f="f="+str(repeticiones.encontrar(pos).encontrar(contadoriño).encontrar(1))
                    n1="g"+str(contadoriño)
                    n2="f"+str(contadoriño)
                    grafoR.node(n1, g, color="red") #Creando los nodos de las dimensiones de la MatrizReducida
                    grafoR.node(n2, f, color="red") #Creando los nodos de las dimensiones de la matriz
                    grafoR.edge("MatrizReducida", n1) #Creando las aristas de las dimensiones de la MatrizReducida
                    grafoR.edge(n1, n2)
                    contadoriño=contadoriño+1
            #Creación de la matriz reducida -----------------------------------------------------
            print("-----------------------")
            print("Gráfica generada exitosamente")
            grafo.render("grafica de matriz", format="pdf", view=True) #Generando la gráfica
            if(orden>1):
                print("Gráfica reducida generada exitosamente")
                grafoR.render("grafica de matriz reducida", format="pdf", view=True) #Generando la gráfica reducida
        else:
            print("No se encontró la matriz con el nombre indicado")
    else:
        print("No se ha cargado un archivo, cargue un archivo primero")

print("      BIENVENIDO")
salir = True  # Variable para salir del ciclo
while salir:  # El ciclo para mostrar el menu principal
    print("-----------------------")
    print("--MENU PRINCIPAL--")
    print("1. -- Cargar Archivo")
    print("2. -- Procesar Archivo")
    print("3. -- Escribir Archivo de salida")
    print("4. -- Mostrar Datos del Estudiante")
    print("5. -- Generar Grafica")
    print("6. -- Salir")
    op = input("Ingrese una opción: ")
    match op:
        case "1":
            print("-----------------------")
            cargarArchivo()
        case "2":
            print("-----------------------")
            procesarArchivo()
        case "3":
            print("-----------------------")
            escribirArchivo()
        case "4":
            print("-----------------------")
            print("Mostrando Datos del Estudiante...")
            print("Nombre: Enner Esaí Mendizabal Castro")
            print("Carnet: 202302220")
            print('Curso: Introducción a la Programación y Computación 2 Sección "C"')
            print("Ingenieria en Ciencias y Sistemas")
            print("Segundo Semestre 2024")
        case "5":
            print("-----------------------")
            generarGrafica()
        case "6":
            print("Salir --")
            salir = False
        case _:
            print("Opción no válida")