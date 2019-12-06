""" Script calling fmr.R to produce plot """

__appname__ = 'run_fmr.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports

import subprocess


# open subprocess
p = subprocess.Popen(["Rscript", "fmr.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()

# check whether stderr is empty
if stderr != b'':
    # print error message to console if not empty
    print("error message produced:")
    print(stderr.decode())

# print stdout to console
print(stdout.decode())