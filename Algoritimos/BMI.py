# Calculo do BMI e indicador de qual faixa o usuario esta
weight = float(input("Insert your weight: "))
height = float(input("Insert your height: "))

BMI = weight / (height * height)
print("Seu BMI e " + str(BMI))

if( BMI < 17 ) :
    print("You are very underweight")
elif( BMI >= 17 ) and ( BMI < 18.5 ):
    print("You are underweight")
elif( BMI >= 18.5 ) and ( BMI < 25 ):
    print("You are at your ideal weight")
elif( BMI >= 25 ) and ( BMI < 30 ):
    print("You are overweight")
elif( BMI >= 30 ) and ( BMI < 35 ):
    print("You are obese") 
elif( BMI >= 35 ) and ( BMI < 40 ):
    print("You are severely obese")
else:
    print("You have morbid obesity") 
      