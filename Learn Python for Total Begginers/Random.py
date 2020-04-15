import random as rd
from random import *

print(random())
#just give numbers < 0
print(randint(10,20))
#just int numbers between 10 and 20
print(randrange(10, 100, 2))
#give any even number betwen 10 and 100
print(uniform(2,3))
#give any number (including the floats) between 2 and 3

animals = ["cat", "dog", "rabbit", "mouse", "snake", "horse"]
# shuffle(animals)
# print(animals[0])
print(rd.choice(animals))

heroes = ["Batman", "Spiderman", "Iron Man", "Captain America"]
villains = ["Jocker", "Venom", "Thanos", "Red Skull"]
num = list(range(len(heroes)))

#PRINT 4 PAIRS:
# shuffle(heroes)
# shuffle(villains)
# for i in num:
#     print(heroes[i], "VS", villains[i])

#PRINT 1 PAIR:
print(rd.choice(heroes), "VS", rd.choice(villains))