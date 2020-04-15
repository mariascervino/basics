d1 = {}
d1 ["A"] = 10
d1 ["B"] = 20
d1 ["C"] = 30
print(d1)

# pode-se substituir um item de um dict
d1 ["A"] = 40
print(d1)

# assim como pode-se substituir um item de uma lista
myList = [10, 20]
print(myList)
myList[1] = 120
myList.append(30)
print(myList)

d2 = {"robot": "$25.99", "car": "$15.95"}
print(d2)
print(d2.clear())

print(tuple(d1.keys()))
print(tuple(d1.values()))

menu = [("chips", "$24"), ("soup", "$14")]
print(dict(menu))