import random

class RandomWithoutReplacement:
    def __init__(self, start, end):
        self.numbers = list(range(start, end + 1))
        random.shuffle(self.numbers)

    def get(self):
        if not self.numbers:
            raise IndexError("No more numbers to pick.")
        return self.numbers.pop()

letras = 'hlvcfyifyuhjgghkhibhsfdjnfnuodsfnigfrugesr'

codigo = [24, 17, 34, 12, 39, 41]

encriptada = ''

palavra = ''

contador = 0

for i in range(6):
    encriptada += letras[codigo[i]]

while palavra != encriptada:
    palavra = ''

    randomizer = RandomWithoutReplacement(0, len(encriptada) - 1)

    for i in range(len(encriptada)):
        palavra += encriptada[randomizer.get()]

    print('==========\n')

    print(palavra)

    print('\n==========')

    contador += 1

print(f'Palavra encontrada em {contador} iteracoes.')