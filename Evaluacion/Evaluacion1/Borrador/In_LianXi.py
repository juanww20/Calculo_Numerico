import flet as ft

def main (page:ft.Page):
    page.title = 'Titulo'
    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 15
    page.update()

    def FUZHI (e):
        bb.value = option111.value
        bb.update()
        

    cont = ft.Container(
        ft.Row([
            ft.Column(
                [ft.TextField(width=500)]
            ),ft.Column(
                [ft.ElevatedButton("WOAC",width=95,bgcolor="#83e696",color = "white")]
            ),ft.Column(
                [ft.CupertinoButton("Hola")]
            )
        ],spacing=50)
    )
    bb = ft.TextField(label="NO se", max_lines=5,multiline=True,min_lines=5)
    option111 = ft.Dropdown(label="OPtion",options=[ft.dropdown.Option("HAHAH"),ft.dropdown.Option("[12,8]")]) #agregar vector[]
    cont2 = ft.Container(
        ft.Column([bb,
                ft.ElevatedButton("WWW WED WORLD WIDE WEB",on_click=FUZHI),
                option111
        ]))
    cont3 = ft.Container(ft.Row([ft.TextButton("sdnjksahjdk")])
    )
    
    #cont.visible = False
    #tf = ft.TextField()
    #tf2 = ft.TextField()
    #btn = ft.ElevatedButton("WOAC")
    #btn2 = ft.FilledButton("Hola")
    #btn2 = ft.CupertinoButton("Hola")
    page.add(cont,cont2,cont3)


ft.app(main)