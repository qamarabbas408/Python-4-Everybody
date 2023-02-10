#  Write a program to look for lines of the form:
#  such as: New Revision: 39772 in file data.txt
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.
import re 
revNumberLst=list()
sum=0
count=0
fhand=open('dataFiles/data.txt')
for line in fhand:
    line=line.rstrip()
    revNumberLst=re.findall('^New [a-zA-z]+: ([0-9]+)',line)
    if len(revNumberLst) > 0:
        for number in revNumberLst:
            sum=int(number)+sum
            count=count+1
print(sum)
print(count)
print('Average Revision Number is: ',int(sum/count))