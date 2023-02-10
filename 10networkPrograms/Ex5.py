# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents
import urllib.request
httpResponse=urllib.request.urlopen('http://data.pr4e.org')
count=0
while True:
    info=httpResponse.read(300)
    if len(info)<1: break
    count=count+len(info)
    print('Data Chunks: %d  Count: %d'%(len(info),count))
    if(count==3000):
        print('Limit Acheived: %d'%len(info))
        break
    