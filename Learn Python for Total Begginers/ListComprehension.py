cosmos = []
for i in "universe":
    cosmos.append(i)
print(cosmos)
# OR JUST
print([u for u in "universe"])
# OR JUST
print(list("universe"))

comp = [x*2 for x in range(0,11)]
print(comp)

comp2 = [x**2 for x in range(0,11)]
print(comp2)

pets = ["cat", "dog", "rabbit", "duck", "mouse", "piglet"]
print([pets[i] + " is hungry!" for i in range (len(pets))])
