import random

def find(lst,element):
    """Function which checks existence of element in given list. """
    if element in lst:
        return True
    else:
        return False

lst = random.sample(range(1,20),5)
lst.sort()
print(f"List is:  {lst}")
print(f"Is 5 present in list? {find(lst,5)}")
print(f"Is -1 present in list? {find(lst,-1)}")
print(f"Is 8 present in list? {find(lst,8)}")
print(f"Is 12 present in list? {find(lst,12)}")
print(f"Is 36 present in list? {find(lst,36)}")
