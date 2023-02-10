fhand=open('dataFiles/data.txt')
lineList=list()
emailIdList=list()
emailDict=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    lineList=line.split()
    emailIdList=lineList.pop(1) #pop returns string 
    emailIdList=emailIdList.split() #convert back list
    for email in emailIdList:
        emailDict[email]=emailDict.get(email,0)+1
for key in emailDict:
    print(key,'-->',emailDict[key],' ', end='')


# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
print('\n')
largest=None
EmailAdress=None
for key in emailDict:
    if largest is None or largest < emailDict[key]:
        largest=emailDict[key]
        emailAdress=key
print(largest,'Most mails received by: ',end='')
print(emailAdress)