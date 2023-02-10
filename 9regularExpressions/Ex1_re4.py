##RE to search and Extract Data
# If we wanted to extract all of the revision numbers (the integer number at the end
# of these lines)  Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

# '^Details:.*rev=([0-9]+)' we are looking for lines that start with Details:, 
# followed by any number of characters (.*),  followed by rev=, and then  by one or more digits. 
import re
fhand=open('dataFiles/data.txt')
for line in fhand:
    line=line.rstrip()
    lstDetails=re.findall('^Details:.*rev=([0-9]+)',line)
    if len(lstDetails)>0:
        print(lstDetails)