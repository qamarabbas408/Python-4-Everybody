some_string='Hello i am a string'
print(type(some_string))
# print(dir(some_string))  #lists methods available for string objects
# print(help(str.capitalize)) #provides help about the method

#calling syntax to methods is diffrent from functions
some_string=some_string.capitalize() #object.methodName() and a method call is call invocation
print(some_string)
some_string=some_string.upper()
print(some_string)

#find()
word='laptop'
index=word.find('a') #returns the index of the word
print(index)

#strip
some_string='  Hello i am a string     '
print(some_string.strip()) #removes spaces from beginning and end of the string

#startwith() returns  T or F
some_string='hello paksistan'
print(some_string.startswith('hello'))

#lower()
some_string='ADCDASD'
print(some_string.lower())