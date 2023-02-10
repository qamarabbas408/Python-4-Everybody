#counting no of values
count=0
for iterval in [2,3,234521,522342334,546234,345,3,2342,23,2424]:
    count=count+1
print('Number of Values',count)

#summing multiple values
total=0
for iterval in [2,3,234521,522342334,546234,345,3,2342,23,2424]:
    total=total + iterval
print('Sum of Values are', total)

#Maximum Value
largest=None
print ("Before: Largest= ", largest)
for iterval in [2,3,234,5234,5234,345,3,2342,23,2343423]:
    if largest is None or largest < iterval:
        largest=iterval
    print('array value',iterval,' largest= ',largest)

print('----------------------')
#smallest Value
smallest=None
print ("Before: Smallest= ", smallest)
for iterval in [2,3,234521,522342334,546234,345,3,2342,23,2424,0]:
    if smallest is None or smallest > iterval:
        smallest=iterval
    print('array value',iterval,' smallest= ',smallest)

