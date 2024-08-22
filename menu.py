# Aquí solo meteré el menu y probablemente
# Algunas funciones que se necesiten para el menu o todo el programa
# Pretendiéndo que sea como mi Main
import xml.etree.ElementTree as ET
import apuntador as ap

matrices=ap.listita() #aquí las matrices se guardarán :)
matrix=ap.listita() #aquí las matrices de acceso se crearán :)
matrixR=ap.listita() #aquí las matrices de acceso reducidas se guardarán :)

def cargarArchivo():  # Función para cargar el archivo
    ruta = "e.xml"
    # ruta = input("Ingrese la ruta del archivo: ") -----------------------------------------------------------------
    print("Cargando Archivo...")  # Mensaje de carga
    arbol = ET.parse(ruta)  # parseando la ruta del archivo
    ramas = arbol.getroot()  # Obteniendo la raíz del archivo
    for i in ramas.iter("matriz"):
        nombre = str(i.get("nombre"))
        n = int(i.get("n"))
        m = int(i.get("m"))
        nombre=ap.matriz(nombre, n, m) #creación de la matriz con los datos respectivos
        for j in i.iter("dato"):
            x = int(j.get("x"))
            y = int(j.get("y"))
            text = int(j.text)
            nombre.modificar(x, y, text) #modificando cada dato de la matriz en su lugar
        matrices.agregar(nombre) #Agregando la matriz a la lista de la matrices
    print("Archivo", ruta,"cargado con exitosamente")
    #Ciclo para ver si lo hice bien :)
    contodini=0
    while contodini<=matrices.tamaño:
        matrices.encontrar(contodini-1).mostrar()
        contodini+=1
    #kasjdfhkasdhfoiusadhvpiuafsadhidjdskfklaerehnfcehrlcgnerwknhljdrlewvqporcof
    
    


def procesarArchivo():  # Función para procesar el archivo
    print("Procesando Archivo...")
    print("Transformando matrices en matrices de entrada...")
    contando=0
    matrix=matrices
    while contando<=matrix.tamaño: #Moviendo en la lista en donde están la matrices
        contodono=0
        while contodono<=matrix.encontrar(contando-1).n: #Recorriendo las filas de la matriz
            contodororo=0
            while contodororo<=matrix.encontrar(contando-1).m: #Recorriendo las columnas de la matriz
                if (matrix.encontrar(contando-1).encontrar(contodono, contodororo)<=0): #Si tiene una entrada, lo vuelve 1
                    matrix.encontrar(contando-1).modificar(contodono,contodororo,0)
                else:
                    matrix.encontrar(contando-1).modificar(contodono,contodororo,1) #Si no tiene entrada, lo vuelve 0
                contodororo+=1
            contodono+=1 #Los contadorinis xd
        contando+=1
    contodini=0
    #Aquí tambien solo ando viendo que se haya realizado correctamente
    while contodini<=matrices.tamaño:
        matrices.encontrar(contodini-1).mostrar()
        contodini+=1
    #......................................................................
    print("Matrices de entrada creadas con exitosamente")
    print("Generando matrices de frecuencia reducidas...")
    #En proceso creativo de mi cabecita cabezosaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    contuno=0
    matrixxi=matrices
    matrixxixxi=matrix
    while contuno<=matrixxixxi.tamaño: #moviendo en el arreglo de las matrices
        contdos=0
        borde=matrixxixxi.encontrar(contuno-1).n
        while contdos<=borde: #recorriendo las filas de la matriz
            conttres=0
            jala=0
            fila=matrixxixxi.encontrar(contuno-1).encontrarF(contdos).concatenarF() #obteniendo la fila que evaluaré
            while conttres<=borde: #recorriendo las filas de la matriz
                fila2=matrixxixxi.encontrar(contuno-1).encontrarF(conttres).concatenarF() #obteniendo la fila que compararé
                if fila==fila2: #verificando
                    jala+=1
                if(jala>=2):
                    matrixxi.encontrar(contuno-1).sumaModificaEliminaF(contdos, conttres) #Suma, modifica y elimina la fila
                    matrixxixxi.encontrar(contuno-1).encontrarF(conttres).eliminar(conttres) #Elimina la fila de la matriz
                    borde-=1
                    contdos-=1
                conttres+=1
            contdos+=1
        contuno+=1

    #En proceso creativo de mi cabecita cabezosaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    
def escribirArchivo():  # Función para escribir el archivo de salida
    print("Escribir Archivo de salida --")


def generarGrafica():  # Función para generar la gráfica
    print("Generando gráfica...")

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
            cargarArchivo()

        case "2":
            procesarArchivo()
        case "3":
            print("Escribir Archivo de salida --")
        case "4":
            print("Mostrando Datos del Estudiante...")
            print("Nombre: Enner Esaí Mendizabal Castro")
            print("Carnet: 202302220")
            print('Curso: Introducción a la Programación y Computación 2 Sección "C"')
            print("Ingenieria en Ciencias y Sistemas")
            print("Segundo Semestre 2024")
        case "5":
            print("Generando gráfica...")
        case "6":
            print("Salir --")
            salir = False
        case _:
            print("Opción no válida")
