import urllib.request, urllib.parse, urllib.error
import json


url ='http://py4e-data.dr-chuck.net/comments_43532.json'

rep = urllib.request.urlopen(url)
data = rep.read()

info = json.loads(data)

print('User count:', len(info))

lst =list()
#print(info)
for item in info['comments']: #info is a dictionary and comments is a key of another dictionary of this dictionary 
    #print(item['name'])
    num = (item['count'])
    num = int(num)
    number = lst.append(num)


total = sum(lst)
print(total)