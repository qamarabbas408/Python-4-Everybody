##Using RE to search and extract data 
# If we want to find numbers on lines that start with the string “X-” such as:
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000

# '^X\S*: [0-9.]+' means Search for lines that start with 'X' followed by any non  whitespace characters 
# and ':'followed by a space and any number. The number can include a decimal.
#here + operator is applied to left [0-9.] means numbers including decimal numbers
import re
fhand=open('dataFiles/data_short.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('^X\S*: [0-9.]+',line):
        numbers=line.split(' ')
        print(numbers[1])

#restructure above program using findall()
#in RE part in which we are interested are enclosed in paranthesis ([0-9.]+)
fhand=open('dataFiles/data.txt')
for line in fhand:
    line=line.rstrip()
    dsmlst=re.findall('^X\S*: ([0-9.]+)',line) #findall() will only return floating point numbers encolsed in () in lst
    if len(dsmlst) > 0:
        print(dsmlst)