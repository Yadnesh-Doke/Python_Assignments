# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10

# DIGITS 3


sentence = input("Enter a sentence: ")

LETTERS = 0
DIGITS = 0

for c in sentence:
    if(c.isalpha()):
        LETTERS += 1
    elif(c.isdigit()):
        DIGITS += 1

print("LETTERS: ",LETTERS)
print("DIGITS: ",DIGITS)
