# Exercicio 14



# Exercicio 20

# Determinar se um numero é ou não um numero de Armstrong

print('\t\n---AVALIADOR DE NUMEROS DE ARMSTRONG---\n')

def numeroArmstrong(numero):

    numero = str(numero)

    # Avaliar se o número é igual à soma dos seus algarismos ao cubo
    # Soma dos algarismos ao cubo

    alg1 = int(numero[0])
    alg2 = int(numero[1])
    alg3 = int(numero[2])

    somaAoCubo = alg1**3 + alg2**3 + alg3**3

    if int(numero) == somaAoCubo:
        return True

# Determinar os 4 numeros de armstrong com 3 algarismos
listaNA = []

for i in range(100, 1000):
    if numeroArmstrong(i):
        listaNA.append(i)

print(listaNA)