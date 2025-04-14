import matrizes as mz
from math import inf
# Seja A matriz de m linhas e n colunas

# a) Escreva um algoritmo para calcular o maximo da matriz e respetiva posicao (indice da linha e da coluna)

# DEFINIR A MATRIZ
m, n = 3, 3
A = mz.randMz(m, n)
print('\t--- MATRIZ A ---')
mz.printMz(A)

# CALCULAR O MAXIMO E INDICE DA MATRIZ

maximo = -inf
indiceMax = None

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] > maximo:
            maximo = A[i][j] 
            indiceMax = (i + 1,j + 1)
        
print('\t--- MAXIMO E INDICE ---')
print(f'MAXIMO: {maximo}')
print(f'INDICE: {indiceMax}')


# b) Defina a funcao max_matriz_indices(A) para implementar o algoritmo anterior


# c) Defina a funcao min_matriz_indices(A) para calcular o minimo da matriz A e respetiva posicao (indice da linha e coluna)