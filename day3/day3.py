#!/usr/bin/python3

with open('input.txt', 'r') as infile:
    data = [line.strip() for line in infile]


#need to put this in a multidimesional list

biglist=[]

for i in data:
    #list comprehension 
    x = [int(a) for a in str(i)]
    print(x)
    #print(i)
    #biglist.append(x)
