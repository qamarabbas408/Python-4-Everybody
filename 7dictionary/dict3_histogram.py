##creates a historgram using dictionay that counts no of letters appear in a word
word='neprhostomy'
countDict=dict()
for letter in word:
    if letter not in countDict:
        countDict[letter]=1
    else:
        countDict[letter]=countDict[letter]+1
print(countDict)

##get method takes key and a default value and outputs value.
listStrings={'marquard':1,'frankenstein':2,'paploo':3,'nakamura':4}
print(listStrings.get('marquard',0)) #if key is located returns value of key 
print(listStrings.get('qamar',0))   #if key is not located returns default value 0

##restructured historgram using get()
getCountDic=dict()
for letter in word:
    getCountDic[letter]=getCountDic.get(letter,0) +1
print(getCountDic)


