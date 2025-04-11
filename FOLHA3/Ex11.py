import matrizes as m
# Seja A uma matriz de m linhas e n colunas
# Escreva um algoritmo que transforme uma matriz substituindo a última linha pela soma das anteriores

A = m.ler_matriz()
m.printMz(A)
print('--------------')

# Vetor soma dos elementos anteriores de cada coluna
v = [0]*len(A[0])

# Criar um vetor-linha com a soma das linhas anteriores
# Quero que o A[-1][0] seja igual a soma de A[i-1][0]
for i in range(len(A[0])):
    for j in range(len(A) - 1):
        v[i] += A[j][i]
    
A[-1] = v # Soma das anteriores

m.printMz(A)

