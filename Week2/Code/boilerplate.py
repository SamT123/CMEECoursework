#!/usr/bin/env python3

"""A boilerplate demonstrating the structure of a Python program"""

__appname__ = 'boilerplate.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

## imports

import sys

## functions

def main(argv):
    """main entry point for program"""
    print('This is a boilerplate')
    return 0

# ensures the main funtion is called when program is run from command line
if __name__ == '__main__':
    
    status = main(sys.argv)
    sys.exit(status)
    