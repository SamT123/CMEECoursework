"""Script to demonstrate csv input and output"""

__appname__ = 'basic_csv.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import csv


############
# FILE INPUT
############
# Open a  file for reading
f = open('../Data/testcsv.csv','r')


# Read file containing species, phylogeny, distribution and body mass data
csvread = csv.reader(f)
temp = []

# print only species name
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("The species is", row[0])

f.close()


# write a file containing only speices name and Body mass

f = open('../Data/testcsv.csv','r')
g = open('../Results/bodymass.csv', 'w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()
