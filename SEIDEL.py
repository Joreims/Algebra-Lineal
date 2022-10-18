# -*- coding: utf-8 -*-
# Algoritmo Gauss-Seidel,
# matrices, métodos iterativos
# ingresar iteramax si requiere más iteraciones

# Gauss Jordan
# Supone que los elementos de diagonal no son cero
# Tarea: verificar diagonal no tiene ceros
# Muestra proceso
import numpy as np

# INGRESO
A = np.array([[8,2,-2],
              [10,2,4],
              [12,2,2]])

B = np.array([[-2],
              [4],
              [6]])

# PROCEDIMIENTO
# Matriz aumentada
AB = np.concatenate((A,B), axis=1)
print('matriz ampliada:')
print(AB)

print(' *** Gauss elimina hacia adelante ***')
casicero = 0 # 1e-15
# Gauss elimina hacia adelante
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]
for i in range(0,n,1):
    pivote = AB[i,i]
    adelante = i+1 
    for k in range(adelante,n,1):
        if (np.abs(AB[k,i])>=casicero):
            coeficiente = pivote/AB[k,i]
            AB[k,:] = AB[k,:]*coeficiente - AB[i,:]
        else:
            coeficiente= 'division para cero'
        print('coeficiente: ',coeficiente)
        print(AB)

print(' *** Gauss-Jordan elimina hacia atras *** ')
# Gauss-Jordan elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    # Normaliza a 1 elemento diagonal
    AB[i,:] = AB[i,:]/AB[i,i]
    pivote = AB[i,i] # uno
    # arriba de la fila i
    atras = i-1 
    for k in range(atras,0-1,-1):
        if (np.abs(AB[k,i])>=casicero):
            coeficiente = pivote/AB[k,i]
            AB[k,:] = AB[k,:]*coeficiente - AB[i,:]
        else:
            coeficiente= 'division para cero'
        print('coeficiente: ', coeficiente)
        print(AB)
X = AB[:,ultcolumna]
X = np.transpose([X])

# SALIDA
print('ampliada: ')
print(AB)
print('X: ')
print(X)
