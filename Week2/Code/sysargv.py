#!/usr/bin/env python3

""" Script demonstrating how to access command line arguments in a python program """


__appname__ = 'sysargv.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public'
# imports
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))