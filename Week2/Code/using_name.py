#!/usr/bin/env python3

""" Script demonstrating the __name_- environment variable"""

__appname__ = 'using_name.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public'

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

print("This module's name is ", __name__)