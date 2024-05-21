import flet as ft
from random import *

#Ventana2
#Funciones
def Gauss_Jordan (a,x,tfr2):
    b = len(x)
    for i in range(b):
        if a[i][i] == 0.0:
            tfr2.value = 'No se puede iniciando con numero 0!'
                
        for j in range(b):
            if i != j:
                r = a[j][i]/a[i][i]

                for k in range(b+1):
                    a[j][k] = a[j][k] - r * a[i][k]

    for i in range(b):
        x[i] = a[i][b]/a[i][i]
    tfr2.value = ""
    for i in range (len(x)):
        aux_num = round(x[i],2)
        tfr2.value += "X" + str(i+1) + ": " + str(aux_num) + "\n"

def num (mxx):
    for i in range (len(mxx)):
        for j in range(len(mxx[0])):
            mxx[i][j] = randint(1,100)