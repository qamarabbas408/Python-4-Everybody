# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
fhand=open('dataFiles/data.txt')
emailAddressDict=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    listLine=line.split()
    emailAddress=listLine.pop(1)
    emailAddressList=emailAddress.split()
    for emailAddress in emailAddressList:
        emailAddressDict[emailAddress]=emailAddressDict.get(emailAddress,0)+1
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most commits.
counterList=list()
largestVal=None
for email,count in list(emailAddressDict.items()):
    counterList.append((count,email)) #created a (count,email) tuples 
    if largestVal is None or largestVal < count:
        largestVal=count
        largestKey=email
    counterList.sort(reverse=True)

print(counterList)
print(largestVal,largestKey)
