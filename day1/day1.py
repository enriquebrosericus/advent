#!/usr/bin/python3

my_file = open("input2.txt", "r")
content_list = my_file. readlines()

#clean up newlines in list
stripped = [s.strip() for s in content_list]
stripped = [ int(x) for x in stripped ]


#f = open("test.txt", "r")
#data = f.read().splitlines()
#stripped = [ int(x) for x in data ]



mobigah=0;
i = 0

print("length of stripped:  ", len(stripped))

while i < len(stripped):
  #print(stripped[i])

  if i == 0 :
    print(stripped[i] , ": (N/A - no previous measurement)")
  elif  stripped[i] < stripped[i-1] :
    print(stripped[i] , ': decreased')
  elif  stripped[i] > stripped[i-1] :
    print(stripped[i] , ': increased')
    mobigah += 1
  else :
    print('NO CHANGE')

  i += 1

print ("The number of mobigah numbas is: {}".format(mobigah))
#print (mobigah)


