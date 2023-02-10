##parsing HTML file located in online server
import urllib.request
import re
import ssl
url='https://docs.python.org'
# PROBLEM--wont on some sites b/c some sites use strict enforce strict HTTPS (ssl)
html=urllib.request.urlopen(url).read()
links=re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())

print('____SSL SITES___')
#Resolving ssl PROBLEM
# so to access stricly enforce HTTPS sites 
# we use ssl module uncomment following  lines to ignore ssl in some sites
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

urlstrict='https://www.siteground.com/kb/how-do-i-enforce-https/' #HTTPS stricly enforced site
htmlNew=urllib.request.urlopen(urlstrict, context=ctx).read()
links=re.findall(b'href="(http[s]?://.*?)"',htmlNew)
for link in links:
    print(link.decode())
# PROBLEM--Even ignoring SSL policies some sites are forbidden
