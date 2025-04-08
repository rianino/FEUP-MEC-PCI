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