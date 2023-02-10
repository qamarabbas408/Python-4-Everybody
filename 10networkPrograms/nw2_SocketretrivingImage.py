##retrive an image from web 
import socket
import time

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mysock.sendall(cmd)
count=0
picture=b"" #store picture data in encoded form
while True:
    data=mysock.recv(5120)
    if len(data)<1: break
    time.sleep(.25)  #puts system on hold for .25 seconds until recv() receive 5120 chunks of characters
    count=count+len(data)
    print(len(data),count)
    picture=picture+data #at end you will get 230608bytes or 230608/1024 = 225KB which is size of the image
mysock.close()
print(type(data)) #byte object
print(type(picture)) #byte object

#removing header
#before sending data actual data server sends a blank line 
posEndofHeader=picture.find(b'\r\n\r\n') 
print('Header Length:',posEndofHeader)

#header HTTP
print(picture[:posEndofHeader].decode()) #print data until you encounter a blank line

#save picture to a file
picture=picture[posEndofHeader+4:]
fhand=open('10networkPrograms/downloaded/newstuff.jpg','wb')
fhand.write(picture)
fhand.close()
#PROBLEM:::: as you can see we dont get data in chunks of 5120 each time when recv() is invoked.
#server randomly sent characters few  as 40 and large as 5120 results depend on network speed
#this behavior of server can be changed in such a way that recv sends 5120 chunks of character everytime 
#using time module which will put our system on hold unless server sends complete chunk of 5120 characters
#(uncomment line 14)
