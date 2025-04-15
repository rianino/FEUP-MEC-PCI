import random


# 12. Escrever um algoritmo e um programa para multiplicar duas matrizes.

# Matriz A

print('\n\t === ===   AB = C   === ===')

print('\n\t--- MATRIZ A ---\n')

print('Dimensao m x n')

mA = int(input('m = '))
nA = int(input('n = '))

print('\n\t--- MATRIZ B ---\n')

print('Dimentsao m x n\n')

mB = int(input('m = '))
nB = int(input('n = '))

if nA != mB:
    raise TypeError('\nDimensoes incompativeis.\n')

A = [0] * mA
B = [0] * mB
C = [0] * mA

for i in range(mA):
    A[i] = [0] * nA
    for j in range(nA):
        A[i][j] = random.randint(1, 10)

for i in range(mB):
    B[i] = [0] * nB
    C[i] = [0] * nB
    for j in range(nB):
        B[i][j] = random.randint(1, 10)

# Multiplicar as matrizes
# As linhas de A multiplicam com as colunas de B, para formar uma matriz com
# o mesmo numero de linhas de A e o mesmo numero de colunas de B

for i in range(mA):
    for j in range(nB):
        for k in range(nA):
            C[i][j] += A[i][k] * B[k][j]

print()

[print(A[i]) for i in range(mA)]

print()

[print(B[i]) for i in range(mB)]

print()

[print(C[i]) for i in range(len(C))]