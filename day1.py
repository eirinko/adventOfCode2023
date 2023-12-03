#First, open txt file
file = open("day1input.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content=file.readlines()
file.close()

#Test list. 
#content=["6fkjkbc", "2htpxbqvtg3one", "2threezhxzfslfxhvzdbfour15", "nrfdrzdjtlthreeonennzfbone9one", "sixtwosevenqplrqvxreight6", "bbsix2"]

#For each line, isolate the first and the last digit and add these to a counter.
count = 0

for element in content:
#     element = element.replace("one","1")
#     element = element.replace("two","2")
#     element = element.replace("three","3")
#     element = element.replace("four","4")
#     element = element.replace("five","5")
#     element = element.replace("six","6")
#     element = element.replace("seven","7")
#     element = element.replace("eight","8")
#     element = element.replace("nine","9")
    
    numbers = []
    for char in element:
        if char.isdigit():
            numbers.append(char)
    charNumber = numbers[0]+numbers[-1]
    number = int(charNumber)
    count+=number

print(count)