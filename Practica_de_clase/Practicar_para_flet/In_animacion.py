import flet as ft

def main (page:ft.Page):
    page.title = 'Sencillo_practica'
    page.window_width = 750
    page.window_height = 750
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.update()

    tf = ft.TextButton("Cambiar")

    contf = ft.Container(ft.Row([tf],alignment=ft.MainAxisAlignment.CENTER))

    page.add(contf)
ft.app(main)