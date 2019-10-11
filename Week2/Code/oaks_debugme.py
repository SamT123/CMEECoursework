

"""
Program which determines whether a species falls within the oak genus, Quercus.
"""

__appname__ = 'oaks_debugme.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 
import csv
import sys
import stringdist

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' 
    >>> is_an_oak('Fagus sylvatica')
    False

    >>> is_an_oak('QuercAs 123')
    '\n***THIS LOOKS LIKE A TYPO***\n'
    False

    >>> is_an_oak('QuercusX abc')
    '\n***THIS LOOKS LIKE A TYPO***\n'
    False

    >>> is_an_oak('QuErCuS abc')
    True

    >>> is_an_oak('quercus xyz')    
    True
    """

    if name.split(' ')[0].lower() == 'quercus':
        return True
    elif stringdist.rdlevenshtein(name.split(' ')[0].lower(), 'quercus') <= 2:
        print('\n***THIS LOOKS LIKE A TYPO***\n')
        return False
    else:
        return False

def main(argv):
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    csvwrite.writerow(['Genus', 'species'])
    oaks = set()
    for row in taxa:
        if row[0] != 'Genus':
            print(row)
            print ("The genus is: ") 
            print(row[0] + '\n')
            if is_an_oak(row[0]):
                print('FOUND AN OAK!\n')
                csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

