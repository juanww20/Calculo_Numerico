import flet as ft
from random import randint
import numpy as np

def main (page:ft.Page):
    page.title = 'Matriz: Gauss-Jordan'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Horizontal
    page.window_width = 1000
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 25
    page.window_center()
    page.update()

    #Todas las funciones

    def Gauss_Jordan (a,x):
        b = len(x)
        for i in range(b):
            if a[i][i] == 0.0:
                tfr2.value = 'Divide by zero detected!'
                
            for j in range(b):
                if i != j:
                    ratio = a[j][i]/a[i][i]

                    for k in range(b+1):
                        a[j][k] = a[j][k] - ratio * a[i][k]

        for i in range(b):
            x[i] = a[i][b]/a[i][i]
        tfr2.value = ""
        for i in range (len(x)):
            aux_num = round(x[i],2)
            tfr2.value += "X" + str(i+1) + ": " + str(aux_num) + "\n"

    def aleatorio_matriz (e):
        c = int(tfi.value)
        mx = np.zeros((c,c+1))
        mr = np.zeros(c)
        tfr1.value = ""

        for i in range (len(mx)):
            for j in range(len(mx[0])):
                mx[i][j] = randint(1,100)
        
        aux = len(mx[0]) -1
        aux2 = len(mx[0])
        for i in range (len(mx)):
            for j in range(aux):
                if j == (aux-1):
                    tfr1.value += str(mx[i][j]) + "x" + "(" + str(j+1) + ")"
                else:
                    tfr1.value += str(mx[i][j]) + "x" + "(" + str(j+1) + ")" + " + "
            tfr1.value += "= "+ str(mx[i][aux2-1])
            tfr1.value += "\n"
        Gauss_Jordan(mx,mr)
        page.update()
        
    def borrar (e):
        tfr1.value = ""
        tfr2.value = ""
        tfi.value = ""
        page.update()


    #Titulo de proyecto
    ti1 = ft.Text("Gauss-Jordan",font_family="New Times Roman",weight=ft.FontWeight.BOLD,size=56)
    contpr = ft.Container(ft.Row([ti1,ft.Icon(ft.icons.CALCULATE, color = "blue", size = 52)],alignment=ft.MainAxisAlignment.CENTER))

    #El Ingreso de digitos y mostrar la matriz, y con su primer contenedor
    tfi = ft.TextField(label = "Ingresar tamaño de matriz",hint_text="Por ejemplo 2, será: '2x2'",bgcolor="white",width=page.width*0.45)
    btnal = ft.ElevatedButton("Aleatorio",on_click=aleatorio_matriz)
    btnmn = ft.ElevatedButton("Manual",on_click=aleatorio_matriz)
    btnb = ft.IconButton(icon=ft.icons.DELETE_FOREVER_ROUNDED,icon_color="pink600",icon_size=40,tooltip="Borrar",on_click= borrar)
    tfr1 = ft.TextField(multiline=True,min_lines=4,bgcolor="white",disabled=True)
    
    cont1 = ft.Container(ft.Row([tfi,btnal,btnmn,btnb],alignment=ft.MainAxisAlignment.CENTER))
    cont11 = ft.Container(ft.Column([tfr1],alignment=ft.MainAxisAlignment.CENTER))
    cont1v = ft.Container(ft.Column([cont1,cont11],spacing=30))

    #Demostrar el resultado y con su segundo contenedor
    subt1 = ft.Text("Resultado",font_family="New Times Roman",weight=ft.FontWeight.BOLD,size=24)
    tfr2 = ft.TextField(multiline=True,min_lines=4,width=400,bgcolor="white",disabled=True)
    cont2 = ft.Container(ft.Column([
        subt1,tfr2
    ],spacing=30))

    page.add(contpr,cont1v,cont2)

ft.app(main)