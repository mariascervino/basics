tup1 = 40, 50, 60, 70, 80
print(tup1)
print(type(tup1))

myList = [10, 20, 30]
tup2 = tuple(myList)
print(tup2)
print(type(tup2))
# You can transform a list into a tuple

print (tup2 + tup1)

# print(tup1.index(70)) ???


tup4 = "cat", "cat", "dog", "cat", "dog", 10, 10, 10, 10
print(tup4)
print(tup4.count("cat"))
print(tup4.count(10))

# se há itens repetidos no tupple, eu posso contar quantos de cada item há.

print(sum(tup1))
print(sum(tup1*2))
print(sum(tup1 + tup2))
# se o tupple é apenas feito de numeros, podemos solicitar a soma desses números utilizando a palavra
# reservada sum

print(sorted(tup1 + tup2))