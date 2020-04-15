# Exercise 2: There were 20 people on a bus. 10 got off. 3 came on. 15
# came on. 5 came off. If there were 3 more buses, and each had 15 people
# throughout the bus ride, how many people were on all the buses at the last
# stop? (Should be done via one equation in Python Shell)

bus1 = 20
bus2 = bus1 - 10
bus3 = bus2 + 3
bus4 = bus3 + 15
bus5 = bus4 - 5

bus6 = 15
bus7 = 15
bus8 = 15

total1 = (bus5 + bus6 + bus7 + bus8)
print(total1)

#OR

total2 = ((((20-10)+3)+15)-5)+15+15+15
print(total2)