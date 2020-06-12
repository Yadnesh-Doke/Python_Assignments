import sys

def filetolist(filename):
    """Function that adds the contents of the file to a list and return that list. """
    file = open(filename)
    line = file.readline()

    lst = []
    while line:
        lst.append(int(line.strip()))
        line = file.readline()

    return lst

file1 = "primenumbers.txt"
file2 = "happynumbers.txt"
try:
    prime_no_list = filetolist(file1)
except FileNotFoundError:
    print(f"No such file found named '{file1}'")
    sys.exit(1)

try:
    happy_no_list = filetolist(file2)
except FileNotFoundError:
    print(f"No such file found named '{file2}'")
    sys.exit(1)

overlapping_numbers = [num for num in prime_no_list if num in happy_no_list]
print(overlapping_numbers)
