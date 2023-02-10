
fhand=open("dataFiles/data_slice.txt")  #compiler is in parrent directory thus explicity write the address of child driectory
print(fhand) #file found no error otherwise get an error 

#counting no of lines
fhand=open('dataFiles/data.txt')
count=0
for line in fhand:
    count=count+1
print("total LInes in the file are %d"%count)

#no of characters in the file
#if file size is less than your RAM then entire file can be read into one string
fhand=open('dataFiles/data.txt')
inp=fhand.read()
print('Total characters in the File' ,len(inp)) #prints no of characters in the file not the lines
print(inp[:20]) #first 20 characters
