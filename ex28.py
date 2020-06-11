try:
    first = int(input("Enter 1st number: "))
    second = int(input("Enter 2nd number: "))
    third = int(input("Enter 3rd number: "))
except ValueError:
    print("Please enter Integer numbers for calculation.Try again.")
    exit(1)

def largest(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c

max = largest(first,second,third)
print("The largest number is: ",max)
