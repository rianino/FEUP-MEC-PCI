import matrizes as mz
# Sejam A e B matrizes de numeros reais
# Escreva um algoritmo para calcular a soma das matrizes

# LER AS MATRIZES

print('LER COLUNA A')
A = mz.ler_matriz()
mz.printMz(A)

print('LER COLUNA B')
B = mz.ler_matriz()
mz.printMz(B)

# SOMAR AS MATRIZES

print('\n\t--- A + B ---')
C = mz.somaMz(A, B)
print('A + B = ')
mz.printMz(C)