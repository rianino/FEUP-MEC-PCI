from modulo_acesso_ficheiros import *

A = le_matriz_de_ficheiro_de_texto('FOLHA3/matriz_ler.txt')

# B = kA

k = float(input('k = '))

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = A[i][j] * k

escreve_matriz_ficheiro('FOLHA3/matriz_escrever.txt', A)

