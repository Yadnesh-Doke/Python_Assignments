file = "namesfile.txt"
try:
    file = open(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'.")
    exit(1)

line=file.readline()

count = {}
while line:
    name = line.strip()
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

    line = file.readline()

print(count)
