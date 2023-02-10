data='From qmarabbas715@gmail.com Friday,25,2022'

#finding emailProvider
findPos_at_rate=data.find('@')
print(findPos_at_rate)
space_after_at_rate=data.find(' ',findPos_at_rate)
print(space_after_at_rate)

while findPos_at_rate < space_after_at_rate:
    print(data[findPos_at_rate+1],end='')
    findPos_at_rate=findPos_at_rate+1

print('\n---------------')
#finding emailId 
findPos=data.find('F')
findWhiteSpace=data.find(' ',findPos)

findPos_at_rate=data.find('@')
print(type(findPos_at_rate))
print(findPos_at_rate,findWhiteSpace)
while findWhiteSpace < findPos_at_rate:
    print(data[findWhiteSpace+1],end='')
    findWhiteSpace=findWhiteSpace+1
