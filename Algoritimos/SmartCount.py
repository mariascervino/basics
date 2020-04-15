# usuario escolhe dois numeros, se o primeiro for maior que o segundo, contar do menor para o maior
# se o segundo numero for maior que o primeiro, contar do maior para o menor (regressiva)

start = int(input("Insert the start number: "))
end = int(input("Insert the end number: "))

if(start < end):
    while (start <= end):
        print(start)
        start = (start + 1)
else:
    while (start >= end):
        print(start)
        start = (start - 1)