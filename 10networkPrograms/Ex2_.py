##write a program that extracts domains from a list of links dataFiles/links.txt
##strip all https or www before domain and as well other stuff after domain such as
#https:www.google.com >>>domain=google.com
from os import link
import socket
import re
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# url=input("Enter__url: ")
linklst=list()
domainlst=list()
fhand=open('dataFiles/links.txt')
for line in fhand:
    line=line.rstrip()
    linkslst=re.findall('(http[s]?://.*)',line)
    if(len(linkslst)<1): continue
    for link in linkslst:
        link=link.split('/')
        domainstr=link.pop(2)
        if domainstr.startswith('www'): 
            afterWWWIndex=domainstr.find('.')
            domainstr=domainstr[afterWWWIndex+1:]
            domainlst.append(domainstr)
        else:
         domainlst.append(domainstr)
for domain in domainlst:
    print(domain)
print("Total Domains: ",len(domainlst))
