#!/usr/bin/env python3

"""
Sequence aligner. Finds best sequence alignment (without indels) between two sequences provided
from the command line in the form:

python3 align_seqs_fasta seq1.fasta seq2.fasta

Alternatively, if no command line args are provided, default fasta sequences will be used.
Results are written to ../Results/best_align_fasta.csv.

INPUTS:
    arg1 : .fasta file
    arg2 : .fasta file

OUTPUTS:
    ../Results/best_align_fasta.csv.

"""

__appname__ = 'align_seqs_fasta.py'
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

    # # some formatted output
    # print("." * startpoint + matched)           
    # print("." * startpoint + s2)
    # print(s1)
    # print(score) 
    # print(" ")

    return score, matched



# Two example sequences to match

def main(argv):
    """ Main entry point for program when called from terminal. Opens passed fasta files, or defaults.
    Finds one best alignment (discarding others of equal score), saving to csv and printing to console """

    # determine whether command line args are provided correctly.
    if len(argv) == 1:
        print('\nNo file path arguments provided: using default .fasta files: 407228326.fasta, 407228412.fasta\n')
        f1 = open('../Data/fasta/407228326.fasta','r')
        f2 = open('../Data/fasta/407228412.fasta','r')
    

    elif len(argv) == 2 or len(argv) > 3:
        print('Please provide two fasta files to align. Otherwise, provide no files to use default .fasta files.')
        return 1


    elif len(argv) == 3:
        print('\nUsing provided fatsa files: ', argv[1], argv[2] )
        f1 = open(argv[1],'r')
        f2 = open(argv[2],'r')

    # read sequences from fasta files

    csvread1 = csv.reader(f1)
    seq1_list = []

    for row in csvread1:
        seq1_list.append(row[0])

    csvread2 = csv.reader(f2)
    seq2_list = []

    for row in csvread2:
        seq2_list.append(row[0])

    seq1 = ''.join(s for s in seq1_list[1:])
    seq2 = ''.join(s for s in seq2_list[1:])

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
    my_best_align = None
    my_best_match = None
    my_best_score = -1

    for i in range(l1): # Note that you just take the last alignment with the highest score
        z,match = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_match = "." * i + match
            my_best_align = "." * i + s2 # think about what this is doing!
            my_best_score = z
        if i%1000 == 0:
            print(str(i) + ' / ' + str(l1) + ' comparisons complete')


    # write results to file

    g = open('../Results/best_align_fasta.txt', 'w')
    g.write("\n".join([my_best_match, my_best_align, s1,"Best score:\t" + str(my_best_score), "Lengths:\t" + str(l1), str(l2)]))


    print("\nBest score: " + str(my_best_score)) 
    print("Best alignment saved to ../Results/best_align_fasta.csv")

    # sequences too ong to meaningfully print to terminal
    # print(my_best_align)
    # print(s1)
    # print("Best score:", my_best_score)

    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)