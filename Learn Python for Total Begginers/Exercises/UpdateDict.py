lifeStages = {0:"embryo", 1: "fettus", 2: "baby", 3: "infant", 4: "teen"}

midLife = {5:"adult", 6: "big kid"}

# def Merge(lifeStages, midLife): 
#     lista={**lifeStages, **midLife} 
#     print(lista)
# Merge(lifeStages, midLife)

# OR JUST

lifeStages.update(midLife)
print(lifeStages)