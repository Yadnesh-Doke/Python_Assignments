player1 = input("Player 1' name:  ")
player2 = input("Player 2' name:  ")

print("Let's start the game!!")

while True:
    print("\n")
    user1 = input(f"{player1} please select one--  rock  paper  scissor : ")
    user2 = input(f"{player2} please select one--  rock  paper  scissor : ")

    if user1 == user2:
        print("It's a tie")
    elif user1 == "rock":
        if user2 == "scissor":
            print(f"{player1} with 'rock' wins!")
        else:
            print(f"{player2} with 'paper' wins!")

    elif user1 == 'scissor':
        if user2 == 'paper':
            print(f"{player1} with 'scissor' wins!")
        else:
            print(f"{player2} with 'rock' wins!")

    elif user1 == 'paper':
        if user2 == 'rock':
            print(f"{player1} with 'paper' wins!")
        else:
            print(f"{player2} with 'scissor' wins!")

    else:
        print("Invalid input!! plz try again.")
