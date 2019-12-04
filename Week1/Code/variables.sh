#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: variables.sh
# Desc: demonstrate use of variables
# Arguments: none
# Date: Oct 2018

# Demonstrating variable assignment
MyVar='some string'
echo 'the current value of the variable is' $MyVar
echo 'Please enter a new string'

read MyVar
echo 'the current value of the variable is' $MyVar

# Reading multiple values
echo 'Enter 2 values separated by a space'
read a b 


# check if two values were entered - echo error message if not.
if [ -z "$b" ]
then
    echo 'Error: you must enter 2 values'
else
    echo 'you entered' $a 'and' $b '. Their sum is:'

    mysum=`expr $a + $b`
    echo $mysum
fi