##list of words sort them from longest to smallest
#D Decorator:a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
#S sort
#U Unsorted
txt = 'but soft what light in yonder window breaks'
words = txt.split()
# wordsSorted=words.sort(reverse=True)
# print(wordsSorted) #print None
t = list()
for word in words:
    t.append((len(word), word)) #builds list of tuples each tuple is preceded by its length--DECORATOR
print(t) 
t.sort(reverse=True) #sort
print(t)
res = list()
for length, word in t:
    res.append(word) #removing sorted keys UNDECORATED
print(res)