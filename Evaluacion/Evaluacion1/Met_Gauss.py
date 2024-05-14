import numpy as np

def gauss_jordan (ma,mb,x):
    #Aqui es para de cambiar los numeros hacia tipo float
    ma = np.array(ma,dtype=float)
    mb = np.array(mb,dtype=float)

    #Aqui es para concantenar, una matriz y con el resultado correspondiente
    mab = np.concatenate((ma,mb),axis=1)

    # Pivoteo parcial por filas
    size = np.shape(mab) #En este "shape, es para separar de forma tupla, para obtener el tamaño de matriz concantenada"
    n = size[0]
    m = size[1]

    # Para cada fila en la matriz "mab" y intercambiamos la fila por el caso que el numero que se encuentra fuera de diagonal
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(mab[i:,i])
        NumMayor = np.argmax(columna)
    
    if (NumMayor !=0):
        temp = np.copy(mab[i,:])
        mab[i,:] = mab[NumMayor+i,:]
        mab[NumMayor+i,:] = temp  
    
    #Ahora ya se puede calcular el valor de x:
    for i in range(n):
        for j in range(n):
            if i != j:
                pp = mab[j][i]/mab[i][i]

                for k in range(n+1):
                    mab[j][k] = mab[j][k] - pp * mab[i][k]

    #Obtener la solucion:
    for i in range(n):
        x[i] = mab[i][n]/mab[i][i]

    #Colocar la prueba 
    """
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
    """

#El intento de comprobar:
"""
A = np.array([[2,3],
              [0,2]])

B = np.array([[4],
              [3]])
x = np.zeros(2)

print(gauss_jordan(A,B,x))
"""