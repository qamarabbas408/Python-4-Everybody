##list concatenation
nameList=['marquard','frankenstein','paploo','nakamura']
anotherNameList=['qamar','annsa']
combineNameList=nameList+anotherNameList #here + is the concatenation operator
print(combineNameList)

## list repeat operator  
anotherNameList=anotherNameList*2 #here # repeats the list items by a given number
print(anotherNameList)

##list Slices
print(combineNameList[0:2]) #from 0th to 1st not including 2nd
print(combineNameList[:3]) #from 0th to 2nd not including 3rd
print(combineNameList[2:]) #from 2nd to end
print(combineNameList[:]) #whole list
combineNameList[0:3]=['abbas','rohan','anabeya'] #updates the list
print(combineNameList)
