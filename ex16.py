import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

try:
    length = int(input("Enter length of the password: "))
except ValueError:
    print("Please enter length as a Integer number.Try again.")
    exit(1)

password = "".join(random.sample(chars,length))
print(password)
