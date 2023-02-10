##string to list
str='virus'
strToList=list(str) #list function converts strings to list--it breaks words into letters including white spaces
print(strToList)

##split() method it splits strings into words
str='computer is infected by a virus'
strToList=str.split()
print(strToList)
print(type(strToList))

#split() also takes a parameter which is a boundry where it splits the word
str='my-laptop-is-accer'
delimiter='-' #here - is the delimiter
strToList=str.split(delimiter)
print(strToList)

#join() method  is inverse of split() converts list back to string
delimiter=' ' #here white-space is the delimter or it can be a - 
print(delimiter.join(strToList))
print(type(delimiter.join(strToList)))

