#Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line

# this regular expression is that we are looking for lines that start
# with From (note the space), followed by any number of characters (.*), followed by
# a space, followed by two digits [0-9][0-9], followed by a colon character. 
import re
fhand=open('dataFiles/data_short.txt')
for line in fhand:
    line=line.rstrip()
    hoursLst=re.findall('^From .* ([0-9][0-9]):',line)
    if len(hoursLst) > 0:
        print(hoursLst)