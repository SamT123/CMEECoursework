#!/usr/bin/env python3

"""
Script containing functions producing square numbers and concatenated strings to demonstrate code profiling and optimisation.
The squares function is implemented using numpy array operations, which are faster than list comprehensions of a for loop.
"""

__appname__ = 'profileme_np.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports

import numpy as np

def my_squares(iters):
    """
    Calculate all square numbers for 1 to n using numpy array operations
    PARAMETERS
    ----------
    iters : int
        number of squares we want to calculate
    RETURNS
    -------
    list
        squared values of arguement iters
    """ 
    out = np.arange(iters)
    out = out**2
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