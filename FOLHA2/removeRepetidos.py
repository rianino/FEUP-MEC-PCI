'''Escreva um algoritmo que modifica um vetor, eliminando todos os elementos que
estão repetidos.'''

v = [0,1,1,1,2,3,8,6,45,5,5,6,3,3,4,56,78,89,45,1]
i = 0

while i < len(v):
    j = i + 1
    while j < len(v):
        if v[j] == v[i]:
            del v[j]
        else:
            j += 1
    i += 1

print(v)