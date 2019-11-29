""" Script calling fmr.R to produce plot """

import subprocess

p = subprocess.Popen(["Rscript", "fmr.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # A bit silly! 
stdout, stderr = p.communicate()

if stderr != b'':
    print("error message produced:")
    print(stderr.decode())

print(stdout.decode())