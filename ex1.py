name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
except:
    print("Please enter age as a Number.Try again.")
    exit(1)

year = (2020 - age) + 100

print(f"{name}, you will turn 100 years old in the year {year}")
