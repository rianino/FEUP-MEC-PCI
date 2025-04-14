import random
import math as m
import matrizes as mz
# 6. Seja A uma matriz de m linhas e n colunas e X um vetor de dimensão N. 
# a) Escreva um algoritmo para multiplicar uma matriz por um vetor. 
# b) Defina a função transforma_linear(A,X) para calcular o produto da matriz A pelo 
# vetor X. 

N = int(input('N = '))

m = int(input('m = '))

n = int(input('n = '))

if n != N:
    raise TypeError(f'A matriz de dimensao {m} x {n} e o vetor de dimensao {N} nao sao multiplicaveis.')

A = [0] * m

X = [None] * N

Ax = [0] * N

for i in range(m):
    A[i] = [0] * N
    for j in range(n):
        if X[j] == None:
            X[j] = random.randint(0,100)
        A[i][j] = random.randint(0,100)
        Ax[i] = A[i][j] * X[j]

print(Ax)

print('-- Verificar --')

print(mz.transforma_linear(A,X))

