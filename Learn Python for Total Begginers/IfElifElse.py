a = 10
b = 25
c = 100
d = ("cat", "dog", "bird")

if a == 10:
    print("a is true!")
    if b < 40:
        print("b is true!")
        if c > 9:
            print("c is true!")
            if "zebra" in d:
                print("d is true")
            else:
                print("d is false")
        else:
            print("c is false!")
    else:
        print("b is false!")
else:
    print("a is false!")

# se o "a" for falso, ele nao varificará "b"", "c" e "d"
# se "b" for falso, ele nao verificará "c" e "d"
# se "c" for falso, ele nao verificará "d"

total = [list(range(11)), list(range(11, 21)), list(range(21,31))]
v = int(input("Enter a number: "))

if v in total [0]:
    print(v, "is in the first list")
elif v in total [1]:
    print(v, "is in the second list")
elif v in total [2]:
    print(v, "is in the tird list")
else:
    print("This number is not in the lists")