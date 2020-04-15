name = ("Jake")
print (name, "is 15 years old")

sent = "%s is 25 years old"
print (sent%name)

print (sent%("Maria"))

sent2 = "%s %s is the President of the US"
print(sent2%("Donald", "Trump"))

sent3 = "%s is %s years old"
print(sent3%("Ana", 56))