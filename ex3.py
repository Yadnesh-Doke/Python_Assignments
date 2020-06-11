a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Original List: ")
print(a)
print("Elements that are less than 5 are: ")

# for i in a:
#     if i<5:
#         print(i)

print([i for i in a if i<5])
