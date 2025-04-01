import vetores as v

# Sejam A B e C vetores e k um esclar real. Escreva um programa para calcular ||(AB)C+kA||
# usando as funcoes definidas anteriormente, incluidas no modulo.

print('\t--- CALCULAR O MODULO: ||(AB)C + kA|| ---')

# Inicializar as variaveis
A = None
B = None
C = None

print('VETOR A')
A = v.inputVetor()

print('VETOR B')
B = v.inputVetor()

print('VETOR C')
C = v.inputVetor()

k = int(input('Insira o valor de k: '))

AB = v.mult_vetores(A,B)
ABC = v.mult_vetores(AB,C)
kA = v.escalar_vetor(k,A)

conta = v.soma_vetores(ABC, kA)

resultado = v.modulo_vetor(conta)

print(resultado)