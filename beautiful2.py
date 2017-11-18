#!/usr/bin/python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Latif.html'
#url = ' http://py4e-data.dr-chuck.net/known_by_Fikret.htm'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
url2 = (tags[17].get('href',None))
#url2 = (tags[2].get('href',None))
print(url2 + '\n')

for i in range(6):

    html = urllib.request.urlopen(url2, context=ctx).read()
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url2 = (tags[17].get('href', None))
    print(url2)