with open("namesfile.txt","r") as file:
    line=file.readline()
    count = {}
    while line:
        if line.strip() in count:
            count[line.strip()] += 1
        else:
            count[line.strip()] = 1

        line = file.readline()

    print(count)
