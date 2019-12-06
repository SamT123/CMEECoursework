#!/usr/bin/env python3

""" Extracting information from tuple of tuples using for loops and list comprehensions """

__appname__ = 'lc1.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

print("\nQ1: list comprehensions\n----------------------\n")

latin_names_lc = [bird_info[0] for bird_info in birds]
print("Latin names: ")
discard = [print("\t" + n) for n in latin_names_lc]

common_names_lc = [bird_info[1] for bird_info in birds]
print("Common names: ")
discard = [print("\t" + n) for n in common_names_lc]

weights_lc = [bird_info[2] for bird_info in birds]
print("Weights: ")
discard = [print("\t" + str(w)) for w in weights_lc]

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

print("\n\nQ2: for loops\n-------------\n")

latin_names_loop = []
for bird_info in birds:
    latin_names_loop.append(bird_info[0])

print("Latin names: ")
discard = [print("\t" + n) for n in latin_names_loop]


common_names_loop = []
for bird_info in birds:
    common_names_loop.append(bird_info[1])

print("Common names: ")
discard = [print("\t" + n) for n in common_names_loop]


weights_loop = []
for bird_info in birds:
    weights_loop.append(bird_info[2])

print("Weights: ")
discard = [print("\t" + str(w)) for w in weights_loop]