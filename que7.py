# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# 1. At least 1 letter between [a-z]

# 2. At least 1 number between [0-9]

# 1. At least 1 letter between [A-Z]

# 3. At least 1 character from [$#@]

# 4. Minimum length of transaction password: 6

# 5. Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

import re

inp = input("Enter comma separated passwords:  \n")

passwords  = []
pattern = re.compile(".*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).*")
for password in inp.split(","):
    if (len(password)>=6 and len(password)<=12):
        if (pattern.findall(password)):
            passwords.append(password)

if len(passwords) > 0:
    print("Correct passwords are:")
    print(",".join(passwords))
else:
    print("No password matches the criteria.")
