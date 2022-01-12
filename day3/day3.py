#!/usr/bin/python3

with open('/Users/edawg/gitsome/advent/day3/input.txt', 'r') as infile:
    data = [line.strip() for line in infile]


#need to put this in a multidimesional list

biglist=[]

for i in data:
    #list comprehension 
    x = [int(a) for a in str(i)]
    #print(x)
    biglist.append(x)

#find most common bit value in each position and store that in a list

#scrape length of element - could just hard code since it's 12
itemlength=len(biglist[0])
biglistlength=len(biglist)

i=0
j=0

#1st element is 0 totals for each position
#2nd element is 1 totals for each position
gamma_totals = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
                
print(len(biglist))

while i < biglistlength:
    #reset inner counter j to 0
    j=0
    while j < itemlength:
        #print(biglist[i][j])
        if biglist[i][j] == 0:
            gamma_totals[0][j] += 1
            j+=1
        else :
            gamma_totals[1][j] += 1
            j+=1
    i+=1


print(gamma_totals)






