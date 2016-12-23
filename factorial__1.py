def factorial (num):
    return num if (num == 1) else (num * factorial(num - 1))

factorial(5)
## => 120