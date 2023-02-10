# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
# of the number of characters at the end of the document.
import socket
import time
url4 = 'http://data.pr4e.org'
url = url4
domain = ''
datastr=''
if url.startswith('https://') or url.startswith('http://'):
    url = url.split('/')
    domain = url.pop(2)
    print(domain)
elif url.startswith('www.'):
    domain = url.split('/')
    domain = domain.pop(0)
else:
    print('Invalid URL')
    url = input('Enter a new URL___:')


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((domain, 80))
cmd = 'GET http://'+domain+' HTTP/1.0\r\n\r\n'
cmd=cmd.encode()
print(mysocket.send(cmd))
count=0
while True:
    data=mysocket.recv(500)
    if(len(data) <1): break
    time.sleep(.25)  #puts system on hold for .25 seconds until recv() receive 5120 chunks of characters
    count=count+len(data)
    print('Data: %d ----- Count: %d'%(len(data),count))
    datastr+=data.decode()
    if len(datastr)==3000: 
        mysocket.close()
        break
print('Characters Received: ',len(datastr))


