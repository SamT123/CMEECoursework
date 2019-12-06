"""script demonstrating file writing"""

__appname__ = 'basic_io2.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
list_to_save = range(100)

print("Saving list to ../Sandbox/testout.txt")

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
    
    f.write(str(i) + '\n') ## Add a new line at the end

f.close()
