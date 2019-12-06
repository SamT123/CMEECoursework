"""
Calculates heights of trees of trees given in input file (or default file if input file absent)
given distance of each tree from its base and angle to its top, using  the trigonometric formula:
height = distance * tan(radians)
Saves tree heights as column in ../Results/<input_name_tree_heights>_python.csv
"""

__appname__ = 'get_TreeHeight.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import csv
import math
import sys
import os

def TreeHeight(degrees, distance):
    """Calculate a tree height given and angle and distance to the tree
    
    PARAMETERS
    ----------
    degrees : int, float
        angle from the observer to the top of the tree in degrees
        
    distance : int, float
        distance from the observer to the tree
        
    RETURNS
    -------
    height : int, float
        height of tree in same units as distnace parameter
    """
    radians = float(degrees) * math.pi / 180
    height = float(distance) * math.tan(radians)

    return height


def main(argv):
    """
    Main entry point for program. Opens passed tree data file, or uses default. Saves output file
    with tree heights to Data directorty.
    """
    # get file name from command line arg
    if len(argv) == 1 :
        print("No input file specified: using default trees.csv")
        fname = "../Data/trees.csv"
    
    elif len(argv) > 2:
        print("please provide one input file")
        return 1
    
    else:
        fname = sys.argv[1]

    # read in tree distance and angle data
    f = open(fname)
    MyDataReader = csv.reader(f)
    temp = []
    for row in MyDataReader:
        temp.append(row)
    f.close()


    # calculate heights
    heights = ['no val' for i in range(len(temp))]
    temp[0].append("Tree.Height")
    for i in range(len(temp)-1):
        temp[i+1].append(TreeHeight(temp[i+1][2],temp[i+1][1]))


    basename = os.path.splitext(os.path.basename(fname))[0]
    writepath = "../Results/" + basename + "_treeheights_python.csv"

    # save dataset
    print("Saving output csv to "+writepath+"...")
    g = open(writepath, 'w')
    csvwrite = csv.writer(g)
    for row in temp:
        csvwrite.writerow(row)

    g.close()

    return 0


if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
