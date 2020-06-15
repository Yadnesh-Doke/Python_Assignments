# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
import sys

class GeneratorClass:
    """ This class is for creating a generator which will give the no.s divisible by 7 between a range """

    def create_generator(self,n):
        """Function which will create a generator to give numbers divisile by 7 between given range and will iterate over it"""
        div7 = (i for i in range(1,n+1) if i%7 == 0)
        divBy7 = [i for i in range(1,n+1) if (i % 7 == 0)]

        for i in range(len(divBy7)):
            print(next(div7), end=" ")


try:
    n = int(input("Enter maximum value of range: "))
except:
    print("Please enter Integer numbers for calculation.Try again.")
    sys.exit(1)
generator = GeneratorClass()
# generator.get_range()
generator.create_generator(n)
