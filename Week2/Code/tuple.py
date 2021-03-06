#!/usr/bin/env python3

""" Using list comprehension to print tuple of tuples data. """

__appname__ = 'tuple.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public'

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehensions!


# discard variable catches the NoneType list which the comprehension evaluates to, as print(arg) evaluates to NoneType.
discard = [print('Latin:\t%s\nCommon:\t%s\nWeight:\t%s\n' % bird_info) for bird_info in birds]
