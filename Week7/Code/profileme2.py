#!/usr/bin/env python3

"""
Script containing functions producing square numbers and concatenated strings to demonstrate code profiling and optimisation.
They are implemented with list comprehension and direct str + str concatention respectively, which is faster than the 
solutions in profileme.py
"""
__appname__ = 'profileme2.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

def my_squares(iters):
    """
    Calculate all square numbers for 1 to n using list comprehension
    PARAMETERS
    ----------
    iters : int
        number of squares we want to calculate
    RETURNS
    -------
    list
        squared values of arguement iters
    """ 
    out = [i ** 2 for i in range(iters)]
    return out

def my_join(iters, string):
    """
    Join string n times, separated by ', ' using direct string concatenation

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
        out += ", " + string
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