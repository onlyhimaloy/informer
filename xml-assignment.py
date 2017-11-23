import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_43531.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)
comment = tree.findall('.//count')
#comment = tree.findall('comments/comment')

lst =list()

for item in comment:
     #print(item)
     #num = item.find('count').text
     number =int(item)
     lst.append(number)

total =sum(lst)
print(total)

