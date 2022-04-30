#!/usr/bin/python3

from multiprocessing.connection import answer_challenge


with open('day3/input.txt', 'r') as infile:
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

#compare gamma lists elements and see if 0 or 1 is the most frequent
i=0
gamma_final=""
epsilon_final=""
while i < itemlength:
    if gamma_totals[0][i] > gamma_totals[1][i]:
        winner="0"
        loser="1"
    else:
        winner="1"
        loser="0"

    i +=1 
    #append to string
    gamma_final += winner
    epsilon_final += loser
    #print("I ame the winner:  ", winner)
    #print("i am gamma_final", gamma_winner)
    #print("i am gamma_final", gamma_final)
    #print("i am epsilon_final", epsilon_final)

    #convert from binary to decimal
    gamma_decimal = int(gamma_final, 2)
    epsilon_decimal = int(epsilon_final, 2)

    #print("i am gamma_decimal", gamma_decimal)
    #print("i am epsilon_decimal", epsilon_decimal)

    final_answer = gamma_decimal * epsilon_decimal
    print("i am final_answer", final_answer)



















