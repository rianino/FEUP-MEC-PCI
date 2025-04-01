def soma_vetores(X,Y):
    if len(X) == len(Y):
        Z = [0] * len(X)
        for i in range(len(X)):
            Z[i] = X[i] + Y[i]
        return Z

def inputVetor():
    # Dimensao de A
    DA = int(input('Escreva a dimensão do vetor: '))
    # Dar a dimensao a A
    A = [0] * DA
    # Inserir os elementos de A
    for i in range(DA):
        A[i] = int(input(f'Insira o elemento da posicao {i + 1}: '))
    return A

def mult_vetores(A,B):
    if len(A) != len(B):
        raise ValueError('Os vetores devem ter a mesma dimensao')
    return [A[i] * B[i] for i in range(len(A))]

def escalar_vetor(k,A):
    return [k * A[i] for i in range(len(A))]

def modulo_vetor(A):
    soma = 0
    for i in range(len(A)):
        soma += A[i]**2
    modulo = soma**0.5
    return modulo

def calcula_divisores(N):
    divisores = []
    for i in range(1, N // 2):
        if N % i == 0:
            divisores.append(i)
    divisores.append(N)
    return divisores

# Ordenar o vetor com os negativos a esquerda

def ordena_esq(A):
    left = []
    mid = []
    right = []
    for i in A:
        if i < 0:
            left.append(i)
        elif i == 0:
            mid.append(i)
        else:
            right.append(i)
    Y = left + mid + right
    return Y

def novo_elimina_repete(X):
    for i in X:
        A = X.remove(i)
        for j in A:
            if j == i:
                A.remove(j)
        