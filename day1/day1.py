my_file = open("input.txt", "r")
content_list = my_file. readlines()

#clean up newlines in list
stripped = [s.strip() for s in content_list]



mobigah=0;
i = 0

print("length of stripped:  ", len(stripped))

while i < len(stripped):

  if i == 0 :
    print(stripped[i] + ': (N/A - no previous measurement)')
  elif  stripped[i] < stripped[i-1] :
    print(stripped[i] + ': decreased')
  elif  stripped[i] > stripped[i-1] :
    print(stripped[i] + ': increased')
    mobigah += 1
  else :
    print('NO CHANGE')

  i += 1

#print ("The number of mobigah numbas is: {}".format(mobigah))
print (mobigah)
#print("Hello to the {} {}".format(var2,var1))


