class Persona:
    def __init__(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def getNombre (self):
        return self.nombre

    def getEdad (self):
        return self.edad

    def getCedula (self):
        return self.cedula

    def setNombre (self,nombre):
        self.nombre = nombre

    def setEdad (self,edad):
        self.edad = edad

    def setCedula(self,cedula):
        self.cedula = cedula

    def verificar (self):
        if self.edad > 18:
            return True
        else:
            return False

    def imprimir (self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Cedula: ",self.cedula)
        print("Validacion: ",self.verificar())

#Ejemplo 1
per1 = Persona("Jose",20,30256559)
per1.imprimir()
print("")

#Ejemplo 2 pero con getter y setter
per1.setNombre("Mario")
per1.imprimir()
print("")
print("Mostracion por getter: ",per1.getCedula())
print("")

#Utilizar con una lista
per2 = Persona("Luis",17, 31033532)
per3 = Persona("Adriana",25, 29055300)

lista = []
lista.append(per1)
lista.append(per2)
lista.append(per3)

for i in range (len(lista)):
    per = lista[i]
    per.imprimir()
    print("")
    