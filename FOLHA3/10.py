# 10. Seja A uma matriz (m x n). Escrever um algoritmo para transformar a matriz A trocando a 
# primeira coluna com a última.

import random
import math as m
import matrizes as mz
# 9.  
# Seja A uma matriz (m x n). Escrever um algoritmo para transformar a matriz A trocando a 
# primeira linha com a última.

# MATRIZ A

print('\n\tMATRIZ A (m x n)\n')

m = int(input('m = '))
n = int(input('n = '))

linha1 = [0] * m
A = [0] * m

for i in range(m):
    A[i] = [0] * n
    for j in range(n):
        A[i][j] = random.randint(0,100)


[print(A[i]) for i in range(m)]

print('---------------------')

for i in range(m):
    A[i][0], A[i][m - 1] = A[i][m - 1], A[i][0]

[print(A[i]) for i in range(m)]
