import random

class RandomWithoutReplacement:
    def __init__(self, start, end):
        self.numbers = list(range(start, end + 1))
        random.shuffle(self.numbers)

    def get(self):
        if not self.numbers:
            raise IndexError("No more numbers to pick.")
        return self.numbers.pop()


while True:

    letras = ['g','i','n','g','e','r']

    palavra = ''

    randomizer = RandomWithoutReplacement(0, len(letras) - 1)
    for i in range(len(letras)):
        palavra += letras[randomizer.get()]

    print('==========\n')

    print(palavra)

    print('\n==========')

    input()
