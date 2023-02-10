
import string
import re
fhand=open('dataFiles/namesList.txt')
letterDict=dict()
letterlst=list()
total=0
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()    
    alphabets=re.findall('[a-z]',line)
    if len(alphabets) > 0:
        for letter in alphabets:
            letterDict[letter]=letterDict.get(letter,0)+1
largest=None
totalPer=0
print(letterDict)
print('____________FREQUENCY_____________')
for key,val in letterDict.items():
    total=total+int(val)
    letterlst.append((key,val))
    if largest is None or largest < letterDict[key] :
        largest=val
        largestKey=key
    letterlst.sort()
for letter in letterlst:
    appPercentage=float((letter[1]*100)/total)
    totalPer=appPercentage+totalPer
    print(letter[0],'\t',letter[1],'\t Times Appeared:\t',appPercentage ,'%')
print('Total Count',total)
print('Most Appeared letter: ',largestKey)
print(totalPer)