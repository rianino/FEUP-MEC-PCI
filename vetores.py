def soma_vetores(X,Y):
    if len(X) == len(Y):
        Z = [0] * len(X)
        for i in range(len(X)):
            Z[i] = X[i] + Y[i]
        return Z

def inputVetor():
    # Dimensao de A
    DA = int(input('Escreva a dimensão de A'))
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









# Converter números decimais para binário
def binario(N):
    resto = ''
    binario = ''

    # N e um numero decimal, obter os restos da divisao de N por 2
    while N > 1:
        resto += str(N % 2)
        N = N // 2
    
    # Inverter a ordem do resto
    for i in range(len(resto) - 1, -1, -1):
        binario += resto[i]
    return binario