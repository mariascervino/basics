def add(arg1, arg2, arg3):
    print (arg1 + arg2 + arg3)
add(10, 40, 50)
g = lambda x, y, z : x + y + z
g (10, 40, 50)
#OR JUST
def add(arg1=10, arg2=40, arg3=50):
    print (arg1 + arg2 + arg3)
add()
g = lambda x=10, y=40, z=50 : x + y + z
g ()

#dizer se um numero é par OU maior que 10, return True or False
g2 = lambda num: num % 2 == 0 or num > 10
print(g2(5))

def compare (a, b):
    if a > 10:
        print(a)
    else:
        print(b)
compare(20,2)
#OR JUST
g3 = lambda a, b: print(a) if a > 10 else print(b)
g3(7,2)

def size (x):
    if x > 100:
        print("Big")
    else:
        print("Small")
size(150)
#OR JUST
g4 = lambda x: print("Big") if x > 100 else print("Small")
g4(40)