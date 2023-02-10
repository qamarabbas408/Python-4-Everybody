##parse the data
fhand=open('dataFiles/data_slice.txt')
print(fhand)
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    print(words[2:])
