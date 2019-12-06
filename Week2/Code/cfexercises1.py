#!/usr/bin/env python3

"""A collection of trivial mathematical operations in unhelpfully named functions to demonstrate how to
organise a python program"""

__appname__ = 'cfexercises1.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import sys

# What does each of foo_x do? 
def foo_1(x=25):
    """
    compute square root of x
    PARAMETERS
    ----------
    x : int, float
        number whose root we require

    RETURNS
    -------
    str
        string stating square root

    """
    
    return '{:.4f} is the square root of {}'.format(x ** 0.5, x)

def foo_2(x=5, y=10):
    """
    return the largest of x, y
    
    PARAMETERS
    ----------
    x : int, float
    y : int, float

    RETURNS
    -------
    str
        string stating largest input value
    """
    if x > y:
        return '{} is the larger of {} and {}'.format(x,x,y)
    return '{} is the larger of {} and {}'.format(y,x,y)

def foo_3(x=3, y=2, z=1):
    """
    return x, y, z, partially sorted into descending order: 
    if x>y, switch x and y; then, if y>z, switch y and z
    
    PARAMETERS
    ----------
    x : int, float
    y : int, float
    z : int, float   

    RETURNS
    -------
    str
        string stating partially sorted list
    """


    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return 'the paritally sorted list is {}, {}, {}'.format(x,y,z)

def foo_4(x=5):
    """
    calculate factorial of x iteratively
    PARAMETERS
    ----------
    x : int, float

    RETURNS
    -------
    str
        string stating value of x factorial
    """
    # initialise result to to multiplicative identity...
    result = 1

    # iterate over all values between 1 and x, inclusive
    for i in range(1, x + 1):
        # mulktiply result by each value
        result = result * i
    return '{} is {} factorial'.format(result,x)

def foo_5(x=5): # a recursive function that calculates the factorial of x
    """
    calculate factorial of x recursively

    PARAMETERS
    ----------
    x : int, float

    RETURNS
    -------
    str
        string stating value of x factorial
    """

    # base case x = 1
    if x == 1:
        return 1

    # if x != 1, x_factorial = x-1_factorial * x
    return x * foo_5(x - 1)

def foo_6(x=5): # Calculate the factorial of x in a different way
    """
    calculate factorial of x iteratively
    PARAMETERS
    ----------
    x : int, float

    RETURNS
    -------
    str
        string stating value of x factorial
    """
    x2 = x
    facto = 1
    # iterate from x to 1, multiplying the result variable by each value
    while x >= 1:
        facto = facto * x
        x = x - 1
    return '{} is {} factorial'.format(facto,x2)


def main(argv):
    """main entry point for program. Runs mathematical functions."""
    print(foo_1(10))
    print(foo_2())
    print(foo_3())
    print(foo_4())
    print(foo_5())
    print(foo_6())

    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)


    