import sys

try:
    first = int(input("Enter 1st number: "))
    second = int(input("Enter 2nd number: "))
    third = int(input("Enter 3rd number: "))
except ValueError:
    print("Please enter Integer numbers for calculation.Try again.")
    sys.exit(1)

def largest(*args):
    """Function which finds the largest number etween the given 3 numbers. """
    # if a>b and a>c:
    #     return a
    # if b>a and b>c:
    #     return b
    # else:
    #     return c

    lst = []
    for i in args:
        lst.append(i)

    lst.sort()
    return lst[-1]

max = largest(first,second,third)
print("The largest number is: ",max)
