# Somar a quantidade de valores fornecidos pelo usuario
sum = 0
resp = "Y"
while (resp == "Y"):
    value = int(input("Insert a value: "))
    sum = (sum + value)
    resp = input("Do you want to continue? [Y/N]")
print("The sum of all values was ", str(sum))