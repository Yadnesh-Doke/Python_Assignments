import sys

try:
    board_size = int(input("Enter the board size: "))
except:
    print("Please enter a Integer number for calculation.")
    sys.exit(1)


for i in range(board_size):
    print(" --- " * board_size)
    print("|    " * (board_size+1))
print(" --- " * board_size)
