# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
n = int(input("Digite o valor de n: "))
count = 0
impar = 1

while (count < n):
    print(impar)
    impar = impar+2
    count= count+1
    