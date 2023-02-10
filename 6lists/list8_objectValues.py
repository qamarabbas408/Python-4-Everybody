##is operator treats same string as single object
a='chewgum'
b='chewgum'
print(a is b ) #here is operator looks whether both variables refer to same object (same string object)

## is operator treats equivalent lists as diffrent objects
a=[1,2]
b=[1,2]
print(a is b) #False

##object assignment
#the assignment of variable with an object is called refrence
a=[1,2]
b=a #here assinging list object to variable b now both variable refrence to same object -- are equivelant and identical
print(a is b) #True 
 
##list passing to a function... the function gets a refrence to the list
def deleteLetter(t):
    del t[0]
#here we didn't return any value from the function but still value from list shown deleted at print statement
#the parameter t and variable a are said to object aliased. Aliasing means two or more variables refer to same object
a=[1,2,3,4,5,6,7]
deleteLetter(a)
print(a)

##append() and + operator
a=[1,2,3,4,5,6,7]
b=a.append(8) #the append methods modifies existing list but doesn't create new list
print(a is b) #returns false
print(b)
#on the other hand the + operator
a=[1,2,3,4,5,6,7]
b=a+ [8] #here + operator creates a new list b 
print(a)
print(b)
print( a is b ) #False