# calcular a age e dizer se o usuario e maior, menor ou idoso
atualYear = int(input("Insert the atual year: "))
birthYear = int(input("Insert your birth year: "))

age = atualYear-birthYear
print("You are " + str(age) + " years old!")

if( age > 60 ) :
    print("And you are old")
elif( age >= 18 ) :
    print("And you are of legal age")
else:
    print( "And you are still underage")
