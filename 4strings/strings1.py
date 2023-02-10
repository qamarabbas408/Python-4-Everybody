game='Anno1800_CityBuilderGame'
print(len(game))
lastletter=len(game)-1
# print(game[lastletter])

#traversel through a string forward
count=0
for index in game:
    count=count+1
    # print(index)
print('Total Letters',count)

print('-------------')
#traversel through a string backward
index=len(game)-1
while index >=0:
    # print(game[index])
    index=index-1

#slicing 
print(game[0:10])
print(game[:10])
print(game[10:])
print(game[3:3])  #empty string
print(game[:]) #prints entire string

print('------------')
#strings are immutable means unchangable 
language='Python'
# language[0]='j' #throw an error
new_language='J' + language[1:]
print(new_language)
 
#format Operator %
device='computer'
print('%s' %device)
ram=2
speed=1.3
print('my %s has %g MHz speed %dGB RAM' %(device,speed,ram))