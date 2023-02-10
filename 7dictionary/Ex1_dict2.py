fhand=open('dataFiles/words.txt')
wordDict=dict()
words=list()
for line in fhand: 
    line=line.rstrip()
    wordsList=line.split( ) #line to wordlist
    for word in wordsList:
        words.append(word) #wordslist to words
count=0
for word in words: 
    wordDict[word]=count+1 #assinging each word to dictionary key
    count=count+1
print(wordDict)