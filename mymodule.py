import unittest

def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2
def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2

class TestAddFunction(unittest.TestCase):
    def add(a,b):
        """
        This function returns the sum of the given numbers
        """
        return a + b

    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")
    total = add(num1, num2)
    print ('When {} and {} are given as input the output must be {}'.format(num1, num2, total))
    assertNotEqual(total, 0, "The output should not be 0 when -2 and -2 are given as input")

unittest.main()