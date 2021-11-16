#test

class Estudiante:
#falta asignar id
    def __init__(self,nombres,apellidos,rut,direccion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.rut = rut
        self.direccion = direccion

    def getNombres(self):
        return self.nombres
    def getApellidos(self):
        return self.apellidos
    def getRut(self):
        return self.rut
    def getDireccion(self):
        return self.direccion

    def imprimirEtudiante(self):
        print("\nNombres: " +self.getNombres()+"\nApellidos: "+self.getApellidos()+"\nRut: "+self.getRut()+"\nDireccion: "+self.getDireccion())

nombres = input("ingrese nombres: ")
apellidos = input("Ingrese apellidos: ")
rut = input("Ingrese Rut: ")
direccion = input("Ingrese direccion: ")

e = Estudiante(nombres,apellidos,rut,direccion)
e.imprimirEtudiante()