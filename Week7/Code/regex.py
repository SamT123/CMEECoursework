"""regex notes from lectures"""

# imports

import re
import pandas as pd 


my_string = "a given string"

match = re.search(r'\s', my_string)
print(match)
match.group()

match = re.search(r'\d', my_string)
print(match)

MyStr = 'an example'

match = re.search(r'\w*\s', MyStr) # what pattern is this?

if match:                      
    print('found a match:', match.group()) 
else:
    print('did not find a match')

match = re.search(r'2' , "it takes 2 to tango")
match.group()

match = re.search(r'\d' , "it takes 2 to tango")
match.group()

match = re.search(r'\d.*' , "it takes 2 to tango")
match.group()

match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

match = re.search(r'\s\w*$', 'once upon a time')
match.group()

re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()


re.search(r'^\w*.*\s', 'once upon a time').group() 

re.search(r'^\w*.*?\s', 'once upon a time').group()

re.search(r'<.+>', 'This is a <EM>first</EM> test').group()

re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()

re.search(r'\d*\.?\d*','1432.75+60.22i').group()

re.search(r'[AGTC]+', 'the sequence ATTCGT').group()

re.search(r'\s+[A-Z]\w+\s*\w+', "The bird-shit frog's name is Theloderma asper.").group()

re.search(r'[\w\s]+', "Sam Tu?rner").group()

#re.search(r'^abc[ab]+\s\t\d', "abcabacbcaba \t2").group()

re.search(r'\s*[a-zA-Z,\s]+\s*', '     gxzDFS,, ghd ,h GIKL       ').group()

#YYYYMMDD
re.search(r'(19\d{2}|2\d{3})[01]\d[0123]\d', '19080224').group()

MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory; Another academic, a-academic@imperial.ac.uk, Some other stuff thats equally boring; Yet another academic, y.a_academic@imperial.ac.uk, Some other stuff thats even more boring"


emails = re.findall(r'[\w\.-]+@[\w\.-]+', MyStr) 
for email in emails:
    print(email)

f = open('../data/TestOaksData.csv', 'r')
found_oaks = re.findall(r"Q[\w\s].*\s", f.read())

found_oaks

MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and ecological theory; Another academic, a.academic@imperial.ac.uk, Some other stuff thats equally boring; Yet another academic, y.a.academic@imperial.ac.uk, Some other stuff thats even more boring"

found_matches = re.findall(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+)", MyStr)
found_matches

for item in found_matches:
    print(item)

# text from webpages
import urllib3

conn = urllib3.PoolManager() # open a connection
r = conn.request('GET', 'https://www.imperial.ac.uk/silwood-park/academic-staff/') 
webpage_html = r.data #read in the webpage's contents

My_Data  = webpage_html.decode()
print(My_Data)

pattern = r"(Dr|Prof)\s+([\w']+)\s+([\w']+)"
regex = re.compile(pattern) # example use of re.compile(); you can also ignore case  with re.IGNORECASE
matches = re.findall(pattern,My_Data)
matches_unique = {' '.join(n) for n in matches}
for match in regex.finditer(My_Data): # example use of re.finditer()
    print(match.group())




