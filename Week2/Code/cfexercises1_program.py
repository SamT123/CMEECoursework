#!/usr/bin/env python3

"""A collection of trivial mathematical operations in unhelpfully named functions"""

__appname__ = 'cfexercises1_program.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

import sys

# What does each of foo_x do? 
def foo_1(x=25):
    ''' compute square root of x'''
    return '{:.4f} is the square root of {}'.format(x ** 0.5, x)

def foo_2(x=5, y=10):
    '''return the largest of x, y'''
    if x > y:
        return '{} is the larger of {} and {}'.format(x,x,y)
    return '{} is the larger of {} and {}'.format(y,x,y)

def foo_3(x=3, y=2, z=1):
    '''return partially sorted x, y, z: 
    if x>y, switch x and y; then, if y>z, switch y and z'''

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
    '''calculate factorial of x iteratively'''
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return '{} is {} factorial'.format(result,x)

def foo_5(x=5): # a recursive function that calculates the factorial of x
    '''calculate factorial of x recursively'''
    if x == 1:
        return 1
    return x * foo_5(x - 1)

def foo_6(x=5): # Calculate the factorial of x in a different way
    '''calculate factorial of x iteratively'''
    x2 = x
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return '{} is {} factorial'.format(facto,x2)


def main(argv):
    '''main entry point for program'''
    print(foo_1(10))
    print(foo_2())
    print(foo_3())
    print(foo_4())
    print(foo_5())
    print(foo_6())

    return 0

if __name__ == '__main__':
    '''makes sure the main funtion is called from command line'''
    status = main(sys.argv)
    sys.exit(status)


    