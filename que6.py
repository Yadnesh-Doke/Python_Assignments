# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
sentence = input("Enter a sentence:  ")

upper = 0
lower = 0

for c in sentence:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1

print("UPPER CASE: ",upper)
print("LOWER CASE: ",lower)
