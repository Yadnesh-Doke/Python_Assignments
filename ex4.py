try:
    num = int(input("Enter a number:  "))

    divisor = []
    for i in range(1,num+1):
        if num%i == 0:
            divisor.append(i)

    print(f"Divisors of {num} are")
    print(divisor)

except ValueError:
    print("Please enter a Integer number for calculation.Try again.")
