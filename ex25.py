import sys

def guess():
    """Function that guesses the user's number. """
    i = 0
    j = 100
    m = (i + j) // 2
    counter = 1

    try:
        condition = int(input("Is "+ str(m) +" your number? (Type 0 if it's less than your no., type 1 if it is your number, or type 2 if it is higher than your no.): "))
        while condition != 1:
            counter += 1

            if condition == 0:
                i = m + 1
            elif condition == 2:
                j = m - 1

            m = (i + j) // 2
            condition = int(input("Is "+ str(m) +" your number? (Type 0 if it's less than your no., type 1 if it is your number, or type 2 if it is higher than your no.): "))

    except ValueError:
        print("Please enter a Integer number for calculation.Try again.")
        sys.exit(1)

    print(f"It took {counter} attempts to guess your number.")

if __name__ == "__main__":
    guess()
