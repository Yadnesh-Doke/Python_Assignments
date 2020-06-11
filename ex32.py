import random

def filetolist(filename):
    file = open(filename)

    lst = []
    line = file.readline()
    while line:
        line = line.strip()
        lst.append(line)
        line = file.readline()

    return lst

file = "wordsList.txt"
try:
    words = filetolist(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'")
    exit(1)

word = random.sample(words,1)
print("word: ",word)
word = list(word[0])

l = []
guessed = []
incorrect = 0

for i in range(len(word)):
    l.append("_")

while True:
        if incorrect < 6:
            for i in range(len(l)):
                print(l[i],end=" ")

            user = input("\nGuess your letter(plz enter a single character):  ")
            user = user.upper()
            if len(user)>1:
                print("Please enter only a single character.")
                continue

            if user in guessed:
                print("Already guessed!")
            elif user in word:
                index = word.index(user)
                l[index] = user
                word[index] = '_'
            else:
                guessed.append(user)
                print("Incorrect!")
                incorrect += 1
                print(f"You have only {6-incorrect} more incorrect guesses left.")

            if '_' not in l:
                    print("Congrats!! You have guessed it right!")
                    for i in range(len(l)):
                        print(l[i],end=" ")
                    break

        else:
            print("\nSorry you made 6 incorrect attempts.You lost the game.")
