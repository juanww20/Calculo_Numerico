#Importacion de la libreria
import numpy as np

#Implemnetacion de Metodo de Potencia
def metodo_potencia(A, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        nuevo_mm = np.dot(A, x)
        lambda_max = np.linalg.norm(nuevo_mm) / np.linalg.norm(x)
        if np.abs(lambda_max - 1) < tol:
            break
    x = nuevo_mm

    v = x / np.linalg.norm(x)
    
    return lambda_max, v

#Colocando los numeros para probar
a = np.array([[11, 12], [11, 12]])
x0 = np.array([1, 1])

autovalor, autovector = metodo_potencia(a, x0)
#En este caso, el autovalor es el dominante para esta matriz dicha y se muestra el autovector correspondiente