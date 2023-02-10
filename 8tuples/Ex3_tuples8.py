# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour 
fhand = open('dataFiles/data.txt')
hourList=list()
hourDict=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    listLines=line.split()
    stringTime=listLines.pop(5)
    posColon=(stringTime.find(':'))
    hourList=(stringTime[:posColon].split())
    for hour in hourList:
        hourDict[hour]=hourDict.get(hour,0)+1
hoursList=list()
for key,val in list(hourDict.items()):
    hoursList.append((val,key))
    hoursList.sort(reverse=False)
for val,key in hoursList:
    print(key,'th hour', val)
