import matrizes as mz
import random
# 8. Escreva um programa para testar a resolução da questão anterior, definindo a função 
# construir_vetor (B). 

# MATRIZ A

m = random.randint(1,10)
n = random.randint(1,10)

A = [0] * m

for i in range(m):
    A[i] = [0] * n
    for j in range(n):
        A[i][j] = float(random.randint(0, 100))

[print(A[i]) for i in range(m)]

print('----------------------')

print(mz.construir_vetor(A))