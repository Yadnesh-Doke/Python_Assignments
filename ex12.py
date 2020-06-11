import random

a = random.sample(range(1,30),5)

print("Original list:  ",a)

def newlist(a_list):
    return [ a_list[0], a_list[len(a_list)-1] ]

new_list = newlist(a)

print("New list with only first and last element: ",new_list)
