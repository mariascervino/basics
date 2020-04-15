d1 = {"k1": [1,2,3, (100, 300, 500)], "k2": [4,5,6, ["phone", "computer", "robot"]]}
var = eval(input("Enter a number: "))

if var in d1["k1"]:
    print("found you!")
    num = input("Enter a number or string: ")

    if (num) in d1["k2"][:3]:
        print("Found another one!")
    
    elif num in d1["k2"][3]:
        print("Got a", num)
        
    else:
        print("Can't find anything")
        
elif var in d1 ["k1"][3]:
    print("can't hide!")
else:
    print("Where are you?")
