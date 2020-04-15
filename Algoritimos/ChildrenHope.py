# Fazer uma doação to o criança esperanca, incluindo a opcao de um valor escolhido pelo usuario
print ("------------------------------")
print ("   WELCOME TO CHILDREN HOPE   ")
print ("------------------------------")
print ("    THANK YOU FOR DONATING!   ")
print ("[1] to donate R$10")
print ("[2] to donate R$25")
print ("[3] to donate R$50")
print ("[4] to donate other values")
print ("[5] to cancel")
D = int(input("Insert your opition: "))
if ( D == 1 ):
    print("You donated R$10")
    print("We appreciate your donation")
elif( D == 2 ):
        print("You donated R$25")
        print("We appreciate your donation")
elif( D == 3 ):
        print("You donated R$50")
        print("We appreciate your donation!")
elif( D == 4 ):
        D = int(input("How much would you like to donate? "))
        print ("You donated R$", D)
        print("We appreciate your donation")
elif( D == 5 ):
        print("The operation was canceled")
else:
        print("Invalid Character")