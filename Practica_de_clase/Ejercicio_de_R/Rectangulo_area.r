print("Ingrese los valores para calcular la area de rectangulo")

altura <- readline(prompt = "Ingrese el valor de altura: ")
altura <- as.integer(altura)

base <- readline(prompt = "Ingrese el valor de base: ")
base <- as.integer(base)

rec_area <- altura * base

print(paste("Los valores que ha dado, la area de rectangulo sera: ", rec_area))