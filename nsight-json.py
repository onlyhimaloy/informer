#!/usr/bin/python3.5
#fetching load avarage data from nsight api
#the duration and intervalhas added to the parameter.


import json
import requests

hostname = input("give me the hostname : ")

url ="http://api.nsight-jp.nhncorp.com/monapi/api/request?r=R&kt=hostnm&data=1.1.1.1&k="+hostname+"&fdt=201710290000&tdt=201711290000&interval=5&rt=json"
#print(url)

response = requests.get(url)
data = json.loads(response.content.decode())

#print(data)

for item in data['result']:
        print(item['max'])
