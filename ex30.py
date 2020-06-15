import random

def filetolist(filename):
    """Function that adds list of words into a list and returns the list. """
    lst = []
    # file = open(filename)
    #
    # lst = []
    # line = file.readline()
    # while line:
    #     line = line.strip()
    #     lst.append(line)
    #     line = file.readline()
    with open(filename,"r") as file:
        line = file.readline()
        while line:
            line = line.strip()
            lst.append(line)
            line = file.readline()

    return lst

words = filetolist("wordsList.txt")
word = random.sample(words,1)
print("Random word picked from the file is: ",word[0])
