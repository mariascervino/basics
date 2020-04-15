import time
score = 0
name = str(input("Insert your name: "))
print("Welcome", name,"\nLet's get started!")

def scorePlus():
    global score
    score += 1
    print("Your score: ", score)
# def scoreMinus():
#     global score
#     score -= 1
#     print("Your score: ", score)

def q1():
    global score
    print("\n1. What is El Capitan?")
    print("a) An operation system for Windows.")
    print("b) An operation system for Mac.")
    print("c) A third-party application.\n")
    answer = str(input("What is the right answer? "))
    if answer == "b":
        print("Well done, that is correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        # scoreMinus
        print("Your score: ", score)
    q2()

def q2():
    global score
    print("\n2. What is Apple's lastest device?")
    print("a) iPhone.")
    print("b) MacBook Pro.")
    print("c) iPod Touch.\n")
    answer = str(input("What is the right answer? "))
    if answer == "b":
        print("Well done, that is correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        # scoreMinus()
        print("Your score: ", score)
    q3()

def q3():
    global score
    print("\n3. Who is the CEO of KARSID?")
    print("a) Karthik N.")
    print("b) Bill G.")
    print("c) Steve J.\n")
    answer = str(input("What is the right answer? "))
    if answer == "a":
        print("Well done, that is correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        # scoreMinus()
        print("Your score: ", score)
q1()

print("\nYour final score is: ", score)
if score == 0 or score == 1:
    print("Sorry, you are repproved!")
elif score == 2 or score == 3:
    print("Congratualations, you are approved!")

#you can also go to the next question if the answer is correct, 
#just moving the call of function before else (after print at if)