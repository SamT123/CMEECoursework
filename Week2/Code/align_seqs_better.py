#!/usr/bin/env python3
"""
Sequence aligner. Finds best sequence alignment(s) (without indels) between two sequences provided
in ../Data/sequences_better.csv

INPUTS:
    None

OUTPUTS:
    ../Results/best_align_better.csv
"""

__appname__ = 'align_seqs_better.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import csv
import sys

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """
    Calculate the alignment score for a pair of sequences and a startpoint for the shorter sequence.
    
    Parameters
    ----------
    s1 : str
        the longer of the two sequences to align

    s2 : str
        the shorter of the two sequences to align

    l1 : int
        the length of the longer sequence

    l2 : int
        the length of the shorter sequence

    startpoint : int
        the position at which the shorter sequence should be placed
        for this alignment calculation

    Returns
    -------
    score : int
        number of matching base positions for this alignment

    matched : str
        per base alignment



    >>> calculate_score('ATCGATCG','TCGATCG',8,7,0)
    0, '-------'

    >>> calculate_score('ATCGTCG','TCGATCG',7,7,1)
    3, '***---'
    """

    matched = "" # to hold string displaying alignements
    score = 0


    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score, matched



def main(argv):
    """ Main entry point for program when called from terminal. Opens and 
    aligns two sequences, saving best matches to csv and printing to console """

    # read sequences from ../Data/sequences.csv

    f = open('../Data/sequences_better.csv','r')

    csvread = csv.reader(f)
    sequences = []

    for row in csvread:
        sequences.append(row[0])

    seq1, seq2 = sequences[0],sequences[1]

    # Assign the longer sequence s1, and the shorter to s2
    # l1 is length of the longest, l2 that of the shortest

    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths


    # now try to find the best match (highest score) for the two sequences

    # keep lists of best alignments, appending equally good alignments.
    my_best_align = []
    my_best_match = []
    my_best_score = -1

    for i in range(l1):
        z,match = calculate_score(s1, s2, l1, l2, i)
        # append alignment to list of best alignments if it is equally good
        if z == my_best_score:
            my_best_align.append("." * i + s2)
            my_best_match.append("." * i + match)
        # make list with only this alignment if it is better than all previous alignments
        if z > my_best_score:
            my_best_align = ["." * i + s2] # think about what this is doing!
            my_best_match = ["." * i + match]
            my_best_score = z


    # write results to file

    g = open('../Results/best_align_better.txt', 'w')

    # produce list of lines in the file
    lines = ["Best score: {} achieved {} times.".format(my_best_score,len(my_best_match))]

    for i in range(len(my_best_match)):
        lines.append('')
        lines.append(str(i))
        lines.append(my_best_match[i])
        lines.append(my_best_align[i])
        lines.append(s1)
    
    g.write("\n".join(lines))



    print("\nBest score: {} achieved {} times.\n-------------------------------".format(my_best_score,len(my_best_match)))

    for i in range(len(my_best_match)):
        print(my_best_match[i])
        print(my_best_align[i])
        print(s1)
        print('\n')
    

    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)


