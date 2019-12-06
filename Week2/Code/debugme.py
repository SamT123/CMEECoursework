#!/usr/bin/env python3

"""Script with divide-by-zero error to demonstraste python debugging"""

__appname__ = 'debugme.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import ipdb; ipdb.set_trace()

def createabug(x):
    """function with divide by zero error"""
    y = x**4

    z = 0
    # divide by zero error
    y = y/z
    return y

createabug(25)