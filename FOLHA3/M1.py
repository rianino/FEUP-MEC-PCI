import modulo_acesso_ficheiros as f
A = f.le_matriz_de_ficheiro_de_texto('matrizA.txt')
print(A)
f.escreve_matriz_ficheiro('matrizB.txt', A)