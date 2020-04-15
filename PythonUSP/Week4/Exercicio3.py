#somar todos as unidades presentes em um numero maior
init = 123
result = 0
while(init > 0):
    num = init%10
    result = result+num
    init = init//10 
print(result)