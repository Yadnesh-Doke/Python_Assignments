birthday_dictionary = {"yadnesh":"08/05/1998",
                        "mahesh":"12/02/1997",
                        "yogesh":"13/11/1996",
                        "nikhil":"18/10/1997"
                        }

print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in birthday_dictionary:
    print(i.capitalize())

key = input("Who's birth date do you want to know? ")

if key.lower() not in birthday_dictionary.keys():
    print(f"Sorry! We don't know {key}'s birthday")
else:
    print(f"{key}'s birthday is ",birthday_dictionary[key.lower()])
