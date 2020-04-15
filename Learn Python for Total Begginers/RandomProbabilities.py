import random as rd
from random import *

#The probability is the percentage of chance of each number or name has to be called in the random
# choice, and they are given respectively in the variables "probabilities"

students = ["Ana", "Maria", "Kaleb", "João"]

# SAME CHANCES
probabilities = [0.25]*4
print(choices(students, probabilities, k = 2))
# k is the number of times that I want the number to be drawn

# DIFFERENT CHANCES
probabilities1 = [0.50, 0.10, 0.20, 0.20]
print(choices(students, probabilities1))

num5 = print(rd.sample(range(10, 40), k = 5))
myList = list(num5)
print(sorted(myList))