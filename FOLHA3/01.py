import matrizes as mz
from modulo_acesso_ficheiros import *
# 1. Seja A uma matriz (m linhas e n colunas) e k um escalar.  
# a) Escreva um algoritmo para multiplicar uma matriz por um escalar. 
# b) Defina a função m_matriz_escalar(A,k) para calcular o produto da matriz A pelo 
# escalar k. 

print('\n\tkA = ?\n')

# Definir k

print('\t--- ESCALAR k ---')

k = float(input('k = '))

# Definir a matriz A (input ou aleatória)

# Matriz A por input

print('\n\t--- MATRIZ A ---')
print('Matriz de m linhas e n colunas:')
m = int(input('m = '))
n = int(input('n = '))

A = [0] * m

for i in range(m):
    # Inicializar a matriz
    A[i] = [0] * n

    print(f'\n-- LINHA {i + 1} --')

    for j in range(n):
        A[i][j] = k * float(input(f'Elemento da Coluna {j + 1}: '))


# Print da matriz kA

print('\t\nkA = ')

[print(A[i]) for i in range(m)]

# Verificar a funcao

print('\n\t--- MATRIZ B ---')

print('B = 2 * kA')

B = mz.m_matriz_escalar(2, A)

escreve_matriz_ficheiro('escreverMatriz.txt', A)



def funcaoqualquer(A, k):
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= k

    return A