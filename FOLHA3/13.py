import random
'''
13. Um sistema de análise e registo de dados marítimos está colocado numa plataforma 
a alguns metros da costa de uma praia atlântica. Todos os dias à mesma hora a temperatura 
da água, a salinidade e a densidade da água são registados. Estes registos vão sendo guardados 
automaticamente. Cada registo corresponde a uma temperatura a registar T, a um grau de 
salinidade S e a uma densidade D. Ao fazer o registo de cada um destes 3 dados, sempre que 
um deles: 
• ultrapassa o dobro do máximo dos valores registados nos 4 dias anteriores ou 
• é inferior a metade do mínimo dos valores registados nos 4 dias anteriores, 
é necessário lançar um alerta para que os tecnicos verifiquem se há erros nos aparelhos 
de análise, se as correntes marítimas alteraram a temperatura ou a salinidade ou se houve 
alteração da densidade da água.
'''

dias = int(input('Nro de Dias para analisar: '))

registos = [0] * dias

alertas = []

alarme = False

for i in range(dias):

    print(f'\nDIA {i + 1}')

    temperatura = float(input(f'\nTemperatura (Celsius) = '))   # registos[i][0]

    salinidade = float(input(f'\nSalinidade (%) = '))           # registos[i][1]

    densidade = float(input(f'\nDensidade (kg/m3) = '))         # registos[i][2]

    registos[i] = [temperatura, salinidade, densidade]

    if i >= 4:
        for j in range(i - 4, i):
            maximo = -9e99
            minimo = 9e99
            if registos[j][0] > maximo:
                maximo = registos[j][0]
            if registos[j][0] < minimo:
                minimo = registos[j][0]
            if temperatura > maximo * 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE TEMPERATURA ALTA !!!')
                input('\tENTER para prosseguir...')
            if temperatura < minimo / 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE TEMPERATURA BAIXA !!!')
                input('\tENTER para prosseguir...')

            maximo = -9e99
            minimo = 9e99
            if registos[j][1] > maximo:
                maximo = registos[j][1]
            if registos[j][1] < minimo:
                minimo = registos[j][1]
            if salinidade > maximo * 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE SALINIDADE ALTA !!!')
                input('\tENTER para prosseguir...')
            if salinidade < minimo / 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE SALINIDADE BAIXA !!!')
                input('\tENTER para prosseguir...')

            maximo = -9e99
            minimo = 9e99
            if registos[j][2] > maximo:
                maximo = registos[j][2]
            if registos[j][2] < minimo:
                minimo = registos[j][2]
            if densidade > maximo * 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE DENSIDADE ALTA !!!')
                input('\tENTER para prosseguir...')
            if salinidade < minimo / 2:
                alarme = True
                print(f'\n\tDia {i + 1}')
                print(f'\t!!! ALERTA DE DENSIDADE BAIXA !!!')
                input('\tENTER para prosseguir...')

    if alarme == True:
        alertas += str(i + 1)
        alarme = False


[print(registos[i]) for i in range(len(registos))]

print(f'Alertas nos dias:\n{alertas}')
