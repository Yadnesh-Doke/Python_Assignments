import json
import sys

file = "birthdays.json"
try:
    f = open(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'")
    sys.exit(1)

birthday_dictionary = json.load(f)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in birthday_dictionary:
    print(i.capitalize())

key = input("Who's birth date do you want to know? ")

if key.lower() not in birthday_dictionary.keys():
    print(f"Sorry! We don't know {key}'s birthday")
else:
    print(f"{key}'s birthday is ",birthday_dictionary[key.lower()])
