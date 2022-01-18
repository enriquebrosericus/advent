#!/usr/bin/python3

my_file = open("input.txt", "r")
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


#part 2
i = 0
j = 0
list_3 = []
sum1 = 0

while i < (len(stripped)-2):
    while j <=2:
        #print("I am j:", j)
        sum1 += stripped[i+j]
        #print("i am sum1:",sum1)
        j += 1
    i +=1

    #push results to list
    #print("i am sum1:",sum1)
    list_3.append(sum1)
    
    #reset inner loop counter
    j = 0
    #reset sum1
    sum1 = 0

print (len(list_3))

    
#should make better use of already defined logic from part one...but just doing again here for now
i = 0
mobigah = 0
while i < len(list_3):

  if i == 0 :
    print(list_3[i] , ": (N/A - no previous measurement)")
  elif  list_3[i] < list_3[i-1] :
    print(list_3[i] , ': decreased')
  elif  list_3[i] > list_3[i-1] :
    print(list_3[i] , ': increased')
    mobigah += 1
  else :
    print('NO CHANGE')

  i += 1

print ("The number of mobigah numbas is: {}".format(mobigah))
