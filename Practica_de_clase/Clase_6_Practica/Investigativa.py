#Aqui presenta algunas practicas y investigativas

#Potencia
def potencia (n):
    if n == 0:
        return 1
    else:
        return n * potencia(n-1)
    
x = 5
result = potencia(x)
print(result)

#Inverso
num = 325
invertido = 0
while num != 0:   
    ultimo = num%10
    invertido = invertido*10 + ultimo
    num = num // 10
print(invertido)

#Agregar por forma recursivo:
def invertir (n,i):
    if n != 0:
        ultimo = n%10
        i = i*10 + ultimo
        return invertir(n//10,i)
    else:
        return i
    
n2 = 258
i = 0
print(invertir(n2,i))