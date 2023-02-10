##searching those lines that start with some value  i.e From
fhand=open('dataFiles/data.txt')
# for line in fhand:
#     if line.startswith('From'):
#         print(line)
 #the output contains lines that start with FROM and as well there is black new line called invisible newline

 ##solution to above problem rstrip()
# for line in fhand:
#     line=line.rstrip() #removes white spaces from the right side of the string
#     if line.startswith('From'):
#         print(line)

##restructure the code for better processing 
# for line in fhand:
#     line=line.rstrip()
#     if not line.startswith('From: '): #if line doesnt starts with FROM then skip that iteration
#         continue #continue the loop 
#     print(line)

##removing line containing media.berkeley.edu from the serach
# for line in fhand:
#     line=line.rstrip()
#     if line.find('@media.berkeley.edu') == -1:  #other then the parameter ignore the iteration
#         continue
#     print(line)

##user Enters file name
filename=input('Enter filename: ')
while True: 
    try:
        fhand=open('dataFiles/%s'%filename)
        print(fhand)
        break
    except: 
        print("No such file Exists")
        filename=input('Enter filename: ')


