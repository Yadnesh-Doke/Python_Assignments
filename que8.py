# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

try:
    n = int(input("Enter maximum value of range: "))
except:
    print("Please enter Integer numbers for calculation.Try again.")
    exit(1)

div7 = (i for i in range(1,n+1) if i%7 == 0)
divBy7 = [i for i in range(1,n+1) if (i % 7 == 0)]

for i in range(len(divBy7)):
    print(next(div7), end=" ")
