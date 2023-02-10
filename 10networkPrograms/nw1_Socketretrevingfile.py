##Socket
#it is a built in module in python that deals with network connections and to retrieve data over a netwokr
# a single socket provides two way communication b/w two programs. You can both read or write to same socket
#write to a socket means you are sending data to web and reading sockeet means reading data send by web
# to request a web from server we use GET request such as:
#GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n here it takes two parameters web page we are requesting URL and 
# a blank line represented by \r\n\r\n. A single pair \r\n means EOL (end of line) so two EOL means nothing in between a line

import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80)) #program makes connection to port 80 on server
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #encode converts string to byte object
mysock.send(cmd)

while True: #recv(): data is receive in 512-character chunks. it will loop until there is no data left to read
    data=mysock.recv(512)
    if len(data) <1:
        break
    print(data.decode(),end='') #decode() removes byte object and converts it back to string
mysock.close()

#output starts with headers and it ends at content-type header which indicates we have a plain text file
# then there is a blank line and then actual output we requested

##byte object
#HTTP protocol sends or receives data in byte object instead strings
#thus encode and deocde doees the conversition
str='some data here to send to web'
print('b\'Hello') #byte object look like this always preceded by b followed by a single quote followed by data
#decode function removes this b from data and prints it back it original format