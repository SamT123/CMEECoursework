""" Script timing unoptimised and optimised versions of profileme.py """

##############################################################################
# loops vs. list comprehensions vs numpy: which is faster?
##############################################################################


# imports for squares

iters = 1000000

import timeit
import time

from profileme import my_squares as my_squares_loops

from profileme2 import my_squares as my_squares_lc

from profileme_np import my_squares as my_squares_np

# Loop timing

print("Squares\n-------")

start = time.time()
my_squares_loops(iters);
t = (time.time() - start)
print("\tLoops:\t{}".format(t))

# List comprehension timing

start = time.time()
my_squares_lc(iters);
t = (time.time() - start)
print("\tlc:\t{}".format(t))

# Numpy timing

start = time.time()
my_squares_np(iters);
t = (time.time() - start)
print("\tNumpy:\t{}".format(t))

# %timeit my_squares_loops(iters)
# %timeit my_squares_lc(iters)


##############################################################################
# loops vs. the join method for strings: which is faster?
##############################################################################

# imports for string joining

mystring = "my string"

from profileme import my_join as my_join_join

from profileme2 import my_join as my_join



print("Strings\n-------")

start = time.time()
my_join_join(iters, mystring);
t = (time.time() - start)
print("\tjoin:\t{}".format(t))

# List comprehension timing

start = time.time()
my_join(iters,mystring);
t = (time.time() - start)
print("\tConcat:\t{}".format(t))
# %timeit(my_join_join(iters, mystring))
# %timeit(my_join(iters, mystring))