# Escreva um programa que receba um número natural n na entrada e imprima n! (factorial) na saída.
num = int(input("Digite o valor de n: "))
result = num

while(num > 1 ):
    result = result*(num-1)
    num = num-1
print(result)