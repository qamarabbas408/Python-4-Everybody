import string
fhand=open('dataFiles/romeo_full.txt')
# print(fhand)
wordsDict=dict()
wordsList=list()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    wordsList=line.split()
    for word in wordsList:
        wordsDict[word]=wordsDict.get(word,0)+1

#sorting words dictionary by  it values
sortedList=list()
for key,val in list(wordsDict.items()):
    sortedList.append((val,key))
sortedList.sort(reverse=True)
for val,key in sortedList[:10]:
    print(val,' ',key)