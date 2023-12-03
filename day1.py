#First, open txt file
file = open("day1input.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content=file.readlines()
file.close()

#Test list below should give a result of 281.
#content = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

result = 0

#PART 1:
# for line in content:
#     numbers = []
#     for char in line:
#         if char.isdigit():
#             numbers.append(char)
#     charNumber = numbers[0]+numbers[-1]
#     number = int(charNumber)
#     result+=number
# print(result)

#PART 2: 
stringnumbers = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
numbers = ["1","2","3","4","5","6","7","8","9","1","2","3","4","5","6","7","8","9"]
for line in content:
    numberindexfromleft = []
    numberindexfromright = []
    
    for word in stringnumbers:
        wordLeftIndex = line.find(word) #Becomes -1 if the line doesn't contain the word.

        if (wordLeftIndex ==-1):
            numberindexfromleft.append(len(stringnumbers)-1)
        else:
            numberindexfromleft.append(wordLeftIndex)

        numberindexfromright.append(line.rfind(word))

    left = numberindexfromleft.index(min(numberindexfromleft))
    right = numberindexfromright.index(max(numberindexfromright))
    
    charNumber = numbers[left] + numbers[right]
    
    number = int(charNumber)
    result += number
    
print(result)