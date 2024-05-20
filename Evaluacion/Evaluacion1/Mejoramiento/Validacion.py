import flet as ft

#Funciones
#Identificar que si el ingreso esta correcto
def ident (ent):
    ver = ent.value
    if ver.isdigit():
        return True
    else:
        return False