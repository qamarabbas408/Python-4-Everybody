# Exercise 1: Change the socket program socket1.py to prompt the user
# for the URL so it can read any web page. You can use split('/') to
# break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and
# except to handle the condition where the user enters an improperly
# formatted or non-existent URL
import socket
import re
# url=input('Enter a URL:__ ')
domainlst=list()
domain=''
fhand=open('10networkPrograms/parseFiles/fetchhtml.html','wb')
url1='httpseserser//www.google.com'
url2='www.sfd.com'
url3=''
url4='http://data.pr4e.org'
url=input('Enter a URL__: ')
while True:
    if url.startswith('https://') or url.startswith('http://'):
        url=url.split('/')
        domain=url.pop(2)
        print(domain)
        break
    elif url.startswith('www.'):
        domain=url.split('/')
        domain=domain.pop(0)
        break
    else:
        print('Invalid URL')
        url=input('Enter a new URL___:')  

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect((domain,80))
cmd='GET https://'+domain+' HTTP/1.0\r\n\r\n'
cmd=cmd.encode()
print(cmd)
# mysocket.send(cmd)
print(mysocket.send(cmd))
while True:
    data=mysocket.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
    fhand.write(data)
mysocket.close()
