""" OS walk exercises"""
import os
from os.path import expanduser
import subprocess

home = expanduser("~")
# Use the subprocess.os module to get a list of files and  directories 
# in your ubuntu home directory 
# 



def flatten(l):
    """
    Recursive function to flatten a list of lists, to single list contiaing elements of passed list.

    PARAMETERS
    ----------
    l : list
        list to flatten

    RETURNS
    -------
    list
        list of elements in passed l
    """
    flatter = []
    flat = True
    for item in l:
        if type(item) == list:
            flat = False
            for subitem in item:
                flatter.append(subitem)
        else:
            flatter.append(item)
    if flat:
        return flatter
    return flatten(flatter)

def get_files_and_dirs(root, recursion_depth, p):
    """
    Get list of files and directories in specified root directory, up to a specified recursion depth.

    PARAMETERS
    ----------
    root : string
        directory to find contents of
    recursion depth : int
        depth to search for files and directories -  (maximum distance from root)
    p : bool
        whether to print directories and contents to console
    """

    filesL = []
    dirsL = []
    for curr_dir, dirs, fs in os.walk(root):

        if p:
            print("files in {}:".format(curr_dir))
            for f in fs:
                print("\t{}".format(f))
            print('\n')

            print("dirs in {}:".format(curr_dir))
            for d in dirs:
                print("\t{}".format(d))
            print('\n')

        filesL.append(fs.copy())
        dirsL.append(dirs.copy())
        if curr_dir.count(os.sep) - root.count(os.sep) == recursion_depth:
                del dirs[:]

    return flatten(filesL), flatten(dirsL)


fs,ds = get_files_and_dirs(home,0,True)

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions


#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory - recursion depth 1
fs,ds = get_files_and_dirs(home,1,False)
FilesDirsStartingWithC = [[f for f in fs if f[0] == "C"], [d for d in ds if d[0] == "C"]]
print("Files/Dirs starting with C:")
print("\tFiles:")
discard = [print("\t\t"+f) for f in FilesDirsStartingWithC[0]]
print("\tDirs:")
discard = [print("\t\t"+f) for f in FilesDirsStartingWithC[1]]
print("\n")
#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:
FilesDirsStartingWithCorc = [[f for f in fs if (f[0] == "C" or f[0] == "c")], [d for d in ds if (d[0] == "C" or d[0] == "c")]]
print("Files/Dirs starting with C/c:")
print("\tFiles:")
discard = [print("\t\t"+f) for f in FilesDirsStartingWithCorc[0]]
print("\tDirs:")
discard = [print("\t\t"+f) for f in FilesDirsStartingWithCorc[1]]
print("\n")

#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:
DirsStartingWithCorc = [d for d in ds if (d[0] == "C" or d[0] == "c")]

print("Dirs:")
discard = [print("\t"+f) for f in DirsStartingWithCorc]