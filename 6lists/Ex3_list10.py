fhand=open('dataFiles/romeo.txt')
wordsList=list()
uniqueWordsList=list()
print("----ORIGINAL WORD LIST-------")
for line in fhand:
    line=line.rstrip()
    wordsList=line.split()
    print(wordsList) #prints all words
    for word in wordsList:
        if word in uniqueWordsList: continue
        uniqueWordsList.append(word)
print("----UNIQUE WORD LIST-------")
uniqueWordsList.sort() #prints unique list of words
print(uniqueWordsList) #sorted list of words