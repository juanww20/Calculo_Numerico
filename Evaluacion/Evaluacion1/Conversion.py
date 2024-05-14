import flet as ft

def main (page:ft.Page):
    page.title = 'Conversion'
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()

    def ident ():
        ver = ent.value
        if ver.isdigit():
            return True
        else:
            return False
    
    def error():
        result.value="Por favor ingresar caracteres correctos"
        page.update()

    def cav (e):
        estado = opcion.value
        band = ident()
        if estado == "1 Decimal a Binario":
            if band == True:
                num = int(ent.value)
                rr = bin(num)
                result.value = rr
                result.update()
            else:
                error()
        elif estado == "2 Binario a decimal":
            if band == True:
                num = ent.value
                rr = int(num,2)
                result.value = str(rr)
                result.update()
            else:
                error()
        elif estado == "3 Decimal a Octal":
            if band == True:
                num = int(ent.value)
                rr = oct(num)
                result.value = str(rr)
                result.update()
            else:
                error()
        elif estado == "4 Octal a decimal":
            if band == True:
                num = ent.value
                rr = int(num,8)
                result.value = str(rr)
                result.update()
            else:
                error()
        elif estado == "5 Decimal a Hexadecimal":
            if band == True:
                num = int(ent.value)
                rr = hex(num)
                result.value = rr
                result.update()
            else:
                error()
        elif estado == "6 Hexadecimal a Decimal":
                num = ent.value
                rr = int(num,16)
                result.value = str(rr)
                result.update()
        elif estado == "7 Decimal a Cuaternario":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%4
                    num = int(num//4)
                    tras += digito*(10**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        elif estado == "8 Cuaternario a Decimal":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%10
                    num = int(num//10)
                    tras += digito*(4**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        elif estado == "9 Decimal a Terciario":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%3
                    num = int(num//3)
                    tras += digito*(10**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        elif estado == "10 Terciario a Decimal":
            if band == True:
                num = int(ent.value)
                i = tras = 0
                while num > 0:
                    digito = num%10
                    num = int(num//10)
                    tras += digito*(3**i)
                    i = i +1
                result.value = tras
                result.update()
            else:
                error()
        
                
    def limpiar(e):
        opcion.value = ""
        ent.value = ""
        result.value = ""
        page.update()
    
    cont1 = ft.Container(ft.Row([
        ft.Text("Conversión", weight = "bold", size = 42),
        ft.Icon(ft.icons.CALCULATE, color = "blue", size = 52)
    ],alignment=ft.MainAxisAlignment.CENTER))

    opcion = ft.Dropdown(label="Seleccion (Si no elige, no hace nada)",options=[
        ft.dropdown.Option("1 Decimal a Binario"),
        ft.dropdown.Option("2 Binario a decimal"),
        ft.dropdown.Option("3 Decimal a Octal"),
        ft.dropdown.Option("4 Octal a decimal"),
        ft.dropdown.Option("5 Decimal a Hexadecimal"),
        ft.dropdown.Option("6 Hexadecimal a Decimal"),
        ft.dropdown.Option("7 Decimal a Cuaternario"),
        ft.dropdown.Option("8 Cuaternario a Decimal"),
        ft.dropdown.Option("9 Decimal a Terciario"),
        ft.dropdown.Option("10 Terciario a Decimal")
        ],width=465)

    cont2 = ft.Container(ft.Row([opcion]))

    ent = ft.TextField(label="Ingresar numero",hint_text="Ingresar correctos caracteres")
    result = ft.TextField(label = "Resultado",disabled= True)
    
    cont3 = ft.Container(
        ft.Column([ent,result])
        )
    
    cont4 = ft.Container(ft.Row([
        ft.ElevatedButton("Convertir",ft.icons.TRANSFORM,on_click=cav),
        ft.ElevatedButton("Borrar",ft.icons.DELETE_ROUNDED,on_click=limpiar)
    ],alignment=ft.MainAxisAlignment.CENTER,
    spacing=210)
    )
    page.add(cont1,cont2,cont3,cont4)

ft.app(main)