# Fibonacci sequence whose values do not exceed 4 million - find the sum of even-valued terms.

fibo0 = 0
fibo1 = 1
fiboSum = 0

while fibo1 <= 4000000:
    if fibo1 % 2 == 0: fiboSum += fibo1
    fibo0, fibo1 = fibo1, fibo0 + fibo1

print(fiboSum)