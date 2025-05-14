'''
1. Escreva um algoritmo para calcular as seguintes operações: 
a) soma de dois vetores; 
b) norma de um vetor; 
c) produto interno de dois vetores; 
d) produto de um vetor por um escalar real;
'''

v = [1,2,3,4]

u = [5,6,7,8]

# Soma de dois vetores

vMu = [0] * len(v)

# u + v

for i in range(len(u)):
    vMu[i] = v[i] + u[i]

print(vMu)

# Norma

somaQuadrado = 0

for i in range(len(v)):
    somaQuadrado += v[i]**2

norma_v = somaQuadrado**0.5

print(round(norma_v, 2))

# Produto interno

prodint = 0

for i in range(len(v)):
    prodint += v[i] * u[i]

print(prodint)

# Produto de um vetor por um escalar real

k = 1.342
kv = [0] * len(v)

for i in range(len(v)):
    kv[i] = k * v[i]

print(kv)