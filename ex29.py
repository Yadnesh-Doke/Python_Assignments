game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

def show_board(values=[1,1],player=0):
    game[int(values[0])-1][int(values[1])-1] = player
    for sublist in game:
        print(sublist)

def validate_input(user_input):
    if len(user_input) != 2:
        print("Input must be two numbers in format row,col e.g.  1,2 ")
        return False
    try:
        if (1 <= int(user_input[0]) <= 3) and (1 <= int(user_input[1]) <= 3):
            #check if position is already filled
            if (game[int(user_input[0])-1][int(user_input[1])-1] != 0):
                print("This position is already taken. Plz try different position.")
                return False
            else:
                return True

        else:
            print("Input values must be numbers between 1 to 3. Please enter the values again.")
            return False

    except:
        print("Input values must be NUMBERS between 1 to 3.")
        return False

def get_winner(board):
    #for rows
    for i in range(3):
        row = set(board[i])
        if len(row) == 1 and board[i][0] != 0:
            return board[i][0]

    #for columns
    for i in range(3):
        col = list([board[0][i],board[1][i],board[2][i]])
        column = set(col)
        if len(column) == 1 and board[0][i] != 0:
            return board[0][i]

    #for diagonals
    dia1 = list([board[0][0],board[1][1],board[2][2]])
    dia2 = list([board[0][2],board[1][1],board[2][0]])
    d1 = set(dia1)
    d2 = set(dia2)

    if len(d1) == 1 and board[0][0] != 0:
        return board[0][0]
    elif len(d2) == 1 and board[0][2] != 0:
        return board[0][2]

    return 0

def game_over():
    if get_winner(game) == 1:
        print("Player1 wins!! Congratulations Player1 !!")
        return True
    elif get_winner(game) == 2:
        print("Player2 wins!! Congratulations Player2 !!")
        return True
    else:
        for lst in game:
            if 0 in lst:
                return False

        print("Game over! Board is filled.")
        return True

if __name__ == "__main__":
    turn = 1
    row_col = []
    show_board()
    while not game_over():
        #ask for the user input one by one for each user
        #validate the user input.if invalid then show msg and ask again for input
        #if valid input, put the user input at the user's specified location
        #draw the board

        while not validate_input(row_col):
            player = turn % 2
            if player == 0:
                player = 2

            inp = input(f"Player {player} input: ")
            row_col = inp.split(",")

        show_board(row_col,player)

        turn += 1
        row_col = []
