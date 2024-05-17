import flet as ft
def main (page:ft.Page):
    page.title = 'Titulo'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Vertical
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.update()

    def bb (e):
        tf2.disabled = False
        page.update()
    
    def bb2 (e):
        tf2.disabled = True
        page.update()

    def agregar(e):
        txt = ft.TextField(width=60,height=60,text_size=15)
        fila.controls.append(txt)
        page.update()
    
    def borrr (e):
        fila.controls.clear()
        page.update()
    
    fila = ft.Row([
    ])

    btn = ft.ElevatedButton("Add",on_click=agregar)


    xz = ft.ElevatedButton("Activo",on_click=bb)
    xz2 = ft.ElevatedButton("Desactivo",on_click=bb2)
    tf2 = ft.TextField(disabled=True)
    btn2 = ft.ElevatedButton("Borrar",on_click=borrr)

    page.add(xz,xz2,tf2,fila,btn,btn2)
ft.app(main)