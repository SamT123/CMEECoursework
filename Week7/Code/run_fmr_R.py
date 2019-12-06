""" Script calling fmr.R to produce plot """

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