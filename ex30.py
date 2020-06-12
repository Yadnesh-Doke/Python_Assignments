import random
import sys

def filetolist(filename):
    """Function that adds list of file into a list and returns the list. """
    file = open(filename)

    lst = []
    line = file.readline()
    while line:
        line = line.strip()
        lst.append(line)
        line = file.readline()

    return lst

file = "wordsList.txt"
try:
    words = filetolist(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'")
    sys.exit(1)

word = random.sample(words,1)
print("Random word picked from the file is:  ",word[0])
