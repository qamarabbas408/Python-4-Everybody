# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
fhand=open('dataFiles/data.txt')
domainDict=dict()
domainList=list()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    strpos=line.find('@')
    line=line[strpos:]
    endpost=line.find(' ')
    line=line[0:endpost]
    domainList=line.split()
    for domain in domainList:
        domainDict[domain]=domainDict.get(domain,0)+1
print(domainDict)


#most email received at domain
largest=None
for key in domainDict:
    if largest is None or largest<domainDict[key]:
        largest=domainDict[key]
        domainAdress=key
print('Most Emails received at: ',domainAdress, end='')
print(' are ',largest)