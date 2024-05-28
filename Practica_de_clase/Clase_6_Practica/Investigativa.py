#Aqui presenta algunas practicas y investigativas

def potencia (n):
    if n == 0:
        return 1
    else:
        return n * potencia(n-1)
    
x = 5
result = potencia(x)
print(result)