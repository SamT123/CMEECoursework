#!/usr/bin/env python3

"""
Script containing functions producing square numbers and concatenated strings to demonstrate code profiling and optimisation.
They are implemented with a for loop and the .join() string method respectively.

"""

__appname__ = 'profileme.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

def my_squares(iters):
    """
    Calculate all square numbers for 1 to n using iteration
    PARAMETERS
    ----------
    iters : int
        number of squares we want to calculate
    RETURNS
    -------
    list
        squared values of arguement iters
    """
    out = []
    for i in range(iters):
        out.append(i ** 2)
    return out

def my_join(iters, string):
    """
    Join string n times, separated by ', ' using str.join() method

    PARAMETERS
    ----------
    iters : int
        number of copies of the string to be joined
    string : str
        string to join

    RETURNS
    -------
    str
        joined string
    """
    out = ''
    for i in range(iters):
        out += string.join(", ")
    return out

def run_my_funcs(x,y):
    """
    Run my_squares and my_join, for the purpose of profiling

    PARAMETERS
    ----------
    x : iters
        the number of iterations for my_squares and my_join
    y : str
        string to pass to my_join

    RETURNS
    -------
    0
    """
    print("iters: " + str(x) + ", str: " + str(y))
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
