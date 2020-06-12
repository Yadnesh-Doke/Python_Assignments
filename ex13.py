import sys

try:
    n = int(input("How many terms in fibonnaci series you want?  "))
except ValueError:
    print("Please enter a Integer number for calculation.Try again.")
    sys.exit(1)

fibo_cache = {}

def fibonacci(n):
    """Function for creating fibonacci series of a given number. """
    if n in fibo_cache:
        return fibo_cache[n]
    if n==0:
        value = 0
    elif n==1:
        value = 1
    elif n > 1:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibo_cache[n] = value
    return value

for i in range(n):
        print(fibonacci(i),end=" ")
