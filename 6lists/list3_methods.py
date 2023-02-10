nameList=['marquard','frankenstein','paploo','nakamura']
anotherNameList=['qamar','annsa']
numberList=[1,23,4,56,78,445,7,34,23,2,2,34,0]

##append()
nameList.append('qamarabbas') #adds a new item at the end of lsit
print(nameList)
##extend() adds a new list to old list 
nameList.extend(anotherNameList)
print(nameList)
##sort()
numberList.sort()
print(numberList)
##pop() removes the item from list and assigns it to new varaible 
x=nameList.pop(0)
print(x)
##del 
print(nameList)
del nameList[4] #removes the item from lis and doesnt returns any value
del nameList[2:]
print(nameList)

##remove() if you dont know the index but item name and its return value is None
nameList=['marquard','frankenstein','paploo','nakamura','annsa']
nameList.remove('annsa')
print(nameList)