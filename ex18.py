#Cows and Bulls game
import random

def compare(num,user):
    """Function that compares the user guessed number with the computer generated number. """
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

print("Let's play Cows and Bulls game!!")
while True:
    print("\nIf you want to stop the game, type 'exit'.")
    user_guess = input("Guess the 4 digit number.:  ")
    if user_guess == "exit":
        break

    if (len(user_guess) != len(number)):
        print("Please enter the 4 digit number only.Try again.")
        continue

    try:
        user_guess = int(user_guess)
    except:
        print("Please enter the 4 digit NUMBER only.")
        continue

    user_guess = str(user_guess)

    guess += 1
    cows_bulls = compare(number,user_guess)
    print(f"You have {cows_bulls[0]} cows and {cows_bulls[1]} bulls")

    if cows_bulls[0] == 4:
        print(f"You have won the game!! You took {guess} attempts.")
        break

    else:
        print("Your guess is not correct though. Plz try again.\n")
