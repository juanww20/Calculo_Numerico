#Practica para matplotlib 3D

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

#Grafica
fig = plt.figure()
grafica = fig.add_subplot(111, projection = '3d')

#Punto en el espacio
[x,y,z] = x0
grafica.scatter(x,y,z, c='blue', marker = 'o', label = 'x0')
grafica.set_xlabel('eje x')
grafica.set_ylabel('eje y')
grafica.set_zlabel('eje z')

plt.show()