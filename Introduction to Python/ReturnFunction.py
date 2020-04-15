def sum(num1, num2):
    return(num1 + num2)

def sub(num1, num2):
    return(num1 - num2)

def mult(num1, num2):
    return(num1 * num2)

def div(num1, num2):
    return(num1 / num2)

num1 = int(input("Insert a number: "))
num2 = int(input("Insert another number: "))

while(num2<=0 or num2 > num1) :
    num2 = int(input("This is not a valid number, type another one: ")) 

resultSum = sum(num1,num2)
resultSub = sub(num1,num2)
resultMult = mult(num1,num2)
resultDiv = div(num1,num2)

print(resultSum, resultSub,resultMult,resultDiv)