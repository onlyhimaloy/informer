#!/usr/bin/python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_43529.html'
#url ='http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

lst = list()
# Retrieve all of the anchor tags
table = soup('span')
for comments in table:
    # Look at the parts of a table
    #print('Comments:', comments.contents[0])
    num = comments.contents[0]
    #print(num)
    val = int(num)
    lst.append(val)

print(lst)
total = sum(lst)
print(total)