#!/usr/bin/env python3

"""Program which finds divisors to demonstrate control flow."""

__appname__ = 'control_flow.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

## imports

import sys

## constants

## functions

def even_or_odd(x=0):
    """find whether a value x is even or odd"""
    if x % 2 == 0:
        return '%d is Even' %x
    return '%d is Odd' %x

def largest_divisor_five(x=10):
    """find which is the largest diviosr of x amongst 2,3,4,5."""
    largest = 0
    if x % 5 == 0:
        largest = 5
    elif x % 4 == 0: #means "else, if"
        largest = 4
    elif x % 3 == 0:
        largest = 3
    elif x % 2 == 0:
        largest = 2
    else: # When all other (if, elif) conditions are not met
        return "No divisor found for %d!" % x # Each function can return a value or a variable.
    return "The largest divisor of %d is %d" % (x, largest)

def is_prime(x=70):
    """Find whether an integer is prime."""
    # loop over all values between 2 and x to check for divisors
    for i in range(2, x): #  "range" returns a sequence of integers
        if x % i == 0:
          print("%d is not a prime: %d is a divisor" % (x, i)) 
          return False
    print("%d is a prime!" % x)
    return True 

def find_all_primes(x=22):
    """Find all the primes up to x"""
    allprimes = []
    # loop over all ints up to x to check if they are prime
    for i in range(2, x + 1):
      if is_prime(i):
        allprimes.append(i)
    print("There are %d primes between 2 and %d" % (len(allprimes), x))
    return allprimes


def main(argv):
    """main entry point of program when called from terminal"""
    print(even_or_odd(22))
    print(even_or_odd(33))
    print(largest_divisor_five(120))
    print(largest_divisor_five(121))
    print(is_prime(60))
    print(is_prime(59))
    print(find_all_primes(100))
    return 0



if __name__ == '__main__':
    '''ensures the main funtion is called from command line'''
    status = main(sys.argv)
    sys.exit(status)
    