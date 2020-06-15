# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:

# without,hello,bag,world

# Then, the output should be:

# bag,hello,without,world


inp = input("Enter comma separated words to be sorted: ")

words = []
for i in inp.split(","):
    words.append(i)

words.sort()
print("After alphabetical sorting: ", end="")
print(",".join(words))
