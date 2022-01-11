#!/usr/bin/python3


#f = open("input.txt", "r")
#data = f.read().splitlines()
#data = [ int(x) for x in data ]

#dimensiion,dimval = open("input.txt".read().split()
dimlist=[]
dimvallist=[]

with open('input.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        #TODO - should be able to do this on one line
        dim,dimval= i.split()
        dimlist.append(dim)
        dimvallist.append(dimval)

#print(dimlist)
#print(dimvallist)

#make dimvals all ints
dimvallist = [ int(x) for x in dimvallist ]

#print (len(dimvallist))
#print (len(dimlist))

i = 0
x = 0
y = 0


while i < len(dimlist):

  if dimlist[i] == 'up' :
    x -= dimvallist[i]
    print(dimlist[i], x, dimvallist[i])
  elif  dimlist[i] == 'down' :
    x += dimvallist[i]
    print(dimlist[i], x, dimvallist[i])
  else :
    y += dimvallist[i]
    print(dimlist[i], y, dimvallist[i])

  i += 1

print ("I am x: {}".format(x))
print ("I am y: {}".format(y))

print ("Positiony: {}".format(x*y))

