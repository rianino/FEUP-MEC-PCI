import random
import math as m
import matrizes as mz

# 2. Seja A uma matriz de ordem N.  
# a) Escreva um algoritmo para multiplicar os elementos da diagonal principal. 
# b) Escreva um algoritmo para multiplicar os elementos da diagonal não principal. 
# c) Defina as funções m_matriz_dp(A) e m_matriz_ds(A) para implementar 
# respetivamente as alíneas anteriores.

# Matriz A (Aleatória)

print('\n\t--- MATRIZ A ---\n')

print('A e uma matriz de m linhas e n colunas: \n')

m = int(input('m = '))
n = int(input('n = '))

print('Foi gerada uma matriz aleatória de inteiros entre 0 e 100 (inclusive)...')

# Inicializar multiplicacao das diagonais

diagPrincipal = 1
diagNaoPrincipal = 1

# Definicao da matriz e calculos

A = [0] * m

for i in range(m):
    A[i] = [0] * n
    for j in range(n):
        A[i][j] = random.randint(0, 100)
        if i == j:
            diagPrincipal *= A[i][j]
        if i == m - (j + 1):
            diagNaoPrincipal *= A[i][j]

print('\t--- Matriz Aleatoria A ---')

[print(A[i]) for i in range(m)]

print(f'\nProduto dos elementos da diagonal principal = {diagPrincipal}')

print(f'\nProduto dos elementos da diagonal NAO principal = {diagNaoPrincipal}\n')


print('\n\t--- VERIFICAR FUNCOES ---')

print(f'Diagonal Principal: {mz.m_matriz_dp(A)}')

print(f'Diagonal Secundaria: {mz.m_matriz_ds(A)}')