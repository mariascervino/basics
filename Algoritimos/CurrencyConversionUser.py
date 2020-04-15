#  Fazer a conversao de moedas de real para dolar quantas vezes o usuario quiser
qtdConvs = int(input("How many times would you like to do this operation? "))
# while Conv = int(input("Quantas vezes voce deseja fazer a conversao?")):
countLoop = 1
while (countLoop <= qtdConvs):
    real = float(input("What is the value in R$? "))
    dolar = float( real / 5 )
    print ("The converted value is US$ ",dolar )
    countLoop = countLoop + 1