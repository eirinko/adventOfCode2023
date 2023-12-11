import math

#First, open txt file
file = open("day4input.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content = file.readlines()
file.close()

#content = ['Card   1: 34 55 49 53 46  7 82 22 59 33 | 33 29  7 66 22 51 59 21 55 85 53 26 94 46 24 82  6 47 38  2 34 89 49 41 76\n', 'Card   2: 92 73 47  1 91 82 52 98 84 63 | 39 31 73 63 67 91 97 44  8  1 52 20 25 92 43 81 10 36 45 82 47 84  2 98 23\n', 'Card   3: 94 35 26 78 66 40 64  7 31 65 | 26 40 65 35 94 36 69 20  7 76 56 27 91 83 66 14 72 31 43 64 34 67 38 78  9\n']

pointsperline = []

def intersection(lst1, lst2): #https://www.geeksforgeeks.org/python-intersection-two-lists/
    return list(set(lst1) & set(lst2))

for line in content:
    #Have to divide it into winning numbers and ticket numbers.
    cardsAndNumbers = line.split(":")
    winnersAndTickets = cardsAndNumbers[1].split("|")
    
    winners = winnersAndTickets[0].split()
    tickets = winnersAndTickets[1].split()
    
    overlap = intersection(winners,tickets)
    
    if (len(overlap)==0):
        pointsperline.append(0)
    else:
        pointsperline.append(math.pow(2,len(overlap)-1))

total = sum(pointsperline)
print(total)