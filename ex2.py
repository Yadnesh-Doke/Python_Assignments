try:
    n = int(input("Enter a number: "))

    if n%2 == 0:
        print(f"{n} is a even number")
    else:
        print(f"{n} is a odd number")

except ValueError:
    print("Please enter a Integer number for calculation.Try again.")
