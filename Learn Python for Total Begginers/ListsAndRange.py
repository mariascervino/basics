print(list(range(11)))
print(list(range(0, 22, 2)))
print(list(range(-100, 110, 10)))

nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nest[0])
print(nest[1] * 2)
print(nest[2])

new = [list(range(11)), list(range(11, 21))]
print(new)

print(nest + new)

print(type(new)) 