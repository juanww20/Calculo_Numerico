import flet as ft

def main (page:ft.Page):
    page.title = 'Sencillo_practica'
    page.window_width = 350
    page.window_height = 200
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.update()

    #Tipos de label
    tf1 = ft.Text("Estas feliz?",theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM)
    tf2 = ft.Text("Biennnn!",theme_style=ft.TextThemeStyle.DISPLAY_LARGE)

    #Contenedor
    cont1 = ft.Container(ft.Row([tf1]),width=250,height=75,bgcolor="#fbf994")
    cont2 = ft.Container(ft.Row([tf2]),width=250,height=75,bgcolor="#cdfde6")

    #Boton de cambiar y la muestra de cambio
    animate = ft.AnimatedSwitcher(
        cont1,
        transition=ft.AnimatedSwitcherTransition.ROTATION, #Aqui le puede cambiar varios formas para la animacion, por ejemplo, scale o rotation
        duration = 500,
        reverse_duration= 100,
        #switch_in_curve=ft.AnimationCurve.BOUNCE_OUT este rota mas rapido
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    def donghua (e):
        animate.content = cont2 if animate.content == cont1 else cont1
        animate.update()
    
    tf = ft.TextButton("¡SI!",on_click=donghua)
    contf = ft.Container(ft.Column([
        ft.Row([animate],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([tf],alignment=ft.MainAxisAlignment.CENTER),
        ],
        spacing=35))

    page.add(contf)
ft.app(main)