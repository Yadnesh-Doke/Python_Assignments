string = input("Enter a string:  ")

lst = string.split()

# for i in reversed(lst):
#     print(i,end=" ")

# for i in lst[::-1]:
#     print(i,end=" ")

print(" ".join(lst[::-1]))
