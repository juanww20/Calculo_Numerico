#Importacion de la libreria
import numpy as np
from plotly import graph_objects as go

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

# Visualización 3D del autovector
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x = [0, autovector[0]],
    y = [0, autovector[1]],
    z = [0, 0],
    mode = 'lines',
    line = dict(color='blue', width=5),
    name = 'El autovector dominante'
))
fig.update_layout(
    title = 'Visualización para el dominante vector de la matriz "A"',
    scene = dict(
        xaxis = dict(title='X'),
        yaxis = dict(title='Y'),
        zaxis = dict(title='Z')
    )
)

fig.show()