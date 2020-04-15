# Exercise 3: Create a small program that will take in a User’s name and last
# name (Hint: varName = input(“Enter your name”)), store both in two
# variables. And then print out a message saying (“Hello there, FirstName
# LastName”) (Using the %s symbols)

firstName = str(input("Insert your first name: "))
lastName = str(input("Insert your last name: "))

sent = ("Hello there %s %s")
print (sent%(firstName, lastName))