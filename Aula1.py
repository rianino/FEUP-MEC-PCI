# Programa para determinar se um número é par

# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é par
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")