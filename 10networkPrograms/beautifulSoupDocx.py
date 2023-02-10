from bs4 import BeautifulSoup

# To parse a document, pass it into the BeautifulSoup constructor.
#  You can pass in a string or an open filehandle:
with open("10networkPrograms/parseFiles/sample.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup)

# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

#converts HTML entities to unicode
print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
    