fhand=open('dataFiles/data.txt')
count=0
notFrom=0
withFrom=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    startIndex=line.find(' ')
    line=line[4:].lstrip()
    endIndex=line.find(' ')
    count=count+1
print("Total Receiptients: ",count)