import flet as ft

#Ventana1
#Funciones
#Identificar que si el ingreso esta correcto
def ident (ent):
    ver = ent.value
    if ver.isdigit():
        return True
    else:
        return False

#Validacion para binario
def identbn(num,b,ent,tfr2):
    num = int(ent.value)
    x = [int(a) for a in str(num)]
    listaa =[]
    i = 0
    b = True
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != 0 and listaa[i] != 1:
            b = False
            tfr2.value = "Error"
        i += 1
    return b

#Validacion para octal
def identbc(num,b,ent,tfr2):
    num = int(ent.value)
    x = [int(a) for a in str(num)]
    listaa =[]
    i = 0
    b = True
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != 0 and listaa[i] != 1 and listaa[i] != 2 and listaa[i] != 3 and listaa[i] != 4 and listaa[i] != 5 and listaa[i] != 6 and listaa[i] != 7:
            b = False
            tfr2.value = "Error"
        i += 1
    return b

#Validacion para hexadecimal
def identbd(b,ent,tfr2):
    num = ent.value
    x = [str(a) for a in str(num)]
    listaa =[]
    i = 0
    b = True
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != "0" and listaa[i] != "1" and listaa[i] != "2" and listaa[i] != "3" and listaa[i] != "4" and listaa[i] != "5" and listaa[i] != "6" and listaa[i] != "7" and listaa[i] != "8" and listaa[i] != "9" and listaa[i] != "A" and listaa[i] != "a" and listaa[i] != "B" and listaa[i] != "b" and listaa[i] != "C" and listaa[i] != "c" and listaa[i] != "D" and listaa[i] != "d" and listaa[i] != "E" and listaa[i] != "e" and listaa[i] != "F" and listaa[i] != "f":
            b = False
            tfr2.value = "Error"
        i += 1
    return b

#Validacion para terciario
def identerciaro(b,ent,tfr2):
    num = int(ent.value)
    x = [int(a) for a in str(num)]
    listaa =[]
    i = 0
    b = True
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != 0 and listaa[i] != 1 and listaa[i] != 2:
            b = False
            tfr2.value = "Error"
        i += 1
    return b

#Validacion para cuaternario
def identcuaternario(b,ent,tfr2):
    num = int(ent.value)
    x = [int(a) for a in str(num)]
    listaa =[]
    i = 0
    b = True
    for i in range (len(x)):
        listaa.append(x[i])
        if listaa[i] != 0 and listaa[i] != 1 and listaa[i] != 2 and listaa[i] != 3:
            b = False
            tfr2.value = "Error"
        i += 1
    return b