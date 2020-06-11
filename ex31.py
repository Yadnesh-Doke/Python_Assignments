word = "EVAPORATE"
word = list(word)

l = []
guessed = []

for i in range(len(word)):
    l.append("_")

while True:
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

        if '_' not in l:
                print("Congrats!! You have guessed it right!")
                for i in range(len(l)):
                    print(l[i],end=" ")
                break
