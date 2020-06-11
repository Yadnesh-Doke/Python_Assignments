board_size = int(input("Enter the board size"))

for i in range(board_size):
    print(" --- " * board_size)
    print("|    " * (board_size+1))
print(" --- " * board_size)
