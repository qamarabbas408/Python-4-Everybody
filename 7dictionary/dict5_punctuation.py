##punctuation in python
import string
print(string.punctuation)

print('------------------')
##
wordList=list()
wordDictCounter=dict()
fhand=open('7dictionary/romeo_actual.txt')
for line in fhand:
    line=line.rstrip()
    # wordsList=line.split()
    # print(wordsList) #as you can see list contains words plus punctuation
    line=line.translate(line.maketrans('','',string.punctuation)) #it removes all the punction from the string
    line=line.lower()
    # print(line)
    wordsList=line.split()
    print(wordsList)
    for word in wordsList:
        wordDictCounter[word]=wordDictCounter.get(word,0)+1
print('------------------')
# print(wordDictCounter)
for key in wordDictCounter:
    print('%s --> %s'%(key,wordDictCounter[key]))