##urllib
#urllib is a python module that has same functionality as of socket 
#but instead doing everything manualy urllib handles it automaticaly
#program in previous topic is given here using urllib
import urllib.request
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #urlopen() takes the url of web page and returns data
for line in fhand:
    print(line.decode().strip()) #here strip() removes whitespaces from both left and right ends of the line
    #at output we see only the content of the text file all other stuff like headers are removed automaticaly
