#Practica para matplotlib 3D

#Importar la libreria
import matplotlib as plt
import numpy as np

#Ingreso
x0 = np.array([0.0,0.0,0.0])
x1 = np.array([1,2,3], dtype = float)
x2 = np.array([2,4,-1], dtype = float)

#Procedimiento
errado = x2 - x1
distancia = np.sqrt(np.sum(errado**2))

#Salida
print(errado)
print(distancia)