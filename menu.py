#Aquí solo meteré el menu y probablemente
#Algunas funciones que se necesiten para el menu o todo el programa
#Pretendiéndo que sea como mi Main
import xml.etree.ElementTree as ET


def cargarArchivo(): #Función para cargar el archivo
    ruta=input("Ingrese la ruta del archivo: ")
    arbol=ET.parse(ruta) #parseando la ruta del archivo
    ramas=arbol.getroot() #Obteniendo la raíz del archivo
    for i in ramas.iter("matriz"):
        print(i.tag ,"número.", i)
        for nombre, fila, columna in i.attrib.items():
            print("Nombre: ", nombre, "Fila: ", fila, "Columna: ", columna)
            print("-----------------------")
        for j in i.iter("dato"):
            print(j.get('x'))
            print(j.get('y'))
            print(j.text)


def procesarArchivo(): #Función para procesar el archivo
    print("Procesar Archivo --")

def escribirArchivo(): #Función para escribir el archivo de salida
    print("Escribir Archivo de salida --")

def generarGrafica(): #Función para generar la gráfica
    print("Generando gráfica...")

print("      BIENVENIDO")
salir = True #Variable para salir del ciclo
while salir: #El ciclo para mostrar el menu principal
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
            print("Cargar Archivo --")
        case "2":
            print("Procesar Archivo --")
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
    
