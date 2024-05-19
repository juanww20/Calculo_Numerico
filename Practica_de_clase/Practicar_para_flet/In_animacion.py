import flet as ft

def main (page:ft.Page):
    page.title = 'Sencillo_practica'
    page.window_width = 750
    page.window_height = 750
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.update()

    #Tipos de label
    tf1 = ft.Text("Estas feliz?",theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM)
    tf2 = ft.Text("Biennnn!",theme_style=ft.TextThemeStyle.DISPLAY_LARGE)

    #Contenedor
    cont1 = ft.Container(ft.Row([tf1]))
    cont2 = ft.Container(ft.Row([tf2]))

    #Boton de cambiar y la muestra de cambio
    animate = ft.AnimatedSwitcher(cont1,
        transition=ft.AnimatedSwitcherTransition.ROTATION,
        duration = 500,
        reverse_duration= 100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT
    )

    def donghua (e):
        animate.content = cont2 if animate.content == cont1 else cont1
        animate.update()
    
    tf = ft.TextButton("¡SI!",on_click=donghua)

    contf = ft.Container(ft.Row([animate,tf],alignment=ft.MainAxisAlignment.CENTER))

    page.add(contf)
ft.app(main)