""" Script containing functions to demonstrate code profiling and optimisation - functions constructed using numpy array operations """


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
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")