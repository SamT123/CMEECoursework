#!/usr/bin/env python3

"""Program which finds divisors to demonstrate control flow."""

__appname__ = 'test_control_flow.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

## imports

import sys
import doctest
## constants

## functions

def even_or_odd(x=0):
    """
    find whether a value x is even or odd.

    Parameters 
    ----------
    x : int, float
        Number whose parity we will determine.

    Returns
    -------
    str
        '%x is Even' or '%x is Odd'

    >>> even_or_odd(10)
    '10 is Even'
    
    >>> even_or_odd(5)
    '5 is Odd'

    >>> even_or_odd('hello')
    'Please enter an int or float'
    
    if float value provided, nearest integer is used:
    >>> even_or_odd(3.2)
    '3 is Odd'
    """

    if type(x) != float and type(x) != int:
        return 'Please enter an int or float'

    # to make 'nearest integer is used' behaviour true.
    # if x % 2 == 0: 
    if round(x) % 2 == 0:
        return '%d is Even' %x
    return '%d is Odd' %x


def main(argv):
    """main entry point for program when called from command line"""
    print(even_or_odd(22))
    print(even_or_odd(33))
    return 0


if __name__ == '__main__':
    """ensures the main funtion is called from command line"""
    status = main(sys.argv)
    sys.exit(status)
