##count frequency of words in file romeo.txt retreived from web
import urllib.request
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
wordDict=dict()
for line in fhand:
    wordsLst=line.decode().split()
    for word in wordsLst:
        wordDict[word]=wordDict.get(word,0)+1
print(wordDict)