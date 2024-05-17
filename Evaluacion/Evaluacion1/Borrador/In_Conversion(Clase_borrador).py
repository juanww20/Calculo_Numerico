import flet as ft

def main (page:ft.Page):
    page.title = "Numero de conversion"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Vertical
    page.window_width = 700
    page.window_height = 750
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()
    page.update()

    def abinario (decimal,binario,i):
        if decimal > 0:
            digito = decimal%2
            decimal = int(decimal//2)
            binario += digito*(10**i)
            i = i +1
            return abinario(decimal,binario,i)
        else:
            return binario
        
    def adecimal (binario,decimal,i):
        while (binario > 0):
            digito = binario%10
            binario = int(binario//10)
            decimal += digito*(2**i)
            i += 1
        return decimal

    
    def cdb (e):
        num = tf.value
        if num.isdigit():
            num = int(tf.value)
            i = 0
            binario = 0
            resultado = abinario(num,binario,i)
            tf2.value = str(resultado)
        else:
            tf2.value = "Por favor ingresar caracteres numeros"
        page.update()
        
    def cdb2 (e):
        num = tf3.value
        if num.isdigit():
            num = int(tf3.value)
            i = 0
            decimal = 0
            resultado = adecimal(num,decimal,i)
            tf4.value = str(resultado)
        else:
            tf4.value = "Por favor ingresar caracteres numeros"
        page.update()
    
    def aaa (e):
        estado = tfs.value
        if estado == "1":
            num = int(tff1.value)
            aa2 = hex(num)
            tff2.value = str(aa2)
            page.update()
        elif estado == "2":
            num = tff1.value
            aa2 = int(num,16)
            tff2.value = str(aa2)
            page.update()
        elif estado == "3":
            num = int(tff1.value)
            aa2 = oct(num)
            tff2.value = str(aa2)
            page.update()
        elif estado == "4":
            num = tff1.value
            aa2 = int(num,8)
            tff2.value = str(aa2)
            page.update()

    t1 = ft.Text("Conversion decimal a binario")        
    tf=ft.TextField(label="Ingresar numero",hint_text="Ingresar caracteres correctos")
    tf2= ft.TextField(label="Resultado",disabled=True)
    btn = ft.ElevatedButton(text="Convertir decimal",on_click=cdb)

    t2 = ft.Text("Conversion binario a decimal")        
    tf3=ft.TextField(label="Ingresar numero",hint_text="Ingresar caracteres correctos")
    tf4= ft.TextField(label="Resultado",disabled=True)
    btn2 = ft.ElevatedButton(text="Convertir binario",on_click=cdb2)

    t3 = ft.Text("Conversion general")
    tfs = ft.TextField(label="Seleccionar estado: 1:decimal a hexadecimal 2:hexadecimal a decimal 3:decimal a octal 4:octal a decimal")
    tff1 = ft.TextField(label="Ingresar numero",hint_text="Ingresar caracteres correctos")
    tff2 = ft.TextField(label="Resultado",disabled=True)
    btn3 = ft.ElevatedButton(text="CONVERTIRLO",on_click=aaa)


    page.add(t1)
    page.add(ft.Column([
        tf,tf2
    ]))
    page.add(btn)

    page.add(t2)
    page.add(ft.Column([
        tf3,tf4
    ]))
    page.add(btn2)

    page.add(t3)
    page.add(ft.Column([
        tfs,tff1,tff2
    ]))
    page.add(btn3)
ft.app(main)