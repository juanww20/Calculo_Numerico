import numpy as np
from numpy.random import *

#Creacion vector/matriz
m1 = np.array([1,2,3,4])
m2 = np.array([[1,2],[3,4]])

print(m1)
print(np.array(10))
print(np.arange(10)) #genera vector Se puede trabajar como ciclo for
print(np.linspace(1., 4., 6))

a = np.eye(3)
print(a)

b = np.diag([1,2,3])
print(b)

c = np.zeros((2,5))
print(c)

d = np.ones((5,5,2))
print(d)

e = default_rng(2).random((2,3))
print(e)
