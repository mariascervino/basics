# Exercise 6: The weight of a person on the moon is 1/6th the weight of a
# person standing on earth. Say that your weight on earth increases by 1 kg
# every year.
# Write a program that will print your weight on the moon every
# year for the next 10 years. (Your initial weight can be anything.)

earthWeight = 56
initialYear = 0

while (initialYear <= 10):
    moonWeight = earthWeight / 6 
    earthWeight = earthWeight + 1
    initialYear = initialYear + 1
    print(moonWeight)

earthWeight = 56
for i in range(0,10):
    moonWeight = earthWeight / 6
    print(moonWeight)
    earthWeight = earthWeight + 1