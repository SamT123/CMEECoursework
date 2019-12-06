#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: MyExampleScript.sh
# Desc: Demonstrate environment variables
# Arguments: none
# Date: Oct 2018

msg1='Hello'
# $USER is an environment variable which evaluates to the user's system username
msg2=$USER
echo "$msg1 $msg2"
echo "Hello $USER"
echo
