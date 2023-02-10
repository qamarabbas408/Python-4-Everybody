# ##Retriving non-binary files such as images or videos or audios other then plain text
# #the data inside them is not useful to print but they can be stored in local disk 
# #using urllib to retreive image from server
import urllib.request
# #read() downloads the entire content and puts it in strvarialbe
# #it stores data in RAM -- program will work if file has less size then your RAM
# # PROBLEM-- otherwise get slow or crash
imgstr=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() 
fhand=open('10networkPrograms/downloaded/urllibImage.jpg', 'wb') #wb argument means open file only to write #makesure of slashes
fhand.write(imgstr) #write() write data into hardisk
fhand.close()

##Resolving Memory Problem for large Files 
#we use buffer to retrive data or blocks and then write each block to disk(harddisk) before getting next blcok
img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')  
size=0
fhand=open('10networkPrograms/downloaded/memoryresolve.jpg','wb')
while True:
    info=img.read(100000) #100000 characters at a time
    if len(info)<1: break #write untill all data is written
    size=size+len(info)
    fhand.write(info)
print(size,' Charcters copied')
fhand.close()