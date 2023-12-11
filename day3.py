import numpy as np

#First, open txt file
file = open("day3inputtest.txt","r")

# The following code gives a list where each element correspons to a line in the txt file. 
content = file.readlines()
file.close()

#Would like to create a matrix for the file and for each number, check if there's an adjacent symbol. 