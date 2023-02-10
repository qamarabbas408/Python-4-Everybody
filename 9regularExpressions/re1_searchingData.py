##regular expression
#re or regular expression is a module in python that handles tasks of searching and extracting
from gettext import find
import re
fhand=open('dataFiles/data_slice.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('From:',line): #the method search() handles same task as startwith() function returns string
        print(line)
        print(type(line))

##caret sign ^ in re:it matches the begining of a line
fhand=open('dataFiles/data_slice.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('^From ',line): #equivelent to startswith() function
        print(line)
        print(type(line))

##character matching in RE
#.. (periods) search for characters in this it will match 2 characters between F and m
#e.g.From:”, “Fxxm:”, “F12m:”, or “F!@m
fhand=open('dataFiles/data_slice.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('^F..m:',line): 
        print(line)
        print(type(line))

# + means one or more characters
# * means zero or more characters
# wildcard character
fhand=open('dataFiles/data_slice.txt')
for line in fhand:
    line=line.rstrip()
    #here search() looks for line starts with(^) From
    # then one or more characters (.+) called wildcharacter matches all character b/w colon and at-sign
    # after that and have at-sign (@) 
    if re.search('^From:.+@', line):
        print(line)
#problem with wildchard characters
str='From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu'
if re.search('^From:.+@',str): #this will print entire string..this outwardness of + is call greedy behaviour
    print(str)
    