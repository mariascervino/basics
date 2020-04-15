for i in range (5):
    print("Hello World")

cats = ["tiger", "lion", "jaguar", "liopard"]
for cat in cats:
    print(cat)

for num in range (4):
    print(num, num + 10, num * num)

nest1 = [[10, 20, 30],
[3.5, 4.5, 5.5],
["sword", "hammer", "shield"]]
for i in range(3):
    #print(nest1[i])
# pode-se imprimir uma, duas ou as tres listas com a função for
    res = nest1[0][i] + nest1[1][i]
    print((nest1)[2][i].capitalize() + ": Power Level =", res)

for i in range(1,8):
    print("{} * {} = {}".format(i, i, (i*i)))

for k in range (1,8):
    print ("%d * %d = %d" % (k, k, (k*k)))

#TUPPLE UNPACKING
tup1 = ((10, 20, 30), ("a", "b", "c"), (200, 400, 600))
#usa-se for para escolher quantas vezes o tuple será printed:
for i in range (2):
    for x, y, z in tup1:
        print(x, y, z)