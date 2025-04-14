import random



"""
Exercício Desafio: Monitoramento de Consumo de Energia em Edifícios

Um edifício inteligente tem sensores distribuídos em diferentes áreas que medem o consumo de energia em intervalos regulares.
Esses sensores geram uma matriz C de dimensão m x n, onde cada elemento C[i][j] representa o consumo de energia (em kWh)
de uma área específica do edifício no intervalo j.

Anomalias no Consumo:
---------------------
Defina uma função analisar_consumo(C) que identifica valores anômalos de consumo de energia. 
Um valor C[i][j] é considerado anômalo se for:
- Maior que o dobro da média de consumo da coluna j (comparado com os outros intervalos da mesma área).
- Menor que metade do desvio padrão de toda a matriz (comparado com o edifício como um todo).

A função deve retornar:
- As posições (i, j) dos valores considerados anômalos.
- O número total de anomalias.

Eficiência Energética:
-----------------------
Implemente uma função calcular_eficiencia(C) que avalie a eficiência energética de cada área (linhas da matriz):
- Uma área é considerada eficiente se a média do seu consumo em todos os intervalos de tempo for menor que 10 kWh.

A função deve retornar:
- Uma lista com os índices das áreas que atendem ao critério de eficiência.

Programa Principal:
-------------------
- Gere uma matriz C com valores aleatórios entre 1 e 50 para simular o consumo de energia em m áreas e n intervalos de tempo
  (com m e n definidos pelo utilizador).
- Solicite ao utilizador um valor limite para identificar anomalias no consumo.
- Use as funções implementadas para:
    - Detetar e exibir os valores anômalos.
    - Avaliar e exibir quais áreas são energeticamente eficientes.
"""

# LER AREAS

with open('OUTROS EXS/spots.txt', 'r') as fin:
    areas = fin.read()
    areas = areas.split(', ')

# MATRIZ DOS DADOS

print('Quantas areas diferentes ha?')

m = int(input(f'Nro Areas (max {len(areas)}) = '))

n = 4

C = [0] * m

# Cada elemento da lista C vai ter uma lista com  elementos - um que mostra o numero associado,
# outro que mostra o nome da area, e um terceiro que da o valor do consumo energetico em kWh

for i in range(m):
    C[i] = [0] * n
    C[i][0] = str(i + 1) + '.'
    C[i][1] = areas[random.randrange(m)]
    C[i][2] = float(random.randint(1, 100))
    C[i][3] = None

# EXEMPLO DO FORMATO: C = [1, 'Chelas', 5.0, None] = [Nro, Nome, Consumo, Anomalidade (para depois)]
# INDICES
# 0 - Numero
# 1 - Nome da area
# 2 - Consumo em kWh
# 3 - Anomalidade (a definir)


# Verificar consumo anormal
# O consumo  e anormal se for:
# - Maior que o dobro da média de consumo da coluna j (comparado com os outros intervalos da mesma área).
# - Menor que metade do desvio padrão de toda a matriz (comparado com o edifício como um todo). 

def analisar_consumo(C):
    # Fazer a media de consumo de C[i][2]
    soma = 0
    for i in range(len(C)):
        soma += C[i][2]
    media = soma / float(len(C))
    # Calcular o desvio padrao de toda a matriz
    for i in range(len(C)):
        somaLaDentro = C[i][2]**2
    desvio = (somaLaDentro/len(C))**0.5
    anomalias = []
    for i in range(len(C)):
        if C[i][2] > 2 * media:
            C[i][3] = '!!ANORMAL!!'
            anomalias.append((i + 1,C[i][1]))
        elif C[i][2] < desvio / 2:
            C[i][3] = '!!ANORMAL!!'
            anomalias.append((i + 1,C[i][1]))
        else:
            C[i][3] = 'OK'
    return C, anomalias

def calcular_eficiencia(C):
    eficientes = []
    for i in range(len(C)):
        if C[i][2] < 10:
            eficientes.append((i + 1, C[i][1]))
    return eficientes

C, anomalias = analisar_consumo(C)

areasEficientes = calcular_eficiencia(C)

print('\n\t--- DADOS FINAIS ---')

print('--------------------------------------------------------------------------------')

for i in range(m):
    [print(C[i][j], end=' | ') for j in range(n)]
    print()
print('--------------------------------------------------------------------------------')

print('ANOMALIAS: ', anomalias)

print('AREAS EFICIENTES: ', areasEficientes)