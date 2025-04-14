import random
import math
# MODULO MATRIZES

def ler_matriz():
    m = int(input('Numero de linhas = '))
    n = int(input('Numero de colunas = '))
    A = [0] * m
    # Linhas
    for i in range(m):
        A[i] = [0] * n
        # Colunas
        print(f'\t--- LINHA {i + 1} ---')
        for j in range(n):
            A[i][j] = float(input(f'Coluna {j + 1} = '))
    return A

def printMz(A):
    return [print(A[i]) for i in range(len(A))]

def somaMz(A, B):
    # SOMAR AS MATRIZES
    C = [0] * len(A)
    for i in range(len(A[0])):
        C[i] = [0] * len(A[0])

    # verificar se A e B sao da mesma dimensao

    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] + B[i][j]
        return C
    else:
        raise ValueError('A devem ter a mesma dimensao')

def randMz(mm,nn):
    '''Esta funcao cria uma matriz m por n com inteiros aleatorios entre 0 e 100, inclusive'''
    A = [0] * mm
    for i in range(mm):
        A[i] = [0] * mm
        for j in range(nn):
            A[i][j] = float(random.randint(0,100))
    return A

def m_matriz_escalar(k, A):
    '''Multiplicar uma matriz por um escalar.'''
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = A[i][j] * k
    return A

def m_matriz_dp(A):
    dp = 1
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            if i == j:
                dp *= A[i][j]
    return dp

def m_matriz_ds(A):
    ds = 1
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            if i == m - (j + 1):
                ds *= A[i][j]
    return ds

def define_mat_TriangInferior(N, valor_1, valor_2):
    A = [0] * N
    for i in range(N):
        A[i] = [0] * N
        for j in range(N):
            if i > j:
                A[i][j] = valor_1
            elif i == j:
                A[i][j] = valor_2
            else:
                A[i][j] = float(random.randint(0, 11))
    return A

def transforma_linear(A,X):
    '''Calcular transformacao linear.'''
    if len(A[0]) != len(X):
        raise TypeError('A matriz e o vetor tem dimensoes incompativeis.')
    m = len(A)
    n = len(A[0])
    Ax = [0] * n
    for i in range(m):
        for j in range(n):
            Ax[i] = A[i][j] * X[j]
    return Ax

def construir_vetor(A):
    m = len(A)
    n = len(A[0])
    B = [0] * m
    for i in range(m):
        maximo = -math.inf
        for j in range(n):
            if maximo < A[i][j]:
                maximo = A[i][j]
        B[i] = maximo
    return B