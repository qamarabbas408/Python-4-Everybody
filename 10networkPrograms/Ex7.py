# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.
import socket

url4 = 'http://data.pr4e.org'
url = url4
domain = ''
datastr = ''
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

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect((domain,80))
cmd = 'GET http://'+domain+' HTTP/1.0\r\n\r\n'
cmd=cmd.encode()
mysocket.send(cmd)
datawithHeader=''
while True:
    data=mysocket.recv(300)
    if( len(data)<1): break
    data.decode()
    datawithHeader=datawithHeader+data.decode()
mysocket.close()
# print(datawithHeader)
posEndHeader=datawithHeader.find('\r\n\r\n')
print('\n ----------HEADER DATA ----------')
print(datawithHeader[:posEndHeader])
print('\n ----------ACTUAL DATA ----------')
print(datawithHeader[posEndHeader+4:])

