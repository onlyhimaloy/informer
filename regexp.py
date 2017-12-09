#!/usr/bin/python3.5
#fetching load avarage data from nsight api
#the duration and interval has added to the parameter.

import csv
import json
import requests

#hostname = raw_input("give me the hostname : ")

file = open('server.txt')


for hostname in file:
    hostname = hostname.strip()
    try:
        url ="http://api.nsight-jp.nhncorp.com/monapi/api/request?r=R&kt=hostnm&data=1.1.1.1&k="+hostname+"&fdt=201710290000&tdt=201711290000&interval=30&rt=json"
        print(url)

        response = requests.get(url)
        data = json.loads(response.content.decode())

        for item in data['result']:
            print(item['max'])
            max = item['max']
            avg = item['avg']

        with open( 'result.csv', 'a') as csvfile:
               writer = csv.writer(csvfile)
               if max and avg < 1.0 :
                   writer.writerow([hostname,max,avg])


    except :
        print("soomething went wrong!, server might not exist")