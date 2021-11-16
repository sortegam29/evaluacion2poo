from typing import List

listaEstudiantes = list()

class Estudiante:
#falta asignar id según diagrama
    def __init__(self):
        self.nombres = ("")
        self.apellidos = ("")
        self.rut = ("")
        self.direccion = ("")


#Primer menu

def menu():
    seleccion=0
    while seleccion!= 4:
        print("---Menu de vio----") 
        print("seleccione una opcion")
        print("........................")
        print("1. registro de alumno")
        print("2. mostrar")
        print("3. buscar")
        print("4. salir")
        seleccion = int(input("Elija una opcion: "))
        if seleccion == 1:
            registrar()
        if seleccion == 2:
            mostrar()
        if seleccion == 3:
            buscar()
        if seleccion == 4:
            salir()

def registrar():
    print ("esta este es registro")
    estudiante = Estudiante()
    estudiante.nombres=input("ingrese nombres: ")
    estudiante.apellidos=input("ingrese apellidos: ")
    estudiante.rut=input("ingrese rut: ")
    estudiante.direccion=input("ingrese direccion: ")
    listaEstudiantes.append(estudiante)


def mostrar():
    print ("esta es una muestra")
    for estudiante in listaEstudiantes:
        print( estudiante.nombres, estudiante.apellidos, estudiante.rut, estudiante.direccion )
        
def buscar():
    print ("esto busca")
def salir():
    print ("chao")



menu()
