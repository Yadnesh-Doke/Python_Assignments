import sys

file = "namesfile.txt"
try:
    file = open(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'.")
    sys.exit(1)

line=file.readline()

count = {}
while line:
    if line.strip() in count:
        count[line.strip()] += 1
    else:
        count[line.strip()] = 1

    line = file.readline()

print(count)
