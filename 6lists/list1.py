##list Introduction
listNumbers=[1,23,41]
listStrings=['marquard','frankenstein','paploo','nakamura']
listMixData=[1,12,'abc','scs']
listNested=[1,2,3,[5,5,6]]
listEmpty=[]
print(listNumbers,listStrings,listNested,listEmpty)

##list are Mutable  
listNumbers[0]=66 #values can be changed
print(listNumbers)

##in operator works in list
print('abs' in listMixData) #T or F

##Traversing List ...Printing elements
for name in listStrings:
    print(name)
##Traversing list ..... update values
length=(len(listNumbers))
print(length)
for i in range(length): #range() returns indices from 0 to n-1
    listNumbers[i]=listNumbers[i]*2
print(listNumbers)

length=len(listNested)
print(length)