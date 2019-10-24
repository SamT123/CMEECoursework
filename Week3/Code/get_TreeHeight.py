""" This function calculates heights of trees given distance of each tree from its base and angle to its top, using  the trigonometric formula: height = distance * tan(radians)
"""

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

# get file name from command line arg

if len(sys.argv) == 1:
    print("Need input file")
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
    writepath = "../Results/" + basename + "_treeheights.csv"

    # save dataset
    g = open(writepath, 'w')
    csvwrite = csv.writer(g)
    for row in temp:
        csvwrite.writerow(row)

    g.close()