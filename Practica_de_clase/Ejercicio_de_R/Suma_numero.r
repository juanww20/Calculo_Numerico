print("Calculo de suma sencillo por 2 numeros")
na <- readline(prompt = "Ingrese el valor de primer numero: ")
na <- as.integer(na)

nb <- readline(prompt = "Ingrese el valor de segundo numero: ")
nb <- as.integer(nb)

resultado <- na + nb

print(paste("El resultado de la suma sera: ", resultado))