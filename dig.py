#! /usr/bin/python
# -*- coding::utf-8 -*-
import re

pattern = re.compile(r'[A-z]+\b')

print "Please enter the length:"
length = raw_input()
length = int(length)
dic = {}
for i in range(0, length):
    string = raw_input()
    match = pattern.findall(string)
    if match:
        for j in match:
            if dic.has_key(j):
                dic[j] += 1
            else:
                dic[j] = 1
print dic
print "Please enter the valve number:"
valve = raw_input()
valve = int(valve)
for i in dic.keys():
    if int(valve) > int(dic[i]):
        del dic[i]
print dic
