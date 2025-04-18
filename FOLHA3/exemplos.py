import ola
from modulo_acesso_ficheiros import*

B = le_matriz_de_ficheiro_de_texto('FOLHA3/matriz_ler.txt')

print(ola.funcaoqualquer(B, 2))

# O código acima importa o módulo "ola" e todas as funções do módulo "modulo_acesso_ficheiros".
# Em seguida, lê uma matriz de um ficheiro de texto chamado 'matriz_ler.txt' localizado na pasta 'FOLHA3'.
# A matriz lida é armazenada na variável B.
# Por fim, chama a função "funcaoqualquer" do módulo "ola", passando a matriz B e o número 2 como argumentos,
# e imprime o resultado.