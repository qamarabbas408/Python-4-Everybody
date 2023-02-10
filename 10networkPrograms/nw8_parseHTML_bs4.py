print('---Extracting tags ----')
##Extracting various parts of a tag using bs4
urlx='http://127.0.0.1/pythonfiles/sample.php' #file is in localserver in htdocs XAMP
htmlx=urllib.request.urlopen(urlx).read()
soup2 = BeautifulSoup(htmlx,'html.parser')
tagsx =soup2('a')
for tag in tagsx:
    print(tag) #returns string
    print(tag.get('href',None)) #returns list
    print(tag.contents) #content btween <a>content</a> returns dictionary
    print(tag.attrs)