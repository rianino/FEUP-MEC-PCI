import matrizes as mz
from math import inf
# Seja A uma matriz de m linhas e n colunas
# a) Escreva um algoritmo que define um vetor B em que o i-esimo elemento de B e igual ao elemento maximo da linha i da matriz dada

# MATRIZ DADA

print('\t--- MATRIZ DADA ---')
m = 3
n = 3
A = mz.randMz(m,n)
mz.printMz(A)

# VETOR B

B = [0] * n

# ELEMENTO MAXIMO DA LINHA

print('\t--- MAXIMOS DAS LINHAS ---')
for i in range(m):
    maximo = -inf
    for j in range(n):
        if maximo < A[i][j]:
            maximo = A[i][j]
    B[i] = maximo
    print('[', maximo,']')



# b) Escreva um algoritmo que define um vetor B em que o i-esimo elemento de B e igual ao elemento minimo da linha i da matriz dada

print('\t--- MINIMOS DAS LINHAS ---')
for i in range(m):
    minimo = inf
    for j in range(n):
        if minimo > A[i][j]:
            minimo = A[i][j]
    B[i] = minimo
    print('[', minimo,']')