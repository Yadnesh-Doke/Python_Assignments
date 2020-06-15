game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]

def get_winner(board):
	"""Function that checks whether any player has won. """

    for i in range(3):
        row = set(board[i])
        if len(row) == 1 and board[i][0] != 0:
            return board[i][0]

    for i in range(3):
        column = set(list([board[0][i],board[1][i],board[2][i]]))
        if len(column) == 1 and board[0][i] != 0:
            return board[0][i]

    dia1 = set(list([board[0][0],board[1][1],board[2][2]]))
    dia2 = set(list([board[0][2],board[1][1],board[2][0]]))

    if len(dia1) == 1 and board[0][0] != 0:
        return board[0][0]
    elif len(dia2) == 1 and board[0][2] != 0:
        return board[0][2]

    return 0

for sublist in game:
	print(sublist)

if get_winner(game) == 1:
    print("Player 1 wins")
elif get_winner(game) == 2:
    print("Player 2 wins")
else:
    print("No one wins!!")
