#Aqui presenta una practica sencilla sobre un diseño para flet
import flet as ft

def main (page:ft.Page):
    page.title = "Matriz"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Horizontal
    page.bgcolor = "#bcc1ff"
    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    page.window_center()
    page.update()

    #Componentes
    titulo = ft.Text(value = "¡MATRIZ!",size = 56,color = "black")
    tf = ft.TextField(label="Numero",hint_text="Ingresar cualquier numero",bgcolor="white")
    tf2 = ft.TextField(label="Resultado",bgcolor= "white")
    btn1 = ft.ElevatedButton("Generar")
    btn2 = ft.ElevatedButton("Limpiar")

    #Agregarlo en la ventana
    page.add(titulo)
    page.add(ft.Column([tf,tf2]))
    page.add(ft.Row([btn1,btn2]))

ft.app(main)