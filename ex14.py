
def unique_list(l):
    # return list(set(l))
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)

    return new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 34, 89]
print(unique_list(a))
