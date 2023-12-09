#Which games can contain 12 red cubes, 13 green cubes, and 14 blue cubes
referencecubes = {"red" : 12, "green" : 13, "blue" : 14}

#First, open txt file
file = open("day2input.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content = file.readlines()
file.close()
#content = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]#,"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
listofgamenumbers = []

for line in content:
    line = line.split()
    for i in range(len(line)):
        newword = line[i].replace(":","")
        newword = newword.replace(";","")
        newword = newword.replace(",","")
        line[i] = newword

    #PART 1
    #gameno = line[1]
    #i = 2
    #errors = 0
    #while i < len(line):
    #    number = int(line[i])
    #    color = line[i+1]
    #    if (referencecubes[color]<number):
    #        errors+=1
    #    i+=2
    
    #if (errors==0):
    #    listofgamenumbers.append(gameno)

    #PART 2
    red = 0
    blue = 0
    green = 0
    
    i = 2
    while i < len(line):
        number = int(line[i])
        color = line[i+1]
        if ((color == 'red') & (number > red)):
            red = number
        if ((color == 'blue') & (number > blue)):
            blue = number
        if ((color == 'green') & (number > green)):
            green = number
        i+=2
    lineresult = red * blue * green
    listofgamenumbers.append(lineresult)

result = 0
for number in listofgamenumbers:
    result += int(number)
print(result)