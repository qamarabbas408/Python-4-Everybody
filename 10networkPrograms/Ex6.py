# Exercise 4: Change the urllinks.py program to extract and count paragraph (p)
#  tags from the retrieved HTML document and display the
# count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several
# small web pages as well as some larger web pages.
import urllib.request
import re
url='https://stackoverflow.com/questions/4883932/regex-needed-to-match-anything-within-p-tags'
url1='https://whatismyipaddress.com/'
url3='https://www.pdfdrive.com/introduction-to-data-mining-e184598079.html'
httpResponse=urllib.request.urlopen(url3)
countTags=0
emptyTags=0
for line in httpResponse:
    line=line.decode().strip()
    targetData=re.findall('<p>.+</p>',line)
    countTags=countTags+1
    if len(targetData)<1: 
        emptyTags=emptyTags+1
        continue
print('Total Non Empty Paragraph Tags are: ',countTags-emptyTags)



