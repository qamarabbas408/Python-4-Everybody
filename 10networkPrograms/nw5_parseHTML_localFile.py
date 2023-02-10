##urllib is used for scrapping 
#web scraping is the process where is write a program that pretends to be web browser and retrieve pages--
#then examines them for useful patterns
# a search engine such as Google will look at the source of one web page and extract 
# the links to other pages and retrieve those pages, extracting links, and so on. other examples are bin

##HTML anchor tag href value extraction using RE (extracting links from a web page)
##File is stored in Local Server
import urllib.request
import re
url='http://127.0.0.1/pythonfiles/sample.php' #file is in localserver in htdocs XAMP
html=urllib.request.urlopen(url).read()
links=re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())
#the RE in this example is translated as we are looking for matching starts with href=" followed by
#http[s]? here ? operator searches for htttp followed by zero or one 's'
#then ://.*? a colon followed by // and followed by any no of characters 
#here ? at the end  indicates non greedy behaviour of matching: smallest matching possible 
