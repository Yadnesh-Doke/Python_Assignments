import sys

try:
    num = int(input("Enter a number:  "))
except ValueError:
    print("Please enter a Integer number for calculation.Try again.")
    sys.exit(1)

if num > 1:
    for i in range(2,num//2):
        if num%i == 0:
            print(f"{num} is not a prime number.")
            break

    else:
        print(f"{num} is a prime number.")

else:
    print(f"{num} is not a prime number.")
