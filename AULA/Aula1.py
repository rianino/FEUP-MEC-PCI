
# # EXERCÍCIO 1
# print('EXERCÍCIO 1')
# # Programa para determinar se um número é par

# # Solicita ao usuário para inserir um número
# numero = int(input("Digite um número: "))

# # Verifica se o número é par
# if numero % 2 == 0:
#     print(f"O número {numero} é par.")
# else:
#     print(f"O número {numero} é ímpar.")

# EXERCICIO 2
print('-------------------')
print('EXERCÍCIO 2')
# Raizes de equações do 2
# Solicita ao usuário para inserir os coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica o número de raízes reais
if delta > 0:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes da equação são {raiz1} e {raiz2}.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A equação tem uma raiz dupla: {raiz}.")
else:
    print("A equação não tem raízes reais.")

# EXERCICIO 3
print('-------------------')
print('EXERCÍCIO 3')