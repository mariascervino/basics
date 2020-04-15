import math
a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = float(input("Qual é o valor de c? "))
delta = (b*b) - (4*a*c)
print(delta)
if delta < 0:
    print("essa equação não possui raízes reais")
elif delta == 0:
    x = -b + delta / (2*a)
    print("a raiz dessa equação é ", x)
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("as raízes da equação são ", x1, "e", x2)