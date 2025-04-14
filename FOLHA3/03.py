import random
import math as m
import matrizes as mz
# 3. Seja N um número inteiro e valor_1, valor_2 escalares reais.  
# a) Escreva um algoritmo para definir uma matriz A de ordem N triangular inferior em 
# que todos os elementos abaixo da diagonal principal são iguais a valor_1 e na 
# diagonal principal valor_2. 
# b) Defina a função define_mat_TriangInferior(N, valor_1, valor_2) para 
# implementar o algoritmo.

N = int(input('N = '))

valor_1 = float(input('Valor 1 = '))

valor_2 = float(input('Valor 2 = '))

A = [0] * N

for i in range(N):
    A[i] = [0] * N
    for j in range(N):
        if i > j:
            A[i][j] = valor_1
        elif i == j:
            A[i][j] = valor_2
        else:
            A[i][j] = float(random.randint(0, 11))

[print(A[i]) for i in range(N)]

print('-----------------------------')

B = mz.define_mat_TriangInferior(N, valor_1, valor_2)

[print(B[i]) for i in range(N)]