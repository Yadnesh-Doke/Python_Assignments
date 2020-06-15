import random

num = random.randint(1,9)

guess = 0

while guess != num:
    try:
        guess = int(input("Guess the number between 1 to 9: "))
    except ValueError:
        print("Please enter a Integer number for calculation.Try again.")
        continue

    if guess<num:
        print("Too low!")
    elif guess>num:
        print("Too high!")
    elif(guess == num):
        print("Your guess mathced!!")
