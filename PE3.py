# Verificar se o numero é primo

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Digite um número: "))
    if is_prime(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")

if __name__ == "__main__":
    main()

# Maior Fator Primo

def maior_fator_primo(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def main():

    n = int(input("Digite um número: "))
    print(f"Maior fator primo de {n} é {maior_fator_primo(n)}")

if __name__ == "__main__":
    main()
