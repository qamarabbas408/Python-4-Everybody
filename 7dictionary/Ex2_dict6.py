# Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
fhand=open('dataFiles/data.txt')
wordsList=list()
wordsDict=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    # line=line.translate(line.maketrans('','',string.punctuation))
    # line=line.lower()
    wordsList=line.split()
    wordsList=wordsList[2:3]
    #days historgram
    for word in wordsList:
        wordsDict[word]=wordsDict.get(word,0)+1
print(wordsDict)

