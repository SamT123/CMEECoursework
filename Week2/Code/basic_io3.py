#!/usr/bin/env python3


"""Script demosntrating file input and handling of arbitrary data types using pickle"""

__appname__ = 'basic_io3.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import pickle

#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}



print("\nSaving dictionary as pickle at ../Sandbox/testp.p")
f = open('../Sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
print("\nLoading dictionary from pickle at ../Sandbox/testp.p")
f = open('../Sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()
print("\nUnpickled data:")
print(another_dictionary)