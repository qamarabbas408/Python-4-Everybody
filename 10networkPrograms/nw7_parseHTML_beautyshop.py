##parsing HTML using beautyshop
#RE work with HTML when it is formated correctly but there are alot of broken HTML pages so
#working with only RE might miss some links or give up bad data

#beautifulsoup library extracts highly flawed HTML 
# Beautiful Soup is a library that makes it easy to scrape information from web pages.
#  It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, 
# searching, and modifying the parse tree.
#pip install beautifulsoup4 
import urllib.request

from bs4 import BeautifulSoup
url='https://docs.python.org'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
#the output contains a large list including relative paths and in page references that don't include
#http or https which was requirement in last program where we use RE
