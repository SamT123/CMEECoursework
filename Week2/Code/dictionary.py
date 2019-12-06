#!/usr/bin/env python3

""" Creates dictionary of Order - Taxon relationships, and prints these relationships """

__appname__ = 'dictionary.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

taxa = [
         ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 


# produce a dictionary {order1: set(), order2: set()... }
print('finding orders...\n')
taxa_dic = {order_taxon_pair[1]: set() for order_taxon_pair in taxa}

# populate dictionary by looping over tuples in taxa list
print('adding taxa...\n')
for taxon,order in taxa:
        taxa_dic[order].add(taxon)

# print dictionary
for order in taxa_dic.keys():
        print('Order:\t', order)
        s=''.join((ind + ', ') for ind in taxa_dic[order])
        print('Taxa:\t', s[:-2])
        print('\n')
