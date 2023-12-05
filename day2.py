#Which games can contain 12 red cubes, 13 green cubes, and 14 blue cubes
referencecubes = {"red" : 12, "green" : 13, "blue" : 14}

#First, open txt file
file = open("day2input.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content = file.readlines()
file.close()

listofgamenumbers = []

for line in content:
    line = line.split()
    for i in range(len(line)):
        newword = line[i].replace(":","")
        newword = newword.replace(";","")
        newword = newword.replace(",","")
        line[i] = newword

    gameno = line[1] #Verified

    i = 2
    errors = 0
    
    while i < len(line):
        number = int(line[i])
        color = line[i+1]
        if (referencecubes[color]<number):
            errors+=1
        i+=2
        
    if (errors==0):
        listofgamenumbers.append(gameno)
        
print(listofgamenumbers)

result = 0
for number in listofgamenumbers:
    result += int(number)
    
print(result)