fhand=open('py4e/dataFiles/romeo.txt')
countDict=dict()
countWords=0
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        # if word not in countDict:
        #     countDict[word]=1
        # else:
        #     countDict[word]+=1
        countDict[word]=countDict.get(word,0)+1
print(countDict)

# way1 to print dictionay
for key in countDict:
    print(key,'-->',countDict[key])
print('------------------')

#way2 to print dictionary
for key in countDict:
    if countDict[key]>=3:
        print(key,' ',countDict[key])
print('------------------')

#ways 3 sort dictionary then print
valueList=list(countDict.keys()) #keys() method saves keys 
valueList.sort()
for key in valueList:
    print(key,' ',countDict[key])
