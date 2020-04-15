for count, i in enumerate(range(10,40,5), 200):
    print(count, i)

for i in range (10,40,5):
    print(190+i, i)

tup1 = (10, 20, 30)
myList = [40, 50, 60]
z = list(zip(tup1, myList))
print(z)
for t, m in z:
    print(t + m)

myList2 = list(range(6))
print(myList2)

groceries = ["Apples", "Juice", "Ice Cream", "Bread"]
prices = ["$2.50", "$1.90", "$5.00", "$3.40"]
for food in range (4):
    print(groceries[food], "=" , prices[food])

zipShop = list(zip(groceries, prices))
print (zipShop)
for g, p in zipShop:
    print(g, "=", p)

num1 = [100, 2, 90, 10]
num2 = [12, 7, 90, 50]
zipNum = zip(num1, num2)
for i, j in zipNum:
    if i > j:
        print(i)
    elif j > i:
        print(j)
    else:
        print(i, j)
        #essa função compara ps valores das duas listas e retorna os valores conforme o pedido.
        # o valor que esta na posição 0 de uma lista será comparado com o valor 0 de outra,
        #e assim por diante
#The function zip(*iterables) takes in iterables as arguments and returns an iterator.
# This iterator generates a series of tuples containing elements from each iterable.
# zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
