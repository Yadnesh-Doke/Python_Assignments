import sys

def filetolist(filename):
    """Function that adds the contents of the file to a list and return that list. """
    lst = []
    with open(filename,"r") as file:
        line = file.readline()
        while line:
            lst.append(int(line.strip()))
            line = file.readline()

    return lst


prime_no_list = filetolist("primenumbers.txt")
happy_no_list = filetolist("happynumbers.txt")

overlapping_numbers = [num for num in prime_no_list if num in happy_no_list]
print(overlapping_numbers)
