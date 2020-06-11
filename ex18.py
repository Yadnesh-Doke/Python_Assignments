#Cows and Bulls game
import random

def compare(num,user):
    cows_bulls = [0,0]
    for i in range(len(num)):
        if user[i] in num:
            if num[i] == user[i]:
                cows_bulls[0] += 1
            else:
                cows_bulls[1] += 1

    return cows_bulls

guess = 0
number = str(random.randint(0,9999))

while True:
    print("Let's play Cows and Bulls game!!")
    print("If you want to stop the game, type 'exit'.")
    user_guess = input("Guess the 4 digit number.:  ")
    if user_guess == "exit":
        break

    guess += 1
    cows_bulls = compare(number,user_guess)
    print(f"You have {cows_bulls[0]} cows and {cows_bulls[1]} bulls")

    if cows_bulls[0] == 4:
        print(f"You have won the game!! You took {guess} attempts.")
        break

    else:
        print("Your guess is not correct though. Plz try again.\n")
