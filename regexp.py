#!/usr/bin/python

import re
file = open('reg_sum_43527.txt')

lst =list()
for line in file:
    if not re.findall('[0-9]+' , line): continue
    num = re.findall('[0-9]+' , line)
    for val in num:
        number = int(val)

        #print(number)
        lst.append(number)

#print(lst)
total = sum(lst)
print(total)


