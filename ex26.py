game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]

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


if get_winner(game) == 1:
    print("Player 1 wins")
elif get_winner(game) == 2:
    print("Player 2 wins")
else:
    print("No one wins!!")
