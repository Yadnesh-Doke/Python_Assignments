
def unique_list(l):
    """Function that returns new list that contains all the elements of the given list without duplicates """
    # return list(set(l))
    # new_list = []
    # for i in l:
    #     if i not in new_list:
    #         new_list.append(i)

    new_list = [i for n,i in enumerate(l) if i not in l[:n]]

    return new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 34, 89]
print(unique_list(a))
