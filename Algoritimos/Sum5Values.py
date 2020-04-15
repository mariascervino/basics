# Somar 5 valores fornecidos pelo usuario
count = 1
sum = 0
while (count <= 5):
    value = int(input("Insert a value: "))
    sum = (sum + value)
    count = (count + 1)
print("The sum of all the values was ", str(sum))