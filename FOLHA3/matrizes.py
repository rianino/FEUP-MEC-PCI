import random

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
            A[i][j] = random.randint(0,101)
    return A