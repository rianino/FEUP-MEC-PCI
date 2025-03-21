# FUNCOES

# Identificar os numeros pares de uma lista de N numeros

def pares(lista):
    nroPares = 0
    for i in lista:
        if i % 2:
            nroPares += 1
    return nroPares

lista1 = [5, 17, 8, 83, 88, 18, 19, 20]

print(pares(lista1))