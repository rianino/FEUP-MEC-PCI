# Sucessao de Collatz

N = int(input('Insira N: '))

collatz = []

collatz.append(N)

while N > 1:

    if N % 2 == 0:
        N = N // 2
        collatz.append(N)

    else:
        N = N * 3 + 1
        collatz.append(N)

print(collatz)