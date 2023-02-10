##Extracting data using RE
#in previous programs we extracted emailAdresses by finding the right line
#then spliting it into addresses and so on
#by using RE we can perform same task but with more effficiency 

import re
#findall method takes two arguments RE and the string
#RE=\S+@\S+ means we are looking for substrings that have at least
# one non-whitespace character, followed by an at-sign, followed by at least one more non-whitespace character. 
# The \S+ matches as many non-whitespace or non-blank characters as possible.
str='A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst=re.findall('\S+@\S+',str) #methods returns a list
#The RE has matched with two mail addresses but not with @2PM because no  characters before at-sign
print(type(lst))
print(lst)

##using RE to extract addresses from a file
lstEmailAddress=list()
fhand=open('dataFiles/data_short.txt')
for line in fhand:
    line=line.rstrip()
    lstEmailAddress=re.findall('\S+@\S+',line)
    if len(lstEmailAddress) >0 : #if list is not empty
        print(lstEmailAddress) # PROBLEM some addresses have < > or ; characters

##restructring above program using more versatile RE 
print('----RESTRUCTRING----')
fhand=open('dataFiles/data_short.txt')
for line in fhand:
    line=line.rstrip()
    lstEmailAddress=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
    if len(lstEmailAddress)>0:
        print(lstEmailAddress) #as you notice < > are removed b/c RE says email must start with [a-zA-Z0-9] and end with a letter
#here we used more efficient RE where we are looking for substrings that start with a single lowercase letter,
#  uppercase letter, or number “[a-zA-Z0-9]”, followed by zero or more non-blank characters
# (\S*), followed by an at-sign, followed by zero or more non-blank characters (\S*), followed by an uppercase or lowercase letter. 
#\S* means asterisk applied to left i.e \S means zero or more non-blank characters
